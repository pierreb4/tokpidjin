import random
import re
import ast

from timeit import default_timer as timer

from utils import *
from batt import batt
from call import t_call


class VariableInliner(ast.NodeTransformer):
    def __init__(self):
        self.assignments = {}
        self.safe_to_inline = set()  # Track which variables are safe to inline
        self.processing = set()      # Track variables being processed to avoid recursion loops
        # self.func_name = ''
        # self.all_func_names = set()  # NEW: Track all function names seen
        # self.func_name_counts = {}   # NEW: Count frequency of each function name
        # self.func_name_order = []    # NEW: Track order of function names encountered

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


def run_batt(total_data, task_id, start_time):
    train_task = total_data['train'][task_id]
    test_task = total_data['test'][task_id]
    # total_task = total_data['train'][task_id] + total_data['test'][task_id]

    o = {'train': {}, 'test': {}}
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in train_task)

    print(f'------ {task_id} ', end='')

    for i, sample in enumerate(train_task):
        I = sample['input']
        O = sample['output']
        o['train'][i] = batt(S, I, O)
        # print(f"Sample: {i+1}/{len(train_task)} - {o['train'][i] = }")
        print('-', end='', flush=True)

    for i, sample in enumerate(test_task):
        I = sample['input']
        O = sample['output']
        o['test'][i] = batt(S, I, O)
        # print(f"Sample: {i+1}/{len(test_task)} - {o['test'][i]} = ")
        print('-', end='', flush=True)


    # Values present in all output lists are valid solutions
    valid_solutions = set(o['train'][0])
    for sample in o['train']:
        valid_solutions.intersection_update(set(o['train'][sample]))
    for sample in o['test']:
        valid_solutions.intersection_update(set(o['test'][sample]))

    if not valid_solutions:
        print('<')
        print(f"Failed {task_id} after {timer() - start_time:.1f}s")
    else:
        print('>')

    # Print valid solutions
    for solution in valid_solutions:
        print(f"Solved {task_id} after {timer() - start_time:.1f}s from {solution}")

        # Track calls then reverse sequence to rebuild solver
        t_var = solution[1]
        done = track_solution(t_var, None)

        # Rebuild solution
        solver_source = f'def solve_{solution[0]}(S, I):\n'
        for t_var in sorted(done, key=lambda x: int(x[1:])):
            solver_source += f'    {t_var} = {t_call[t_var]}\n'
        solver_source += f'    O = {t_call[solution[1]]}\n'
        solver_source += '    return O\n'

        # print(solver_source)

        # Write inlined source to file
        suffix = f'_{solution[3]}' if solution[2] else ''
        if not os.path.exists('solver_tst'):
            os.makedirs('solver_tst')
        with open(f'solver_tst/solve_{task_id}{suffix}.def', 'w') as f:
            f.write(inline_variables(solver_source))
            f.write('\n')


def track_solution(t_var, done):
    if done is None:
        done = set()

    call = t_call[t_var]
    if t_list := re.findall(r't\d+', call):
        for t_var in t_list:
            if t_var not in done:
                done.add(t_var)
                track_solution(t_var, done)

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

    # XXX Limit to first 5
    # task_list = full_list[:5]
    task_list = full_list

    if do_list is None:
        do_list = pick_rnd_task(task_list, total_data)
    elif len(do_list) == 0:
        # List all tasks
        do_list = task_list

    # Run batt for each task in do_list
    start_time = timer()
    for task_id in do_list:
        run_batt(total_data, task_id, start_time)


if __name__ == "__main__":
    # TODO Make these proper options
    # Random task
    # do_list = None
    # All tasks
    do_list = []
    # Specific task(s)
    # do_list = ['662c240a']

    main(do_list)