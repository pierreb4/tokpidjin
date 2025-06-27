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


def run_batt(total_data, task_num, task_id, start_time):
    train_task = total_data['train'][task_id]
    test_task = total_data['test'][task_id]
    # total_task = total_data['train'][task_id] + total_data['test'][task_id]

    o = {'train': {}, 'test': {}}
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in train_task)

    print(f'------ {task_id} - {task_num} ', end='')

    for i, sample in enumerate(train_task):
        I = sample['input']
        O = sample['output']
        # o['train'][i] = batt(S, I, O)
        timed_out, o['train'][i] = run_with_timeout(batt, [S, I, O], timeout=2)
        if timed_out:
            print('|')
            # Give up on this task
            return True
        # print(f"Sample: {i+1}/{len(train_task)} - {o['train'][i] = }")
        print('+', end='', flush=True)

    for i, sample in enumerate(test_task):
        I = sample['input']
        O = sample['output']
        # o['test'][i] = batt(S, I, O)
        timed_out, o['test'][i] = run_with_timeout(batt, [S, I, O], timeout=2)
        if timed_out:
            print('|')
            # Give up on this task
            return True
        # print(f"Sample: {i+1}/{len(test_task)} - {o['test'][i]} = ")
        print('-', end='', flush=True)

    # Values present in all output lists are valid solutions
    # TODO Keep track of partial solutions, then try improving them
    valid_solutions = set(o['train'][0])
    for sample in o['train']:
        valid_solutions.intersection_update(set(o['train'][sample]))
    for sample in o['test']:
        valid_solutions.intersection_update(set(o['test'][sample]))

    if not valid_solutions:
        print('<')
        elapsed = timer() - start_time
        print(f"Failed {task_id} after {elapsed:.1f}s - {elapsed / (task_num + 1):.1f}spt")
    else:
        print('>')

    # Print valid solutions
    for solution in valid_solutions:
        elapsed = timer() - start_time
        print(f"Solved {task_id} after {elapsed:.1f}s - {elapsed / (task_num + 1):.1f}spt from {solution}")

        # Track calls then reverse sequence to rebuild solver
        done = track_solution(solution[1], None)

        # print_l(f'{done = }')

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
        solver_body += f'    return t{solution[1]}\n'

        # Get md5_hash of the source code
        md5_hash = hashlib.md5(solver_body.encode()).hexdigest()
        solver_source = f'def solve_{md5_hash}(S, I):\n{solver_body}'

        # print(solver_source)

        # Write inlined source to file
        ensure_dir('solver_md5')

        solve_name = f'solver_md5/{md5_hash}'
        with open(f'{solve_name}.def', 'w') as f:
            f.write(inline_variables(solver_source))
            f.write('\n')

        ensure_dir('solver_dir')
        solve_task = f'solver_dir/solve_{task_id}'

        ensure_dir(solve_task)
        solve_link = f'solver_dir/solve_{task_id}/{md5_hash}'

        symlink(f'{solve_name}.def', f'{solve_link}.def')
        symlink(f'{solve_name}.py', f'{solve_link}.py')


        # # Check things
        # python_exp = 'python expand_solver.py -q --source solver_lnk/ --solvers-file solvers_lnk.py'
        # python_cmd = f'python run_test.py --solvers solvers_lnk -k {task_id}'
        # os.system(python_exp)
        # assert(os.system(python_cmd) == 0), f"Incorrect solution found by:\n{python_cmd}"


    # No timeout
    return False


def symlink(file_name, link_name):
    """
    Create a symlink for the given file.
    If the symlink already exists, remove it and create a new one.
    """
    # full_name = os.path.abspath(file_name)
    full_name = f'../../{file_name}'
    try:
        os.symlink(full_name, link_name)
    except FileExistsError:
        # If the symlink already exists, remove it and create a new one
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


def main(do_list):
    train_data = get_data(train=True, sort_by_size=True)
    eval_data = get_data(train=False, sort_by_size=True)
    total_data = {k: {**train_data[k], **eval_data[k]} for k in ['train', 'test']}

    # NOTE We could have a task list just for unsolved tasks
    full_list = list(total_data['train'].keys())

    # XXX Limit to first few
    # task_list = full_list[:9]
    task_list = full_list

    if do_list is None:
        do_list = pick_rnd_task(task_list, total_data)
    elif len(do_list) == 0:
        # List all tasks
        do_list = task_list

    # Run batt for each task in do_list
    start_time = timer()
    timeout = sum(run_batt(total_data, task_num, task_id, start_time)
              for task_num, task_id in enumerate(do_list))
    
    print(f'{len(do_list)} tasks - {timeout} timeouts')


if __name__ == "__main__":
    # TODO Optionally accept a task_num to restart from there
    # TODO Make these proper options    
    # Random task
    # do_list = None
    # All tasks
    do_list = []
    # Specific task(s)
    # do_list = ['662c240a']

    main(do_list)