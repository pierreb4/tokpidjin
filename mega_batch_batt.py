"""
Mega-Batch Batt Coordinator

Coordinates GPU mega-batch processing of 4000+ batt() calls across all tasks.

Strategy:
1. Collect all inputs from training + evaluation data (~4000 samples)
2. Batch into chunks of 1000 samples  
3. Call vectorized batt() on each batch
4. Merge results back to per-task format

Expected speedup: 4.8-9x (1200s → 133-250s)

Author: Pierre
Date: October 13, 2025
"""

import importlib
import asyncio
from typing import Dict, List, Tuple, Any
from collections import defaultdict
from timeit import default_timer as timer
import logging

logger = logging.getLogger(__name__)


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
    
    def __init__(self, batt_module_name: str = 'batt', batch_size: int = 1000):
        """
        Initialize coordinator.
        
        Args:
            batt_module_name: Name of module containing batt() function
            batch_size: Number of samples per batch (default 1000)
        """
        self.batt_module_name = batt_module_name
        self.batch_size = batch_size
        self.batt = None
        
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
    
    def process_batch(self, batch: List[BatchInput], batch_idx: int) -> List[BatchResult]:
        """
        Process a single batch by calling batt() for each input.
        
        Note: This is currently sequential. Week 5 will add GPU vectorization.
        
        Args:
            batch: List of BatchInput objects to process
            batch_idx: Index of this batch
            
        Returns:
            List of BatchResult objects
        """
        results = []
        
        for input_idx, batch_input in enumerate(batch):
            # Call batt function
            try:
                o_result, s_result = self.batt(*batch_input.to_args())
                result = BatchResult(
                    batch_idx=input_idx,
                    o_result=o_result,
                    s_result=s_result
                )
                results.append(result)
            except Exception as e:
                logger.error(f"Batch {batch_idx}, input {input_idx} failed: {e}")
                # Return empty results on error
                result = BatchResult(
                    batch_idx=input_idx,
                    o_result=[],
                    s_result=[]
                )
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
        
        # Load batt function
        self.load_batt()
        
        # Collect all inputs
        inputs = self.collect_inputs(total_data, task_list, log_path)
        logger.info(f"Collection time: {timer() - start_time:.3f}s")
        
        # Create batches
        batches = self.create_batches(inputs)
        
        # Process each batch
        batch_results = []
        batch_start = timer()
        for batch_idx, batch in enumerate(batches):
            if batch_idx % 10 == 0:
                elapsed = timer() - batch_start
                logger.info(f"Processing batch {batch_idx}/{len(batches)} ({elapsed:.1f}s elapsed)")
            
            results = self.process_batch(batch, batch_idx)
            batch_results.append(results)
        
        batch_time = timer() - batch_start
        logger.info(f"Batch processing time: {batch_time:.3f}s")
        
        # Merge results
        merge_start = timer()
        merged = self.merge_results(inputs, batch_results)
        logger.info(f"Merge time: {timer() - merge_start:.3f}s")
        
        total_time = timer() - start_time
        logger.info(f"Total time: {total_time:.3f}s for {len(inputs)} calls")
        logger.info(f"Average: {total_time/len(inputs)*1000:.2f}ms per call")
        
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
    
    # Test coordinator
    print("Testing MegaBatchCoordinator...")
    coordinator = MegaBatchCoordinator(batt_module_name='mock_batt', batch_size=2)
    
    task_list = ['task1', 'task2']
    results, elapsed = coordinator.process_all(mock_data, task_list)
    
    print(f"\n✅ Processed {len(task_list)} tasks in {elapsed:.3f}s")
    print(f"Results structure: {list(results.keys())}")
    for task_id in results:
        print(f"  {task_id}: {len(results[task_id]['demo'])} demo, {len(results[task_id]['test'])} test")
    
    print("\n✅ MegaBatchCoordinator working!")
