import argparse
import random
import re
import ast
import hashlib
import math
import importlib
import os

from timeit import default_timer as timer
from pathlib import Path
from collections import defaultdict
from contextlib import contextmanager

from utils import *
import utils as utils_module
from expand_solver import expand_file
import expand_solver as expand_solver_module
from run_test import check_solver_speed


def check_batt(total_data, task_i, task_id, d_score, start_time, fluff_log_path, timeout=1, prof=None):
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
        if prof is not None:
            prof_start = timer()
        timed_out, run_result = run_with_timeout(batt,
            [task_id, S, I, O, flags, fluff_log_path], timeout)
        if prof is not None:
            prof['batt.train.run_with_timeout'] += timer() - prof_start

        if timed_out:
            print_l(f'-- {task_id} - train[{i}] timed out')

        t_set = set()
        if run_result is not None:
            o['train'][i], s['train'][i] = run_result

            print_l(f"train[{i}] - {task_id} - {len(o['train'][i])} - {len(s['train'][i])}")

            all_o = all_o.union(o['train'][i])
            for t_n, evo, o_solver_id, match in o['train'][i]:


                # if not evo:
                #     continue

                update_scores(o_score, o_solver_id, match)

                for last_t, s_solver_id, d_name, score in s['train'][i]:
                    if s_solver_id == 'None':
                        d_score[d_name] = {'last_t': last_t, 'score': 0}

                if o_solver_id not in s_score:
                    s_score[o_solver_id] = 0

                if prof is not None:
                    loop_start = timer()
                for name in d_score.keys():
                    for last_t, s_solver_id, d_name, score in s['train'][i]:
                        none_val = score if name == d_name and s_solver_id == 'None' else 0
                        last_val = score if name == d_name and s_solver_id == o_solver_id else 0
                        diff_val = max(0, none_val - last_val)
                        s_score[o_solver_id] += diff_val

                        if name == d_name and none_val > 0 and ((last_val == 0 and match) or (last_val != 0 and not match)):
                            d_score[name]['score'] += 1
                if prof is not None:
                    prof['batt.train.scoring'] += timer() - loop_start

    for i, sample in enumerate(test_task):
        I = sample['input']
        O = sample['output']
        flags = Flags(False, False)
        if prof is not None:
            prof_start = timer()
        timed_out, run_result = run_with_timeout(batt,
            [task_id, S, I, O, flags, fluff_log_path], timeout)
        if prof is not None:
            prof['batt.test.run_with_timeout'] += timer() - prof_start

        if timed_out:
            print_l(f'-- {task_id} - test[{i}] timed out')

        t_set = set()
        if run_result is not None:
            o['test'][i], s['test'][i] = run_result

            print_l(f"test[{i}] - {task_id} - {len(o['test'][i])} - {len(s['test'][i])}")

            all_o = all_o.union(o['test'][i])
            for t_n, evo, o_solver_id, match in o['test'][i]:


                # if not evo:
                #     continue


                update_scores(o_score, o_solver_id, match)

                for last_t, s_solver_id, d_name, score in s['test'][i]:
                    if s_solver_id == 'None':
                        d_score[d_name] = {'last_t': last_t, 'score': 0}

                if o_solver_id not in s_score:
                    s_score[o_solver_id] = 0

                if prof is not None:
                    loop_start = timer()
                for name in d_score.keys():
                    for last_t, s_solver_id, name, score in s['test'][i]:
                        none_val = score if name == d_name and s_solver_id == 'None' else 0
                        last_val = score if name == d_name and s_solver_id == o_solver_id else 0
                        diff_val = max(0, none_val - last_val)
                        s_score[o_solver_id] += diff_val

                        if name == d_name and none_val > 0 and ((last_val == 0 and match) or (last_val != 0 and not match)):
                            d_score[name]['score'] += 1
                if prof is not None:
                    prof['batt.test.scoring'] += timer() - loop_start


    elapsed = timer() - start_time
    len_task = len(train_task) + len(test_task)
    return all_o, o_score, s_score, d_score


def update_scores(o_score, solver_id, match):
    if solver_id not in o_score:
        o_score[solver_id] = 0
    o_score[solver_id] += match


