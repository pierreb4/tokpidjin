#!/usr/bin/env python3
"""
Profile inline_variables() timeout - Quick profiling guide

The simplest way to profile inline_variables() is to run the actual pipeline
with profiling enabled. The inline_variables() function already has built-in
timing instrumentation that records:
  - parse time (AST parsing)
  - visit time (AST inlining)  
  - unparse time (AST conversion back to source)
  - total time (overall inlining time)

Usage:
  1. On server, run: bash run_card.sh -c -32 2>&1 | tee profile.log
  2. Then: tail -50 profile.log (see summary statistics)
  3. Then: grep -i 'inline\|timeout\|error' profile.log (see any issues)

That's it! The profiling data is collected automatically during actual execution.
"""

import os
import sys
from pathlib import Path

def show_instructions():
    """Show profiling instructions"""
    
    print("""
================================================================================
PROFILE inline_variables() TIMEOUT - QUICK GUIDE
================================================================================

The inline_variables() function has built-in profiling that records timing
for each call. To collect profiling data:

STEP 1: Run the pipeline with a small task count
----------------------------------------
  bash run_card.sh -c -32 2>&1 | tee profile.log
  
  Time: 2-5 minutes
  Output: profile.log (contains all run output + timing data)

STEP 2: Check summary statistics
----------------------------------------
  tail -50 profile.log
  
  Look for:
  - Cache statistics (hit rate, sizes)
  - Any timeout or error messages
  - Final statistics

STEP 3: Analyze inlining performance
----------------------------------------
  grep -i 'inline' profile.log | head -20
  grep -i 'timeout' profile.log
  grep -i 'error' profile.log

STEP 4: Make decision based on observations
----------------------------------------
  If no timeouts and all solvers inline quickly:
    → Keep current 1.0s timeout
  
  If seeing timeouts:
    → Increase timeout: sed -i 's/timeout_seconds=1/timeout_seconds=2/' utils.py
  
  If all inline very fast (< 50ms):
    → Reduce timeout: sed -i 's/timeout_seconds=1/timeout_seconds=0.5/' utils.py

================================================================================
CURRENT TIMEOUT SETTINGS
================================================================================

  utils.py:322          timeout_seconds=1
  run_batt.py:1560      timeout_per_item=1  (solver batch inlining)
  run_batt.py:1808      timeout_per_item=1  (differ batch inlining)

================================================================================
PROFILING DATA AVAILABLE
================================================================================

The inline_variables() function tracks these times (if _prof is set):
  - utils.inline_variables.parse     (AST parsing)
  - utils.inline_variables.visit     (AST inlining)
  - utils.inline_variables.unparse   (AST to source conversion)
  - utils.inline_variables.total     (overall time)

These are accumulated across all calls and would show in detailed profiling.

================================================================================
EXAMPLE WORKFLOW (5 MINUTES)
================================================================================

1. Run pipeline:
   bash run_card.sh -c -32 2>&1 | tee profile.log   # 2-5 min

2. Check for timeouts:
   grep -i timeout profile.log

3. Check errors:
   grep -i "error.*inline" profile.log

4. If no issues:
   echo "✓ Current 1.0s timeout is working well"

5. If timeouts:
   sed -i 's/timeout_seconds=1/timeout_seconds=2/' utils.py
   git add utils.py && git commit -m "tune: Increase inline_variables timeout to 2s"

6. Verify change:
   grep "def inline_variables" utils.py

Done!

================================================================================
""")

if __name__ == "__main__":
    show_instructions()
