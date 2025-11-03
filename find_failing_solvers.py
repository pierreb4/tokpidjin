#!/usr/bin/env python3
"""
Find which solvers are failing in the current codebase.
Compare with git to find what changed.
"""
import subprocess
import json
import sys
from pathlib import Path

# Get all solver IDs
import solvers_pre
all_solvers = sorted([name.replace('solve_', '') for name in dir(solvers_pre) if name.startswith('solve_')])
print(f"Total solvers: {len(all_solvers)}")

# Test each one
failing = []
passing = []

for i, task_id in enumerate(all_solvers):
    if i % 50 == 0:
        print(f"Testing {i}/{len(all_solvers)}...")
    
    cmd = f'timeout 5 python3 run_test.py -i {task_id} --solvers solvers_pre -q'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    output = result.stdout + result.stderr
    
    # Check result
    if '1 out of 1' in output:
        passing.append(task_id)
    else:
        failing.append(task_id)

print(f"\n✅ Passing: {len(passing)}")
print(f"❌ Failing: {len(failing)}")

# Save for later analysis
with open('failing_solvers.txt', 'w') as f:
    for task_id in failing[:50]:  # Show first 50
        f.write(f"{task_id}\n")

print(f"\nFirst 50 failing solvers saved to failing_solvers.txt")
print("Failing solvers:", failing[:20])
