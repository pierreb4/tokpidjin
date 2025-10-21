#!/bin/bash
# Quick reference commands for profiling inline_variables() timeout

# ============================================================================
# QUICK START (choose one)
# ============================================================================

# Option 1: Isolated profiling (recommended first step)
# Run this to get detailed timing on individual solvers
echo "=== Option 1: Isolated Profiling (fastest, focused) ==="
echo "python profile_inline_isolated.py | tee profile_inline_isolated.log"
echo ""

# Option 2: Stress test with different timeouts
# Determines optimal timeout value
echo "=== Option 2: Stress Test (comprehensive) ==="
echo "python profile_inline_stress.py | tee profile_inline_stress.log"
echo ""

# Option 3: Real-world profiling with small run
# Actual pipeline performance
echo "=== Option 3: Real-World 10-task Run ==="
echo "bash run_card.sh -c -10 2>&1 | tee profile_inline_10.log"
echo ""

# ============================================================================
# DETAILED WORKFLOW
# ============================================================================

echo "=== Full Profiling Workflow ==="
echo ""
echo "Step 1: Generate a batt module (if needed)"
echo "  timeout 120 bash run_card.sh -c -1"
echo ""
echo "Step 2: Run isolated profiling"
echo "  python profile_inline_isolated.py 2>&1 | tee profile_inline_isolated.log"
echo ""
echo "Step 3: Run stress test to find optimal timeout"
echo "  python profile_inline_stress.py 2>&1 | tee profile_inline_stress.log"
echo ""
echo "Step 4: Analyze results"
echo "  # Check for patterns"
echo "  grep -i 'timeout\|error' profile_inline_*.log"
echo ""
echo "Step 5: Adjust timeout if needed"
echo "  # Edit utils.py line 322:"
echo "  # Change: def inline_variables(source_code, timeout_seconds=1):"
echo "  # To:     def inline_variables(source_code, timeout_seconds=X):"
echo "  # where X is your chosen timeout"
echo ""
echo "Step 6: Verify with real run"
echo "  bash run_card.sh -c -32 2>&1 | tee profile_inline_verify.log"
echo ""

# ============================================================================
# ANALYSIS COMMANDS
# ============================================================================

echo "=== Analysis Commands ==="
echo ""
echo "Extract timing data:"
echo "  grep -E '[0-9]+\.[0-9]+ms' profile_inline_*.log | head -20"
echo ""
echo "Count timeouts:"
echo "  grep -c 'TIMEOUT\|timeout' profile_inline_*.log"
echo ""
echo "Count errors:"
echo "  grep -c 'ERROR\|error' profile_inline_*.log"
echo ""
echo "Show statistics section:"
echo "  grep -A 10 'STATISTICS:' profile_inline_*.log"
echo ""
echo "Show recommendations:"
echo "  grep -A 10 'RECOMMENDATIONS' profile_inline_*.log"
echo ""

# ============================================================================
# ADJUSTING TIMEOUT
# ============================================================================

echo "=== How to Adjust Timeout ==="
echo ""
echo "If profile shows most solvers < 50ms:"
echo "  - Reduce timeout to 0.5s"
echo "  - Command: sed -i 's/timeout_seconds=1/timeout_seconds=0.5/' utils.py"
echo ""
echo "If profile shows most solvers < 100ms, no timeouts:"
echo "  - Keep 1.0s (current, safe default)"
echo ""
echo "If profile shows many timeouts or slow solvers (100-500ms):"
echo "  - Increase timeout to 2.0s"
echo "  - Command: sed -i 's/timeout_seconds=1/timeout_seconds=2/' utils.py"
echo ""
echo "If profile shows very slow solvers (> 500ms):"
echo "  - Check if these are legitimate (complex inlining)"
echo "  - Or AST errors (need upstream fix)"
echo "  - If legitimate: sed -i 's/timeout_seconds=1/timeout_seconds=5/' utils.py"
echo ""

# ============================================================================
# SAMPLE OUTPUT
# ============================================================================

echo "=== Expected Output Format ==="
echo ""
echo "From profile_inline_isolated.py:"
echo "  solve_36d67576        :  120.34ms - OK"
echo "  solve_36fdfd69        :   58.31ms - OK"
echo "  solver_avg           :   45.23ms"
echo ""
echo "From profile_inline_stress.py:"
echo "  Timeout | Success | Timeout | Error | Success% | Avg Time"
echo "    0.1s |      20 |       5 |     0 |    66.7% |    15.23ms"
echo "    0.5s |      28 |       2 |     0 |    93.3% |    25.15ms"
echo "    1.0s |      30 |       0 |     0 |   100.0% |    30.23ms"
echo "    2.0s |      30 |       0 |     0 |   100.0% |    35.45ms"
echo ""

# ============================================================================
# CURRENT SETTINGS
# ============================================================================

echo "=== Current Timeout Settings ==="
echo ""
echo "utils.py:322:"
grep "def inline_variables" utils.py | head -1
echo ""
echo "run_batt.py solver inlining:"
grep -A 1 "inline_one, candidate_data" run_batt.py | grep timeout_per_item | head -1
echo ""
echo "run_batt.py differ inlining:"
grep -A 1 "inline_differ, differ_data_list" run_batt.py | grep timeout_per_item | head -1
echo ""

# ============================================================================
# TIPS
# ============================================================================

echo "=== Tips ==="
echo ""
echo "1. Run isolated profile first (fast, focused results)"
echo "2. If isolated shows all OK with ~50ms max: timeout is good"
echo "3. If isolated shows mixed results: run stress test for guidance"
echo "4. Always verify with real run after changing timeout"
echo "5. Archive profiling scripts after documenting results"
echo ""
echo "Example workflow on server:"
echo "  python profile_inline_isolated.py 2>&1 | tee log.txt && tail -50 log.txt"
echo ""
