"""
Mega-Batch Batt Coordinator

Coordinates GPU mega-batch processing of 4000+ batt() calls across all tasks.

Strategy:
1. Collect all inputs from training + evaluation data (~4000 samples)
2. Batch into chunks of 1000 samples  
3. Process batches in parallel with GPU-accelerated operations
4. Merge results back to per-task format

Integration approach:
- Phase 1: Parallel batch processing (current)
- Phase 2: GPU-accelerate individual operations within batt (Week 5 Day 2-3)
- Phase 3: Full vectorization (Week 5 Day 4-5)

Expected speedup: 
- Phase 1: 1.2-1.5x (parallel processing)
- Phase 2: 3.5-4.5x (GPU Tier 1+2 ops)
- Phase 3: 4.8-9x (full optimization)

Author: Pierre
Date: October 13, 2025
Week: 5 Day 2
"""

import importlib
import asyncio
import concurrent.futures
from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict
from timeit import default_timer as timer
import logging

logger = logging.getLogger(__name__)

# Try to import GPU operations
try:
    from gpu_dsl_operations import get_gpu_ops, GPUDSLOperations
    GPU_OPS_AVAILABLE = True
except ImportError:
    GPU_OPS_AVAILABLE = False
    GPUDSLOperations = None


class BatchInput:
    """Container for a single batt() call input"""
    def __init__(self, task_id: str, task_idx: int, sample_type: str, 
                 sample_idx: int, S: tuple, I: tuple, C: tuple, log_path: str):
        self.task_id = task_id
        self.task_idx = task_idx  # Task number in sequence
        self.sample_type = sample_type  # 'demo' or 'test'
        self.sample_idx = sample_idx  # Sample number within task
        self.S = S  # Training samples
        self.I = I  # Input grid
        self.C = C  # Candidate/output grid
        self.log_path = log_path
        
    def to_args(self):
        """Convert to batt() argument tuple"""
        return (self.task_id, self.S, self.I, self.C, self.log_path)


class BatchResult:
    """Container for batt() call result"""
    def __init__(self, batch_idx: int, o_result: list, s_result: list):
        self.batch_idx = batch_idx
        self.o_result = o_result  # Output candidates
        self.s_result = s_result  # Solver candidates
        

