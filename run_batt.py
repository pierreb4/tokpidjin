import argparse
import random
import re
import ast
import hashlib
import math
import importlib
import os
import asyncio
import multiprocessing as mp
import gc
import threading
import atexit
import signal
import time
import types

import dill as pickle

from contextlib import suppress
from timeit import default_timer as timer
from pathlib import Path
from collections import defaultdict
from contextlib import contextmanager

# Monkey patch to suppress harmless thread cleanup KeyError under high load
# Issue: threading._active can have race condition during rapid thread creation/deletion
# Symptom: "Exception ignored in thread started by: ... KeyError: <thread_id>"
# Impact: Harmless but noisy - thread cleanup issue in Python's threading module
import sys
_original_thread_delete = None
try:
    import threading as _threading_module
    _original_thread_delete = _threading_module.Thread._delete
    
    def _patched_thread_delete(self):
        """Suppress KeyError during thread cleanup (race condition in threading._active)"""
        try:
            _original_thread_delete(self)
        except KeyError:
            # Ignore KeyError during thread cleanup - harmless race condition
            # Thread was already removed from _active by another operation
            pass
    
    _threading_module.Thread._delete = _patched_thread_delete
except Exception:
    # If patch fails, continue without it (error will still be noisy but functional)
    pass

from utils import *
import utils as utils_module
from expand_solver import expand_file, generate_expanded_content
import expand_solver as expand_solver_module
from run_test import check_solver, eval_match
from mega_batch_batt import MegaBatchCoordinator
from batt_cache import (
    cached_check_solver,
    cached_inline_variables,
    print_cache_stats,
    get_cache_stats,
    init_cache
)

# Phase 2b: GPU batch processing
from gpu_batch_integration import BatchSolverAccumulator

from concurrent.futures import ThreadPoolExecutor, as_completed
# Use loky for better pickling support (handles closures like rbind.<locals>.f)
try:
    from loky import ProcessPoolExecutor
    LOKY_AVAILABLE = True
except ImportError:
    from concurrent.futures import ProcessPoolExecutor
    LOKY_AVAILABLE = False
try:
    import cupy as cp
    from dsl import GPU_AVAILABLE
    # Import optimized GPU batch processor
    from gpu_optimizations import KaggleGPUOptimizer
    
    if GPU_AVAILABLE:
        try:
            # Kaggle GPU detection and configuration
            gpu_count = cp.cuda.runtime.getDeviceCount()
            print(f"Kaggle GPU Support: {GPU_AVAILABLE} ({gpu_count} devices)")
            for i in range(gpu_count):
                device = cp.cuda.Device(i)
                mem_total = device.mem_info[1] / (1024**3)
                print(f"  GPU {i}: Compute {device.compute_capability}, Memory: {mem_total:.1f}GB")
            
            # Initialize optimized batch processor
            gpu_optimizer = KaggleGPUOptimizer(device_id=0)
            print("✓ Kaggle GPU Optimizer initialized")
        except Exception as e:
            # CUDA driver not available or insufficient (common on Kaggle CPU-only sessions)
            print(f"GPU detected but not accessible: {e}")
            GPU_AVAILABLE = False
            gpu_optimizer = None
    else:
        gpu_optimizer = None
except ImportError:
    GPU_AVAILABLE = False
    gpu_optimizer = None
    # Only print message if GPU was expected (not in forced CPU mode)
    if os.environ.get('EXPECT_GPU', '1') != '0':
        print_l("GPU Support: Disabled (CuPy not available)")

import multiprocessing as mp

# Debug flag for validation and score detection messages
# Set to False to suppress timeout and mismatch warnings
DEBUG_VALIDATION = False

# Track active executors for cleanup on exit/interrupt
_active_executors = []
_executor_lock = threading.Lock()

def _safe_executor_shutdown(executor, wait=True, cancel_futures=False):
    """
    Safely shutdown executor with compatibility for both stdlib and loky.
    
    - Standard library ProcessPoolExecutor uses 'cancel_futures' (Python 3.9+)
    - Loky ProcessPoolExecutor uses 'kill_workers' instead
    - ThreadPoolExecutor uses 'cancel_futures' (Python 3.9+)
    
    Falls back to simple shutdown(wait) if neither parameter is supported.
    """
    if not hasattr(executor, 'shutdown'):
        return
    
    try:
        # Try loky's API first (kill_workers)
        executor.shutdown(wait=wait, kill_workers=cancel_futures)
    except TypeError:
        try:
            # Try stdlib API (cancel_futures)
            executor.shutdown(wait=wait, cancel_futures=cancel_futures)
        except TypeError:
            # Fall back to basic API (Python 3.7-3.8 or other)
            try:
                executor.shutdown(wait=wait)
            except Exception:
                pass

def _cleanup_executors():
    """Clean up any active executors to prevent semaphore leaks"""
    with _executor_lock:
        for executor in _active_executors[:]:
            try:
                _safe_executor_shutdown(executor, wait=False, cancel_futures=True)
            except Exception:
                pass
        _active_executors.clear()

# Register cleanup on normal exit
atexit.register(_cleanup_executors)

# Register cleanup on interrupt (Ctrl-C)
def _signal_handler(signum, frame):
    """Handle interrupt signals by cleaning up executors"""
    _cleanup_executors()
    # Re-raise KeyboardInterrupt to allow normal handling
    raise KeyboardInterrupt

signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)

# Execution timing and error tracking for timeout optimization
_stats_lock = threading.Lock()
_stats_file = Path('logs/run_batt_timing_stats.jsonl')

def _log_execution_stats(task_id, execution_time, error_type=None, error_msg=None, timeout_value=None):
    """
    Log execution timing and error stats for timeout optimization.
    
    Args:
        task_id: The ARC task ID
        execution_time: Time in seconds for the execution
        error_type: Type of error if any ('timeout', 'thread_error', 'memory_error', etc.)
        error_msg: Brief error message
        timeout_value: The timeout value used (for correlation analysis)
    """
    import json
    from datetime import datetime
    
    stats_entry = {
        'timestamp': datetime.now().isoformat(),
        'task_id': task_id,
        'execution_time': round(execution_time, 3),
        'success': error_type is None,
        'error_type': error_type,
        'error_msg': error_msg,
        'timeout_value': timeout_value
    }
    
    try:
        with _stats_lock:
            # Ensure logs directory exists
            _stats_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Append to JSONL file (one JSON object per line)
            with open(_stats_file, 'a') as f:
                f.write(json.dumps(stats_entry) + '\n')
    except Exception as e:
        # Don't let stats logging break the main execution
        print_l(f"Warning: Failed to log execution stats: {e}")

def _log_and_exit(task_id, start_time, error_type, error_msg, timeout_value=None):
    """
    Log execution stats for a critical error and exit.
    Used when encountering MemoryError or other critical failures.
    
    Args:
        task_id: The ARC task ID
        start_time: The start time (from timer())
        error_type: Type of error ('memory_error', 'critical_error', etc.)
        error_msg: Brief error message
        timeout_value: The timeout value used
    """
    execution_time = timer() - start_time
    _log_execution_stats(task_id, execution_time, error_type=error_type, 
                        error_msg=error_msg, timeout_value=timeout_value)
    import sys
    sys.exit(1)

def _log_task_start(task_id, timeout_value):
    """
    Log the start of a task execution.
    Used to detect incomplete executions (crashes, timeouts) by comparing starts vs completions.
    
    Args:
        task_id: The ARC task ID
        timeout_value: The timeout value used
    """
    import json
    from datetime import datetime
    
    stats_entry = {
        'timestamp': datetime.now().isoformat(),
        'task_id': task_id,
        'event': 'task_start',  # Mark as start event
        'timeout_value': timeout_value
    }
    
    try:
        with _stats_lock:
            # Ensure logs directory exists
            _stats_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Append to JSONL file
            with open(_stats_file, 'a') as f:
                f.write(json.dumps(stats_entry) + '\n')
    except Exception as e:
        # Don't let stats logging break the main execution
        print_l(f"Warning: Failed to log task start: {e}")

def _safe_map_with_timeout(executor, func, items, timeout_per_item=0.5, operation_name="operation"):
    """
    Safe version of executor.map() that doesn't hang on stuck tasks.
    Uses chunked submission to avoid thread exhaustion with large item lists.
    
    Args:
        executor: ThreadPoolExecutor or ProcessPoolExecutor
        func: Function to apply to each item
        items: Iterable of items to process
        timeout_per_item: Timeout in seconds for each item (default 30s)
        operation_name: Name for logging (e.g., "inline_variables")
    
    Returns:
        List of results (None for timed-out items)
    """
    from concurrent.futures import as_completed
    
    items_list = list(items)
    results = [None] * len(items_list)
    
    # Get max_workers from executor (defaults to 2 if not available)
    max_workers = getattr(executor, '_max_workers', 2)
    
    # Submit in chunks to avoid thread exhaustion
    # Chunk size = max_workers * 4 (keep 4x items in flight)
    chunk_size = max(max_workers * 4, 8)  # At least 8, typically 8-16
    
    for chunk_start in range(0, len(items_list), chunk_size):
        chunk_end = min(chunk_start + chunk_size, len(items_list))
        chunk_items = items_list[chunk_start:chunk_end]
        
        # Submit chunk
        futures = {}
        for offset, item in enumerate(chunk_items):
            i = chunk_start + offset
            try:
                futures[executor.submit(func, item)] = (i, item)
            except RuntimeError as e:
                if "can't start new thread" in str(e):
                    print_l(f"Warning: Thread exhaustion submitting {operation_name} item {i}, skipping remaining in chunk")
                    break
                raise
        
        # Collect chunk results with timeout
        # Use try/except to catch TimeoutError from as_completed and continue with partial results
        try:
            for future in as_completed(futures, timeout=timeout_per_item * len(futures)):
                i, item = futures[future]
                try:
                    result = future.result(timeout=timeout_per_item)
                    results[i] = result
                except TimeoutError:
                    print_l(f"Warning: {operation_name} timed out after {timeout_per_item}s for item {i}")
                    results[i] = None
                except Exception as e:
                    print_l(f"Warning: {operation_name} failed for item {i}: {type(e).__name__}: {e}")
                    results[i] = None
        except TimeoutError as e:
            # Some futures didn't complete - collect what we have and mark rest as None
            unfinished_count = str(e).split('(')[1].split(')')[0] if '(' in str(e) else 'unknown'
            print_l(f"Warning: {operation_name} chunk timeout - {unfinished_count} futures unfinished, using partial results")
            # Results for unfinished futures are already None (initialized above)
    
    return results

# Inlining telemetry tracking (Week 6E)
_inlining_stats = {
    'total_attempts': 0,
    'timeout_count': 0,
    'timeout_retry_success': 0,  # Succeeded by skipping inlining
    'timeout_retry_fail': 0,      # Failed even after retry
    'other_errors': 0,
    'success_count': 0,
    'retry_time_ms': 0.0           # Total time spent in retry operations
}
_inlining_stats_lock = threading.Lock()

def _log_inlining_stats():
    """Log inlining statistics to file for analysis"""
    stats_file = Path('logs/inlining_telemetry.jsonl')
    stats_file.parent.mkdir(parents=True, exist_ok=True)
    
    with _inlining_stats_lock:
        stats_copy = _inlining_stats.copy()
    
    from datetime import datetime
    stats_entry = {
        'timestamp': datetime.now().isoformat(),
        **stats_copy
    }
    
    try:
        with open(stats_file, 'a') as f:
            import json
            f.write(json.dumps(stats_entry) + '\n')
    except Exception as e:
        print_l(f"Warning: Could not log inlining stats: {e}")

