"""
Unit tests for GPU DSL core operations.

Tests gpu_o_g against CPU implementation (dsl.o_g) for:
- All 8 modes (0-7)
- Edge cases (empty, single cell, all same color)
- Various grid sizes and patterns
- Performance benchmarking
"""

import sys
import time
import numpy as np
from typing import List, Tuple

# Import implementations
try:
    from gpu_dsl_core import gpu_o_g, CUPY_AVAILABLE
    GPU_AVAILABLE = CUPY_AVAILABLE
except ImportError:
    print("Error: Cannot import gpu_dsl_core")
    sys.exit(1)

try:
    from dsl import o_g as cpu_o_g
except ImportError:
    print("Error: Cannot import dsl.o_g")
    sys.exit(1)

from arc_types import Grid


class TestGPUO_G:
    """Test suite for GPU o_g implementation."""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.failures = []
        self.test_grids = []
        self.generate_test_grids()
    
    def generate_test_grids(self):
        """Generate diverse test grids."""
        
        # Edge case: Empty grid
        self.test_grids.append(tuple())
        
        # Edge case: Single cell
        self.test_grids.append(((1,),))
        
        # Edge case: All same color
        self.test_grids.append((
            (5, 5, 5),
            (5, 5, 5),
            (5, 5, 5),
        ))
        
        # Simple 2x2
        self.test_grids.append((
            (1, 2),
            (3, 4),
        ))
        
        # Small grid with multiple objects
        self.test_grids.append((
            (1, 1, 0, 2, 2),
            (1, 0, 0, 0, 2),
            (0, 0, 3, 3, 3),
        ))
        
        # Grid with diagonal patterns
        self.test_grids.append((
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1),
        ))
        
        # Grid with background (0 is most common)
        self.test_grids.append((
            (0, 0, 0, 0, 0),
            (0, 1, 1, 0, 0),
            (0, 1, 1, 0, 0),
            (0, 0, 0, 2, 0),
            (0, 0, 0, 0, 0),
        ))
        
        # Checkerboard pattern
        self.test_grids.append((
            (1, 0, 1, 0),
            (0, 1, 0, 1),
            (1, 0, 1, 0),
            (0, 1, 0, 1),
        ))
        
        # Single horizontal line
        self.test_grids.append((
            (0, 0, 0),
            (1, 1, 1),
            (0, 0, 0),
        ))
        
        # Single vertical line
        self.test_grids.append((
            (0, 1, 0),
            (0, 1, 0),
            (0, 1, 0),
        ))
        
        # Complex pattern with multiple colors
        self.test_grids.append((
            (1, 1, 0, 2, 2, 0),
            (1, 0, 0, 2, 0, 0),
            (0, 0, 3, 3, 0, 4),
            (5, 5, 3, 0, 0, 4),
            (5, 0, 0, 0, 4, 4),
        ))
        
        # Large grid (10x10)
        self.test_grids.append((
            (0, 0, 1, 1, 0, 0, 2, 2, 0, 0),
            (0, 1, 1, 1, 1, 0, 2, 2, 2, 0),
            (0, 1, 1, 1, 0, 0, 0, 2, 0, 0),
            (0, 0, 1, 0, 0, 3, 3, 0, 0, 0),
            (0, 0, 0, 0, 3, 3, 3, 3, 0, 0),
            (0, 4, 4, 0, 3, 3, 3, 0, 0, 5),
            (0, 4, 0, 0, 0, 3, 0, 0, 5, 5),
            (0, 0, 0, 0, 0, 0, 0, 5, 5, 5),
            (6, 6, 0, 7, 7, 0, 0, 5, 5, 0),
            (6, 0, 0, 7, 0, 0, 0, 0, 0, 0),
        ))
        
        # Grid with single isolated cells
        self.test_grids.append((
            (1, 0, 2, 0, 3),
            (0, 0, 0, 0, 0),
            (4, 0, 5, 0, 6),
            (0, 0, 0, 0, 0),
            (7, 0, 8, 0, 9),
        ))
        
        # L-shaped object
        self.test_grids.append((
            (1, 0, 0),
            (1, 0, 0),
            (1, 1, 1),
        ))
        
        # T-shaped object
        self.test_grids.append((
            (1, 1, 1),
            (0, 1, 0),
            (0, 1, 0),
        ))
        
        # Multiple disconnected same-color objects
        self.test_grids.append((
            (1, 1, 0, 1, 1),
            (0, 0, 0, 0, 0),
            (1, 1, 0, 1, 1),
        ))
        
        print(f"Generated {len(self.test_grids)} test grids")
    
    def test_correctness(self, verbose=False):
        """Test correctness for all modes and grids."""
        print("\n" + "="*70)
        print("CORRECTNESS TESTS")
        print("="*70)
        
        if not GPU_AVAILABLE:
            print("GPU not available - skipping GPU tests")
            return
        
        for grid_idx, grid in enumerate(self.test_grids):
            for mode in range(8):
                test_name = f"Grid {grid_idx} (shape {self._grid_shape(grid)}), Mode {mode}"
                
                try:
                    # CPU result
                    cpu_result = cpu_o_g(grid, mode)
                    
                    # GPU result
                    gpu_result = gpu_o_g(grid, mode, return_format='frozenset')
                    
                    # Compare
                    if cpu_result == gpu_result:
                        self.passed += 1
                        if verbose:
                            print(f"✓ {test_name}")
                    else:
                        self.failed += 1
                        failure = {
                            'test': test_name,
                            'cpu_objects': len(cpu_result),
                            'gpu_objects': len(gpu_result),
                            'cpu_result': cpu_result,
                            'gpu_result': gpu_result
                        }
                        self.failures.append(failure)
                        print(f"✗ {test_name}")
                        print(f"  CPU: {len(cpu_result)} objects")
                        print(f"  GPU: {len(gpu_result)} objects")
                
                except Exception as e:
                    self.failed += 1
                    failure = {
                        'test': test_name,
                        'error': str(e)
                    }
                    self.failures.append(failure)
                    print(f"✗ {test_name} - ERROR: {e}")
        
        # Summary
        print(f"\n{'-'*70}")
        print(f"Correctness Tests: {self.passed} passed, {self.failed} failed")
        print(f"Total: {self.passed + self.failed} tests")
        if self.failed == 0:
            print("✓ ALL TESTS PASSED!")
        else:
            print(f"✗ {self.failed} tests failed")
            print(f"\nFirst 3 failures:")
            for failure in self.failures[:3]:
                print(f"  - {failure['test']}")
                if 'error' in failure:
                    print(f"    Error: {failure['error']}")
    
    def test_performance(self):
        """Benchmark performance for all modes."""
        print("\n" + "="*70)
        print("PERFORMANCE TESTS")
        print("="*70)
        
        if not GPU_AVAILABLE:
            print("GPU not available - skipping performance tests")
            return
        
        # Test on larger grids for meaningful timing
        perf_grids = [g for g in self.test_grids if self._grid_size(g) >= 9]
        
        if len(perf_grids) < 3:
            print("Not enough large grids for performance testing")
            return
        
        results = {}
        
        for mode in range(8):
            cpu_times = []
            gpu_times_frozenset = []
            gpu_times_tuple = []
            
            # Warmup GPU (JIT compilation)
            if GPU_AVAILABLE and perf_grids:
                for _ in range(3):
                    _ = gpu_o_g(perf_grids[0], mode, return_format='frozenset')
            
            for grid in perf_grids:
                # CPU timing
                start = time.perf_counter()
                _ = cpu_o_g(grid, mode)
                cpu_time = (time.perf_counter() - start) * 1000  # ms
                cpu_times.append(cpu_time)
                
                # GPU timing (frozenset)
                start = time.perf_counter()
                _ = gpu_o_g(grid, mode, return_format='frozenset')
                gpu_time = (time.perf_counter() - start) * 1000  # ms
                gpu_times_frozenset.append(gpu_time)
                
                # GPU timing (tuple)
                start = time.perf_counter()
                _ = gpu_o_g(grid, mode, return_format='tuple')
                gpu_time = (time.perf_counter() - start) * 1000  # ms
                gpu_times_tuple.append(gpu_time)
            
            avg_cpu = sum(cpu_times) / len(cpu_times)
            avg_gpu_frozenset = sum(gpu_times_frozenset) / len(gpu_times_frozenset)
            avg_gpu_tuple = sum(gpu_times_tuple) / len(gpu_times_tuple)
            
            speedup_frozenset = avg_cpu / avg_gpu_frozenset if avg_gpu_frozenset > 0 else 0
            speedup_tuple = avg_cpu / avg_gpu_tuple if avg_gpu_tuple > 0 else 0
            
            results[mode] = {
                'cpu': avg_cpu,
                'gpu_frozenset': avg_gpu_frozenset,
                'gpu_tuple': avg_gpu_tuple,
                'speedup_frozenset': speedup_frozenset,
                'speedup_tuple': speedup_tuple,
            }
        
        # Print results
        print(f"\nTested on {len(perf_grids)} grids (size >= 9)")
        print(f"\n{'Mode':<6} {'CPU (ms)':<12} {'GPU-FS (ms)':<12} {'GPU-T (ms)':<12} {'Speedup-FS':<12} {'Speedup-T':<12}")
        print("-" * 70)
        
        for mode in range(8):
            r = results[mode]
            print(f"{mode:<6} {r['cpu']:<12.3f} {r['gpu_frozenset']:<12.3f} {r['gpu_tuple']:<12.3f} "
                  f"{r['speedup_frozenset']:<12.2f}x {r['speedup_tuple']:<12.2f}x")
        
        # Overall average
        avg_cpu = sum(r['cpu'] for r in results.values()) / len(results)
        avg_gpu_fs = sum(r['gpu_frozenset'] for r in results.values()) / len(results)
        avg_gpu_t = sum(r['gpu_tuple'] for r in results.values()) / len(results)
        avg_speedup_fs = avg_cpu / avg_gpu_fs if avg_gpu_fs > 0 else 0
        avg_speedup_t = avg_cpu / avg_gpu_t if avg_gpu_t > 0 else 0
        
        print("-" * 70)
        print(f"{'AVG':<6} {avg_cpu:<12.3f} {avg_gpu_fs:<12.3f} {avg_gpu_t:<12.3f} "
              f"{avg_speedup_fs:<12.2f}x {avg_speedup_t:<12.2f}x")
        
        # Expected performance
        print(f"\n{'Expected Performance:'}")
        print(f"  CPU: 4-7ms")
        print(f"  GPU (frozenset): 1.45-2.15ms (2.3-4.8x speedup)")
        print(f"  GPU (tuple): 0.95-1.65ms (2.5-7.8x speedup)")
        
        # Check if meets expectations
        if avg_speedup_fs >= 2.3:
            print(f"\n✓ Frozenset speedup meets expectations ({avg_speedup_fs:.2f}x >= 2.3x)")
        else:
            print(f"\n✗ Frozenset speedup below expectations ({avg_speedup_fs:.2f}x < 2.3x)")
        
        if avg_speedup_t >= 2.5:
            print(f"✓ Tuple speedup meets expectations ({avg_speedup_t:.2f}x >= 2.5x)")
        else:
            print(f"✗ Tuple speedup below expectations ({avg_speedup_t:.2f}x < 2.5x)")
    
    def _grid_shape(self, grid):
        """Get grid shape as string."""
        if not grid:
            return "empty"
        return f"{len(grid)}x{len(grid[0]) if grid[0] else 0}"
    
    def _grid_size(self, grid):
        """Get grid size (total cells)."""
        if not grid:
            return 0
        return len(grid) * len(grid[0] if grid[0] else 0)
    
    def run_all(self, verbose=False):
        """Run all tests."""
        print("\n" + "="*70)
        print("GPU O_G UNIT TESTS")
        print("="*70)
        print(f"GPU Available: {GPU_AVAILABLE}")
        print(f"Test Grids: {len(self.test_grids)}")
        print(f"Modes to Test: 0-7 (8 modes)")
        print(f"Total Tests: {len(self.test_grids) * 8}")
        
        self.test_correctness(verbose=verbose)
        self.test_performance()
        
        print("\n" + "="*70)
        print("TEST SUMMARY")
        print("="*70)
        if self.failed == 0:
            print("✓ ALL CORRECTNESS TESTS PASSED")
            print("\nReady for Kaggle testing!")
        else:
            print(f"✗ {self.failed} CORRECTNESS TESTS FAILED")
            print("\nFix failures before Kaggle testing")
        print("="*70)


if __name__ == '__main__':
    import sys
    
    verbose = '--verbose' in sys.argv or '-v' in sys.argv
    
    tester = TestGPUO_G()
    tester.run_all(verbose=verbose)
