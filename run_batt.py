import argparse
import random
import re
import ast
import hashlib
import math
import importlib
import os
import asyncio

import dill as pickle

from contextlib import suppress
from timeit import default_timer as timer
from pathlib import Path
from collections import defaultdict
from contextlib import contextmanager

from utils import *
import utils as utils_module
from expand_solver import expand_file, generate_expanded_content
import expand_solver as expand_solver_module
from run_test import check_solver_speed

from concurrent.futures import ThreadPoolExecutor, as_completed
try:
    import cupy as cp
    from dsl import GPU_AVAILABLE
    # Import optimized GPU batch processor
    from gpu_optimizations import KaggleGPUOptimizer
    
    if GPU_AVAILABLE:
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
    else:
        gpu_optimizer = None
except ImportError:
    GPU_AVAILABLE = False
    gpu_optimizer = None
    print("GPU Support: Disabled (CuPy not available)")

import multiprocessing as mp

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
        # NOTE: Add whether it's iz or zo differ
        # or just pick the best score?
        last_t, s_solver_id, d_name, return_tuple = s_item

        # Keep track of last_t per differ
        if s_solver_id == 'None':
            self.last_t[d_name] = last_t

        if solver_id not in self.score:
            self.score[solver_id] = {}
        if d_name not in self.score[solver_id]:
            self.score[solver_id][d_name] = {
                'last_t': self.last_t[d_name],
                'iz': 0,
                'zo': 0    
            }
        
        # if not return_tuple.ok or type(return_tuple.t) != tuple or type(return_tuple.t[0]) != int:
        if type(return_tuple) != tuple or type(return_tuple[0]) != int:
            return

        # size = return_tuple.t[0]
        size = return_tuple[0]

        # Score for iz differ
        if s_solver_id == 'None':
            self.score[solver_id][d_name]['iz'] += size > 0
        if s_solver_id == solver_id:
            self.score[solver_id][d_name]['iz'] += size == 0

        # Score for zo differ
        if s_solver_id == 'None':
            self.score[solver_id][d_name]['zo'] += size == 0
        if s_solver_id == solver_id:
            self.score[solver_id][d_name]['zo'] += size > 0