def _print_inlining_summary():
    """Print inlining statistics summary"""
    with _inlining_stats_lock:
        total = _inlining_stats['total_attempts']
        timeouts = _inlining_stats['timeout_count']
        retry_success = _inlining_stats['timeout_retry_success']
        retry_fail = _inlining_stats['timeout_retry_fail']
        errors = _inlining_stats['other_errors']
        success = _inlining_stats['success_count']
        retry_time_ms = _inlining_stats['retry_time_ms']
        error_types = _inlining_stats.get('error_types', {})
        thread_retry_success = _inlining_stats.get('thread_retry_success', 0)
        thread_retry_fallback = _inlining_stats.get('thread_retry_fallback', 0)
    
    if total == 0:
        return
    
    print_l("\n=== INLINING TELEMETRY ===")
    print_l(f"Total attempts: {total}")
    print_l(f"Success (first try): {success} ({100*success/total:.1f}%)")
    print_l(f"Timeouts: {timeouts} ({100*timeouts/total:.1f}%)")
    if timeouts > 0:
        print_l(f"  → Retry success (raw source): {retry_success} ({100*retry_success/timeouts:.1f}% of timeouts)")
        print_l(f"  → Retry fail: {retry_fail} ({100*retry_fail/timeouts:.1f}% of timeouts)")
        avg_retry_time = retry_time_ms / (retry_success + retry_fail) if (retry_success + retry_fail) > 0 else 0
        print_l(f"  → Total retry time: {retry_time_ms:.1f}ms (avg {avg_retry_time:.2f}ms per retry)")
    
    # Print thread retry statistics if any occurred
    if thread_retry_success > 0 or thread_retry_fallback > 0:
        print_l(f"Thread exhaustion retries:")
        print_l(f"  → Retry success: {thread_retry_success}")
        print_l(f"  → Retry fallback (raw source): {thread_retry_fallback}")
    
    print_l(f"Other errors: {errors} ({100*errors/total:.1f}%)")
    
    # Print error type breakdown if errors occurred
    if error_types:
        print_l("Error breakdown:")
        for error_key, count in sorted(error_types.items(), key=lambda x: -x[1]):
            print_l(f"  → {error_key}: {count} ({100*count/errors:.1f}% of errors)")
    
    print_l("=" * 30)

