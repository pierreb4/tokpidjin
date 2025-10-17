#!/bin/bash
# Quick Win #1 Validation Workflow
# This script runs the complete validation sequence for Quick Win #1

set -e

echo "======================================================================"
echo "QUICK WIN #1 VALIDATION WORKFLOW"
echo "======================================================================"
echo ""

# Step 1: Verify files exist
echo "Step 1: Verifying Quick Win #1 files..."
if [ ! -f "solver_body_cache.py" ]; then
    echo "✗ ERROR: solver_body_cache.py not found!"
    exit 1
fi
if [ ! -f "test_quick_win_1.py" ]; then
    echo "✗ ERROR: test_quick_win_1.py not found!"
    exit 1
fi
if [ ! -f "validate_quick_win_1.py" ]; then
    echo "✗ ERROR: validate_quick_win_1.py not found!"
    exit 1
fi
echo "✓ All Quick Win #1 files present"
echo ""

# Step 2: Run unit tests
echo "======================================================================"
echo "Step 2: Running Unit Tests..."
echo "======================================================================"
python test_quick_win_1.py
echo ""

# Step 3: Run performance validation
echo "======================================================================"
echo "Step 3: Running Performance Validation (5-task benchmark)..."
echo "======================================================================"
echo "This will run two sequential 5-task runs to measure cache benefit..."
echo ""
python validate_quick_win_1.py
echo ""

# Step 4: Display results
echo "======================================================================"
echo "Step 4: Results Summary"
echo "======================================================================"
if [ -f "qw1_validation_results.json" ]; then
    echo "Quick Win #1 Results:"
    cat qw1_validation_results.json | python -m json.tool
    echo ""
    echo "✓ Validation complete! Results saved to qw1_validation_results.json"
else
    echo "⚠ No results file generated"
fi

echo ""
echo "======================================================================"
echo "NEXT STEPS:"
echo "======================================================================"
echo "1. Review the results above"
echo "2. If speedup >= 3%: Move to Quick Win #2"
echo "3. If speedup < 3%: Investigate cache hit rate or run larger benchmark"
echo "4. Run 'bash run_card.sh -c -10' for small validation run"
echo "5. Run 'bash run_card.sh -c -100' for full 100-task benchmark"
echo ""