async def check_batt(total_data, task_i, task_id, d_score, start_time, pile_log_path, timeout=1, prof=None):
    task_start = timer()
    demo_task = total_data['demo'][task_id]
    test_task = total_data['test'][task_id]
    # total_task = total_data['demo'][task_id] + total_data['test'][task_id]

    o = {'demo': {}, 'test': {}}
    s = {'demo': {}, 'test': {}}
    all_o = set()
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in demo_task)

    print_l(f'-- {task_id} - {task_i} --') if DO_PRINT else None

    o_score = O_Score()
    s_score = {}
    for i, sample in enumerate(demo_task):
        I = sample['input']
        O = sample['output']
        if prof is not None:
            prof_start = timer()
        solve_timed_out, solve_result = await run_with_timeout(batt,
            [task_id, S, I, None, pile_log_path], timeout)
        if prof is not None:
            prof['batt.demo.run_with_timeout'] += timer() - prof_start

        if solve_timed_out and DO_PRINT:
            print_l(f'-- {task_id} - demo[{i}] timed out')

        t_set = set()
        if solve_result is not None:
            o['demo'][i], _ = solve_result

            print_l(f"demo[{i}] - {task_id} - {len(o['demo'][i])}") if DO_PRINT else None

            all_o = all_o.union(o['demo'][i])
            for t_n, evo, o_solver_id, okt in o['demo'][i]:
                # if not okt.ok:
                #     continue

                # Compare candidate C with expected output O
                # C = okt.t
                C = okt
                if match := C == O:
                    print_l(f'- {o_solver_id = } - {match = }')
                o_score.update(o_solver_id, match)

                # We know the correct output for both train and eval tasks
                diff_timed_out, diff_result = await run_with_timeout(batt,
                    [task_id, S, I, O, pile_log_path], timeout)
                    # [task_id, S, I, C, pile_log_path], timeout)

                if diff_result is not None:
                    _, s['demo'][i] = diff_result

                    for s_item in s['demo'][i]:
                        d_score.update(o_solver_id, s_item)

    # NOTE Move this around when we start with 'eval' runs?
    for o_solver_id in d_score.score.keys():
        for name in d_score.score[o_solver_id].keys():
            if name not in s_score:
                s_score[name] = {'iz': S_Score(), 'zo': S_Score()}
            for score_type in ['iz', 'zo']:
                s_score[name][score_type].update(o_solver_id, d_score.score[o_solver_id][name][score_type])

    for i, sample in enumerate(test_task):
        I = sample['input']
        O = sample['output']
        if prof is not None:
            prof_start = timer()
        solve_timed_out, solve_result = await run_with_timeout(batt,
            [task_id, S, I, None, pile_log_path], timeout)
        if prof is not None:
            prof['batt.test.run_with_timeout'] += timer() - prof_start

        if solve_timed_out and DO_PRINT:
            print_l(f'-- {task_id} - test[{i}] timed out')

        t_set = set()
        if solve_result is not None:
            o['test'][i], _ = solve_result

            print_l(f"test[{i}] - {task_id} - {len(o['test'][i])}") if DO_PRINT else None

            all_o = all_o.union(o['test'][i])
            for t_n, evo, o_solver_id, okt in o['test'][i]:
                # if not okt.ok:
                #     continue

                # Compare candidate C with expected output O
                # C = okt.t
                C = okt
                if match := C == O:
                    print_l(f'- {o_solver_id = } - {match = }')
                o_score.update(o_solver_id, match)

                # We know the correct output for demo tasks, not eval tasks
                # TODO Try comparing to C when we start dealing with eval tasks
                # XXX Or just do that all the time, to simplify? The performance
                # hit is only on demoing tasks, that are pre-processed, right? 
                diff_timed_out, diff_result = await run_with_timeout(batt,
                    # [task_id, S, I, O, pile_log_path], timeout)
                    [task_id, S, I, C, pile_log_path], timeout)

                if diff_result is not None:
                    _, s['test'][i] = diff_result

                    for s_item in s['test'][i]:
                        d_score.update(o_solver_id, s_item)

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


