#!/usr/bin/env python3
"""
Quick diagnostic script to check if batch_dsl_context is available on Kaggle.

Run this FIRST on Kaggle to diagnose the import issue.

Expected output:
  ✅ "batch_dsl_context imported successfully!" → File present, Option 1 will work
  ❌ "ModuleNotFoundError: No module named 'batch_dsl_context'" → File NOT uploaded
  ❌ Other error → File uploaded but has issues
"""

import sys
import os

print("=" * 70)
print("KAGGLE IMPORT DIAGNOSTIC")
print("=" * 70)

# Show Python path
print("\n📂 Python path:")
for i, path in enumerate(sys.path):
    print(f"  {i}: {path}")

# Show files in /kaggle/input/tokpidjin (if exists)
kaggle_path = '/kaggle/input/tokpidjin'
if os.path.exists(kaggle_path):
    print(f"\n📁 Files in {kaggle_path}:")
    try:
        files = sorted(os.listdir(kaggle_path))
        for f in files:
            file_path = os.path.join(kaggle_path, f)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                print(f"  ✓ {f:40s} ({size:8,d} bytes)")
        
        # Check specifically for batch_dsl_context.py
        if 'batch_dsl_context.py' in files:
            print(f"\n✅ batch_dsl_context.py IS present in dataset")
            batch_path = os.path.join(kaggle_path, 'batch_dsl_context.py')
            size = os.path.getsize(batch_path)
            print(f"   Size: {size:,} bytes")
            if size < 5000:
                print(f"   ⚠️  WARNING: File seems too small (expected ~8,000 bytes)")
            elif size > 10000:
                print(f"   ⚠️  WARNING: File seems too large (expected ~8,000 bytes)")
            else:
                print(f"   ✓ File size looks correct")
        else:
            print(f"\n❌ batch_dsl_context.py NOT FOUND in dataset")
            print(f"   This is why GPU context is not activating!")
            print(f"   Action: Upload batch_dsl_context.py to Kaggle dataset")
    except Exception as e:
        print(f"  ❌ Error listing files: {e}")
else:
    print(f"\n⚠️  {kaggle_path} does not exist")
    print(f"   Running locally, not on Kaggle")

# Try importing batch_dsl_context
print("\n🔍 Attempting import...")
try:
    # Add Kaggle path if it exists
    if os.path.exists(kaggle_path) and kaggle_path not in sys.path:
        sys.path.insert(0, kaggle_path)
        print(f"   Added {kaggle_path} to Python path")
    
    from batch_dsl_context import batch_dsl_context
    print("   ✅ batch_dsl_context imported successfully!")
    print("   ✅ GPU-aware context will work!")
    
    # Try to instantiate it
    try:
        ctx = batch_dsl_context(gpu_ops=None, enable_gpu=False)
        print("   ✅ BatchContext instantiated successfully!")
    except Exception as e:
        print(f"   ⚠️  Import OK but instantiation failed: {e}")
    
except ModuleNotFoundError as e:
    print(f"   ❌ ModuleNotFoundError: {e}")
    print(f"   → batch_dsl_context.py is NOT in Python path")
    print(f"   → This is why GPU context is not activating!")
    print(f"\n   ACTION REQUIRED:")
    print(f"   1. Go to Kaggle dataset")
    print(f"   2. Check if batch_dsl_context.py is uploaded")
    print(f"   3. If missing: Upload batch_dsl_context.py")
    print(f"   4. If present: Check file permissions/corruption")
    
except ImportError as e:
    print(f"   ❌ ImportError: {e}")
    print(f"   → File exists but has import issues")
    print(f"   → Check file contents and dependencies")
    
except Exception as e:
    print(f"   ❌ Unexpected error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
print("DIAGNOSTIC COMPLETE")
print("=" * 70)
