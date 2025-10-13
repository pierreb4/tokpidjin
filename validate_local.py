"""
Local GPU Validation Script

Quick test to verify everything works before deploying to Kaggle.
This will run a mini-benchmark locally with CPU fallback.

Author: Pierre
Date: October 13, 2025
Week: 5 Day 3
"""

import sys
import logging
from timeit import default_timer as timer

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def check_dependencies():
    """Check all required dependencies are available"""
    print("\n" + "="*60)
    print("DEPENDENCY CHECK")
    print("n="*60)
    
    deps_ok = True
    
    # Check CuPy (optional)
    try:
        import cupy as cp
        print("✅ CuPy available")
        try:
            gpu_count = cp.cuda.runtime.getDeviceCount()
            print(f"✅ GPU count: {gpu_count}")
        except:
            print("⚠️  CuPy installed but no GPU detected (will use CPU fallback)")
    except ImportError:
        print("⚠️  CuPy not available (will use CPU fallback)")
    
    # Check required modules
    required = [
        'gpu_dsl_operations',
        'mega_batch_batt',
        'batt_mega_test',
        'dsl',
        'arc_types'
    ]
    
    for module in required:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module} - {e}")
            deps_ok = False
    
    print("="*60 + "\n")
    return deps_ok


def run_quick_test():
    """Run quick validation test"""
    from mega_batch_batt import MegaBatchCoordinator
    
    print("\n" + "="*60)
    print("QUICK VALIDATION TEST")
    print("="*60)
    
    # Create simple test data
    grid1 = ((0, 1, 0), (1, 0, 1), (0, 1, 0))
    grid2 = ((1, 1, 1), (1, 0, 1), (1, 1, 1))
    
    mock_data = {
        'demo': {
            'test_001': [
                {'input': grid1, 'output': grid2},
                {'input': grid2, 'output': grid1},
            ]
        },
        'test': {
            'test_001': [
                {'input': grid1, 'output': None},
            ]
        }
    }
    
    task_list = ['test_001']
    
    print(f"Test data: 1 task, 3 samples")
    print("="*60 + "\n")
    
    # Test 1: Sequential
    print("[1/3] Testing Sequential Mode...")
    try:
        coordinator = MegaBatchCoordinator(
            batt_module_name='batt_mega_test',
            batch_size=10,
            enable_gpu=False,
            parallel=False,
            max_workers=1
        )
        
        start = timer()
        results, elapsed = coordinator.process_all(mock_data, task_list)
        
        print(f"✅ Sequential: {elapsed:.3f}s")
        seq_time = elapsed
    except Exception as e:
        print(f"❌ Sequential failed: {e}")
        return False
    
    # Test 2: Parallel
    print("\n[2/3] Testing Parallel Mode...")
    try:
        coordinator = MegaBatchCoordinator(
            batt_module_name='batt_mega_test',
            batch_size=10,
            enable_gpu=False,
            parallel=True,
            max_workers=2
        )
        
        start = timer()
        results, elapsed = coordinator.process_all(mock_data, task_list)
        
        speedup = seq_time / elapsed if elapsed > 0 else 0
        print(f"✅ Parallel: {elapsed:.3f}s ({speedup:.2f}x)")
        par_time = elapsed
    except Exception as e:
        print(f"❌ Parallel failed: {e}")
        return False
    
    # Test 3: GPU-enabled (will use CPU fallback if no GPU)
    print("\n[3/3] Testing GPU-Enabled Mode...")
    try:
        coordinator = MegaBatchCoordinator(
            batt_module_name='batt_mega_test',
            batch_size=10,
            enable_gpu=True,
            parallel=True,
            max_workers=2
        )
        
        start = timer()
        results, elapsed = coordinator.process_all(mock_data, task_list)
        
        speedup = seq_time / elapsed if elapsed > 0 else 0
        print(f"✅ GPU-enabled: {elapsed:.3f}s ({speedup:.2f}x)")
        
        # Check if GPU was actually used
        if coordinator.gpu_ops is not None:
            print("   GPU operations available ✅")
        else:
            print("   Using CPU fallback (no GPU) ⚠️")
        
    except Exception as e:
        print(f"❌ GPU-enabled failed: {e}")
        return False
    
    print("\n" + "="*60)
    print("✅ ALL TESTS PASSED")
    print("="*60)
    print("\nReady to deploy to Kaggle!")
    print("Next step: Follow KAGGLE_DEPLOYMENT_GUIDE.md")
    print("="*60 + "\n")
    
    return True


def main():
    """Main validation routine"""
    print("\n" + "="*60)
    print("LOCAL GPU VALIDATION SCRIPT")
    print("="*60)
    print("This script validates your setup before Kaggle deployment")
    print("="*60 + "\n")
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ DEPENDENCY CHECK FAILED")
        print("Please install missing dependencies:")
        print("  pip install cupy-cuda11x  # Optional, for GPU")
        print("  pip install numpy")
        return False
    
    # Run quick test
    success = run_quick_test()
    
    if success:
        print("\n🎉 VALIDATION SUCCESSFUL!")
        print("\nYour setup is ready for Kaggle deployment.")
        print("Expected speedup on Kaggle: 7-12x")
        print("\nNext steps:")
        print("1. Read KAGGLE_DEPLOYMENT_GUIDE.md")
        print("2. Upload files to Kaggle")
        print("3. Run kaggle_gpu_benchmark.py")
        print("4. Document results")
        return True
    else:
        print("\n❌ VALIDATION FAILED")
        print("Please fix the errors above before deploying to Kaggle.")
        return False


if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