async def run_batt(total_data, task_i, task_id, d_score, start_time, pile_log_path, timeout=1, prof=None):
    if prof is not None:
        prof_call_start = timer()

    print_l(f'-- {task_id} - {task_i} start --') if DO_PRINT else None

    all_o, o_score, s_score = await check_batt(total_data,
            task_i, task_id, d_score, start_time, pile_log_path, timeout=1, prof=prof)

    print_l(f'-- {task_id} - {task_i} scored --') if DO_PRINT else None

    if prof is not None:
        prof['run_batt.check_batt'] += timer() - prof_call_start

    print_l(f'-- {task_id} - {task_i} done - {len(all_o)} candidates scored') if DO_PRINT else None

    # NOTE all_o contains candidates for 'demo' and 'test' tasks
    # TODO Avoid double work below
    t_log = 10
    max_files = 32
    for candidate in all_o:
        sol_t, sol_e, sol_solver_id, sol_m = candidate

        # Prepare storage folder
        ensure_dir('solver_dir')
        solve_task = f'solver_dir/solve_{task_id}'
        ensure_dir(solve_task)

        task_o_score = o_score.get(sol_solver_id)

        if check_save(solve_task, task_o_score, max_files):
            # print_l(f'Skip saving solver {sol_solver_id} as worse than existing ones')
            continue

        # Track calls then reverse sequence to rebuild solver
        done = track_solution(sol_t, None)

        # Build candidate body
        solver_body = ''
        for t_num in sorted(done):
            t_split = [item.strip() for item in t_call[t_num].split(',')]
            t = [s[:-2] if s.endswith('.t') else s for s in t_split]

            func = t[0]
            args = t[1:]
            solver_body += f'    t{t_num} = '
            solver_body += f'{func}('
            solver_body += ', '.join(args)
            solver_body += ')\n'
        solver_body += f'    return t{sol_t}\n'

        # Get md5_hash of inlined source code
        solver_source = f'def solve(S, I, C):\n{solver_body}'
        inlined_source = inline_variables(solver_source)
        md5_hash = hashlib.md5(inlined_source.encode()).hexdigest()

        # Put task_id in function name to make solvers_dir.py usable
        # solver_source = re.sub(r'def solve\((.*)\):', f'def solve_{task_id}(\g<1>):', solver_source)
        # inlined_source = inline_variables(solver_source)

        # ensure_dir('solver_def')
        # solver_def_path = f'solver_def/{md5_hash}.def'

        ensure_dir('solver_md5')
        solver_md5_path = f'solver_md5/{md5_hash}.py'

        check_start = timer()
        timed_out = await check_solver_speed(total_data, solver_source, task_id, sol_solver_id, timeout)
        t_log = 11 - int(math.log(timer() - check_start))

        # if not Path(solver_def_path).exists():
        #     with open(solver_def_path, 'w') as f:
        #         f.write(inlined_source)
        #         f.write('\n')

        # Expand to .py file
        if not Path(solver_md5_path).exists():
            # expand_file(solver_def_path, solver_md5_path, None, True)
            # TODO Check if generate_expanded_content can be stremlined
            generate_expanded_content(inlined_source, solver_md5_path)

        task_o_score = o_score.get(sol_solver_id)
        solver_score = f'solver_dir/solve_{task_id}/{task_o_score}/{t_log}'

        ensure_dir(solver_score)
        solver_link = f'{solver_score}/{md5_hash}.py'

        symlink(solver_md5_path, solver_link)

        # TODO Control this with option
        # # Check things
        # python_exp = 'python expand_solver.py -q --source solver_dir/ --solvers-file solvers_dir.py'
        # python_cmd = f'python run_test.py --solvers solvers_dir -k {task_id}_{md5_hash}'
        # os.system(python_exp)
        # assert(os.system(python_cmd) == 0), f"Unfit candidate found by:\n{python_cmd}"

        for name, last_t in d_score.last_t.items():

            # task_s_score_iz = s_score[name]['iz'].get(sol_solver_id)
            # task_s_score_zo = s_score[name]['zo'].get(sol_solver_id)
            # if task_s_score_iz == 0 and task_s_score_zo == 0:
            #     continue

            # print_l(f"{name} - {last_t}")
            done = track_solution(last_t, None)

            # Build differ body
            differ_body = ''
            for t_num in sorted(done):
                t_split = [item.strip() for item in t_call[t_num].split(',')]
                t = [s[:-2] if s.endswith('.t') else s for s in t_split]

                func = t[0]
                args = t[1:]
                differ_body += f'    t{t_num} = '
                differ_body += f'{func}('
                differ_body += ', '.join(args)
                differ_body += ')\n'
            differ_body += f'    return t{last_t}\n'

            differ_source = f'def differ(S, I, C):\n{differ_body}'
            inlined_source = inline_variables(differ_source)
            md5_hash = hashlib.md5(inlined_source.encode()).hexdigest()

            ensure_dir('differ_dir')

            # ensure_dir('differ_def')
            # differ_def_path = f'differ_def/{md5_hash}.def'

            ensure_dir('differ_md5')
            differ_md5_path = f'differ_md5/{md5_hash}.py'

            # if not Path(differ_def_path).exists():
            #     with open(differ_def_path, 'w') as f:
            #         f.write(inlined_source)
            #         f.write('\n')

            # Expand to .py file
            if not Path(differ_md5_path).exists():
                # expand_file(differ_def_path, differ_md5_path, None, True)
                generate_expanded_content(inlined_source, differ_md5_path)

            for score_type in ['iz', 'zo']:
                # Differs aren't always scored
                if name not in s_score:
                    continue

                task_s_score = s_score[name][score_type].get(sol_solver_id)

                differ_task = f'differ_dir/{score_type}/solve_{task_id}'
                if check_save(differ_task, task_s_score, max_files):
                    # print_l(f'Skip saving differ {name} as worse than existing ones')
                    continue


                # if task_s_score == 0:
                #     continue

                # differ_score = f'differ_dir/solve_{task_id}/{score_type}/{task_s_score}/{t_log}'
                # differ_link = f'{differ_score}/{solver_md5}/{md5_hash}.py'
                # ensure_dir(f'{differ_score}/{solver_md5}')
                differ_score = f'differ_dir/{score_type}/solve_{task_id}/{task_s_score}/{t_log}'
                ensure_dir(differ_score)
                differ_link = f'{differ_score}/{md5_hash}.py'
                symlink(differ_md5_path, differ_link)

    # No timeout
    return False, d_score


