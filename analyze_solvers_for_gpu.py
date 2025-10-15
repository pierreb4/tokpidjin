#!/usr/bin/env python3
"""
Analyze solvers to find best candidates for GPU o_g_t conversion.

Identifies solvers that:
1. Use o_g operations (target for conversion)
2. Work on grids with mean size ≥70 cells (GPU beneficial)
3. Have execution time that would benefit from GPU acceleration

Usage:
    python analyze_solvers_for_gpu.py
    python analyze_solvers_for_gpu.py --top 20  # Show top 20 candidates
"""

import argparse
import inspect
import ast
from typing import Dict, List, Tuple, Set
from collections import defaultdict
from utils import get_data, print_l
import solvers_pre


class SolverAnalyzer:
    """Analyze solvers for GPU conversion potential."""
    
    def __init__(self):
        self.data = None
        
    def load_data(self):
        """Load ARC training data."""
        print_l("Loading ARC data...")
        train_data = get_data(train=True)
        eval_data = get_data(train=False)
        self.data = {k: {**train_data[k], **eval_data[k]} for k in ['demo', 'test']}
        print_l(f"Loaded {len(self.data['demo'])} tasks\n")
        
    def get_grid_stats(self, task_id: str) -> Dict:
        """Get grid size statistics for a task."""
        if task_id not in self.data['demo']:
            return None
        
        task = self.data['demo'][task_id]
        if len(task) == 0:
            return None
        
        # Collect all grid sizes (input and output)
        grid_sizes = []
        for sample in task:
            # Input grid
            I = sample['input']
            input_size = len(I) * len(I[0]) if len(I) > 0 and len(I[0]) > 0 else 0
            grid_sizes.append(input_size)
            
            # Output grid
            O = sample['output']
            output_size = len(O) * len(O[0]) if len(O) > 0 and len(O[0]) > 0 else 0
            grid_sizes.append(output_size)
        
        if len(grid_sizes) == 0:
            return None
        
        return {
            'min': min(grid_sizes),
            'max': max(grid_sizes),
            'mean': sum(grid_sizes) / len(grid_sizes),
            'count': len(grid_sizes),
            'samples': len(task)
        }
    
    def check_o_g_usage(self, solver_func) -> Dict[str, int]:
        """Check which o_g variants a solver uses."""
        try:
            source = inspect.getsource(solver_func)
            
            # Count different o_g usages
            usage = {
                'o_g': source.count('o_g('),
                'o_g_t': source.count('o_g_t('),
                'o_g_tuple': source.count('o_g_tuple('),
            }
            
            return usage
        except Exception as e:
            return {'o_g': 0, 'o_g_t': 0, 'o_g_tuple': 0}
    
    def analyze_solver(self, task_id: str) -> Dict:
        """Analyze a single solver for GPU conversion potential."""
        # Get solver function
        solver_name = f'solve_{task_id}'
        solver_func = getattr(solvers_pre, solver_name, None)
        
        if solver_func is None:
            return None
        
        # Get grid statistics
        grid_stats = self.get_grid_stats(task_id)
        if grid_stats is None:
            return None
        
        # Check o_g usage
        o_g_usage = self.check_o_g_usage(solver_func)
        
        # Calculate GPU viability score
        # Higher score = better candidate
        score = 0
        
        # Factor 1: Mean grid size (70+ cells is GPU territory)
        mean_size = grid_stats['mean']
        if mean_size >= 100:
            score += 10  # Strong GPU candidate
        elif mean_size >= 70:
            score += 5   # GPU viable
        
        # Factor 2: Uses o_g (needs conversion)
        if o_g_usage['o_g'] > 0:
            score += o_g_usage['o_g'] * 3  # 3 points per o_g call
        
        # Factor 3: Already uses o_g_t (no conversion needed, but still good)
        if o_g_usage['o_g_t'] > 0:
            score += o_g_usage['o_g_t'] * 1  # Already optimized
        
        # Factor 4: Multiple samples (more opportunities for speedup)
        if grid_stats['samples'] >= 3:
            score += 2
        
        return {
            'task_id': task_id,
            'solver_name': solver_name,
            'grid_stats': grid_stats,
            'o_g_usage': o_g_usage,
            'gpu_score': score,
            'needs_conversion': o_g_usage['o_g'] > 0,
            'already_optimized': o_g_usage['o_g_t'] > 0 or o_g_usage['o_g_tuple'] > 0,
        }
    
    def analyze_all_solvers(self) -> List[Dict]:
        """Analyze all solvers in solvers_pre."""
        print_l("Analyzing all solvers...")
        
        results = []
        
        # Get all solve_* functions
        solver_names = [name for name in dir(solvers_pre) if name.startswith('solve_')]
        print_l(f"Found {len(solver_names)} solvers\n")
        
        for solver_name in solver_names:
            task_id = solver_name.replace('solve_', '')
            result = self.analyze_solver(task_id)
            
            if result is not None:
                results.append(result)
        
        # Sort by GPU score (descending)
        results.sort(key=lambda x: x['gpu_score'], reverse=True)
        
        return results
    
    def print_summary(self, results: List[Dict], top_n: int = 50):
        """Print analysis summary."""
        print_l("=" * 120)
        print_l("GPU CONVERSION CANDIDATE ANALYSIS")
        print_l("=" * 120)
        print_l("")
        
        # Overall statistics
        total_solvers = len(results)
        needs_conversion = sum(1 for r in results if r['needs_conversion'])
        already_optimized = sum(1 for r in results if r['already_optimized'])
        
        # Grid size stats
        mean_70_plus = sum(1 for r in results if r['grid_stats']['mean'] >= 70)
        mean_100_plus = sum(1 for r in results if r['grid_stats']['mean'] >= 100)
        
        print_l(f"Total solvers analyzed: {total_solvers}")
        print_l(f"Solvers needing conversion (use o_g): {needs_conversion}")
        print_l(f"Solvers already optimized (use o_g_t): {already_optimized}")
        print_l(f"Solvers with mean grid size ≥70 cells: {mean_70_plus} ({mean_70_plus/total_solvers*100:.1f}%)")
        print_l(f"Solvers with mean grid size ≥100 cells: {mean_100_plus} ({mean_100_plus/total_solvers*100:.1f}%)")
        print_l("")
        
        # Print top candidates
        print_l(f"TOP {top_n} GPU CONVERSION CANDIDATES")
        print_l("=" * 120)
        print_l(f"{'Task ID':<12} {'Score':<6} {'Mean Size':<12} {'o_g':<6} {'o_g_t':<8} {'Samples':<8} {'Status':<20}")
        print_l("-" * 120)
        
        for i, result in enumerate(results[:top_n]):
            task_id = result['task_id']
            score = result['gpu_score']
            mean_size = result['grid_stats']['mean']
            o_g_count = result['o_g_usage']['o_g']
            o_g_t_count = result['o_g_usage']['o_g_t']
            samples = result['grid_stats']['samples']
            
            # Status
            if result['already_optimized']:
                status = "✅ Already optimized"
            elif result['needs_conversion']:
                if mean_size >= 100:
                    status = "🎯 HIGH PRIORITY"
                elif mean_size >= 70:
                    status = "⭐ GOOD CANDIDATE"
                else:
                    status = "⚠️  Low priority"
            else:
                status = "ℹ️  No o_g operations"
            
            print_l(f"{task_id:<12} {score:<6} {mean_size:>10.1f}  {o_g_count:<6} {o_g_t_count:<8} {samples:<8} {status}")
        
        print_l("=" * 120)
        print_l("")
        
        # Priority list for conversion
        print_l("CONVERSION PRIORITY LIST")
        print_l("-" * 120)
        
        high_priority = [r for r in results if r['needs_conversion'] and r['grid_stats']['mean'] >= 100][:20]
        good_candidates = [r for r in results if r['needs_conversion'] and 70 <= r['grid_stats']['mean'] < 100][:20]
        
        print_l(f"\nHIGH PRIORITY (mean ≥100 cells): {len(high_priority)} solvers")
        if high_priority:
            for r in high_priority:
                print_l(f"  solve_{r['task_id']:<12} - {r['o_g_usage']['o_g']} o_g calls, {r['grid_stats']['mean']:.1f} mean cells")
        
        print_l(f"\nGOOD CANDIDATES (70-99 cells): {len(good_candidates)} solvers")
        if good_candidates:
            for r in good_candidates:
                print_l(f"  solve_{r['task_id']:<12} - {r['o_g_usage']['o_g']} o_g calls, {r['grid_stats']['mean']:.1f} mean cells")
        
        print_l("")
        
        # Expected impact
        print_l("EXPECTED IMPACT")
        print_l("-" * 120)
        print_l("Based on Week 3 validation (8,616 real grids):")
        print_l("  • Mean grid size: 168 cells")
        print_l("  • Median grid size: 100 cells")
        print_l("  • 65% of grids are ≥70 cells (GPU beneficial)")
        print_l("  • 57% of grids are ≥100 cells (strong GPU speedup)")
        print_l("")
        print_l("Expected speedup after converting top 20-50 solvers:")
        print_l("  • Individual solvers: 2-6x faster")
        print_l("  • Average across all tasks: 2.0-2.5x faster")
        print_l("  • Production run_batt.py: 40-50% reduction in execution time")
        print_l("")


def main():
    parser = argparse.ArgumentParser(description='Analyze solvers for GPU conversion')
    parser.add_argument('--top', type=int, default=50, help='Number of top candidates to show')
    args = parser.parse_args()
    
    analyzer = SolverAnalyzer()
    analyzer.load_data()
    results = analyzer.analyze_all_solvers()
    analyzer.print_summary(results, top_n=args.top)
    
    print_l("=" * 120)
    print_l("NEXT STEPS:")
    print_l("=" * 120)
    print_l("1. Run: python convert_solver_to_gpu.py solve_TASKID")
    print_l("2. Test: python run_test.py -q -i TASKID")
    print_l("3. Validate on Kaggle: bash run_card.sh -i -b -c -1")
    print_l("4. Repeat for top 20-50 solvers")
    print_l("")
    print_l("Use the conversion tool to automate o_g → o_g_t transformation:")
    print_l("  python convert_solver_to_gpu.py --help")
    print_l("")


if __name__ == '__main__':
    main()