def run_batt(total_data, task_i, task_id, d_score, start_time, fluff_log_path, timeout=1, prof=None):
    if prof is not None:
        prof_call_start = timer()
    all_o, o_score, s_score, d_score = check_batt(total_data,
            task_i, task_id, d_score, start_time, fluff_log_path, timeout=1, prof=prof)
    if prof is not None:
        prof['run_batt.check_batt'] += timer() - prof_call_start

    # NOTE all_o contains solutions to 'train' and 'test' tasks
    #      Maybe don't save twice the same things
    for solution in all_o:
        sol_t, sol_e, sol_solver_id, sol_m = solution

        # Track calls then reverse sequence to rebuild solver
        if prof is not None:
            t0 = timer()
        done = track_solution(sol_t, None)
        if prof is not None:
            prof['run_batt.track_solution'] += timer() - t0

        # Build solution body
        solver_body = ''
        for t_num in sorted(done):
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
        solver_source = f'def solve(S, I, O=None):\n{solver_body}'
        if prof is not None:
            t0 = timer()
        inlined_source = inline_variables(solver_source)
        if prof is not None:
            prof['run_batt.inline_variables'] += timer() - t0
        md5_hash = hashlib.md5(inlined_source.encode()).hexdigest()

        # Put task_id in function name to amke solvers_dir.py usable
        solver_source = re.sub(r'def solve\((.*)\):', f'def solve_{task_id}(\g<1>):', solver_source)
        inlined_source = inline_variables(solver_source)

        # Write inlined source to file
        ensure_dir('solver_dir')
        solve_task = f'solver_dir/solve_{task_id}'
        ensure_dir(solve_task)

        ensure_dir('solver_def')
        solver_def_path = f'solver_def/{md5_hash}.def'

        ensure_dir('solver_md5')
        solver_md5_path = f'solver_md5/{md5_hash}.py'

        check_start = timer()
        if prof is not None:
            t0 = timer()
        timed_out = check_solver_speed(total_data, solver_source, task_id, timeout)
        if prof is not None:
            prof['run_batt.check_solver_speed'] += timer() - t0
        t_log = 11 - int(math.log(timer() - check_start))

        if not Path(solver_def_path).exists():
            with open(solver_def_path, 'w') as f:
                f.write(inlined_source)
                f.write('\n')

        # Expand to .py file
        if not Path(solver_md5_path).exists():
            if prof is not None:
                t0 = timer()
            expand_file(solver_def_path, solver_md5_path, None, True)
            if prof is not None:
                prof['run_batt.expand_file'] += timer() - t0

        task_o_score = o_score.get(sol_solver_id, 0)
        task_s_score = s_score.get(sol_solver_id, 0)
        solver_score = f'solver_dir/solve_{task_id}/{task_o_score}/{task_s_score}/{t_log}'

        if prof is not None:
            t0 = timer()
        ensure_dir(solver_score)
        if prof is not None:
            prof['run_batt.ensure_dir'] += timer() - t0
        solver_link = f'{solver_score}/{md5_hash}.py'

        if prof is not None:
            t0 = timer()
        symlink(solver_md5_path, solver_link)
        if prof is not None:
            prof['run_batt.symlink'] += timer() - t0


        # TODO Control this with option
        # # Check things
        # python_exp = 'python expand_solver.py -q --source solver_dir/ --solvers-file solvers_dir.py'
        # python_cmd = f'python run_test.py --solvers solvers_dir -k {task_id}_{md5_hash}'
        # os.system(python_exp)
        # assert(os.system(python_cmd) == 0), f"Incorrect solution found by:\n{python_cmd}"

    # No timeout
    return False, d_score


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


def main(do_list, start=0, count=0, timeout=1, enable_timing=False, profile=None):
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

    d_score = {}
    d_score_sum = {}
    to_sum = 0
    prof = defaultdict(float) if enable_timing else None
    if prof is not None:
        # Register profiler with modules that support it
        if hasattr(utils_module, 'set_profiler'):
            utils_module.set_profiler(prof)
        if hasattr(expand_solver_module, 'set_profiler'):
            expand_solver_module.set_profiler(prof)
    for task_i, task_id in enumerate(do_list):
        loop_start = timer() if prof is not None else None
        to, d_score = run_batt(total_data, task_i, task_id, d_score, start_time, fluff_log_path, timeout, prof=prof)
        if prof is not None:
            prof['main.run_batt'] += timer() - loop_start
        if to:
            to_sum += 1
        for name, value in d_score.items():
            if name not in d_score_sum:
                d_score_sum[name] = {'last_t': value['last_t'], 'score': 0}
            d_score_sum[name]['score'] += value['score']
    
    print_l(f'{d_score_sum}')

    print(f'{len(do_list)} tasks - {to_sum} timeouts')

    # Print lightweight timing report
    if prof is not None:
        print("\nTiming summary (seconds):")
        for k, v in sorted(prof.items(), key=lambda kv: kv[1], reverse=True):
            print(f"  {k:32s} {v:8.3f}")


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
    parser.add_argument('--timing', action='store_true', help='Print lightweight timing breakdown')
    parser.add_argument('--cprofile', action='store_true', help='Run with cProfile and print top stats')
    parser.add_argument('--cprofile-top', type=int, default=30, help='Number of top functions to show in cProfile')
    args = parser.parse_args()

    batt_module = importlib.import_module(args.batt_import)
    batt = batt_module.batt if hasattr(batt_module, 'batt') else batt

    call_module = importlib.import_module(f'{args.batt_import}_call')
    t_call = call_module.t_call if hasattr(call_module, 't_call') else {}

    if args.cprofile:
        import cProfile, pstats, io
        pr = cProfile.Profile()
        pr.enable()
        main(do_list=args.task_ids, start=args.start, count=args.count, timeout=args.timeout, enable_timing=args.timing)
        pr.disable()
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats(args.cprofile_top)
        print('\n[cProfile cumulative top]')
        print(s.getvalue())
        s = io.StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
        ps.print_stats(args.cprofile_top)
        print('\n[cProfile tottime top]')
        print(s.getvalue())
    else:
        main(do_list=args.task_ids, start=args.start, count=args.count, timeout=args.timeout, enable_timing=args.timing)