class GPUBatchProcessor:
    """
    Batch processor optimized for Kaggle GPUs (T4x2, P100, L4x4)
    - T4: 16GB, Compute 7.5, good for inference
    - P100: 16GB, Compute 6.0, high memory bandwidth
    - L4: 24GB, Compute 8.9, newest architecture
    """
    def __init__(self, batch_size=32, use_gpu=True):
        self.batch_size = batch_size
        self.use_gpu = use_gpu and GPU_AVAILABLE
        self.gpu_id = 0  # Default to first GPU
        
        # Use optimized Kaggle GPU processor if available
        if self.use_gpu and gpu_optimizer is not None:
            self.optimizer = gpu_optimizer
            print(f"Using KaggleGPUOptimizer (batch_size={batch_size})")
        elif self.use_gpu:
            # Fallback: Configure GPU manually
            try:
                cp.cuda.Device(self.gpu_id).use()
                mem_info = cp.cuda.Device(self.gpu_id).mem_info
                available_mem = mem_info[0]
                mem_limit = int(available_mem * 0.8)
                cp.get_default_memory_pool().set_limit(size=mem_limit)
                print(f"GPU batch processor initialized on device {self.gpu_id}")
                print(f"  Memory limit: {mem_limit/(1024**3):.2f}GB")
                self.optimizer = None
            except Exception as e:
                print(f"GPU initialization warning: {e}")
                self.use_gpu = False
                self.optimizer = None
        else:
            self.optimizer = None
        
    def process_tasks_batch(self, tasks):
        """Process multiple tasks in parallel with GPU acceleration"""
        if not tasks:
            return []
        
        # Adjust batch size based on task complexity and GPU memory
        effective_batch_size = self._get_effective_batch_size(len(tasks))
        
        results = []
        for i in range(0, len(tasks), effective_batch_size):
            batch = tasks[i:i+effective_batch_size]
            try:
                if self.use_gpu:
                    batch_results = self._process_batch_gpu(batch)
                else:
                    batch_results = self._process_batch_cpu(batch)
                results.extend(batch_results)
            except Exception as e:
                print(f"Batch processing error: {e}, falling back to CPU")
                batch_results = self._process_batch_cpu(batch)
                results.extend(batch_results)
            finally:
                if self.use_gpu:
                    self._cleanup_gpu_memory()
        
        return results
    
    def _get_effective_batch_size(self, num_tasks):
        """Adjust batch size based on available GPU memory"""
        if not self.use_gpu:
            return min(self.batch_size, num_tasks)
        
        try:
            mem_info = cp.cuda.Device(self.gpu_id).mem_info
            available_mem = mem_info[0]
            # Reduce batch size if memory is low
            if available_mem < 1024**3:  # Less than 1GB available
                return max(4, self.batch_size // 4)
            elif available_mem < 2 * 1024**3:  # Less than 2GB
                return max(8, self.batch_size // 2)
        except:
            pass
        
        return min(self.batch_size, num_tasks)
        
    def _process_batch_gpu(self, task_batch):
        """
        Process task batch on GPU
        Optimized for grid operations common in ARC tasks
        """
        if not GPU_AVAILABLE:
            return self._process_batch_cpu(task_batch)
        
        results = []
        try:
            # Process each task with GPU-accelerated operations
            for task in task_batch:
                result = self._process_single_task_gpu(task)
                results.append(result)
            
        except cp.cuda.memory.OutOfMemoryError:
            print("GPU OOM, falling back to CPU for this batch")
            return self._process_batch_cpu(task_batch)
        except Exception as e:
            print(f"GPU processing error: {e}")
            return self._process_batch_cpu(task_batch)
        
        return results
    
    def _process_single_task_gpu(self, task):
        """Process a single task with GPU acceleration"""
        # This is a template - actual implementation depends on task structure
        # For now, return the task as-is
        # TODO: Implement GPU-accelerated grid operations
        return task
    
    def _process_batch_cpu(self, task_batch):
        """Fallback CPU processing for tasks"""
        # Process tasks sequentially on CPU
        return [self._process_single_task_cpu(task) for task in task_batch]
    
    def _process_single_task_cpu(self, task):
        """Process a single task on CPU"""
        # This is a template - return task as-is
        return task
    
    def _cleanup_gpu_memory(self):
        """Clean up GPU memory between batches"""
        if self.use_gpu:
            try:
                mempool = cp.get_default_memory_pool()
                pinned_mempool = cp.get_default_pinned_memory_pool()
                mempool.free_all_blocks()
                pinned_mempool.free_all_blocks()
            except:
                pass

    def _gpu_batch_solve(self, task_batch):
        """Process task batch on GPU"""
        if not GPU_AVAILABLE:
            return self._cpu_batch_solve(task_batch)
        
        try:
            # Convert grids to GPU arrays
            gpu_grids = [cp.asarray(task['grid']) for task in task_batch]
            # Batch process on GPU
            results = []
            for gpu_grid in gpu_grids:
                result = self._solve_on_gpu(gpu_grid)
                results.append(cp.asnumpy(result))
            return results
        except Exception as e:
            print(f"GPU batch failed, falling back to CPU: {e}")
            return self._cpu_batch_solve(task_batch)

    def _cpu_batch_solve(self, task_batch):
        """Fallback CPU processing"""
        return [self._solve_cpu(task) for task in task_batch]

# GPU memory management optimized for Kaggle GPUs
def configure_gpu_memory(device_id=0, memory_fraction=0.8):
    """
    Configure GPU memory for Kaggle environment
    
    Args:
        device_id: GPU device ID (0 for first GPU)
        memory_fraction: Fraction of available memory to use (0.8 = 80%)
    
    Returns:
        bool: True if successful, False otherwise
    """
    if not GPU_AVAILABLE:
        return False
    
    try:
        cp.cuda.Device(device_id).use()
        
        # Get available memory
        mem_info = cp.cuda.Device(device_id).mem_info
        total_mem = mem_info[1]
        available_mem = mem_info[0]
        
        # Set memory pool limit
        mem_limit = int(total_mem * memory_fraction)
        cp.get_default_memory_pool().set_limit(size=mem_limit)
        
        print(f"GPU {device_id} configured:")
        print(f"  Total memory: {total_mem/(1024**3):.2f}GB")
        print(f"  Available: {available_mem/(1024**3):.2f}GB")
        print(f"  Pool limit: {mem_limit/(1024**3):.2f}GB")
        
        return True
    except Exception as e:
        print(f"GPU configuration error: {e}")
        return False


def gpu_memory_cleanup():
    """Clean up GPU memory pools to prevent OOM errors"""
    if not GPU_AVAILABLE:
        return
    
    try:
        mempool = cp.get_default_memory_pool()
        pinned_mempool = cp.get_default_pinned_memory_pool()
        
        # Free unused blocks
        mempool.free_all_blocks()
        pinned_mempool.free_all_blocks()
        
        # Optional: Print memory stats
        # mem_info = cp.cuda.Device().mem_info
        # print(f"GPU memory after cleanup: {mem_info[0]/(1024**3):.2f}GB free")
    except Exception as e:
        print(f"GPU cleanup warning: {e}")


def get_optimal_batch_size(grid_size=None, num_samples=None):
    """
    Calculate optimal batch size based on GPU memory and task characteristics
    
    Args:
        grid_size: Average grid size (rows * cols)
        num_samples: Number of samples to process
    
    Returns:
        int: Optimal batch size
    """
    if not GPU_AVAILABLE:
        return 16  # Default CPU batch size
    
    try:
        mem_info = cp.cuda.Device().mem_info
        available_mem = mem_info[0]
        
        # T4/P100: 16GB, L4: 24GB
        # Conservative estimates for grid operations
        if available_mem > 10 * 1024**3:  # > 10GB available
            base_batch = 64
        elif available_mem > 5 * 1024**3:  # > 5GB available
            base_batch = 32
        elif available_mem > 2 * 1024**3:  # > 2GB available
            base_batch = 16
        else:
            base_batch = 8
        
        # Adjust for grid size if provided
        if grid_size:
            if grid_size > 900:  # Large grids (30x30)
                base_batch = max(4, base_batch // 4)
            elif grid_size > 400:  # Medium grids (20x20)
                base_batch = max(8, base_batch // 2)
        
        # Cap at num_samples if provided
        if num_samples:
            base_batch = min(base_batch, num_samples)
        
        return base_batch
    except:
        return 16


class O_Score:    
    def __init__(self):
        self.score = {}

    def update(self, solver_id, match):
        if solver_id not in self.score:
            self.score[solver_id] = 0
        self.score[solver_id] += match

    def get(self, solver_id):
        return self.score.get(solver_id, 0)


class S_Score:    
    def __init__(self):
        self.score = {}

    def update(self, solver_id, match):
        if solver_id not in self.score:
            self.score[solver_id] = 0
        self.score[solver_id] += match

    def get(self, solver_id):
        return self.score.get(solver_id, 0)


class D_Score:    
    def __init__(self):
        self.score = {}
        self.last_t = {}

    def update(self, solver_id, s_item):
        # Updated for unified differ scoring with 0-1000 scale (matching solvers)
        last_t, s_solver_id, d_name, return_tuple = s_item

        # Keep track of last_t per differ
        if s_solver_id == 'None':
            self.last_t[d_name] = last_t

        if solver_id not in self.score:
            self.score[solver_id] = {}
        if d_name not in self.score[solver_id]:
            self.score[solver_id][d_name] = {
                'last_t': self.last_t[d_name],
                'score': 0
            }
        
        # Check if return_tuple is valid: must be a tuple with at least 2 elements, both integers
        if type(return_tuple) != tuple or len(return_tuple) < 2:
            return
        
        if type(return_tuple[0]) != int or type(return_tuple[1]) != int:
            return
        
        # Convert differ tuple to 0-1000 score (like eval_match)
        # For differ_exact_dims: (total_cells, matching_cells)
        # Score = (matching_cells * 1000) // total_cells
        total = return_tuple[0]
        matching = return_tuple[1]
        
        if total <= 0:
            return
        
        # Calculate score (0-1000 per sample, just like solvers)
        sample_score = (matching * 1000) // total
        
        # Clamp to 0-1000 range for safety
        sample_score = max(0, min(1000, sample_score))
        
        # Accumulate the score across samples, taking into account
        # score improvement from 'None' to actual solver
        if s_solver_id == 'None':
            self.score[solver_id][d_name]['score'] += 1000 - sample_score
        if s_solver_id == solver_id:
            self.score[solver_id][d_name]['score'] += sample_score


def score_sample(args):
    """Score a single sample - works for both demo and test (Week 6B optimization)"""
    i, sample, sample_type, task_id, S, pile_log_path, timeout, DO_PRINT, batt_module_name, batch_accumulator = args
    
    # Import batt in worker process (needed for ProcessPoolExecutor)
    import importlib
    batt_module = importlib.import_module(batt_module_name)
    batt_func = batt_module.batt
    
    I = sample['input']
    O = sample['output']
    
    # Call batt with thread-based timeout
    solve_timed_out, solve_result = call_with_timeout(batt_func,
        [task_id, S, I, None, pile_log_path], timeout)
    
    if solve_timed_out and DO_PRINT:
        print_l(f'-- {task_id} - {sample_type}[{i}] timed out')
    
    sample_o = []
    sample_s = []
    diff_call_count = 0
    score_count = 0
    match = False
    
    if solve_result is not None:
        sample_o, sample_s = solve_result
        
        if DO_PRINT:
            print_l(f"{sample_type}[{i}] - {task_id} - {len(sample_o)}")
        
        # Score outputs and collect matching solver ids
        for t_n, evo, o_solver_id, okt in sample_o:
            C = okt
            match, score = eval_match(S, C, O)
            score_count += score
            if match and DO_PRINT:
                print_l(f'- MATCH: {o_solver_id = } - sample_type={sample_type}[{i}] task_id={task_id}')
        
        # OPTIMIZATION: Only run diff ONCE per sample if any output matches
        # Calling batt multiple times with identical O parameter returns identical results

        if match:
        # if score > 0:

            diff_call_count += 1
            # Run diff to get solver-level scores (only once per sample)
            diff_timed_out, diff_result = call_with_timeout(batt_func,
                [task_id, S, I, O, pile_log_path], timeout)
            
            if diff_result is not None:
                _, sample_s_result = diff_result
                sample_s.extend(sample_s_result)
    
    # Phase 2b: Add input grid to batch accumulator for GPU processing
    if batch_accumulator:
        batch_accumulator.add('input', I, operation='sample_input')
        if sample_o:
            # Add first output as representative of solver outputs
            for t_n, evo, o_solver_id, okt in sample_o[:1]:
                batch_accumulator.add('output', okt, operation='solver_output')
    
    return {
        'index': i,
        'sample_type': sample_type,
        'outputs': sample_o,
        'solver_scores': sample_s,
        'timed_out': solve_timed_out,
        'diff_calls': diff_call_count,
        'matches': score_count
    }


def check_batt(total_data, task_i, task_id, d_score, start_time, pile_log_path, timeout=1, prof=None, batt_module_name='batt', batch_accumulator=None):
    """Check batt - now synchronous with parallel demo sample scoring"""
    task_start = timer()
    demo_task = total_data['demo'][task_id]
    test_task = total_data['test'][task_id]
    # total_task = total_data['demo'][task_id] + total_data['test'][task_id]

    o = {'demo': {}, 'test': {}}
    s = {'demo': {}, 'test': {}}
    all_o = set()
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in demo_task)
    
    # DEBUG: Log S to verify it's created fresh per task
    if DEBUG_VALIDATION and DO_PRINT:
        print_l(f"DEBUG check_batt: task_id={task_id} S_len={len(S)}")

    # print_l(f'-- {task_id} - {task_i} --') if DO_PRINT else None

    o_score = O_Score()
    s_score = {}
    
    # Week 6B: Unified parallel sample scoring for demo + test together
    # Uses call_with_timeout (pure threading) instead of asyncio.gather
    prof_start = timer() if prof is not None else None
    
    # Week 6B Optimization: Process ALL samples (demo + test) together for better parallelization
    # GPU environments use ThreadPoolExecutor (GPU context not fork-safe)
    # CPU environments use ProcessPoolExecutor (avoids GIL, better for CPU-bound work)
    
    # Prepare arguments for ALL samples (demo + test combined)
    all_sample_args = []
    
    # Add demo samples
    for i, sample in enumerate(demo_task):
        all_sample_args.append((i, sample, 'demo', task_id, S, pile_log_path, timeout, DO_PRINT, batt_module_name, batch_accumulator))
    
    # Add test samples
    for i, sample in enumerate(test_task):
        all_sample_args.append((i, sample, 'test', task_id, S, pile_log_path, timeout, DO_PRINT, batt_module_name, batch_accumulator))
    
    if GPU_AVAILABLE:
        # GPU: Parallel execution with ThreadPoolExecutor (GPU context not fork-safe)
        # Check system health before attempting parallel execution
        thread_count = threading.active_count()
        system_overloaded = thread_count > 40  # Conservative threshold
        
        if system_overloaded:
            # System under heavy load - use sequential processing
            if DO_PRINT:
                print_l(f"-- System overloaded ({thread_count} threads), using sequential processing")
            
            all_results = []
            for args in all_sample_args:
                try:
                    result = score_sample(args)
                    all_results.append(result)
                except Exception as e:
                    sample_type, sample_idx = args[2], args[0]
                    if DO_PRINT:
                        print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed: {e}")
                    all_results.append({
                        'index': sample_idx,
                        'sample_type': sample_type,
                        'outputs': [],
                        'solver_scores': [],
                        'timed_out': True,
                        'diff_calls': 0,
                        'matches': 0
                    })
        else:
            # Normal load - use limited parallelism
            # Reduce max_workers from 5 to 2 for memory safety
            max_workers = min(2, len(all_sample_args))
            
            try:
                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    # Submit all samples (demo + test) for parallel execution
                    sample_futures = {executor.submit(score_sample, args): args 
                                    for args in all_sample_args}
                    
                    # Collect results as they complete
                    all_results = []
                    for future in as_completed(sample_futures):
                        try:
                            # Use generous timeout to prevent hanging on stuck workers
                            result = future.result(timeout=600)  # 10 minutes max per sample result
                            all_results.append(result)
                        except TimeoutError:
                            args = sample_futures[future]
                            sample_type, sample_idx = args[2], args[0]
                            if DO_PRINT:
                                print_l(f"-- {task_id} - {sample_type}[{sample_idx}] result collection timed out after 600s")
                            all_results.append({
                                'index': sample_idx,
                                'sample_type': sample_type,
                                'outputs': [],
                                'solver_scores': [],
                                'timed_out': True,
                                'diff_calls': 0,
                                'matches': 0
                            })
                        except MemoryError:
                            # Handle memory exhaustion in thread - immediate exit to prevent hang
                            args = sample_futures[future]
                            sample_type, sample_idx = args[2], args[0]
                            if DO_PRINT:
                                print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed due to MemoryError")
                            print_l(f"CRITICAL: MemoryError in GPU ThreadPoolExecutor. System out of memory. Exiting.")
                            _log_and_exit(task_id, start_time, 'memory_error', 
                                        f"GPU ThreadPoolExecutor MemoryError at {sample_type}[{sample_idx}]", timeout)
                        except RuntimeError as e:
                            # Handle "can't start new thread" from nested call_with_timeout
                            if "can't start new thread" in str(e):
                                args = sample_futures[future]
                                sample_type, sample_idx = args[2], args[0]
                                if DO_PRINT:
                                    print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed due to nested thread exhaustion (in call_with_timeout)")
                                all_results.append({
                                    'index': sample_idx,
                                    'sample_type': sample_type,
                                    'outputs': [],
                                    'solver_scores': [],
                                    'timed_out': True,
                                    'diff_calls': 0,
                                    'matches': 0
                                })
                            else:
                                # Different RuntimeError
                                args = sample_futures[future]
                                sample_type, sample_idx = args[2], args[0]
                                if DO_PRINT:
                                    print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed: {e}")
                                all_results.append({
                                    'index': sample_idx,
                                    'sample_type': sample_type,
                                    'outputs': [],
                                    'solver_scores': [],
                                    'timed_out': True,
                                    'diff_calls': 0,
                                    'matches': 0
                                })
                        except Exception as e:
                            args = sample_futures[future]
                            sample_type, sample_idx = args[2], args[0]
                            if DO_PRINT:
                                print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed: {e}")
                            all_results.append({
                                'index': sample_idx,
                                'sample_type': sample_type,
                                'outputs': [],
                                'solver_scores': [],
                                'timed_out': True,
                                'diff_calls': 0,
                                'matches': 0
                            })
            except MemoryError:
                # MemoryError during thread creation (Thread._bootstrap)
                # This happens before any futures can be collected
                print_l(f"CRITICAL: MemoryError during GPU ThreadPoolExecutor thread creation (Thread._bootstrap)")
                print_l(f"System critically low on memory. Cannot create worker threads. Exiting.")
                _log_and_exit(task_id, start_time, 'memory_error', 
                            'GPU ThreadPoolExecutor thread creation MemoryError (Thread._bootstrap)', timeout)
    else:
        # CPU-only: Use ProcessPoolExecutor for true CPU parallelism (Week 6B)
        # Conservative workers for multi-instance server environment
        # Check sample count to decide strategy
        sample_count = len(all_sample_args)
        
        # Check system health before attempting parallel execution
        # If too many threads already exist, skip ProcessPoolExecutor entirely
        thread_count = threading.active_count()
        # Lower threshold to 40 (was 50) to prevent thread cleanup issues
        # Under extreme load, thread cleanup can fail with KeyError in threading._active
        system_overloaded = thread_count > 40  # Conservative threshold
        
        if system_overloaded and DO_PRINT:
            print_l(f"-- System overloaded ({thread_count} threads), using sequential processing")
        
        # Memory-aware worker selection
        # Small batches (<4 samples): Use threads (lighter, good for small work)
        # Large batches (>=4 samples): Try processes (better CPU parallelism)
        use_threads = sample_count < 4 or system_overloaded
        
        if not LOKY_AVAILABLE and not use_threads and DO_PRINT:
            print_l("Warning: loky not available, using standard ProcessPoolExecutor (may fail on closures)")
        
        # Try ProcessPoolExecutor first for CPU parallelism, fall back to threads if memory issues
        process_pool_failed = False
        try:
            if use_threads:
                # Small batch or system overloaded: Use ThreadPoolExecutor (lighter weight)
                executor_class = ThreadPoolExecutor
                max_workers = 1 if system_overloaded else min(sample_count, 3)
            else:
                # Large batch: Try ProcessPoolExecutor
                executor_class = ProcessPoolExecutor
                max_workers = min(sample_count, 3)  # Reduced from 4 to 3 for memory safety
            
            executor = executor_class(max_workers=max_workers)
            # Register executor for cleanup on exit/interrupt to prevent semaphore leaks
            with _executor_lock:
                _active_executors.append(executor)
            
            try:
                # Submit all samples (demo + test) for parallel execution
                # Use retry with backoff for "can't start new thread" errors
                sample_futures = {}
                failed_samples = []  # Track samples that failed to submit even after retries
                
                for args in all_sample_args:
                    # Retry submission with exponential backoff if thread creation fails
                    max_retries = 5
                    retry_delay = 0.1  # Start with 100ms
                    submitted = False
                    
                    for attempt in range(max_retries):
                        try:
                            future = executor.submit(score_sample, args)
                            sample_futures[future] = args
                            submitted = True
                            break  # Success, move to next sample
                        except RuntimeError as e:
                            if "can't start new thread" in str(e):
                                if attempt < max_retries - 1:
                                    # Backoff and retry
                                    if DO_PRINT and attempt == 0:
                                        sample_type, sample_idx = args[2], args[0]
                                        print_l(f"-- {task_id} - {sample_type}[{sample_idx}] thread creation failed, retrying with backoff...")
                                    time.sleep(retry_delay)
                                    retry_delay *= 2  # Exponential backoff
                                    gc.collect()  # Try to free resources
                                else:
                                    # Max retries exceeded, record as failed
                                    if DO_PRINT:
                                        sample_type, sample_idx = args[2], args[0]
                                        print_l(f"-- {task_id} - {sample_type}[{sample_idx}] thread creation failed after {max_retries} retries")
                                    break  # Exit retry loop, will handle below
                            else:
                                # Different RuntimeError, don't retry
                                break
                    
                    # If submission failed after all retries, record the failure
                    if not submitted:
                        sample_type, sample_idx = args[2], args[0]
                        failed_samples.append({
                            'index': sample_idx,
                            'sample_type': sample_type,
                            'outputs': [],
                            'solver_scores': [],
                            'timed_out': True,
                            'diff_calls': 0,
                            'matches': 0
                        })
                
                # Collect results as they complete
                all_results = list(failed_samples)  # Start with pre-failed samples
                for future in as_completed(sample_futures):
                    try:
                        # Use generous timeout to prevent hanging on stuck workers
                        # Each sample has internal timeout, but this catches worker hangs
                        result = future.result(timeout=600)  # 10 minutes max per sample result
                        all_results.append(result)
                    except TimeoutError:
                        args = sample_futures[future]
                        sample_type, sample_idx = args[2], args[0]
                        if DO_PRINT:
                            print_l(f"-- {task_id} - {sample_type}[{sample_idx}] result collection timed out after 600s")
                        all_results.append({
                            'index': sample_idx,
                            'sample_type': sample_type,
                            'outputs': [],
                            'solver_scores': [],
                            'timed_out': True,
                            'diff_calls': 0,
                            'matches': 0
                        })
                    except MemoryError:
                        # Handle memory exhaustion in process - immediate exit to prevent hang
                        args = sample_futures[future]
                        sample_type, sample_idx = args[2], args[0]
                        if DO_PRINT:
                            print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed due to MemoryError")
                        print_l(f"CRITICAL: MemoryError in CPU ProcessPoolExecutor. System out of memory. Exiting.")
                        _log_and_exit(task_id, start_time, 'memory_error', 
                                    f"CPU ProcessPoolExecutor MemoryError at {sample_type}[{sample_idx}]", timeout)
                    except RuntimeError as e:
                        # Handle "can't start new thread" from nested call_with_timeout
                        if "can't start new thread" in str(e):
                            args = sample_futures[future]
                            sample_type, sample_idx = args[2], args[0]
                            if DO_PRINT:
                                print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed due to nested thread exhaustion (in call_with_timeout)")
                            all_results.append({
                                'index': sample_idx,
                                'sample_type': sample_type,
                                'outputs': [],
                                'solver_scores': [],
                                'timed_out': True,
                                'diff_calls': 0,
                                'matches': 0
                            })
                        else:
                            # Different RuntimeError
                            args = sample_futures[future]
                            sample_type, sample_idx = args[2], args[0]
                            if DO_PRINT:
                                print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed: {e}")
                            all_results.append({
                                'index': sample_idx,
                                'sample_type': sample_type,
                                'outputs': [],
                                'solver_scores': [],
                                'timed_out': True,
                                'diff_calls': 0,
                                'matches': 0
                            })
                    except Exception as e:
                        args = sample_futures[future]
                        sample_type, sample_idx = args[2], args[0]
                        if DO_PRINT:
                            print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed: {e}")
                        all_results.append({
                            'index': sample_idx,
                            'sample_type': sample_type,
                            'outputs': [],
                            'solver_scores': [],
                            'timed_out': True,
                            'diff_calls': 0,
                            'matches': 0
                        })
                
                # Explicit shutdown to ensure clean resource cleanup
                # Prevents "leaked semlock objects" warning from loky
                _safe_executor_shutdown(executor, wait=True, cancel_futures=False)
            finally:
                # Remove executor from tracking
                with _executor_lock:
                    if executor in _active_executors:
                        _active_executors.remove(executor)
                        
        except MemoryError as e:
            # MemoryError is critical - system is out of memory
            # Do NOT try fallback as it will also fail
            print_l(f"CRITICAL: MemoryError in CPU {executor_class.__name__}")
            print_l(f"System critically low on memory. Cannot create workers. Exiting.")
            _log_and_exit(task_id, start_time, 'memory_error', 
                        f"CPU {executor_class.__name__} creation MemoryError", timeout)
        except (OSError, RuntimeError) as e:
            # Resource errors (not memory) - fall back to ThreadPoolExecutor or sequential
            process_pool_failed = True
            error_type = type(e).__name__
            if DO_PRINT:
                print_l(f"-- {executor_class.__name__} failed ({error_type}: {e}), trying ThreadPoolExecutor")
            
            # Force garbage collection to free memory before trying fallback
            gc.collect()
            
            # Try ThreadPoolExecutor as fallback (lighter weight)
            # Use only 1 worker to minimize memory usage
            try:
                try:
                    executor = ThreadPoolExecutor(max_workers=1)
                    # Register executor for cleanup
                    with _executor_lock:
                        _active_executors.append(executor)
                    
                    try:
                        # Submit tasks with retry for thread creation failures
                        sample_futures = {}
                        for args in all_sample_args:
                            max_retries = 5
                            retry_delay = 0.1  # Start with 100ms
                            
                            for attempt in range(max_retries):
                                try:
                                    future = executor.submit(score_sample, args)
                                    sample_futures[future] = args
                                    break  # Success
                                except RuntimeError as e:
                                    if "can't start new thread" in str(e):
                                        if attempt < max_retries - 1:
                                            # Log on first retry only to avoid spam
                                            if DO_PRINT and attempt == 0:
                                                sample_type, sample_idx = args[2], args[0]
                                                print_l(f"-- {task_id} - {sample_type}[{sample_idx}] thread creation failed (ThreadPool fallback), retrying with backoff...")
                                            time.sleep(retry_delay)
                                            retry_delay *= 2  # Exponential backoff: 0.1, 0.2, 0.4, 0.8, 1.6s
                                            gc.collect()  # Free resources before retry
                                        else:
                                            # Max retries exceeded
                                            sample_type, sample_idx = args[2], args[0]
                                            print_l(f"-- {task_id} - {sample_type}[{sample_idx}] thread creation failed after {max_retries} retries")
                                            raise
                                    else:
                                        # Different RuntimeError, don't retry
                                        raise
                        
                        all_results = []
                        for future in as_completed(sample_futures):
                            try:
                                # Use generous timeout to prevent hanging on stuck workers
                                result = future.result(timeout=600)  # 10 minutes max per sample result
                                all_results.append(result)
                            except TimeoutError:
                                args = sample_futures[future]
                                sample_type, sample_idx = args[2], args[0]
                                if DO_PRINT:
                                    print_l(f"-- {task_id} - {sample_type}[{sample_idx}] result collection timed out after 600s")
                                all_results.append({
                                    'index': sample_idx,
                                    'sample_type': sample_type,
                                    'outputs': [],
                                    'solver_scores': [],
                                    'timed_out': True,
                                    'diff_calls': 0,
                                    'matches': 0
                                })
                            except MemoryError:
                                # Handle memory exhaustion in thread - immediate exit to prevent hang
                                args = sample_futures[future]
                                sample_type, sample_idx = args[2], args[0]
                                if DO_PRINT:
                                    print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed due to MemoryError")
                                print_l(f"CRITICAL: MemoryError in ThreadPoolExecutor fallback. System out of memory. Exiting.")
                                _log_and_exit(task_id, start_time, 'memory_error', 
                                            f"ThreadPoolExecutor fallback MemoryError at {sample_type}[{sample_idx}]", timeout)
                            except RuntimeError as e:
                                # Handle "can't start new thread" from nested call_with_timeout
                                if "can't start new thread" in str(e):
                                    args = sample_futures[future]
                                    sample_type, sample_idx = args[2], args[0]
                                    if DO_PRINT:
                                        print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed due to nested thread exhaustion (in call_with_timeout)")
                                    all_results.append({
                                        'index': sample_idx,
                                        'sample_type': sample_type,
                                        'outputs': [],
                                        'solver_scores': [],
                                        'timed_out': True,
                                        'diff_calls': 0,
                                        'matches': 0
                                    })
                                else:
                                    # Different RuntimeError
                                    args = sample_futures[future]
                                    sample_type, sample_idx = args[2], args[0]
                                    if DO_PRINT:
                                        print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed: {e}")
                                    all_results.append({
                                        'index': sample_idx,
                                        'sample_type': sample_type,
                                        'outputs': [],
                                        'solver_scores': [],
                                        'timed_out': True,
                                        'diff_calls': 0,
                                        'matches': 0
                                    })
                            except Exception as e:
                                args = sample_futures[future]
                                sample_type, sample_idx = args[2], args[0]
                                if DO_PRINT:
                                    print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed: {e}")
                                all_results.append({
                                    'index': sample_idx,
                                    'sample_type': sample_type,
                                    'outputs': [],
                                    'solver_scores': [],
                                    'timed_out': True,
                                    'diff_calls': 0,
                                    'matches': 0
                                })
                        
                        # Explicit shutdown for clean resource cleanup
                        _safe_executor_shutdown(executor, wait=True, cancel_futures=False)
                    finally:
                        # Remove executor from tracking
                        with _executor_lock:
                            if executor in _active_executors:
                                _active_executors.remove(executor)
                except MemoryError:
                    # MemoryError during ThreadPoolExecutor fallback creation/execution
                    # System is critically low on memory - immediate exit
                    print_l(f"CRITICAL: MemoryError in ThreadPoolExecutor fallback (Thread._bootstrap)")
                    print_l(f"System critically low on memory. Cannot create fallback threads. Exiting.")
                    _log_and_exit(task_id, start_time, 'memory_error', 
                                'ThreadPoolExecutor fallback creation MemoryError (Thread._bootstrap)', timeout)
            except (OSError, RuntimeError, Exception) as e:
                # ThreadPoolExecutor also failed - fall back to sequential
                if DO_PRINT:
                    print_l(f"-- ThreadPoolExecutor also failed ({e}), using sequential processing")
                all_results = []
                for args in all_sample_args:
                    try:
                        result = score_sample(args)
                        all_results.append(result)
                    except Exception as e:
                        sample_type, sample_idx = args[2], args[0]
                        if DO_PRINT:
                            print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed: {e}")
                        all_results.append({
                            'index': sample_idx,
                            'sample_type': sample_type,
                            'outputs': [],
                            'solver_scores': [],
                            'timed_out': True,
                            'diff_calls': 0,
                            'matches': 0
                        })
        except Exception as e:
            # Other errors - fall back to sequential
            if DO_PRINT:
                print_l(f"-- Parallel execution failed ({e}), falling back to sequential")
            all_results = []
            for args in all_sample_args:
                try:
                    result = score_sample(args)
                    all_results.append(result)
                except Exception as e:
                    sample_type, sample_idx = args[2], args[0]
                    if DO_PRINT:
                        print_l(f"-- {task_id} - {sample_type}[{sample_idx}] failed: {e}")
                    all_results.append({
                        'index': sample_idx,
                        'sample_type': sample_type,
                        'outputs': [],
                        'solver_scores': [],
                        'timed_out': True,
                        'diff_calls': 0,
                        'matches': 0
                    })
    
    # Split results back into demo and test
    demo_results = [r for r in all_results if r['sample_type'] == 'demo']
    test_results = [r for r in all_results if r['sample_type'] == 'test']
    
    # DEBUG: Log result counts before sorting
    if DEBUG_VALIDATION and DO_PRINT:
        print_l(f"DEBUG SPLIT: task_id={task_id} demo_results={len(demo_results)} test_results={len(test_results)}")
    
    # Sort by index to maintain order
    demo_results.sort(key=lambda x: x['index'])
    test_results.sort(key=lambda x: x['index'])
    
    # DEBUG: Log result counts after sorting
    if DEBUG_VALIDATION and DO_PRINT:
        print_l(f"DEBUG SPLIT: task_id={task_id} sorted")
    
    if prof is not None:
        prof['batt.demo.parallel'] = timer() - prof_start
        # Track optimization metrics for ALL samples (demo + test)
        total_diff_calls = sum(r.get('diff_calls', 0) for r in all_results)
        total_matches = sum(r.get('matches', 0) for r in all_results)
        total_outputs = sum(len(r.get('outputs', [])) for r in all_results)
        if DO_PRINT:
            print_l(f"-- Demo+Test scoring: {total_outputs} outputs, {total_matches} matches, {total_diff_calls} diff calls (skipped {total_outputs - total_diff_calls})")
    
    # Week 6B: Profile result aggregation to find overhead
    if prof is not None:
        agg_start = timer()
    
    # Aggregate demo results
    for result in demo_results:
        if result is None:
            continue
            
        i = result['index']
        o['demo'][i] = result['outputs']
        s['demo'][i] = result['solver_scores']
        
        # DEBUG: Log which result is being assigned to which demo index
        if result['outputs'] and DO_PRINT:
            result_solver_ids = [s_id for _, _, s_id, _ in result['outputs'][:3]]
            if DEBUG_VALIDATION:
                print_l(f"DEBUG AGGREGATE: Assigning demo[{i}] from result - first solvers: {result_solver_ids}")
        
        # Use update instead of union for better performance
        if prof is not None:
            union_start = timer()
        all_o = all_o.union(result['outputs'])
        if prof is not None:
            prof['batt.result.union'] = prof.get('batt.result.union', 0) + (timer() - union_start)
        
        # Update scores
        if prof is not None:
            score_start = timer()
        O = demo_task[i]['output']
        
        # DEBUG: Log when processing demo results to catch cross-task contamination
        if result['outputs'] and DEBUG_VALIDATION and DO_PRINT:
            print_l(f"DEBUG: task_id={task_id} demo[{i}] has {len(result['outputs'])} outputs")
        
        for t_n, evo, o_solver_id, okt in result['outputs']:
            C = okt
            _, score = eval_match(S, C, O)
            o_score.update(o_solver_id, score)
        if prof is not None:
            prof['batt.score.update'] = prof.get('batt.score.update', 0) + (timer() - score_start)
        
        # Update solver scores
        if prof is not None:
            dscore_start = timer()
        for s_item in result['solver_scores']:
            # Extract o_solver_id from s_item tuple: (t_n, solver_id, differ_id, result)
            if len(s_item) >= 2:
                o_solver_id = s_item[1]
                d_score.update(o_solver_id, s_item)
        if prof is not None:
            prof['batt.dscore.update'] = prof.get('batt.dscore.update', 0) + (timer() - dscore_start)

    # Aggregate test results (now processed in parallel with demo!)
    for result in test_results:
        if result is None:
            continue
            
        i = result['index']
        o['test'][i] = result['outputs']
        s['test'][i] = result['solver_scores']
        
        # Use update instead of union for better performance
        if prof is not None:
            union_start = timer()
        all_o = all_o.union(result['outputs'])
        if prof is not None:
            prof['batt.result.union'] = prof.get('batt.result.union', 0) + (timer() - union_start)
        
        # Update scores
        if prof is not None:
            score_start = timer()
        O = test_task[i]['output']
        
        # DEBUG: Log when processing test results to catch cross-task contamination
        if result['outputs'] and DEBUG_VALIDATION and DO_PRINT:
            print_l(f"DEBUG: task_id={task_id} test[{i}] has {len(result['outputs'])} outputs")
        
        for t_n, evo, o_solver_id, okt in result['outputs']:
            C = okt
            _, score = eval_match(S, C, O)
            o_score.update(o_solver_id, score)
        if prof is not None:
            prof['batt.score.update'] = prof.get('batt.score.update', 0) + (timer() - score_start)
        
        # Update solver scores
        if prof is not None:
            dscore_start = timer()
        for s_item in result['solver_scores']:
            # Extract o_solver_id from s_item tuple: (t_n, solver_id, differ_id, result)
            if len(s_item) >= 2:
                o_solver_id = s_item[1]
                d_score.update(o_solver_id, s_item)
        if prof is not None:
            prof['batt.dscore.update'] = prof.get('batt.dscore.update', 0) + (timer() - dscore_start)
    
    if prof is not None:
        prof['batt.aggregation.total'] = timer() - agg_start

    # NOTE Move this around when we start with 'eval' runs?
    if prof is not None:
        consolidate_start = timer()
    
    for o_solver_id in d_score.score.keys():
        for name in d_score.score[o_solver_id].keys():
            if name not in s_score:
                s_score[name] = S_Score()
            s_score[name].update(o_solver_id, d_score.score[o_solver_id][name]['score'])
    
    if prof is not None:
        prof['batt.score.consolidate'] = timer() - consolidate_start

    # Week 6B: Test samples now processed in parallel with demo samples above!
    # Old sequential test processing removed - all samples processed together
    
    len_task = len(demo_task) + len(test_task)
    elapsed = timer() - start_time
    return all_o, o_score, s_score


def check_save(path, score, max_files=32):
    # List subpaths in path
    root_path = Path(path)

    done = False
    while not done:
        with suppress(FileNotFoundError):
            paths = list(root_path.rglob("*"))
            done = True

    # List files (not folders) in subpaths
    files = [f for f in paths if f.is_file()]

    no_save = False
    while len(files) > max_files: 
        # Too many files, remove worst one before saving new one
        worst_score = None
        worst_time = None
        worst_file = None
        for file in files:
            if file.is_file():
                file_parts = file.relative_to(root_path).parts
                saved_o = int(file_parts[0])
                saved_t = int(file_parts[1])

                if worst_score is None or saved_o < worst_score:
                    worst_score = saved_o
                    worst_time = saved_t
                    worst_file = file
                elif saved_o == worst_score and saved_t < worst_time:
                    worst_time = saved_t
                    worst_file = file

        if score < worst_score:
            # New candidate is worse than worst saved one, don't save
            no_save = True
            break

        if worst_file is not None:
            with suppress(FileNotFoundError):
                os.remove(worst_file)
            files.remove(worst_file)

    return no_save


async def run_batt(total_data, task_i, task_id, d_score, start_time, pile_log_path, timeout=1, prof=None, batt_module_name='batt', batch_accumulator=None):
    """Run batt - async for validation, but check_batt is now synchronous"""
    # Log task start for crash/timeout detection
    _log_task_start(task_id, timeout)
    
    # Track execution time for timeout optimization
    run_batt_start = timer()
    
    if prof is not None:
        prof_call_start = timer()

    print_l(f'-- {task_id} - {task_i} start --') if DO_PRINT else None

    all_o, o_score, s_score = check_batt(total_data,
            task_i, task_id, d_score, start_time, pile_log_path, timeout=timeout, prof=prof, batt_module_name=batt_module_name, batch_accumulator=batch_accumulator)

    # print_l(f'-- {task_id} - {task_i} scored --') if DO_PRINT else None

    if prof is not None:
        prof['run_batt.check_batt'] += timer() - prof_call_start

    print_l(f'-- {task_id} - {task_i} done - {len(all_o)} candidates scored') if DO_PRINT else None

    # NOTE all_o contains candidates for 'demo' and 'test' tasks
    # TODO Avoid double work below
    t_log = 10
    max_files = 32
    
    # Phase 1: Quick filter - build solver bodies and check for duplicates
    if prof is not None:
        phase1_start = timer()
    
    candidate_data = []
    seen_bodies = {}  # Cache to detect duplicate solver bodies
    
    for candidate in all_o:
        sol_t, sol_e, sol_solver_id, sol_m = candidate
        
        task_o_score = o_score.get(sol_solver_id)
        solve_task = f'solver_dir/solve_{task_id}'
        
        # Quick check if score is too low before expensive operations
        if check_save(solve_task, task_o_score, max_files):
            continue
        
        # Track calls and build solver body (lightweight operation)
        done = track_solution(sol_t, None)
        
        solver_body = ''
        for t_num in sorted(done):
            # t_split = [item.strip() for item in t_call[t_num].value.split(',')]
            # t = [s[:-2] if s.endswith('.t') else s for s in t_split]

            t = t_call[t_num].value

            func = t[0]
            args = t[1:]
            solver_body += f'    t{t_num} = {func}({", ".join(args)})\n'
        solver_body += f'    return t{sol_t}\n'
        
        # Quick dedup check using body hash before expensive inline_variables
        body_hash = hashlib.md5(solver_body.encode()).hexdigest()
        if body_hash in seen_bodies:
            continue
        seen_bodies[body_hash] = True
        
        solver_source = f'def solve(S, I, C):\n{solver_body}'
        candidate_data.append({
            'candidate': candidate,
            'solver_source': solver_source,
            'solver_body': solver_body,
            'sol_t': sol_t,
            'sol_solver_id': sol_solver_id,
            'done': done,
            'task_id': task_id  # Add task_id for error reporting
        })
    
    if prof is not None:
        prof['run_batt.phase1_filter'] = timer() - phase1_start
    
    print_l(f'-- Filtered to {len(candidate_data)} unique candidates (from {len(all_o)})') if DO_PRINT else None
    
    # Phase 2: Batch inline_variables (the expensive AST operation)
    if prof is not None:
        phase2_start = timer()
    
    # Feature flag to disable inlining for debugging
    SKIP_INLINING = os.environ.get('SKIP_INLINING', '0') == '1'
    if SKIP_INLINING:
        print_l("INLINING DISABLED (SKIP_INLINING=1) - Using raw solver source")
    
    # Batch process inlining - do all at once to amortize AST overhead
    def inline_one(data):
        # If inlining is disabled, return raw source with empty md5
        if SKIP_INLINING:
            return {**data, 'inlined_source': data['solver_source'], 'md5_hash': 'disabled'}
        
        # Week 6E: Telemetry tracking
        with _inlining_stats_lock:
            _inlining_stats['total_attempts'] += 1
        
        try:
            # Use cached version for 2x speedup on warm cache
            inlined = cached_inline_variables(inline_variables, data['solver_source'])
            
            # Defensive check - ensure we got a string back
            if inlined is None:
                task_id = data.get('task_id', 'unknown')
                sol_solver_id = data.get('sol_solver_id', 'unknown')
                print_l(f"ERROR: inline_variables returned None for task_id={task_id} solver_id={sol_solver_id}")
                with _inlining_stats_lock:
                    _inlining_stats['other_errors'] += 1
                return None
            
            if not isinstance(inlined, str):
                task_id = data.get('task_id', 'unknown')
                sol_solver_id = data.get('sol_solver_id', 'unknown')
                print_l(f"ERROR: inline_variables returned {type(inlined).__name__} instead of str for task_id={task_id} solver_id={sol_solver_id}")
                with _inlining_stats_lock:
                    _inlining_stats['other_errors'] += 1
                return None
            
            md5 = hashlib.md5(inlined.encode()).hexdigest()
            with _inlining_stats_lock:
                _inlining_stats['success_count'] += 1
            return {**data, 'inlined_source': inlined, 'md5_hash': md5}
        except ValueError as e:
            # Handle ValueError from cached_inline_variables wrapper
            task_id = data.get('task_id', 'unknown')
            sol_solver_id = data.get('sol_solver_id', 'unknown')
            candidate = data.get('candidate', 'unknown')
            error_msg = str(e)
            
            # Check for timeout - this is the adaptive retry case
            if "timed out after" in error_msg:
                with _inlining_stats_lock:
                    _inlining_stats['timeout_count'] += 1
                
                if DEBUG_VALIDATION and DO_PRINT:
                    print_l(f"TIMEOUT: Inlining timeout for task_id={task_id} solver_id={sol_solver_id}")
                    print_l(f"  → Retrying with raw source (skip inlining)")
                
                # Retry: Skip inlining and use raw source (with timing)
                retry_start = time.time()
                try:
                    raw_source = data['solver_source']
                    md5 = hashlib.md5(raw_source.encode()).hexdigest()
                    retry_time_ms = (time.time() - retry_start) * 1000
                    with _inlining_stats_lock:
                        _inlining_stats['timeout_retry_success'] += 1
                        _inlining_stats['retry_time_ms'] += retry_time_ms
                    return {**data, 'inlined_source': raw_source, 'md5_hash': md5}
                except Exception as retry_error:
                    retry_time_ms = (time.time() - retry_start) * 1000
                    with _inlining_stats_lock:
                        _inlining_stats['timeout_retry_fail'] += 1
                        _inlining_stats['retry_time_ms'] += retry_time_ms
                    print_l(f"ERROR: Retry failed for task_id={task_id} solver_id={sol_solver_id}: {retry_error}")
                    return None
            
            # Check for thread exhaustion - retry with backoff
            elif "can't start new thread" in error_msg:
                print_l(f"THREAD EXHAUSTION: task_id={task_id} solver_id={sol_solver_id} - retrying with backoff")
                
                # Exponential backoff retry: 0.1s, 0.2s, 0.4s
                max_retries = 3
                for retry_num in range(max_retries):
                    backoff_time = 0.1 * (2 ** retry_num)  # 0.1s, 0.2s, 0.4s
                    time.sleep(backoff_time)
                    
                    try:
                        inlined = cached_inline_variables(inline_variables, data['solver_source'])
                        if inlined is not None and isinstance(inlined, str):
                            md5 = hashlib.md5(inlined.encode()).hexdigest()
                            with _inlining_stats_lock:
                                _inlining_stats['success_count'] += 1
                                _inlining_stats.setdefault('thread_retry_success', 0)
                                _inlining_stats['thread_retry_success'] += 1
                            print_l(f"  → Retry {retry_num + 1} succeeded after {backoff_time}s")
                            return {**data, 'inlined_source': inlined, 'md5_hash': md5}
                    except ValueError as retry_error:
                        if "can't start new thread" not in str(retry_error):
                            # Different error - stop retrying
                            break
                        # Same thread error - continue to next retry
                        if retry_num < max_retries - 1:
                            print_l(f"  → Retry {retry_num + 1} failed, waiting {backoff_time * 2}s")
                
                # All retries failed - use raw source as fallback
                print_l(f"  → All retries failed, using raw source")
                try:
                    raw_source = data['solver_source']
                    md5 = hashlib.md5(raw_source.encode()).hexdigest()
                    with _inlining_stats_lock:
                        _inlining_stats['other_errors'] += 1
                        _inlining_stats.setdefault('error_types', {})
                        _inlining_stats['error_types'].setdefault('thread_error', 0)
                        _inlining_stats['error_types']['thread_error'] += 1
                        _inlining_stats.setdefault('thread_retry_fallback', 0)
                        _inlining_stats['thread_retry_fallback'] += 1
                    return {**data, 'inlined_source': raw_source, 'md5_hash': md5}
                except Exception as fallback_error:
                    print_l(f"ERROR: Fallback failed for task_id={task_id} solver_id={sol_solver_id}: {fallback_error}")
                    with _inlining_stats_lock:
                        _inlining_stats['other_errors'] += 1
                    return None
            
            # Check for the specific "error return without exception set" error
            elif "error return without exception set" in error_msg:
                print_l(f"SKIP: Inlining failed with AST error for task_id={task_id} solver_id={sol_solver_id}: {error_msg}")
                with _inlining_stats_lock:
                    _inlining_stats['other_errors'] += 1
            else:
                print_l(f"Error inlining task_id={task_id} solver_id={sol_solver_id} candidate={candidate}: ValueError: {e}")
                with _inlining_stats_lock:
                    _inlining_stats['other_errors'] += 1
            return None
        except Exception as e:
            # Provide context about which solver failed
            task_id = data.get('task_id', 'unknown')
            sol_solver_id = data.get('sol_solver_id', 'unknown')
            candidate = data.get('candidate', 'unknown')
            error_type = type(e).__name__
            print_l(f"Error inlining task_id={task_id} solver_id={sol_solver_id} candidate={candidate}: {error_type}: {e}")
            with _inlining_stats_lock:
                _inlining_stats['other_errors'] += 1
            return None
    
    # Use thread pool for parallel inlining
    # CPU-only fix: Reduce concurrency to avoid thread exhaustion
    # CRITICAL: Use _safe_map_with_timeout to prevent hangs on stuck inline operations
    # Timeout: 0.1s per solver (vs 30s previously)
    #   - Normal solvers inline in <100ms
    #   - 0.1s is still generous for pathological cases
    #   - Prevents hanging on infinite loops in AST visitor
    if GPU_AVAILABLE:
        with ThreadPoolExecutor(max_workers=4) as executor:
            inlined_data = _safe_map_with_timeout(executor, inline_one, candidate_data, 
                                                 timeout_per_item=0.5, operation_name="inline_variables")
    else:
        # CPU-only: Use smaller pool to limit total threads
        with ThreadPoolExecutor(max_workers=2) as executor:
            inlined_data = _safe_map_with_timeout(executor, inline_one, candidate_data,
                                                 timeout_per_item=0.5, operation_name="inline_variables")
    
    # Filter out failures
    inlined_data = [d for d in inlined_data if d is not None]
    
    if prof is not None:
        prof['run_batt.phase2_inline_batch'] = timer() - phase2_start
    
    # Phase 3a: Batch validate all solvers in parallel
    if prof is not None:
        phase3a_start = timer()
    
    async def check_one_solver(data):
        """Validate a single solver and return timing info with score validation"""
        solver_source = data['solver_source']
        sol_solver_id = data['sol_solver_id']
        check_start = timer()
        # Use cached version for 5.5x speedup on warm cache
        timed_out, actual_score = await cached_check_solver(
            check_solver, total_data, solver_source, task_id, sol_solver_id, timeout
        )
        check_time = timer() - check_start
        t_log = 11 - int(math.log(check_time)) if check_time > 0 else 10
        
        # Compare actual score from re-execution vs saved score from batt()
        # Only flag mismatch if solver didn't timeout (timeout means incomplete execution)
        saved_score = o_score.get(sol_solver_id)
        score_mismatch = False
        if not timed_out and actual_score != saved_score:
            score_mismatch = True
            if DEBUG_VALIDATION and DO_PRINT:
                print_l(f"SCORE MISMATCH: {sol_solver_id} - saved_score={saved_score} actual_score={actual_score}")
        
        return {**data, 'timed_out': timed_out, 'actual_score': actual_score, 'saved_score': saved_score, 
                'score_mismatch': score_mismatch, 't_log': t_log, 'check_time': check_time}
    
    # Validate all solvers in parallel using asyncio.gather
    import asyncio
    validated_data = await asyncio.gather(*[check_one_solver(d) for d in inlined_data])
    
    if prof is not None:
        phase3a_time = timer() - phase3a_start
        prof['run_batt.phase3a_validate_batch'] = phase3a_time
        prof['run_batt.check_solver'] = sum(d['check_time'] for d in validated_data)
        print_l(f'-- Phase 3a: Validated {len(validated_data)} solvers in {phase3a_time:.3f}s (parallelized)')
    
    # Check for score mismatches
    score_mismatches = [d for d in validated_data if d.get('score_mismatch', False)]
    if score_mismatches and DEBUG_VALIDATION:
        print_l(f"WARNING: Found {len(score_mismatches)} score mismatches:")
        for d in score_mismatches[:5]:  # Show first 5
            print_l(f"  {d['sol_solver_id']}: saved={d['saved_score']} actual={d['actual_score']}")
        if len(score_mismatches) > 5:
            print_l(f"  ... and {len(score_mismatches) - 5} more")
    elif DEBUG_VALIDATION and DO_PRINT:
        print_l("INFO: No score mismatches found - all solvers validated correctly")
    
    # Phase 3b: Process validated results (file I/O, symlinks)
    if prof is not None:
        phase3b_start = timer()
        phase3b_ensure_dir_time = 0
        phase3b_check_save_time = 0
        phase3b_symlink_time = 0
        phase3b_score_calc_time = 0
    
    for data in validated_data:
        sol_t = data['sol_t']
        sol_solver_id = data['sol_solver_id']
        solver_source = data['solver_source']
        inlined_source = data['inlined_source']
        md5_hash = data['md5_hash']
        t_log = data['t_log']

        # Prepare storage folder
        if prof is not None:
            dir_start = timer()
        ensure_dir('solver_dir')
        solve_task = f'solver_dir/solve_{task_id}'
        ensure_dir(solve_task)
        if prof is not None:
            phase3b_ensure_dir_time += timer() - dir_start

        if prof is not None:
            score_start = timer()
        task_o_score = o_score.get(sol_solver_id)
        if prof is not None:
            phase3b_score_calc_time += timer() - score_start

        # Double-check score (might have changed)
        if prof is not None:
            check_start = timer()
        should_skip = check_save(solve_task, task_o_score, max_files)
        if prof is not None:
            phase3b_check_save_time += timer() - check_start
        
        if should_skip:
            continue

        if prof is not None:
            dir_start = timer()
        ensure_dir('solver_md5')
        if prof is not None:
            phase3b_ensure_dir_time += timer() - dir_start
            
        solver_md5_path = f'solver_md5/{md5_hash}.py'

        # Expand to .py file (only if doesn't exist)
        expand_start = timer()
        if not Path(solver_md5_path).exists():
            generate_expanded_content(inlined_source, solver_md5_path)
        if prof is not None:
            prof['run_batt.generate_expanded'] += timer() - expand_start

        if prof is not None:
            score_start = timer()
        task_o_score = o_score.get(sol_solver_id)
        if prof is not None:
            phase3b_score_calc_time += timer() - score_start
            
        solver_score = f'solver_dir/solve_{task_id}/{task_o_score}/{t_log}'

        if prof is not None:
            dir_start = timer()
        ensure_dir(solver_score)
        if prof is not None:
            phase3b_ensure_dir_time += timer() - dir_start
            
        solver_link = f'{solver_score}/{md5_hash}.py'

        if prof is not None:
            sym_start = timer()
        symlink(solver_md5_path, solver_link)
        if prof is not None:
            phase3b_symlink_time += timer() - sym_start

        # Collect differ data for this solver (will batch process all differs later)
        # Phase 4 moved outside the loop
    
    if prof is not None:
        phase3b_total = timer() - phase3b_start
        prof['run_batt.phase3b_file_ops'] = phase3b_total
        prof['run_batt.phase3b_ensure_dir'] = phase3b_ensure_dir_time
        prof['run_batt.phase3b_check_save'] = phase3b_check_save_time
        prof['run_batt.phase3b_symlink'] = phase3b_symlink_time
        prof['run_batt.phase3b_score_calc'] = phase3b_score_calc_time
        phase3b_overhead = phase3b_total - (phase3b_ensure_dir_time + phase3b_check_save_time + 
                                           phase3b_symlink_time + phase3b_score_calc_time + 
                                           prof.get('run_batt.generate_expanded', 0))
        prof['run_batt.phase3b_overhead'] = max(0, phase3b_overhead)
    
    # Phase 4: Batch process differs for all solvers
    if prof is not None:
        phase4_start = timer()
        phase4_build_time = 0
        phase4_inline_time = 0
        phase4_process_time = 0
    
    # Collect all differ data first
    if prof is not None:
        build_start = timer()
        
    differ_data_list = []
    for data in validated_data:
        sol_solver_id = data['sol_solver_id']
        for name, last_t in d_score.last_t.items():
            done_differ = track_solution(last_t, None)
            
            differ_body = ''
            for t_num in sorted(done_differ):
                # t_split = [item.strip() for item in t_call[t_num].value.split(',')]
                # t = [s[:-2] if s.endswith('.t') else s for s in t_split]

                t = t_call[t_num].value

                func = t[0]
                args = t[1:]
                differ_body += f'    t{t_num} = {func}({", ".join(args)})\n'
            differ_body += f'    return t{last_t}\n'
            
            differ_source = f'def differ(S, I, C):\n{differ_body}'
            differ_data_list.append({
                'name': name,
                'differ_source': differ_source,
                'sol_solver_id': sol_solver_id
            })
    
    if prof is not None:
        phase4_build_time = timer() - build_start
    
    # Batch inline differs
    if prof is not None:
        inline_start = timer()
    
    # Feature flag to disable inlining for debugging
    # (same flag as solver inlining to keep them in sync)
    # Use module-level to track if we've logged this message already
    global _differ_inlining_logged
    if SKIP_INLINING and not globals().get('_differ_inlining_logged', False):
        print_l("DIFFER INLINING DISABLED (SKIP_INLINING=1) - Using raw differ source")
        globals()['_differ_inlining_logged'] = True  # Log only once
        
    def inline_differ(data):
        # If inlining is disabled, return raw source with empty md5
        if SKIP_INLINING:
            return {**data, 'inlined_source': data['differ_source'], 'md5_hash': 'disabled'}
        
        # Week 6E: Telemetry tracking
        with _inlining_stats_lock:
            _inlining_stats['total_attempts'] += 1
        
        try:
            # Use cached version for 2x speedup on warm cache
            inlined = cached_inline_variables(inline_variables, data['differ_source'])
            
            # Defensive check - ensure we got a string back
            if inlined is None:
                print_l(f"ERROR: inline_variables returned None for differ {data.get('name', 'unknown')}")
                with _inlining_stats_lock:
                    _inlining_stats['other_errors'] += 1
                return None
            
            if not isinstance(inlined, str):
                print_l(f"ERROR: inline_variables returned {type(inlined).__name__} instead of str for differ {data.get('name', 'unknown')}")
                with _inlining_stats_lock:
                    _inlining_stats['other_errors'] += 1
                return None
            
            md5 = hashlib.md5(inlined.encode()).hexdigest()
            with _inlining_stats_lock:
                _inlining_stats['success_count'] += 1
            return {**data, 'inlined_source': inlined, 'md5_hash': md5}
        except ValueError as e:
            # Handle ValueError from cached_inline_variables wrapper
            differ_name = data.get('name', 'unknown')
            error_msg = str(e)
            
            # Check for timeout - this is the adaptive retry case
            if "timed out after" in error_msg:
                with _inlining_stats_lock:
                    _inlining_stats['timeout_count'] += 1
                
                if DEBUG_VALIDATION and DO_PRINT:
                    print_l(f"TIMEOUT: Inlining timeout for differ {differ_name}")
                    print_l(f"  → Retrying with raw source (skip inlining)")
                
                # Retry: Skip inlining and use raw source (with timing)
                retry_start = time.time()
                try:
                    raw_source = data['differ_source']
                    md5 = hashlib.md5(raw_source.encode()).hexdigest()
                    retry_time_ms = (time.time() - retry_start) * 1000
                    with _inlining_stats_lock:
                        _inlining_stats['timeout_retry_success'] += 1
                        _inlining_stats['retry_time_ms'] += retry_time_ms
                    return {**data, 'inlined_source': raw_source, 'md5_hash': md5}
                except Exception as retry_error:
                    retry_time_ms = (time.time() - retry_start) * 1000
                    with _inlining_stats_lock:
                        _inlining_stats['timeout_retry_fail'] += 1
                        _inlining_stats['retry_time_ms'] += retry_time_ms
                    print_l(f"ERROR: Retry failed for differ {differ_name}: {retry_error}")
                    return None
            
            # Check for thread exhaustion - retry with backoff
            elif "can't start new thread" in error_msg:
                print_l(f"THREAD EXHAUSTION: Differ {differ_name} - retrying with backoff")
                
                # Exponential backoff retry: 0.1s, 0.2s, 0.4s
                max_retries = 3
                for retry_num in range(max_retries):
                    backoff_time = 0.1 * (2 ** retry_num)  # 0.1s, 0.2s, 0.4s
                    time.sleep(backoff_time)
                    
                    try:
                        inlined = cached_inline_variables(inline_variables, data['differ_source'])
                        if inlined is not None and isinstance(inlined, str):
                            md5 = hashlib.md5(inlined.encode()).hexdigest()
                            with _inlining_stats_lock:
                                _inlining_stats['success_count'] += 1
                                _inlining_stats.setdefault('thread_retry_success', 0)
                                _inlining_stats['thread_retry_success'] += 1
                            print_l(f"  → Retry {retry_num + 1} succeeded after {backoff_time}s")
                            return {**data, 'inlined_source': inlined, 'md5_hash': md5}
                    except ValueError as retry_error:
                        if "can't start new thread" not in str(retry_error):
                            # Different error - stop retrying
                            break
                        # Same thread error - continue to next retry
                        if retry_num < max_retries - 1:
                            print_l(f"  → Retry {retry_num + 1} failed, waiting {backoff_time * 2}s")
                
                # All retries failed - use raw source as fallback
                print_l(f"  → All retries failed, using raw source")
                try:
                    raw_source = data['differ_source']
                    md5 = hashlib.md5(raw_source.encode()).hexdigest()
                    with _inlining_stats_lock:
                        _inlining_stats['other_errors'] += 1
                        _inlining_stats.setdefault('error_types', {})
                        _inlining_stats['error_types'].setdefault('thread_error', 0)
                        _inlining_stats['error_types']['thread_error'] += 1
                        _inlining_stats.setdefault('thread_retry_fallback', 0)
                        _inlining_stats['thread_retry_fallback'] += 1
                    return {**data, 'inlined_source': raw_source, 'md5_hash': md5}
                except Exception as fallback_error:
                    print_l(f"ERROR: Fallback failed for differ {differ_name}: {fallback_error}")
                    with _inlining_stats_lock:
                        _inlining_stats['other_errors'] += 1
                    return None
            
            # Check for the specific "error return without exception set" error
            elif "error return without exception set" in error_msg:
                print_l(f"SKIP: Inlining differ failed with AST error for {differ_name}: {error_msg}")
                with _inlining_stats_lock:
                    _inlining_stats['other_errors'] += 1
                    # Track specific error types
                    _inlining_stats.setdefault('error_types', {})
                    _inlining_stats['error_types'].setdefault('ast_error', 0)
                    _inlining_stats['error_types']['ast_error'] += 1
            else:
                print_l(f"Error inlining differ {differ_name}: ValueError: {e}")
                with _inlining_stats_lock:
                    _inlining_stats['other_errors'] += 1
                    # Track specific error types
                    _inlining_stats.setdefault('error_types', {})
                    _inlining_stats['error_types'].setdefault('other_value_error', 0)
                    _inlining_stats['error_types']['other_value_error'] += 1
            return None
        except Exception as e:
            error_type = type(e).__name__
            differ_name = data.get('name', 'unknown')
            error_msg = str(e)
            print_l(f"Error inlining differ {differ_name}: {error_type}: {e}")
            with _inlining_stats_lock:
                _inlining_stats['other_errors'] += 1
                # Track specific error types
                _inlining_stats.setdefault('error_types', {})
                error_key = 'thread_error' if "can't start new thread" in error_msg else error_type.lower()
                _inlining_stats['error_types'].setdefault(error_key, 0)
                _inlining_stats['error_types'][error_key] += 1
            return None
    
    # CPU-only fix: Reduce concurrency to avoid thread exhaustion  
    # CRITICAL: Use _safe_map_with_timeout to prevent hangs on stuck inline operations
    # Timeout: 0.1s per differ (vs 30s previously)
    #   - Normal differs inline in <100ms
    #   - 0.1s is still generous for pathological cases
    if GPU_AVAILABLE:
        with ThreadPoolExecutor(max_workers=4) as executor:
            inlined_differs = _safe_map_with_timeout(executor, inline_differ, differ_data_list,
                                                    timeout_per_item=0.5, operation_name="inline_differ")
    else:
        # CPU-only: Use smaller pool to limit total threads
        with ThreadPoolExecutor(max_workers=2) as executor:
            inlined_differs = _safe_map_with_timeout(executor, inline_differ, differ_data_list,
                                                    timeout_per_item=0.5, operation_name="inline_differ")
    
    inlined_differs = [d for d in inlined_differs if d is not None]
    
    if prof is not None:
        phase4_inline_time = timer() - inline_start
    
    # Process inlined differs
    if prof is not None:
        process_start = timer()
        
    for differ_data in inlined_differs:
        name = differ_data['name']
        inlined_source = differ_data['inlined_source']
        md5_hash = differ_data['md5_hash']
        sol_solver_id = differ_data['sol_solver_id']
        
        ensure_dir('differ_dir')
        ensure_dir('differ_md5')
        differ_md5_path = f'differ_md5/{md5_hash}.py'
        
        if not Path(differ_md5_path).exists():
            generate_expanded_content(inlined_source, differ_md5_path)

        # Differs aren't always scored
        if name not in s_score:
            continue

        task_s_score = s_score[name].get(sol_solver_id)

        differ_task = f'differ_dir/solve_{task_id}'
        if check_save(differ_task, task_s_score, max_files):
            continue

        # Use t_log from the corresponding solver
        # Find the matching validated_data entry
        t_log = 10  # default
        for vdata in validated_data:
            if vdata['sol_solver_id'] == sol_solver_id:
                t_log = vdata['t_log']
                break
        
        differ_score = f'differ_dir/solve_{task_id}/{task_s_score}/{t_log}'
        ensure_dir(differ_score)
        differ_link = f'{differ_score}/{md5_hash}.py'
        symlink(differ_md5_path, differ_link)
    
    if prof is not None:
        phase4_process_time = timer() - process_start
        phase4_total = timer() - phase4_start
        prof['run_batt.phase4_differs'] = phase4_total
        prof['run_batt.phase4_build'] = phase4_build_time
        prof['run_batt.phase4_inline'] = phase4_inline_time
        prof['run_batt.phase4_process'] = phase4_process_time
        
        # Add inlining error stats to profiling data
        with _inlining_stats_lock:
            if _inlining_stats.get('other_errors', 0) > 0:
                prof['run_batt.inline_errors'] = _inlining_stats['other_errors']
            if _inlining_stats.get('timeout_count', 0) > 0:
                prof['run_batt.inline_timeouts'] = _inlining_stats['timeout_count']
            
            # Add breakdown by error type if available
            error_types = _inlining_stats.get('error_types', {})
            for error_key, count in error_types.items():
                prof[f'run_batt.inline_error.{error_key}'] = count

    # Log successful execution stats for timeout optimization
    execution_time = timer() - run_batt_start
    _log_execution_stats(task_id, execution_time, error_type=None, 
                       error_msg=None, timeout_value=timeout)
    
    # Week 6E: Log and print inlining telemetry
    _log_inlining_stats()
    if DO_DEBUG:
        _print_inlining_summary()
    
    # Phase 2b: Flush batch accumulator
    if batch_accumulator:
        stats = batch_accumulator.flush_and_log()
        if DO_PRINT:
            print_l(f"-- {task_id} batch stats: added={stats['total_grids_added']} processed={stats['total_grids_processed']}")
    
    # No timeout
    return False, d_score


# See similar function in card.py
def track_solution(t_num, done):
    if done is None:
        done = set()

    if t_num not in done:
        done.add(t_num)

    call = t_call[t_num].value

    # if t_list := re.findall(r't(\d+)', call):
    #     for t_str in t_list:
    #         t_num = int(t_str)
                
    if t_list := [int(item[1:]) for item in call if re.match(r't\d+', item)]:
        for t_num in t_list:
            if t_num not in done:
                done.add(t_num)
                track_solution(t_num, done)

    return done


def pick_rnd_task(task_list, total_data):
    task_sizes = []
    for task_id in task_list:
        size = 0
        for S in total_data['demo'][task_id] + total_data['test'][task_id]:
            for ex in S.values():
                size += sum(len(inner) for inner in ex)
        task_sizes.append(size)

    weighted_tasks = list(zip(task_list, task_sizes))
    inverse_weights = [1/size for _, size in weighted_tasks]

    task_id = random.choices(
        [t_id for t_id, _ in weighted_tasks],
        weights=inverse_weights,
        k=1
    )[0]

    return [task_id]


async def main_mega_batch(do_list, start=0, count=0, batch_size=1000, batt_module_name='batt', enable_timing=False, data='train'):
    """
    Mega-batch mode: Process all tasks using GPU batch optimization.
    
    Instead of calling batt() 4000+ times sequentially, this:
    1. Collects all inputs from all tasks
    2. Batches them into chunks of ~1000
    3. Processes each batch (Week 5: GPU vectorized)
    4. Merges results back per-task
    
    Expected speedup (Week 5): 4.8-9x faster than sequential
    """
    print(f"\n{'='*60}")
    print("MEGA-BATCH MODE - GPU Batch Processing")
    print(f"{'='*60}")
    print(f"Batch size: {batch_size}")
    print(f"Batt module: {batt_module_name}")
    
    start_time = timer()
    
    # Load data based on data argument
    if data == 'train':
        total_data = get_data(train=True, sort_by_size=True)
    elif data == 'eval':
        total_data = get_data(train=False, sort_by_size=True)
    else:  # data == 'both'
        train_data = get_data(train=True, sort_by_size=True)
        eval_data = get_data(train=False, sort_by_size=True)
        total_data = {k: {**train_data[k], **eval_data[k]} for k in ['demo', 'test']}
    
    # Determine task list
    full_list = list(total_data['demo'].keys())
    
    if start == 0 and count < 0:
        task_list = random.sample(full_list, -count)
    else:
        task_list = full_list[start:start + count] if count > 0 else full_list[start:]
    
    if do_list is None:
        do_list = pick_rnd_task(task_list, total_data)
    elif len(do_list) == 0:
        do_list = task_list
    
    print(f"Processing {len(do_list)} tasks")
    
    # Initialize mega-batch coordinator
    coordinator = MegaBatchCoordinator(
        batt_module_name=batt_module_name,
        batch_size=batch_size
    )
    
    # Process all tasks with mega-batch
    pile_log_path = 'pile.log'
    if os.path.isfile(pile_log_path):
        os.remove(pile_log_path)
    
    print("\nCollecting inputs from all tasks...")
    results, elapsed = coordinator.process_all(total_data, do_list, pile_log_path)
    
    print(f"\n{'='*60}")
    print("MEGA-BATCH RESULTS")
    print(f"{'='*60}")
    print(f"Total time: {elapsed:.3f}s")
    print(f"Tasks processed: {len(results)}")
    
    # Calculate statistics
    total_samples = 0
    total_candidates = 0
    for task_id, task_results in results.items():
        demo_count = len(task_results['demo'])
        test_count = len(task_results['test'])
        total_samples += demo_count + test_count
        
        # Count candidates
        for sample_results in task_results['demo'].values():
            total_candidates += len(sample_results.get('o', []))
        for sample_results in task_results['test'].values():
            total_candidates += len(sample_results.get('o', []))
    
    print(f"Total samples: {total_samples}")
    print(f"Total candidates: {total_candidates}")
    print(f"Average time per sample: {elapsed/total_samples*1000:.2f}ms")
    print(f"Average time per task: {elapsed/len(results):.3f}s")
    
    if enable_timing:
        print("\nPerformance Notes:")
        print("  - This is CPU sequential baseline (Week 4)")
        print("  - Week 5 will add GPU vectorization")
        print("  - Expected Week 5 speedup: 4.8-9x faster")
        print(f"  - Projected GPU time: {elapsed/6:.3f}s (assuming 6x speedup)")
    
    print(f"{'='*60}\n")
    
    return results


async def main(do_list, start=0, count=0, timeout=1, enable_timing=False, profile=None, batt_module_name='batt', data='train'):
    # Load data based on data argument
    if data == 'train':
        total_data = get_data(train=True, sort_by_size=True)
    elif data == 'eval':
        total_data = get_data(train=False, sort_by_size=True)
    else:  # data == 'both'
        train_data = get_data(train=True, sort_by_size=True)
        eval_data = get_data(train=False, sort_by_size=True)
        total_data = {k: {**train_data[k], **eval_data[k]} for k in ['demo', 'test']}

    # NOTE We could have a task list just for unsolved tasks
    full_list = list(total_data['demo'].keys())

    if start == 0 and count < 0:
        task_list = random.sample(full_list, -count)
    else:
        task_list = full_list[start:start + count] if count > 0 else full_list[start:]

    if do_list is None:
        # If count is negative, we already randomly sampled, so use all of task_list
        if start == 0 and count < 0:
            do_list = task_list
        else:
            do_list = pick_rnd_task(task_list, total_data)
    elif len(do_list) == 0:
        # List all tasks
        do_list = task_list

    # Run batt for each task in do_list
    start_time = timer()
    pile_log_path = 'pile.log'
    if os.path.isfile(pile_log_path):
        os.remove(pile_log_path)

    timeouts = 0
    prof = defaultdict(float) if enable_timing else None
    if prof is not None:
        # Register profiler with modules that support it
        if hasattr(utils_module, 'set_profiler'):
            utils_module.set_profiler(prof)
        if hasattr(expand_solver_module, 'set_profiler'):
            expand_solver_module.set_profiler(prof)
    
    # Phase 2b: Initialize batch accumulator for all tasks
    # Note: Disabled GPU (use_gpu=False) - GPU operations not in hot path for test data
    # GPU should accelerate DSL operations during solver execution, not batch processing
    # See PHASE3_ROOT_CAUSE.md for detailed analysis
    batch_acc = BatchSolverAccumulator(batch_size=100, use_gpu=False)
    
    for task_i, task_id in enumerate(do_list):
        d_score = D_Score()
        loop_start = timer() if prof is not None else None
        timed_out = await run_batt(total_data, task_i, task_id, d_score, start_time, pile_log_path, timeout, prof=prof, batt_module_name=batt_module_name, batch_accumulator=batch_acc)
        if prof is not None:
            prof['main.run_batt'] += timer() - loop_start
        if timed_out:
            timeouts += 1
        
    print(f'{len(do_list)} tasks - {timeouts} timeouts')

    # Print cache statistics
    print_cache_stats()

    # Print lightweight timing report
    if prof is not None:
        print("\nTiming summary (seconds):")
        for k, v in sorted(prof.items(), key=lambda kv: kv[1], reverse=True):
            print(f"  {k:32s} {v:8.3f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run batt on specified tasks')
    parser.add_argument('-i', '--task_ids', nargs='*', default=None,
                        help='List of task IDs to run (default: random task)')
    parser.add_argument('-s', '--start', type=int, default=0,
                        help='Start from this task number (default: 0)')
    parser.add_argument('-c', '--count', type=int, default=0,
                        help='Number of tasks to run (default: 0 - all tasks)')
    parser.add_argument('-t', '--timeout', type=float, default=10,
                        help='Timeout for each task in seconds (default: 10)')
    parser.add_argument('-b', '--batt_import', type=str, default='tmp_batt_onerun_run',
                        help='Module to import for batt (default: tmp_batt_onerun_run)')
    parser.add_argument('--timing', action='store_true', help='Print lightweight timing breakdown')
    parser.add_argument('--cprofile', action='store_true', help='Run with cProfile and print top stats')
    parser.add_argument('--cprofile-top', type=int, default=30, help='Number of top functions to show in cProfile')
    parser.add_argument('--mega-batch', action='store_true', help='Use mega-batch GPU processing (4000+ samples)')
    parser.add_argument('--batch-size', type=int, default=1000, help='Batch size for mega-batch mode (default: 1000)')
    parser.add_argument('--data', help="Data to use: 'train', 'eval', or 'both' (default: train)", 
                        type=str, default='train', choices=['train', 'eval', 'both'])
    args = parser.parse_args()

    # Choose execution mode
    if args.mega_batch:
        # Mega-batch mode: GPU batch processing (Week 4-5)
        # Batt module will be loaded by MegaBatchCoordinator
        asyncio.run(main_mega_batch(
            do_list=args.task_ids,
            start=args.start,
            count=args.count,
            batch_size=args.batch_size,
            batt_module_name=args.batt_import,
            enable_timing=args.timing,
            data=args.data
        ))
    else:
        # Standard mode: Load batt module for traditional processing
        batt_module = importlib.import_module(args.batt_import)
        batt = batt_module.batt if hasattr(batt_module, 'batt') else None
        
        if batt is None:
            raise ValueError(f"Module {args.batt_import} has no batt function")

        call_module = importlib.import_module(f'{args.batt_import}_call')
        t_call = call_module.t_call if hasattr(call_module, 't_call') else {}

        # # Try prioritizing mix_task_ids included by card.py
        # mix_module = importlib.import_module(f'{args.batt_import}_mix')
        # mix_task_ids = mix_module.mix_task_ids if hasattr(mix_module, 'mix_task_ids') else {}
        # print_l(f'Prioritizing: {mix_task_ids = }')
        # args.task_ids = mix_task_ids

        # Initialize caching infrastructure
        init_cache()
        
        if args.cprofile:
            import cProfile, pstats, io
            pr = cProfile.Profile()
            pr.enable()
            asyncio.run(main(do_list=args.task_ids, start=args.start, count=args.count, timeout=args.timeout, enable_timing=args.timing, batt_module_name=args.batt_import, data=args.data))
            pr.disable()
            s = io.StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
            ps.print_stats(args.cprofile_top)
            print('\n[cProfile cumulative top]')
            print(s.getvalue())
            s = io.StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
            ps.print_stats(args.cprofile_top)
            print('\n[cProfile tottime top]')
            print(s.getvalue())
        else:
            asyncio.run(main(do_list=args.task_ids, start=args.start, count=args.count, timeout=args.timeout, enable_timing=args.timing, batt_module_name=args.batt_import, data=args.data))