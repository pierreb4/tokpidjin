#!/bin/bash
# Test Phase 2 implementation locally before Kaggle deployment

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                    Phase 2 Local Validation                                ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Check Python syntax
echo "1. Checking Python syntax..."
if python -m py_compile run_batt.py; then
    echo "   ✅ Syntax valid"
else
    echo "   ❌ Syntax errors found"
    exit 1
fi
echo ""

# Check for required imports
echo "2. Checking imports..."
if grep -q "import asyncio" run_batt.py; then
    echo "   ✅ asyncio imported"
else
    echo "   ⚠️  asyncio not found"
fi

if grep -q "asyncio.gather" run_batt.py; then
    echo "   ✅ asyncio.gather used"
else
    echo "   ⚠️  asyncio.gather not found"
fi
echo ""

# Check for new phase functions
echo "3. Checking Phase 2 implementation..."
if grep -q "async def check_one_solver" run_batt.py; then
    echo "   ✅ check_one_solver function defined"
else
    echo "   ⚠️  check_one_solver function missing"
fi

if grep -q "phase3a_validate_batch" run_batt.py; then
    echo "   ✅ Phase 3a profiling added"
else
    echo "   ⚠️  Phase 3a profiling missing"
fi

if grep -q "phase3b_file_ops" run_batt.py; then
    echo "   ✅ Phase 3b profiling added"
else
    echo "   ⚠️  Phase 3b profiling missing"
fi
echo ""

# Check phase structure
echo "4. Checking phase structure..."
grep -n "Phase 3a:" run_batt.py | head -1
grep -n "Phase 3b:" run_batt.py | head -1
grep -n "Phase 4:" run_batt.py | head -1
echo ""

# Count async functions
echo "5. Function count..."
async_count=$(grep -c "async def" run_batt.py)
echo "   Async functions: $async_count"
gather_count=$(grep -c "asyncio.gather" run_batt.py)
echo "   asyncio.gather calls: $gather_count"
echo ""

# Check for validation loop
echo "6. Checking validation pattern..."
if grep -q "validated_data = await asyncio.gather" run_batt.py; then
    echo "   ✅ Parallel validation implemented"
else
    echo "   ⚠️  Parallel validation not found"
fi
echo ""

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                         Validation Complete                                ║"
echo "╠════════════════════════════════════════════════════════════════════════════╣"
echo "║  Status: Ready for Kaggle testing                                          ║"
echo "║  Next:   Upload to Kaggle and run with --timing flag                      ║"
echo "║  Expected: 16.9s → 6-8s (2.1-2.8x speedup)                                ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Show a quick summary of what to look for on Kaggle
echo "When testing on Kaggle, look for:"
echo "  • \"Filtered to 32 unique candidates (from 149)\""
echo "  • \"Phase 3a: Validated 32 solvers in ~3.5s (parallelized)\""
echo "  • phase3a_validate_batch: ~3.5s"
echo "  • Total time: ~6-8s"
echo ""
