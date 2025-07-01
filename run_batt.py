import argparse
import random
import re
import ast
import hashlib

from timeit import default_timer as timer

from utils import *
from batt import batt
from call import t_call


class VariableInliner(ast.NodeTransformer):
    def __init__(self):
        self.assignments = {}
        self.safe_to_inline = set()  # Track which variables are safe to inline
        self.processing = set()      # Track variables being processed to avoid recursion loops


    def visit_Assign(self, node):
        # Only handle simple assignments to variable names
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            # For other kinds of assignments (tuple unpacking, etc.), visit children
            return self.generic_visit(node)
        
        var_name = node.targets[0].id

        # Store the original value before processing
        original_value = ast.unparse(node.value)

        # First, recursively visit all child nodes to inline variables and substitute constants
        node.value = self.visit(node.value)
            
        # Store the expression for later substitution
        self.assignments[var_name] = node.value
        self.safe_to_inline.add(var_name)

        # Remove assignments from the output
        return None


    def visit_Name(self, node):
        # Replace variable reference with its assigned value, if available and safe
        if isinstance(node.ctx, ast.Load) and node.id in self.safe_to_inline:
            # Avoid infinite recursion
            if node.id in self.processing:
                return node
                
            # Track that we're processing this variable
            self.processing.add(node.id)

            # Get a deep copy of the expression to substitute
            expr = ast.parse(ast.unparse(self.assignments[node.id])).body[0].value
            
            # Recursively process the expression to inline any variables inside it
            result = self.visit(expr)
            
            # Done processing this variable
            self.processing.remove(node.id)
            return result
            
        return node


def inline_variables(source_code):
    tree = ast.parse(source_code)
    inliner = VariableInliner()
    
    # Process tree and collect assignments
    tree = inliner.visit(tree)

    # Convert back to source code
    ast.fix_missing_locations(tree)

    return ast.unparse(tree)


def run_batt(total_data, task_num, task_id, start_time, timeout=1):
    train_task = total_data['train'][task_id]
    test_task = total_data['test'][task_id]
    # total_task = total_data['train'][task_id] + total_data['test'][task_id]

    o = {'train': {}, 'test': {}}
    all_o = set()
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in train_task)

    print(f'------ {task_id} - {task_num} - ', end='')

    score = {}
    for i, sample in enumerate(train_task):
        I = sample['input']
        O = sample['output']
        timed_out, o['train'][i] = run_with_timeout(batt, [S, I, O], timeout=timeout)

        t_set = set()
        if o['train'][i] is not None:
            all_o = all_o.union(o['train'][i])
            for t, e, i, m in o['train'][i]:
                t_set.add(t)

            # Add 1 just once for each t value
            for t in t_set:
                if t not in score:
                    score[t] = 0
                score[t] += 1
        
    for i, sample in enumerate(test_task):
        I = sample['input']
        O = sample['output']
        timed_out, o['test'][i] = run_with_timeout(batt, [S, I, O], timeout=timeout)

        t_set = set()
        if o['test'][i] is not None:
            all_o = all_o.union(o['test'][i]) 
            for t, e, i, m in o['test'][i]:
                t_set.add(t)

            # Add 1 just once for each t value
            for t in t_set:
                if t not in score:
                    score[t] = 0                    
                score[t] += 1

    elapsed = timer() - start_time
    len_task = len(train_task) + len(test_task)
    print(f'{len(all_o)}/{len_task} - {elapsed:.1f}s - {elapsed / (task_num + 1):.1f}spt')

    # Save solutions
    for solution in all_o:
        sol_t, sol_e, sol_i, sol_m = solution

        # if not solution[3]:
        #     continue

        # Track calls then reverse sequence to rebuild solver
        done = track_solution(sol_t, None)

        # Build solution body
        solver_body = ''
        for t_num in sorted(done):
            t = t_call[t_num].split(',')
            func = t[0]
            args = t[1:]
            solver_body += f'    t{t_num} = '
            solver_body += f'{func}('
            solver_body += ', '.join(args)
            solver_body += ')\n'
        solver_body += f'    return t{sol_t}\n'

        # Get md5_hash of generic source code
        generic_solver_source = f'def solve(S, I):\n{solver_body}'
        generic_inlined_source = inline_variables(generic_solver_source)
        md5_hash = hashlib.md5(generic_inlined_source.encode()).hexdigest()

        actual_solver_source = f'def solve_{md5_hash}(S, I):\n{solver_body}'
        actual_inlined_source = inline_variables(actual_solver_source)

        # Write inlined source to file
        ensure_dir('solver_dir')
        solve_task = f'solver_dir/solve_{task_id}'

        ensure_dir(solve_task)
        ensure_dir('solver_md5')

        long_hash = f'{md5_hash}_{score[sol_t]}'
        solve_name = f'solver_md5/{long_hash}'

        with open(f'{solve_name}.def', 'w') as f:
            f.write(actual_inlined_source)
            f.write('\n')

        solve_link = f'solver_dir/solve_{task_id}/{long_hash}'

        symlink(f'{solve_name}.def', f'{solve_link}.def')
        symlink(f'{solve_name}.py', f'{solve_link}.py')


        # TODO Control this with option
        # # Check things
        # python_exp = 'python expand_solver.py -q --source solver_dir/ --solvers-file solvers_dir.py'
        # python_cmd = f'python run_test.py --solvers solvers_dir -k {task_id}_{md5_hash}'
        # os.system(python_exp)
        # assert(os.system(python_cmd) == 0), f"Incorrect solution found by:\n{python_cmd}"


    # No timeout
    return False


