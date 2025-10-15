#!/bin/bash
# Quick Kaggle Timeout Fix Tests

echo "=== TEST 1: CPU MODE (No Vectorized) ==="
echo "This disables --vectorized flag which may have bugs"
bash run_card.sh -o -i -c 3 -T -m
echo ""

echo "=== TEST 2: Fewer Solvers (10 instead of 32) ==="
echo "32 solvers might generate too complex code"
# Temporarily edit run_card.sh or:
python card.py -c 10 -f test_batt_small.py
python run_batt.py -c 3 -b test_batt_small -t 10 --timing
echo ""

echo "=== TEST 3: Longer Timeout (30s) ==="
echo "Maybe Kaggle is just very slow"
bash run_card.sh -o -i -c 3 -t 30 -T -g
echo ""

echo "=== TEST 4: Check Generated Code ==="
echo "Look for infinite loops or obvious bugs"
head -200 tmp_batt_onerun_run.py
echo ""

echo "=== TEST 5: Simple Test Case ==="
echo "Test with minimal complexity"
python -c "
from tmp_batt_onerun_run import batt
S = (((0,), (1,)),)  # Minimal sample
I = (0,)
print('Testing batt...')
try:
    result = batt('test', S, I, None, 'test.log')
    print('SUCCESS:', len(result[0]) if result else 'None')
except Exception as e:
    print('ERROR:', e)
"
