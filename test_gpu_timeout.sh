#!/bin/bash
# Test batt with increased timeout to see actual GPU performance

echo "=========================================="
echo "Week 5 Day 3 - GPU Performance Test"
echo "=========================================="
echo ""
echo "Testing with 10 second timeout (was 1 second)"
echo "Goal: See if GPU operations complete without timeout"
echo ""
echo "Test 1: Single task with timing"
echo "------------------------------------------"

python run_batt.py -c 1 -b batt --timing

echo ""
echo "Test 2: 5 tasks with timing"
echo "------------------------------------------"

python run_batt.py -c 5 -b batt --timing

echo ""
echo "=========================================="
echo "Analysis"
echo "=========================================="
echo ""
echo "Compare to expected times:"
echo "  - Without GPU: ~430ms per batt() call"
echo "  - With GPU (tiny batches): ~1,300-1,500ms per batt() call"
echo ""
echo "If times show ~1.3-1.5s per call:"
echo "  → GPU overhead is hurting performance (5.5x slower)"
echo "  → Should disable GPU batch calls"
echo ""
echo "If times show <500ms per call:"
echo "  → GPU is somehow helping (surprising!)"
echo "  → Keep investigating"
echo ""