def track_solution(t_num, done):
    if done is None:
        done = set()

    if t_num not in done:
        done.add(t_num)

    call = t_call[t_num]

    if t_list := re.findall(r't(\d+)', call):
        for t_str in t_list:
            t_num = int(t_str)
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


async def main(do_list, start=0, count=0, timeout=1, enable_timing=False, profile=None):
    train_data = get_data(train=True, sort_by_size=True)
    # eval_data = get_data(train=False, sort_by_size=True)
    # total_data = {k: {**train_data[k], **eval_data[k]} for k in ['demo', 'test']}
    total_data = train_data

    # NOTE We could have a task list just for unsolved tasks
    full_list = list(total_data['demo'].keys())

    if start == 0 and count < 0:
        task_list = random.sample(full_list, -count)
    else:
        task_list = full_list[start:start + count] if count > 0 else full_list[start:]

    if do_list is None:
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
    for task_i, task_id in enumerate(do_list):
        d_score = D_Score()
        loop_start = timer() if prof is not None else None
        timed_out = await run_batt(total_data, task_i, task_id, d_score, start_time, pile_log_path, timeout, prof=prof)
        if prof is not None:
            prof['main.run_batt'] += timer() - loop_start
        if timed_out:
            timeouts += 1
        
    print(f'{len(do_list)} tasks - {timeouts} timeouts')

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
    parser.add_argument('-t', '--timeout', type=float, default=1,
                        help='Timeout for each task in seconds (default: 1)')
    parser.add_argument('-b', '--batt_import', type=str, default='batt',
                        help='Module to import for batt (default: batt)')
    parser.add_argument('--timing', action='store_true', help='Print lightweight timing breakdown')
    parser.add_argument('--cprofile', action='store_true', help='Run with cProfile and print top stats')
    parser.add_argument('--cprofile-top', type=int, default=30, help='Number of top functions to show in cProfile')
    args = parser.parse_args()

    batt_module = importlib.import_module(args.batt_import)
    batt = batt_module.batt if hasattr(batt_module, 'batt') else batt

    call_module = importlib.import_module(f'{args.batt_import}_call')
    t_call = call_module.t_call if hasattr(call_module, 't_call') else {}

    # # Try prioritizing mix_task_ids included by card.py
    # mix_module = importlib.import_module(f'{args.batt_import}_mix')
    # mix_task_ids = mix_module.mix_task_ids if hasattr(mix_module, 'mix_task_ids') else {}
    # print_l(f'Prioritizing: {mix_task_ids = }')
    # args.task_ids = mix_task_ids

    if args.cprofile:
        import cProfile, pstats, io
        pr = cProfile.Profile()
        pr.enable()
        asyncio.run(main(do_list=args.task_ids, start=args.start, count=args.count, timeout=args.timeout, enable_timing=args.timing))
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
        asyncio.run(main(do_list=args.task_ids, start=args.start, count=args.count, timeout=args.timeout, enable_timing=args.timing))