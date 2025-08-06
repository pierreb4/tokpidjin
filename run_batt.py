import argparse
import random
import re
import ast
import hashlib
import math
import importlib

from timeit import default_timer as timer
from pathlib import Path

from utils import *
from expand_solver import expand_file
from run_test import check_solver_speed


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


def check_batt(total_data, task_i, task_id, start_time, fluff_log_path, timeout=1):
    task_start = timer()
    train_task = total_data['train'][task_id]
    test_task = total_data['test'][task_id]
    # total_task = total_data['train'][task_id] + total_data['test'][task_id]

    o = {'train': {}, 'test': {}}
    s = {'train': {}, 'test': {}}
    all_o = set()
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in train_task)

    print_l(f'-- {task_id} - {task_i} --')

    s_score = {}
    o_score = {}
    for i, sample in enumerate(train_task):
        I = sample['input']
        O = sample['output']
        flags = Flags(True, False)
        timed_out, run_result = run_with_timeout(batt,
            [task_id, S, I, O, flags, fluff_log_path], timeout)

        if timed_out:
            print_l(f'-- {task_id} - train[{i}] timed out')

        t_set = set()
        if run_result is not None:
            o['train'][i], s['train'][i] = run_result
            all_o = all_o.union(o['train'][i])
            for t_n, evo, solver_id, match in o['train'][i]:
                update_scores(o_score, solver_id, match)

                if names := [
                    s_t[1] for s_t in s['train'][i] if s_t[0] == 'None'
                ]:
                    if solver_id not in s_score:
                        s_score[solver_id] = 0

                    for name in set(names):
                        for s_t in s['train'][i]:
                            none_val = s_t[2] if s_t[1] == name and s_t[0] == 'None' else 0
                            last_val = s_t[2] if s_t[1] == name and s_t[0] == solver_id else 0
                            diff_val = max(0, none_val - last_val)
                            s_score[solver_id] += diff_val

                    # Add 1 to o_score just once for each t value
                    # NOTE o_score is the number of tasks solved by solver_id solver
                    # for solver_id in t_set:
                    #     update_scores(task_start, solver_id, o_score, t_log)

    for i, sample in enumerate(test_task):
        I = sample['input']
        O = sample['output']
        flags = Flags(False, False)
        timed_out, run_result = run_with_timeout(batt, \
            [task_id, S, I, O, flags, fluff_log_path], timeout=timeout)

        if timed_out:
            print_l(f'-- {task_id} - test[{i}] timed out')

        t_set = set()
        if run_result is not None:
            o['test'][i], s['test'][i] = run_result
            all_o = all_o.union(o['test'][i])
            for t_n, evo, solver_id, match in o['test'][i]:
                update_scores(o_score, solver_id, match)

                if names := [
                    s_t[1] for s_t in s['test'][i] if s_t[0] == 'None'
                ]:
                    if solver_id not in s_score:
                        s_score[solver_id] = 0

                    for name in set(names):
                        for s_t in s['test'][i]:
                            none_val = s_t[2] if s_t[1] == name and s_t[0] == 'None' else 0
                            last_val = s_t[2] if s_t[1] == name and s_t[0] == solver_id else 0
                            diff_val = max(0, none_val - last_val)
                            s_score[solver_id] += diff_val

                            # if s_tuples and names:
                            #     for name in set(names):
                            #         max_val = max(t[2] for t in s_tuples if t[1] == name)
                            #         min_val = min(t[2] for t in s_tuples if t[1] == name)

                            # if solver_id not in s_score:
                            #     s_score[solver_id] = 0
                            # s_score[solver_id] += max_val - min_val

                    # Add 1 to o_score just once for each t value
                    # NOTE o_score is the number of tasks solved by solver_id solver
                    # for solver_id in t_set:
                    #     update_scores(task_start, solver_id, o_score, t_log)

    elapsed = timer() - start_time
    len_task = len(train_task) + len(test_task)
    # print_l(f'-- {len(all_o)}/{len_task} - {elapsed:.1f}s - {elapsed / (task_i + 1):.1f}spt')
    # print_l(f'-- {o_score[t]}/{len_task} - {elapsed:.1f}s - {elapsed / (task_i + 1):.1f}spt')
    # return all_o, o_score, s_score, t_log
    return all_o, o_score, s_score


def update_scores(o_score, solver_id, match):
    if solver_id not in o_score:
        o_score[solver_id] = 0
    o_score[solver_id] += match


def old_update_scores(task_start, solver_id, o_score, t_log):
    if solver_id not in o_score:
        o_score[solver_id] = 0
    o_score[solver_id] += 1

    # XXX t_log is the run time of all batt
    #     We need to get the run time per task
    t_log[solver_id] = 11 - int(math.log(timer() - task_start))


