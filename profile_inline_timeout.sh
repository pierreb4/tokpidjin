#!/bin/bash
# Profile inline_variables() timeout by running actual pipeline

echo "=========================================="
echo "Profile inline_variables() Timeout"
echo "=========================================="
echo ""
echo "Running: bash run_card.sh -o -T -c -32"
echo "This will profile inline_variables during real solver evaluation"
echo "  -o: single optimization loop"
echo "  -T: enable timing output"
echo "  -c -32: run on 32 tasks"
echo ""

# Run the actual pipeline with 32 tasks, single optimization loop, with timing
# Profiling happens automatically during inline_variables calls
bash run_card.sh -o -T -c -32 2>&1 | tee profile_inline_realrun.log

echo ""
echo "=========================================="
echo "Profile Complete"
echo "=========================================="
echo ""
echo "Results saved to: profile_inline_realrun.log"
echo ""
echo "To analyze:"
echo "  tail -100 profile_inline_realrun.log          # See summary stats"
echo "  grep -i 'inline\|timeout\|error' profile_inline_realrun.log | head -50"
echo ""