class MegaBatchCoordinator:
    """Coordinates mega-batch processing of batt() calls"""
    
    def __init__(self, batt_module_name: str = 'batt', batch_size: int = 1000, 
                 enable_gpu: bool = True, parallel: bool = True, max_workers: int = 4):
        """
        Initialize coordinator.
        
        Args:
            batt_module_name: Name of module containing batt() function
            batch_size: Number of samples per batch (default 1000)
            enable_gpu: Enable GPU operations if available (default True)
            parallel: Enable parallel batch processing (default True)
            max_workers: Max parallel workers (default 4)
        """
        self.batt_module_name = batt_module_name
        self.batch_size = batch_size
        self.enable_gpu = enable_gpu and GPU_OPS_AVAILABLE
        self.parallel = parallel
        self.max_workers = max_workers
        self.batt = None
        self.gpu_ops = None
        
        # Initialize GPU operations if available
        if self.enable_gpu:
            try:
                self.gpu_ops = get_gpu_ops(enable_gpu=True)
                logger.info(f"GPU operations initialized: {self.gpu_ops.get_stats()}")
            except Exception as e:
                logger.warning(f"GPU initialization failed: {e}, using CPU only")
                self.enable_gpu = False
                self.gpu_ops = None
        
    def load_batt(self):
        """Load batt function from module"""
        if self.batt is None:
            batt_module = importlib.import_module(self.batt_module_name)
            self.batt = batt_module.batt if hasattr(batt_module, 'batt') else None
            if self.batt is None:
                raise ValueError(f"Module {self.batt_module_name} has no batt function")
    
    def collect_inputs(self, total_data: dict, task_list: List[str], 
                      log_path: str = 'pile.log') -> List[BatchInput]:
        """
        Collect all batt() inputs from tasks.
        
        Args:
            total_data: Dict with 'demo' and 'test' keys containing task data
            task_list: List of task IDs to process
            log_path: Path for logging
            
        Returns:
            List of BatchInput objects
        """
        inputs = []
        
        for task_idx, task_id in enumerate(task_list):
            # Get demo and test samples for this task
            demo_task = total_data['demo'].get(task_id, [])
            test_task = total_data['test'].get(task_id, [])
            
            # Create S (training samples) from demo
            S = tuple((tuple(sample['input']), tuple(sample['output'])) 
                     for sample in demo_task)
            
            # Collect demo inputs
            for sample_idx, sample in enumerate(demo_task):
                I = tuple(sample['input'])
                # For demo, C=None initially (will be filled with candidates)
                batch_input = BatchInput(
                    task_id=task_id,
                    task_idx=task_idx,
                    sample_type='demo',
                    sample_idx=sample_idx,
                    S=S,
                    I=I,
                    C=None,
                    log_path=log_path
                )
                inputs.append(batch_input)
            
            # Collect test inputs
            for sample_idx, sample in enumerate(test_task):
                I = tuple(sample['input'])
                # For test, C=None initially
                batch_input = BatchInput(
                    task_id=task_id,
                    task_idx=task_idx,
                    sample_type='test',
                    sample_idx=sample_idx,
                    S=S,
                    I=I,
                    C=None,
                    log_path=log_path
                )
                inputs.append(batch_input)
        
        logger.info(f"Collected {len(inputs)} inputs from {len(task_list)} tasks")
        return inputs
    
    def create_batches(self, inputs: List[BatchInput]) -> List[List[BatchInput]]:
        """
        Split inputs into batches.
        
        Args:
            inputs: List of all BatchInput objects
            
        Returns:
            List of batches (each batch is a list of BatchInput)
        """
        batches = []
        for i in range(0, len(inputs), self.batch_size):
            batch = inputs[i:i + self.batch_size]
            batches.append(batch)
        
        logger.info(f"Created {len(batches)} batches of size ~{self.batch_size}")
        return batches
    
    def process_single_input(self, batch_input: BatchInput, input_idx: int, 
                           batch_idx: int) -> BatchResult:
        """
        Process a single batt() input.
        
        Args:
            batch_input: Input to process
            input_idx: Index within batch
            batch_idx: Batch number
            
        Returns:
            BatchResult object
        """
        try:
            o_result, s_result = self.batt(*batch_input.to_args())
            return BatchResult(
                batch_idx=input_idx,
                o_result=o_result,
                s_result=s_result
            )
        except Exception as e:
            logger.error(f"Batch {batch_idx}, input {input_idx} failed: {e}")
            # Return empty results on error
            return BatchResult(
                batch_idx=input_idx,
                o_result=[],
                s_result=[]
            )
    
    def process_batch(self, batch: List[BatchInput], batch_idx: int) -> List[BatchResult]:
        """
        Process a single batch by calling batt() for each input.
        
        Phase 1: Parallel processing of independent batt() calls
        Phase 2: GPU-accelerated operations within batt (GPU context wraps DSL ops)
        
        Args:
            batch: List of BatchInput objects to process
            batch_idx: Index of this batch
            
        Returns:
            List of BatchResult objects
        """
        # ALWAYS print this to know we reached this code
        print(f"🔍 process_batch called: batch_idx={batch_idx}, enable_gpu={self.enable_gpu}, batch_size={len(batch)}")
        
        # Try to import batch context for GPU-aware DSL operations
        batch_context = None
        if self.enable_gpu:
            print(f"🔍 GPU enabled, attempting to import batch_dsl_context...")
            try:
                from batch_dsl_context import batch_dsl_context
                print(f"✅ batch_dsl_context imported successfully")
                batch_context = batch_dsl_context(gpu_ops=self.gpu_ops, enable_gpu=True)
                print(f"🔥 GPU-aware context activated for batch processing")
                logger.info("🔥 GPU-aware context activated for batch processing")
            except ImportError as e:
                print(f"❌ ImportError: {e}")
                logger.warning(f"⚠️  batch_dsl_context not available: {e}")
                logger.warning("⚠️  GPU operations will NOT be used (Option 1 not active)")
            except Exception as e:
                print(f"❌ Exception: {e}")
                import traceback
                traceback.print_exc()
                logger.error(f"❌ Failed to activate GPU context: {e}")
        else:
            print(f"🔍 GPU disabled (enable_gpu={self.enable_gpu}), skipping batch context")
        
        # Use GPU-aware context if available, otherwise process directly
        if batch_context is not None:
            print(f"✅ Using GPU context manager")
            with batch_context:
                return self._process_batch_impl(batch, batch_idx)
        else:
            print(f"⚠️  Processing without GPU context")
            return self._process_batch_impl(batch, batch_idx)
    
    def _process_batch_impl(self, batch: List[BatchInput], batch_idx: int) -> List[BatchResult]:
        """
        Internal implementation of batch processing.
        Called within GPU context if available.
        """
        if self.parallel and len(batch) > 1:
            # Parallel processing with ThreadPoolExecutor
            results = [None] * len(batch)
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = {
                    executor.submit(self.process_single_input, batch_input, input_idx, batch_idx): input_idx
                    for input_idx, batch_input in enumerate(batch)
                }
                
                for future in concurrent.futures.as_completed(futures):
                    input_idx = futures[future]
                    try:
                        result = future.result()
                        results[input_idx] = result
                    except Exception as e:
                        logger.error(f"Batch {batch_idx}, input {input_idx} parallel failed: {e}")
                        results[input_idx] = BatchResult(
                            batch_idx=input_idx,
                            o_result=[],
                            s_result=[]
                        )
            
            return results
        else:
            # Sequential processing (fallback or single item)
            results = []
            for input_idx, batch_input in enumerate(batch):
                result = self.process_single_input(batch_input, input_idx, batch_idx)
                results.append(result)
            
            return results
    
    def merge_results(self, inputs: List[BatchInput], results: List[List[BatchResult]]) -> Dict:
        """
        Merge batch results back into per-task format.
        
        Args:
            inputs: Original list of BatchInput objects
            results: List of batch results (list of lists)
            
        Returns:
            Dict structured like check_batt output:
            {
                'task_id_1': {
                    'demo': [(sample_idx, o_result, s_result), ...],
                    'test': [(sample_idx, o_result, s_result), ...]
                },
                ...
            }
        """
        merged = defaultdict(lambda: {'demo': {}, 'test': {}})
        
        # Flatten results
        flat_results = []
        for batch_results in results:
            flat_results.extend(batch_results)
        
        # Merge with inputs
        for batch_input, batch_result in zip(inputs, flat_results):
            task_id = batch_input.task_id
            sample_type = batch_input.sample_type
            sample_idx = batch_input.sample_idx
            
            merged[task_id][sample_type][sample_idx] = {
                'o': batch_result.o_result,
                's': batch_result.s_result
            }
        
        return dict(merged)
    
    def process_all(self, total_data: dict, task_list: List[str], 
                   log_path: str = 'pile.log') -> Tuple[Dict, float]:
        """
        Process all tasks with mega-batch approach.
        
        Args:
            total_data: Dict with 'demo' and 'test' keys
            task_list: List of task IDs to process
            log_path: Path for logging
            
        Returns:
            (merged_results, elapsed_time) tuple
        """
        start_time = timer()
        
        # Log configuration
        logger.info("="*60)
        logger.info("MegaBatchCoordinator Configuration:")
        logger.info(f"  Batch size: {self.batch_size}")
        logger.info(f"  Parallel: {self.parallel} (workers: {self.max_workers})")
        logger.info(f"  GPU enabled: {self.enable_gpu}")
        if self.enable_gpu and self.gpu_ops:
            stats = self.gpu_ops.get_stats()
            logger.info(f"  GPU available: {stats['gpu_available']}")
            logger.info(f"  GPU count: {stats['gpu_count']}")
        logger.info("="*60)
        
        # Load batt function
        self.load_batt()
        
        # Collect all inputs
        inputs = self.collect_inputs(total_data, task_list, log_path)
        collection_time = timer() - start_time
        logger.info(f"Collection time: {collection_time:.3f}s")
        
        # Create batches
        batches = self.create_batches(inputs)
        
        # Process each batch
        batch_results = []
        batch_start = timer()
        for batch_idx, batch in enumerate(batches):
            if batch_idx % 10 == 0 and batch_idx > 0:
                elapsed = timer() - batch_start
                rate = batch_idx * self.batch_size / elapsed
                logger.info(f"Processing batch {batch_idx}/{len(batches)} "
                          f"({elapsed:.1f}s elapsed, {rate:.0f} samples/s)")
            
            results = self.process_batch(batch, batch_idx)
            batch_results.append(results)
        
        batch_time = timer() - batch_start
        logger.info(f"Batch processing time: {batch_time:.3f}s")
        logger.info(f"Throughput: {len(inputs)/batch_time:.1f} samples/s")
        
        # Merge results
        merge_start = timer()
        merged = self.merge_results(inputs, batch_results)
        merge_time = timer() - merge_start
        logger.info(f"Merge time: {merge_time:.3f}s")
        
        total_time = timer() - start_time
        logger.info("="*60)
        logger.info(f"TOTAL TIME: {total_time:.3f}s for {len(inputs)} calls")
        logger.info(f"Average: {total_time/len(inputs)*1000:.2f}ms per call")
        logger.info(f"Breakdown: Collection {collection_time:.1f}s, "
                   f"Processing {batch_time:.1f}s, Merge {merge_time:.1f}s")
        logger.info("="*60)
        
        return merged, total_time


