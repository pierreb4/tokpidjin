#!/usr/bin/env python3
"""
Diagnose 0% Accuracy Issue

The profiler showed 0/35 samples were correct. This script investigates why:
1. Test if generated batt module imports correctly
2. Test if solvers execute without errors
3. Compare results to expected outputs
4. Check for common issues (tuple vs list, formatting, etc.)

Usage:
    python diagnose_accuracy.py
"""

import sys
from utils import print_l, get_data

def test_import():
    """Test if generated batt module can be imported"""
    print_l("="*100)
    print_l("TEST 1: Import Generated Batt Module")
    print_l("="*100)
    
    try:
        import tmp_batt_onerun_run as batt_module
        print_l("✅ Import successful")
        
        # Check if batt function exists
        if hasattr(batt_module, 'batt'):
            print_l("✅ batt() function exists")
        else:
            print_l("❌ batt() function not found!")
            return False
        
        return True
    except ImportError as e:
        print_l(f"❌ Import failed: {e}")
        return False
    except Exception as e:
        print_l(f"❌ Unexpected error: {e}")
        return False


def test_single_solver():
    """Test a single solver in detail"""
    print_l("\n" + "="*100)
    print_l("TEST 2: Single Solver Execution")
    print_l("="*100)
    
    try:
        import tmp_batt_onerun_run as batt_module
        from importlib import reload
        reload(batt_module)
        
        # Load data
        train_data = get_data(train=True)
        
        # Pick first task
        task_ids = list(train_data['demo'].keys())[:5]
        
        for task_id in task_ids:
            print_l(f"\n--- Testing task: {task_id} ---")
            
            task = train_data['demo'][task_id]
            if len(task) == 0:
                print_l(f"  ⚠️ No samples in task")
                continue
            
            S = tuple((tuple(s['input']), tuple(s['output'])) for s in task)
            sample = task[0]
            I = sample['input']
            expected = sample['output']
            
            print_l(f"  Samples in S: {len(S)}")
            print_l(f"  Input shape: {len(I)}x{len(I[0]) if I else 0}")
            print_l(f"  Expected output shape: {len(expected)}x{len(expected[0]) if expected else 0}")
            
            try:
                # Execute batt
                result = batt_module.batt(task_id, S, I, None, None)
                
                print_l(f"  Result type: {type(result)}")
                print_l(f"  Expected type: {type(expected)}")
                
                if result is None:
                    print_l(f"  ❌ Result is None!")
                    continue
                
                # Check result shape
                if hasattr(result, '__len__'):
                    print_l(f"  Result shape: {len(result)}x{len(result[0]) if result and len(result) > 0 else 0}")
                
                # Compare
                if result == expected:
                    print_l(f"  ✅ CORRECT!")
                else:
                    print_l(f"  ❌ INCORRECT")
                    print_l(f"  Expected: {expected[:2] if len(expected) > 2 else expected}")
                    print_l(f"  Got:      {result[:2] if hasattr(result, '__len__') and len(result) > 2 else result}")
                    
                    # Check if it's a formatting issue
                    if str(result) == str(expected):
                        print_l(f"  ⚠️ String representations match - may be type issue")
                    
                    # Check shape mismatch
                    if hasattr(result, '__len__') and hasattr(expected, '__len__'):
                        if len(result) != len(expected):
                            print_l(f"  ⚠️ Length mismatch: {len(result)} vs {len(expected)}")
                        elif len(result) > 0 and len(expected) > 0:
                            if len(result[0]) != len(expected[0]):
                                print_l(f"  ⚠️ Width mismatch: {len(result[0])} vs {len(expected[0])}")
                
            except Exception as e:
                print_l(f"  ❌ Execution failed: {e}")
                import traceback
                traceback.print_exc()
        
        return True
        
    except Exception as e:
        print_l(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_type_compatibility():
    """Test if type mismatches are the issue"""
    print_l("\n" + "="*100)
    print_l("TEST 3: Type Compatibility")
    print_l("="*100)
    
    try:
        import tmp_batt_onerun_run as batt_module
        from importlib import reload
        reload(batt_module)
        
        train_data = get_data(train=True)
        task_id = list(train_data['demo'].keys())[0]
        task = train_data['demo'][task_id]
        
        if len(task) == 0:
            print_l("No samples available")
            return False
        
        S = tuple((tuple(s['input']), tuple(s['output'])) for s in task)
        sample = task[0]
        I = sample['input']
        expected = sample['output']
        
        result = batt_module.batt(task_id, S, I, None, None)
        
        print_l(f"Expected type: {type(expected)}")
        print_l(f"Result type: {type(result)}")
        
        # Check if it's tuple vs list
        if isinstance(expected, tuple) and isinstance(result, list):
            print_l("⚠️ Type mismatch: expected is tuple, result is list")
            result_as_tuple = tuple(tuple(row) for row in result)
            if result_as_tuple == expected:
                print_l("✅ Match after converting to tuple!")
                return True
        
        if isinstance(expected, list) and isinstance(result, tuple):
            print_l("⚠️ Type mismatch: expected is list, result is tuple")
            expected_as_tuple = tuple(tuple(row) for row in expected)
            if result == expected_as_tuple:
                print_l("✅ Match after converting to tuple!")
                return True
        
        # Check element types
        if hasattr(expected, '__len__') and hasattr(result, '__len__'):
            if len(expected) > 0 and len(result) > 0:
                print_l(f"Expected[0] type: {type(expected[0])}")
                print_l(f"Result[0] type: {type(result[0])}")
        
        return False
        
    except Exception as e:
        print_l(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_batt_function_signature():
    """Check batt function signature"""
    print_l("\n" + "="*100)
    print_l("TEST 4: Batt Function Signature")
    print_l("="*100)
    
    try:
        import tmp_batt_onerun_run as batt_module
        import inspect
        
        sig = inspect.signature(batt_module.batt)
        print_l(f"Signature: {sig}")
        
        params = list(sig.parameters.keys())
        print_l(f"Parameters: {params}")
        
        expected_params = ['task_id', 'S', 'I', 'C', 'log_path']
        if params == expected_params:
            print_l("✅ Signature matches expected")
            return True
        else:
            print_l(f"❌ Signature mismatch")
            print_l(f"  Expected: {expected_params}")
            print_l(f"  Got: {params}")
            return False
        
    except Exception as e:
        print_l(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_validation_logic():
    """Test the validation comparison logic"""
    print_l("\n" + "="*100)
    print_l("TEST 5: Validation Logic")
    print_l("="*100)
    
    try:
        import tmp_batt_onerun_run as batt_module
        from importlib import reload
        reload(batt_module)
        
        train_data = get_data(train=True)
        
        correct_count = 0
        total_count = 0
        
        # Test on 5 tasks
        for task_id in list(train_data['demo'].keys())[:5]:
            task = train_data['demo'][task_id]
            if len(task) == 0:
                continue
            
            S = tuple((tuple(s['input']), tuple(s['output'])) for s in task)
            
            for sample in task:
                I = sample['input']
                expected = sample['output']
                
                try:
                    result = batt_module.batt(task_id, S, I, None, None)
                    
                    # Test different comparison methods
                    total_count += 1
                    
                    # Method 1: Direct comparison
                    if result == expected:
                        correct_count += 1
                        print_l(f"✅ {task_id}: Direct comparison works")
                    else:
                        # Method 2: String comparison
                        if str(result) == str(expected):
                            print_l(f"⚠️ {task_id}: String comparison works but direct doesn't")
                        else:
                            print_l(f"❌ {task_id}: Neither comparison works")
                            print_l(f"   Expected: {expected}")
                            print_l(f"   Got: {result}")
                
                except Exception as e:
                    total_count += 1
                    print_l(f"❌ {task_id}: Execution error: {e}")
        
        accuracy = (correct_count / total_count * 100) if total_count > 0 else 0
        print_l(f"\n✅ Accuracy: {correct_count}/{total_count} ({accuracy:.1f}%)")
        
        return accuracy > 0
        
    except Exception as e:
        print_l(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    print_l("="*100)
    print_l("ACCURACY DIAGNOSTIC TOOL")
    print_l("Investigating 0% accuracy issue from profiling")
    print_l("="*100)
    print_l("")
    
    results = {}
    
    # Test 1: Import
    results['import'] = test_import()
    if not results['import']:
        print_l("\n❌ Cannot proceed - import failed")
        return
    
    # Test 2: Single solver
    results['single_solver'] = test_single_solver()
    
    # Test 3: Type compatibility
    results['type_compat'] = test_type_compatibility()
    
    # Test 4: Function signature
    results['signature'] = test_batt_function_signature()
    
    # Test 5: Validation logic
    results['validation'] = test_validation_logic()
    
    # Summary
    print_l("\n" + "="*100)
    print_l("DIAGNOSTIC SUMMARY")
    print_l("="*100)
    print_l("")
    
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print_l(f"{test_name:20s}: {status}")
    
    print_l("")
    
    if all(results.values()):
        print_l("✅ All tests passed - accuracy issue may be in profiler logic")
    else:
        print_l("❌ Some tests failed - issues found:")
        for test_name, passed in results.items():
            if not passed:
                print_l(f"  - {test_name}")
    
    print_l("")
    print_l("="*100)


if __name__ == '__main__':
    main()