def run_batt(total_data, task_i, task_id, start_time, fluff_log_path, timeout=1):
    # all_o, o_score, s_score, t_log = check_batt(total_data, 
    #         task_i, task_id, start_time, fluff_log_path, timeout=1)
    all_o, o_score, s_score = check_batt(total_data, 
            task_i, task_id, start_time, fluff_log_path, timeout=1)

    # Save solutions
    # NOTE all_o contains solutions to 'train' and 'test' tasks
    #      Maybe don't save twice the same things
    for solution in all_o:
        sol_t, sol_e, sol_solver_id, sol_m = solution

        # Track calls then reverse sequence to rebuild solver
        done = track_solution(sol_t, None)

        # Build solution body
        solver_body = ''
        for t_num in sorted(done):
            # t = t_call[t_num].split(',')
            t_split = [item.strip() for item in t_call[t_num].split(',')]
            t = [s[:-2] if s.endswith('.t') else s for s in t_split]

            func = t[0]
            args = t[1:]
            solver_body += f'    t{t_num} = '
            solver_body += f'{func}('
            solver_body += ', '.join(args)
            solver_body += ')\n'
        solver_body += f'    return t{sol_t}\n'

        # Get md5_hash of inlined source code
        solver_source = f'def solve(S, I):\n{solver_body}'
        inlined_source = inline_variables(solver_source)
        md5_hash = hashlib.md5(inlined_source.encode()).hexdigest()

        # Write inlined source to file
        ensure_dir('solver_dir')
        solve_task = f'solver_dir/solve_{task_id}'
        ensure_dir(solve_task)

        ensure_dir('solver_def')
        solver_def_path = f'solver_def/{md5_hash}.def'

        ensure_dir('solver_md5')
        solver_md5_path = f'solver_md5/{md5_hash}.py'

        check_start = timer()
        timed_out = check_solver_speed(total_data, solver_source, task_id, timeout)
        t_log = 11 - int(math.log(timer() - check_start))

        # save_file = not timed_out
        # if timed_out:
        #     print_l(f'Solver for {task_id} timed out')
        #     continue

        if not Path(solver_def_path).exists():
            with open(solver_def_path, 'w') as f:
                f.write(inlined_source)
                f.write('\n')

        # Expand to .py file
        if not Path(solver_md5_path).exists():
            expand_file(solver_def_path, solver_md5_path, None, True)

        # Get s_score for this task, or 0
        # task_o_score = o_score.get(sol_solver_id, 0)
        # task_s_score = s_score.get(task_id, 0)
        # solver_score = f'solver_dir/solve_{sol_solver_id}/{task_o_score}/{task_s_score}/{t_log}'

        # NOTE sol_solver_id is where the solver comes from
        # and task_id is what it solves
        # task_o_score = o_score.get(task_id, 0)
        # task_s_score = s_score.get(task_id, 0)
        task_o_score = o_score.get(sol_solver_id, 0)
        task_s_score = s_score.get(sol_solver_id, 0)
        solver_score = f'solver_dir/solve_{task_id}/{task_o_score}/{task_s_score}/{t_log}'

        # print_l(f'-> {solver_score}/{md5_hash}.py')

        ensure_dir(solver_score)
        solver_link = f'{solver_score}/{md5_hash}.py'

        symlink(solver_md5_path, solver_link)


        # TODO Control this with option
        # # Check things
        # python_exp = 'python expand_solver.py -q --source solver_dir/ --solvers-file solvers_dir.py'
        # python_cmd = f'python run_test.py --solvers solvers_dir -k {task_id}_{md5_hash}'
        # os.system(python_exp)
        # assert(os.system(python_cmd) == 0), f"Incorrect solution found by:\n{python_cmd}"


    # No timeout
    return False


def symlink(file_path, link_path):
    """
    Create a symlink for the given file.
    If the symlink already exists, remove it and create a new one.
    """
    home_folder = Path.home()
    full_name = f'{home_folder}/dsl/tokpidjin/{file_path}'
    try:
        os.symlink(full_name, link_path)
    except FileExistsError:
        os.remove(link_path)
        os.symlink(full_name, link_path)


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

    if start == 0 and count < 0:
        task_list = random.sample(full_list, -count)
    else:
        task_list = full_list[start:start + count] if count > 0 else full_list[start:]

    if do_list is None:
        do_list = pick_rnd_task(task_list, total_data)
    elif len(do_list) == 0:
        # List all tasks
        do_list = task_list

    # Run batt for each task in do_list
    start_time = timer()
    fluff_log_path = 'fluff.log'
    if os.path.isfile(fluff_log_path):
        os.remove(fluff_log_path)
    timeout = sum(run_batt(total_data, task_i, task_id, start_time, fluff_log_path, timeout)
              for task_i, task_id in enumerate(do_list))
    
    print(f'{len(do_list)} tasks - {timeout} timeouts')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run batt on specified tasks')
    parser.add_argument('-i', '--task_ids', nargs='*', default=None,
                        help='List of task IDs to run (default: random task)')
    parser.add_argument('-s', '--start', type=int, default=0,
                        help='Start from this task number (default: 0)')
    parser.add_argument('-c', '--count', type=int, default=0,
                        help='Number of tasks to run (default: 0 - all tasks)')
    parser.add_argument('-t', '--timeout', type=float, default=1,
                        help='Timeout for each task in seconds (default: 1)')
    parser.add_argument('-b', '--batt_import', type=str, default='batt',
                        help='Module to import for batt (default: batt)')
    args = parser.parse_args()

    batt_module = importlib.import_module(args.batt_import)
    batt = batt_module.batt if hasattr(batt_module, 'batt') else batt

    call_module = importlib.import_module(f'{args.batt_import}_call')
    t_call = call_module.t_call if hasattr(call_module, 't_call') else {}

    main(do_list=args.task_ids, start=args.start, count=args.count, timeout=args.timeout)