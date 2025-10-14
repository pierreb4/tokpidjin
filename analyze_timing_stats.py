#!/usr/bin/env python3
"""
Analyze run_batt.py execution timing statistics to optimize timeout values.

Usage:
    python analyze_timing_stats.py [--show-errors] [--percentiles]
"""

import json
import argparse
from pathlib import Path
from collections import Counter
from datetime import datetime

def load_stats(stats_file='logs/run_batt_timing_stats.jsonl'):
    """Load timing stats from JSONL file."""
    stats = []
    stats_path = Path(stats_file)
    
    if not stats_path.exists():
        print(f"Stats file not found: {stats_file}")
        print("Run some tasks to generate timing data.")
        return []
    
    with open(stats_path, 'r') as f:
        for line in f:
            if line.strip():
                stats.append(json.loads(line))
    
    return stats

def analyze_timing(stats, show_errors=False, show_percentiles=False):
    """Analyze timing statistics."""
    if not stats:
        print("No statistics available.")
        return
    
    # Separate successful and failed executions
    successful = [s for s in stats if s['success']]
    failed = [s for s in stats if not s['success']]
    
    print("=" * 70)
    print("RUN_BATT.PY EXECUTION TIMING ANALYSIS")
    print("=" * 70)
    print()
    
    # Overall statistics
    total = len(stats)
    success_count = len(successful)
    failure_count = len(failed)
    success_rate = (success_count / total * 100) if total > 0 else 0
    
    print(f"Total Executions: {total}")
    print(f"Successful: {success_count} ({success_rate:.1f}%)")
    print(f"Failed: {failure_count} ({100 - success_rate:.1f}%)")
    print()
    
    # Successful execution timing
    if successful:
        exec_times = [s['execution_time'] for s in successful]
        exec_times.sort()
        
        avg_time = sum(exec_times) / len(exec_times)
        min_time = min(exec_times)
        max_time = max(exec_times)
        median_time = exec_times[len(exec_times) // 2]
        
        print("-" * 70)
        print("SUCCESSFUL EXECUTION TIMES")
        print("-" * 70)
        print(f"Average: {avg_time:.2f}s")
        print(f"Median:  {median_time:.2f}s")
        print(f"Min:     {min_time:.2f}s")
        print(f"Max:     {max_time:.2f}s")
        print()
        
        if show_percentiles:
            percentiles = [50, 75, 90, 95, 99]
            print("Percentiles:")
            for p in percentiles:
                idx = int(len(exec_times) * p / 100)
                if idx >= len(exec_times):
                    idx = len(exec_times) - 1
                print(f"  P{p:2d}: {exec_times[idx]:.2f}s")
            print()
        
        # Distribution buckets
        print("Time Distribution:")
        buckets = [
            ("0-10s", 0, 10),
            ("10-30s", 10, 30),
            ("30-60s", 30, 60),
            ("60-120s", 60, 120),
            ("120-300s", 120, 300),
            ("300-600s", 300, 600),
            (">600s", 600, float('inf'))
        ]
        
        for label, low, high in buckets:
            count = sum(1 for t in exec_times if low <= t < high)
            pct = (count / len(exec_times) * 100) if exec_times else 0
            bar = "█" * int(pct / 2)
            print(f"  {label:12s}: {count:4d} ({pct:5.1f}%) {bar}")
        print()
        
        # Timeout recommendations
        print("-" * 70)
        print("TIMEOUT RECOMMENDATIONS")
        print("-" * 70)
        p95 = exec_times[int(len(exec_times) * 0.95)] if len(exec_times) > 20 else max_time
        p99 = exec_times[int(len(exec_times) * 0.99)] if len(exec_times) > 100 else max_time
        
        print(f"Conservative (covers 95%): {int(p95 * 1.2)}s")
        print(f"Balanced     (covers 99%): {int(p99 * 1.2)}s")
        print(f"Generous     (covers all): {int(max_time * 1.5)}s")
        print(f"Current setting:            600s")
        print()
        
        if max_time > 600:
            print("⚠️  WARNING: Some tasks exceeded 600s timeout!")
            print(f"   Consider increasing timeout or optimizing slow tasks.")
        elif p99 < 300:
            print("✓ Current 600s timeout is generous (P99 < 300s)")
            print(f"  Could reduce to {int(p99 * 1.5)}s for faster failure detection.")
        else:
            print(f"✓ Current 600s timeout is appropriate.")
        print()
    
    # Error analysis
    if failed:
        print("-" * 70)
        print("ERROR ANALYSIS")
        print("-" * 70)
        
        error_types = Counter(s['error_type'] for s in failed)
        print("Error Types:")
        for error_type, count in error_types.most_common():
            pct = (count / failure_count * 100)
            print(f"  {error_type:20s}: {count:4d} ({pct:5.1f}%)")
        print()
        
        if show_errors:
            print("Recent Errors (last 10):")
            for s in failed[-10:]:
                timestamp = datetime.fromisoformat(s['timestamp']).strftime('%H:%M:%S')
                task_id = s['task_id']
                error_type = s['error_type']
                error_msg = s['error_msg'][:60] if s['error_msg'] else 'N/A'
                print(f"  {timestamp} | {task_id} | {error_type:15s} | {error_msg}")
            print()
    
    # Timeout value analysis
    timeout_values = Counter(s['timeout_value'] for s in stats if s.get('timeout_value'))
    if timeout_values:
        print("-" * 70)
        print("TIMEOUT VALUES USED")
        print("-" * 70)
        for timeout_val, count in sorted(timeout_values.items()):
            print(f"  {timeout_val}s: {count} executions")
        print()

def main():
    parser = argparse.ArgumentParser(description='Analyze run_batt.py timing statistics')
    parser.add_argument('--show-errors', action='store_true', 
                       help='Show recent error details')
    parser.add_argument('--percentiles', action='store_true',
                       help='Show detailed percentile breakdown')
    parser.add_argument('--file', default='logs/run_batt_timing_stats.jsonl',
                       help='Stats file path (default: logs/run_batt_timing_stats.jsonl)')
    
    args = parser.parse_args()
    
    stats = load_stats(args.file)
    analyze_timing(stats, show_errors=args.show_errors, show_percentiles=args.percentiles)

if __name__ == '__main__':
    main()