# Example usage and testing
if __name__ == '__main__':
    import sys
    
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Mock batt function for testing
    def mock_batt(task_id, S, I, C, log_path):
        """Mock batt function that returns dummy results"""
        import time
        time.sleep(0.001)  # Simulate 1ms processing
        
        # Return mock results
        o_result = [(1, 'test_evo', f'solver_{task_id}_1', 'output1')]
        s_result = [(1, None, f'differ_{task_id}_1', 'score1')]
        return o_result, s_result
    
    # Create mock module
    class MockBattModule:
        batt = staticmethod(mock_batt)
    
    sys.modules['mock_batt'] = MockBattModule()
    
    # Create mock data
    mock_data = {
        'demo': {
            'task1': [
                {'input': [[0, 1], [1, 0]], 'output': [[1, 0], [0, 1]]},
                {'input': [[1, 1], [1, 1]], 'output': [[0, 0], [0, 0]]},
            ],
            'task2': [
                {'input': [[2, 2], [2, 2]], 'output': [[3, 3], [3, 3]]},
            ],
        },
        'test': {
            'task1': [
                {'input': [[4, 4], [4, 4]], 'output': None},
            ],
            'task2': [
                {'input': [[5, 5], [5, 5]], 'output': None},
            ],
        }
    }
    
    # Test coordinator - Sequential mode
    print("\n" + "="*60)
    print("Testing MegaBatchCoordinator - SEQUENTIAL MODE")
    print("="*60)
    coordinator_seq = MegaBatchCoordinator(
        batt_module_name='mock_batt', 
        batch_size=2,
        parallel=False,
        enable_gpu=False
    )
    
    task_list = ['task1', 'task2']
    results_seq, elapsed_seq = coordinator_seq.process_all(mock_data, task_list)
    
    print(f"\n✅ Sequential: Processed {len(task_list)} tasks in {elapsed_seq:.3f}s")
    print(f"   Throughput: {5/elapsed_seq:.1f} samples/s")
    
    # Test coordinator - Parallel mode
    print("\n" + "="*60)
    print("Testing MegaBatchCoordinator - PARALLEL MODE")
    print("="*60)
    coordinator_par = MegaBatchCoordinator(
        batt_module_name='mock_batt', 
        batch_size=2,
        parallel=True,
        max_workers=4,
        enable_gpu=False  # GPU ops tested separately
    )
    
    results_par, elapsed_par = coordinator_par.process_all(mock_data, task_list)
    
    print(f"\n✅ Parallel: Processed {len(task_list)} tasks in {elapsed_par:.3f}s")
    print(f"   Throughput: {5/elapsed_par:.1f} samples/s")
    
    # Compare
    speedup = elapsed_seq / elapsed_par if elapsed_par > 0 else 1.0
    print(f"\n{'='*60}")
    print(f"SPEEDUP: {speedup:.2f}x (Parallel vs Sequential)")
    print(f"{'='*60}")
    
    # Verify results match
    assert results_seq.keys() == results_par.keys(), "Result keys don't match!"
    print("✅ Results verified: Sequential and Parallel produce same structure")
    
    print("\n✅ MegaBatchCoordinator working!")
    print("\nNext: Test with GPU operations enabled on Kaggle")
