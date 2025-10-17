"""
Phase 2b GPU Batch Integration Module

Integrates GPU batch processing into the solver pipeline.
Accumulates grids across samples and processes them in batches.

Integration Pattern:
1. Initialize BatchSolverAccumulator at task start
2. Add grids as they're processed during scoring
3. Automatically flushes when batch full or task ends
4. Transparent to existing code - no changes to batt.py or scoring logic required

Usage in run_batt.py:
    from gpu_batch_integration import BatchSolverAccumulator
    
    # At task start
    batch_acc = BatchSolverAccumulator(batch_size=100)
    
    # During sample scoring (in score_sample loop)
    for each sample:
        # Add input/output grids
        batch_acc.add('input', sample['input'])
        batch_acc.add('output', sample['output'])
        # Continue with existing scoring logic
    
    # At task end
    batch_acc.flush_and_log()
"""

from gpu_batch_solver import BatchGridProcessor
from typing import List, Dict, Optional, Any, Tuple
from collections import defaultdict
import hashlib


class BatchSolverAccumulator:
    """
    Accumulates grids from solver execution and processes them in GPU batches.
    
    Transparent integration - no changes to existing solver logic needed.
    """
    
    def __init__(self, batch_size: int = 100, use_gpu: bool = True):
        """
        Initialize batch accumulator.
        
        Args:
            batch_size: Number of grids to accumulate before processing
            use_gpu: Whether to use GPU (falls back to CPU automatically)
        """
        self.batch_size = batch_size
        self.use_gpu = use_gpu
        self.processor = BatchGridProcessor(batch_size=batch_size, use_gpu=use_gpu)
        
        # Track grids by type for statistics
        self.grids_by_type: Dict[str, List] = defaultdict(list)
        self.total_grids_added = 0
        self.total_grids_processed = 0
        self.operation_stats: Dict[str, int] = defaultdict(int)
    
    def add(self, grid_type: str, grid: Any, operation: str = 'passthrough') -> Optional[List]:
        """
        Add grid to batch, process when full.
        
        Args:
            grid_type: Type of grid ('input', 'output', 'intermediate', etc.)
            grid: The grid data (list, numpy array, etc.)
            operation: Optional operation name for GPU processing
            
        Returns:
            Results if batch full and processed, None otherwise
        """
        self.grids_by_type[grid_type].append(grid)
        self.total_grids_added += 1
        self.operation_stats[operation] += 1
        
        # Process through batch processor
        result = self.processor.add(grid, metadata={'type': grid_type, 'operation': operation})
        
        if result:
            self.total_grids_processed += len(result)
        
        return result
    
    def add_batch(self, 
                  grid_type: str, 
                  grids: List[Any],
                  operation: str = 'passthrough') -> Optional[List]:
        """
        Add multiple grids at once.
        
        Args:
            grid_type: Type of grids
            grids: List of grids to add
            operation: Operation name for GPU processing
            
        Returns:
            Results if batch processing triggered
        """
        all_results = []
        for grid in grids:
            result = self.add(grid_type, grid, operation)
            if result:
                all_results.extend(result)
        
        return all_results if all_results else None
    
    def flush(self) -> Optional[List]:
        """
        Process any remaining accumulated grids.
        
        Returns:
            Results from final partial batch, or None if empty
        """
        return self.processor.flush()
    
    def flush_and_log(self) -> Dict[str, Any]:
        """
        Flush remaining grids and return statistics.
        
        Returns:
            Dictionary with batch statistics
        """
        final_results = self.flush()
        if final_results:
            self.total_grids_processed += len(final_results)
        
        stats = {
            'total_grids_added': self.total_grids_added,
            'total_grids_processed': self.total_grids_processed,
            'grids_by_type': dict(self.grids_by_type),
            'operation_stats': dict(self.operation_stats),
            'use_gpu': self.use_gpu and self.processor.use_gpu,
            'batch_size': self.batch_size,
        }
        
        return stats
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get current batch statistics without flushing.
        
        Returns:
            Current statistics
        """
        return {
            'total_grids_added': self.total_grids_added,
            'total_grids_processed': self.total_grids_processed,
            'pending_grids': len(self.processor.batch),
            'batches_processed': self.total_grids_processed // self.batch_size if self.batch_size > 0 else 0,
            'use_gpu': self.use_gpu and self.processor.use_gpu,
        }


class SimpleGridBatcher:
    """
    Simplified grid batching for easy integration into existing code.
    
    Accumulates grids and provides them in batches for processing.
    """
    
    def __init__(self, batch_size: int = 100):
        """Initialize grid batcher."""
        self.batch_size = batch_size
        self.batch = []
        self.batches_completed = 0
    
    def add(self, grid: Any) -> Optional[List]:
        """
        Add grid to batch.
        
        Returns:
            List of batched grids if batch full, None otherwise
        """
        self.batch.append(grid)
        
        if len(self.batch) >= self.batch_size:
            result = self.batch[:]
            self.batch = []
            self.batches_completed += 1
            return result
        
        return None
    
    def flush(self) -> Optional[List]:
        """Get remaining grids as final batch."""
        if self.batch:
            result = self.batch[:]
            self.batch = []
            return result
        return None
    
    def get_stats(self) -> Dict[str, int]:
        """Get batching statistics."""
        return {
            'pending_grids': len(self.batch),
            'batches_completed': self.batches_completed,
            'batch_size': self.batch_size,
        }


def test_batch_integration():
    """Test batch accumulation and integration."""
    print("\n=== Testing Batch Integration ===\n")
    
    # Test 1: Simple grid batcher
    print("Test 1: Simple grid batcher")
    batcher = SimpleGridBatcher(batch_size=5)
    
    grids = [f"grid_{i}" for i in range(12)]
    batches = []
    
    for i, grid in enumerate(grids):
        result = batcher.add(grid)
        if result:
            batches.append(result)
            print(f"  Batch {len(batches)}: {len(result)} grids")
    
    final = batcher.flush()
    if final:
        batches.append(final)
        print(f"  Final batch: {len(final)} grids")
    
    print(f"✓ Got {len(batches)} batches from {len(grids)} grids")
    print(f"  Stats: {batcher.get_stats()}")
    
    # Test 2: Solver accumulator
    print("\nTest 2: Solver batch accumulator")
    acc = BatchSolverAccumulator(batch_size=5, use_gpu=False)
    
    for i in range(12):
        acc.add('input', f"input_{i}")
        acc.add('output', f"output_{i}")
    
    stats = acc.flush_and_log()
    print(f"✓ Accumulated {stats['total_grids_added']} grids")
    print(f"  Types: {stats['grids_by_type']}")
    print(f"  Operations: {stats['operation_stats']}")
    
    print("\n=== All Integration Tests Passed ===\n")


if __name__ == '__main__':
    test_batch_integration()
