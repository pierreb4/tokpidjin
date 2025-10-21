#!/bin/bash
# Simple script to profile inline_variables() timeout during actual run_batt.py execution
# This captures built-in profiling data that's already in the code

echo "=========================================="
echo "Profile inline_variables() Timeout"
echo "=========================================="
echo ""
echo "This runs an actual solver evaluation with profiling enabled."
echo "Timing data is collected from inline_variables() calls."
echo ""
echo "Running: bash run_card.sh -c -10 with profiling enabled..."
echo ""

# Run actual pipeline with a small task count to collect profiling data
# The profiling output will show inline_variables timing breakdown
PROFILE=1 timeout 180 bash run_card.sh -c -10 2>&1 | tee profile_inline_realrun.log

echo ""
echo "=========================================="
echo "Extracting inline_variables timing data..."
echo "=========================================="
echo ""

# Extract inline_variables profiling entries if present
if grep -q "inline_variables" profile_inline_realrun.log; then
    echo "Found inline_variables timing data:"
    grep "inline_variables\|parse\|visit\|unparse" profile_inline_realrun.log | head -20
else
    echo "No inline_variables timing data in output."
    echo "Check if profiling is enabled in run_batt.py"
fi

echo ""
echo "=========================================="
echo "Summary"
echo "=========================================="
echo ""
echo "Profile log saved to: profile_inline_realrun.log"
echo ""
echo "To analyze results:"
echo "  grep 'inline_variables' profile_inline_realrun.log"
echo "  tail -100 profile_inline_realrun.log"
echo ""
