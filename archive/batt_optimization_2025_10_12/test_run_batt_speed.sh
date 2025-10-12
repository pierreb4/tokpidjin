#!/bin/bash
# Test the optimized run_batt.py performance

echo "Testing optimized run_batt.py with profiling..."
echo "================================================"

# Run on a single task with timing enabled
python run_batt.py --timing -i 007bbfb7 -b tmp_batt_onerun_run 2>&1 | tee test_batt_speed.log

echo ""
echo "================================================"
echo "Key Metrics:"
echo "================================================"
grep -E "(Timing summary|main.run_batt|run_batt.check_batt|phase[0-9]|inline_variables|Filtered to)" test_batt_speed.log
