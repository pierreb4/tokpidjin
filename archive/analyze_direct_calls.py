"""
Analyze collected direct calls between solvers.py and dsl.py
"""
import json
import sys
from collections import defaultdict

def analyze_calls(filename):
    """Analyze and print solver-to-dsl call statistics."""
    with open(filename, 'r') as f:
        call_stats = json.load(f)
    
    solver_to_dsl = defaultdict(list)
    dsl_to_solver = defaultdict(list)
    
    # Find DSL functions called from solvers
    for func_name, call_sites in call_stats.items():
        # Skip if this is a solver function
        if func_name.startswith('solve_'):
            continue
        
        # Check each call site
        for call_site, count in call_sites.items():
            if 'solvers.py:' in call_site:
                # Extract line number
                line_num = int(call_site.split(':')[1])
                
                # Try to find the solver using this line number
                solver_found = False
                for solver_name in call_stats:
                    if solver_name.startswith('solve_'):
                        if any('solvers.py:' + str(line) in site 
                               for site in call_stats[solver_name] 
                               for line in range(line_num-10, line_num+10)):
                            solver_to_dsl[solver_name].append({
                                'dsl_function': func_name,
                                'call_site': call_site,
                                'count': count
                            })
                            dsl_to_solver[func_name].append({
                                'solver': solver_name,
                                'call_site': call_site,
                                'count': count
                            })
                            solver_found = True
                            break
                
                # If we couldn't find a matching solver, record as unknown
                if not solver_found:
                    solver_to_dsl[f"unknown_solver_near_line_{line_num}"].append({
                        'dsl_function': func_name,
                        'call_site': call_site,
                        'count': count
                    })
    
    # Print results
    print("\n=== DSL Functions Called By Solvers ===")
    for func_name, solvers in sorted(dsl_to_solver.items(), key=lambda x: len(x[1]), reverse=True):
        total_calls = sum(s['count'] for s in solvers)
        print(f"\n{func_name}: {total_calls} total calls from {len(solvers)} solvers")
        
        # Group by solver for better readability
        by_solver = defaultdict(int)
        for call in solvers:
            by_solver[call['solver']] += call['count']
        
        # Print top 5 solvers using this function
        for solver, count in sorted(by_solver.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {solver}: {count} calls")
    
    print("\n=== Solvers and Their DSL Function Usage ===")
    for solver, calls in sorted(solver_to_dsl.items(), key=lambda x: len(x[1]), reverse=True)[:20]:
        print(f"\n{solver}: uses {len(set(c['dsl_function'] for c in calls))} DSL functions")
        
        # Group by function for better readability
        by_func = defaultdict(int)
        for call in calls:
            by_func[call['dsl_function']] += call['count']
        
        # Print functions used by this solver
        for func, count in sorted(by_func.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {func}: {count} calls")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_direct_calls.py path/to/direct_calls.json")
    else:
        analyze_calls(sys.argv[1])