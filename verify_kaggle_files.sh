#!/bin/bash
# Verify all required files are present for Kaggle deployment

echo "======================================================================"
echo "Kaggle Deployment - File Verification"
echo "======================================================================"
echo ""

# Critical files
CRITICAL_FILES=(
    "batch_dsl_context.py"
    "gpu_dsl_operations.py"
    "mega_batch_batt.py"
)

# Required files
REQUIRED_FILES=(
    "gpu_optimizations.py"
    "dsl.py"
    "safe_dsl.py"
    "arc_types.py"
    "batt_gpu_operations_test.py"
    "kaggle_gpu_benchmark.py"
)

all_present=true

echo "🔴 CRITICAL FILES (GPU Integration):"
for file in "${CRITICAL_FILES[@]}"; do
    if [ -f "$file" ]; then
        lines=$(wc -l < "$file")
        size=$(du -h "$file" | cut -f1)
        echo "  ✅ $file ($lines lines, $size)"
    else
        echo "  ❌ MISSING: $file"
        all_present=false
    fi
done

echo ""
echo "🟡 REQUIRED FILES (Dependencies):"
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        lines=$(wc -l < "$file")
        size=$(du -h "$file" | cut -f1)
        echo "  ✅ $file ($lines lines, $size)"
    else
        echo "  ❌ MISSING: $file"
        all_present=false
    fi
done

echo ""
echo "======================================================================"
if [ "$all_present" = true ]; then
    echo "✅ ALL FILES PRESENT - Ready to upload to Kaggle!"
    echo ""
    echo "Next steps:"
    echo "1. Go to https://www.kaggle.com/datasets/[your-username]/tokpidjin"
    echo "2. Click 'New Version'"
    echo "3. Upload all files listed above"
    echo "4. Save new version"
    echo "5. Run: !python /kaggle/input/tokpidjin/kaggle_gpu_benchmark.py"
else
    echo "❌ SOME FILES MISSING - Cannot deploy yet"
    echo ""
    echo "Please ensure all files are present before uploading."
fi
echo "======================================================================"
