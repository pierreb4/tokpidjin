import re
import random
import time


from utils import *


# Combine all solvers in solver_evo into a single one

# Outline with examples:

# 1. Read all source files in the solver_evo directory
"""
def solve_f25fbde4(S, I):
    x1 = o_g(I, R7)
    x2 = get_nth_f(x1, F0)
    x3 = subgrid(x2, I)
    O = upscale_t(x3, TWO)
    return O

def solve_a740d043(S, I):
    x1 = o_g(I, R7)
    x2 = merge_f(x1)
    x3 = subgrid(x2, I)
    O = replace(x3, ONE, ZERO)
    return O

# 2. Rename all variables to avoid conflicts
def solve_f25fbde4(S, I):
    t[0] = x1 = o_g(I, R7)
idx['x1']['f25fbde4'] = 0

def solve_a740d043(S, I):
    t[0] = x1 = o_g(I, R7)
idx['x1']['solve_a740d043'] = 0
next_idx = 1

def solve_f25fbde4(S, I):
    t[0] = x1 = o_g(I, R7)
    t[1] = x2 = get_nth_f(t[0], F0)
idx['x2']['f25fbde4'] = 1

def solve_a740d043(S, I):
    t[0] = x1 = o_g(I, R7)
    t[2] = x2 = merge_f(t[0])
idx['x2']['solve_a740d043'] = 2
next_idx = 3

def solve_f25fbde4(S, I):
    t[0] = x1 = o_g(I, R7)
    t[1] = x2 = get_nth_f(t[0], F0)
    t[3] = x3 = subgrid(t[1], I)
idx['x3']['f25fbde4'] = 3

def solve_a740d043(S, I):
    t[0] = x1 = o_g(I, R7)
    t[2] = x2 = merge_f(t[0])
    t[4] = x3 = subgrid(t[2], I)
idx['x3']['solve_a740d043'] = 4
next_idx = 5

def solve_f25fbde4(S, I):
    t[0] = x1 = o_g(I, R7)
    t[1] = x2 = get_nth_f(t[0], F0)
    t[3] = x3 = subgrid(t[1], I)
    t[5] = O = upscale_t(t[3], TWO)
    O -> check_done(t[5])

def solve_a740d043(S, I):
    t[0] = x1 = o_g(I, R7)
    t[2] = x2 = merge_f(t[0])
    t[4] = x3 = subgrid(t[2], I)
    t[6] = O = replace(t[4], ONE, ZERO)
    O -> check_done(t[6])


- Start from x1
  - Go through each solver
    - Is it empty?
    - Then remove it from solver list
    - Else take the first assignment - x1 = call(...)
      - Remove entry from equals
      - Was the left side O?
      - Then add check_done(O) to new solver
      - Else is the right side new?
        - Then add it to t_call/t_name
      - Replace x1 with t_name[x_call] in rest of solver

# 3. Output a single file, batt.py

"""


def get_equals(solver):
    # Catalog assignments in solvers
    equals = {}
    for line in solver.split('\n'):
        if ' = ' in line:
            parts = line.split(' = ')
            var_name = parts[0].strip()
            value = parts[1].strip()
            equals[var_name] = value
    return equals


def main(file, seed):
    solvers = get_solvers()

    # print_l(solvers.keys())
    # print(solvers['73182012'])

    equals = {}
    for task_id, source in solvers.items():
        equals[task_id] = get_equals(source)
    
    # print_l(f"{get_equals(solvers['a85d4709']) = }")

    # Work on sample of 3 first solvers
    solvers = {k: solvers[k] for k in list(solvers.keys())[:3]}

    count = 999
    t_call = {}
    t_name = {}
    # Start from t1
    t_num = 1
    while count > 0:
        count -= 1

        # Go through each solver
        solvers_copy = solvers.copy()
        for task_id, source in solvers_copy.items():
            # print_l(f"-- {task_id} -----")

            # Is it empty?
            if not equals[task_id]:
                # Then remove it from solver list
                del solvers[task_id]
                continue

            # Else take the first assignment - x1 = call(...)
            old_name, old_call = next(iter(equals[task_id].items()))

            # print_l(f"{old_name} = {old_call}")

            # Remove entry from equals
            del equals[task_id][old_name]

            # Else is the right side new?
            if old_call not in t_name.keys():
                # Then add it to t_call/t_name
                t_k = f't{t_num}'
                t_call[t_k] = old_call
                t_name[old_call] = t_k
                t_num += 1

                # print_l(f"{task_id}: {old_name} = {old_call}")
                # print_l(f"{task_id}: {t_k} = {t_call[t_k]}")

                # Print new source code
                # t_source = f"{t_k} = {t_call[t_k]}"
                call = t_call[t_k].replace('(', ', ').replace(')', '')
                # NOTE Maybe we won't need t_num
                # t_source = f"{t_k} = do_fluff(SEED, {t_num - 1}, ({call})"

                # TODO Add option to show exception, traceback
#                 print(
# f"""    try:
#         {t_k} = env.do_fluff({t_num - 1}, ({call})
#     except Exception as e:
#         # show_exception("", e)
#         print("traceback: ", traceback.format_exc())
#         {t_k} = None""", file=file)
                print(f'    {t_k} = env.do_fluff({t_num - 1}, [{call}])', file=file)

            # Was the left side O?
            if old_name == 'O':
                print(f"    if {t_name[old_call]} == O:", file=file)
                # print(f"        return True, '{task_id} - {t_name[old_call]}'", file=file)
                print(f"        o.append(('{task_id}', '{t_name[old_call]}'))", file=file)

            # Replace x1 with t_name[x_call] in rest of solver
            for x_name, x_call in equals[task_id].items():
                if old_name in x_call:
                    equals[task_id][x_name] = re.sub(rf'\b{old_name}\b', t_name[old_call], x_call)

    # Write t_call into new file call.py
    with open('call.py', 'w') as call_file:
        print(f'{t_call = }', file=call_file)


if __name__ == "__main__":
    seed = time.time()
    random.seed(seed)

    # Open file for writing
    with open('batt.py', 'w') as batt_file:
        print(
f"""# Generated by tokpidjin/card.py"
import inspect
import traceback

from utils import *
from constants import *
from dsl import *
from fluff import *


def batt(S, I, O):
    env = Env({seed}, S)
    o = []""", file=batt_file)
        main(batt_file, seed)
        print("    return o", file=batt_file)