def symlink(file_name, link_name):
    """
    Create a symlink for the given file.
    If the symlink already exists, remove it and create a new one.
    """
    full_name = f'../../{file_name}'
    try:
        os.symlink(full_name, link_name)
    except FileExistsError:
        os.remove(link_name)
        os.symlink(full_name, link_name)


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def track_solution(t_num, done):
    if done is None:
        done = set()

    if t_num not in done:
        done.add(t_num)

    call = t_call[t_num]

    # print_l(call)

    if t_list := re.findall(r't(\d+)', call):
        for t_str in t_list:
            t_num = int(t_str)
            if t_num not in done:
                done.add(t_num)
                track_solution(t_num, done)

    return done


def pick_rnd_task(task_list, total_data):
    task_sizes = []
    for task_id in task_list:
        size = 0
        for S in total_data['train'][task_id] + total_data['test'][task_id]:
            for ex in S.values():
                size += sum(len(inner) for inner in ex)
        task_sizes.append(size)

    weighted_tasks = list(zip(task_list, task_sizes))
    inverse_weights = [1/size for _, size in weighted_tasks]

    task_id = random.choices(
        [t_id for t_id, _ in weighted_tasks],
        weights=inverse_weights,
        k=1
    )[0]

    return [task_id]


def main(do_list, start=0, count=0, timeout=1):
    train_data = get_data(train=True, sort_by_size=True)
    # eval_data = get_data(train=False, sort_by_size=True)
    # total_data = {k: {**train_data[k], **eval_data[k]} for k in ['train', 'test']}
    total_data = train_data

    # NOTE We could have a task list just for unsolved tasks
    full_list = list(total_data['train'].keys())

    task_list = full_list[start:start + count] if count > 0 else full_list[start:]

    if do_list is None:
        do_list = pick_rnd_task(task_list, total_data)
    elif len(do_list) == 0:
        # List all tasks
        do_list = task_list

    # Run batt for each task in do_list
    start_time = timer()
    timeout = sum(run_batt(total_data, task_num, task_id, start_time, timeout)
              for task_num, task_id in enumerate(do_list))
    
    print(f'{len(do_list)} tasks - {timeout} timeouts')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run batt on specified tasks')
    parser.add_argument('--tasks', '-t', nargs='*', default=None,
                        help='List of task IDs to run (default: random task)')
    parser.add_argument('--start', '-s', type=int, default=0,
                        help='Start from this task number (default: 0)')
    parser.add_argument('--count', '-c', type=int, default=0,
                        help='Number of tasks to run (default: 0 - all tasks)')
    parser.add_argument('--timeout', '-to', type=int, default=1,
                        help='Timeout for each task in seconds (default: 1)')
    args = parser.parse_args()

    main(do_list=args.tasks, start=args.start, count=args.count, timeout=args.timeout)