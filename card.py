import re
import random
import time
import inspect

from pprint import pprint

from utils import *
from constants import *
from dsl import *


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


# Borrowed from regin.py maybe can go to utils.py?
def get_hints(node_name):
    if node_name not in globals():
        return None

    global_id = globals()[node_name]
    if not inspect.isfunction(global_id):
        return None

    return [t for var, t in global_id.__annotations__.items()]


def clean_call(call):
    return call.replace('(', ', ').replace(')', '')

def get_items(call):
    return call.strip('[]').split(',')


def mutate(t_call, t_num, has_mutation, task_id):
    old_call = clean_call(t_call[f't{t_num}'])
    ret_call = old_call

    old_items = get_items(old_call)
    old_func_name = old_items[0].strip()
    old_hints = get_hints(old_func_name)

    if random.random() > 0.5:
        return ret_call
    
    if arg_list := re.findall(r'\b(\w+)\b', old_call):
        # TODO Track t variables to get to hints
        if old_hints is None:
            return ret_call

        for arg, old_hint in zip(arg_list, old_hints):
            # First deal with t variables
            if arg.startswith('t') and arg[1:].isdigit():
                t_num = int(arg[1:])

                while random.random() < 0.5:
                    t_offset = t_num - random.randint(1, 9)
                    if t_offset > 0:
                        new_call = clean_call(t_call[f't{t_offset}'])
                        new_items = get_items(new_call)
                        new_func_name = new_items[0].strip()
                        new_hints = get_hints(new_func_name)
                        new_hint = new_hints[0] if new_hints else None

                        if new_hint == old_hint:
                        # if random.random() < 0.01:
                        #     print_l(f'{t_num = }')
                        #     print_l(f'{old_items = }')
                        #     print_l(f'{old_hints = }')
                        #     print_l(f'{arg = }')
                        #     print_l(f'{old_hint = }')
                        #     print_l(f'{t_offset = }')
                        #     print_l(f'{new_call = }')
                        #     print_l(f'{new_hint = }')
                        #     print_l('--')
                            has_mutation[task_id] = True
                            ret_call = re.sub(rf'\bt{t_num}\b', f't{t_offset}', new_call)

    return ret_call


def main(file, seed):
    solvers = get_solvers()
    equals = {task_id: get_equals(source) for task_id, source in solvers.items()}
    # print_l(f"{get_equals(solvers['a85d4709']) = }")

    # XXX Limit to first 5
    # solvers = {k: solvers[k] for k in list(solvers.keys())[:5]}
    solvers = {k: solvers[k] for k in list(solvers.keys())}

    t_call = {}
    t_name = {}
    # Start from t1
    t_num = 1
    has_mutation = {}
    for _ in range(999):
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

            # Remove entry from equals
            del equals[task_id][old_name]

            # Else is the right side new?
            has_mutation[task_id] = False
            if old_call not in t_name.keys():
                # Then add it to t_call/t_name
                t_k = f't{t_num}'
                t_call[t_k] = old_call
                t_name[old_call] = t_k

                call = mutate(t_call, t_num, has_mutation, task_id)                                    
                print(f'    {t_k} = env.do_fluff({t_num}, [{call}]) # {task_id} - {has_mutation[task_id]}', file=file)
                t_num += 1

            # Was the left side O?
            if old_name == 'O':
                print(f"    if {t_name[old_call]} == O:", file=file)
                print(f"        o.append(('{task_id}', '{t_name[old_call]}', {has_mutation[task_id]}, env.get_seed()))", file=file)

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
f"""# Generated by tokpidjin/card.py

from fluff import *


def batt(S, I, O):
    env = Env({seed}, S)
    o = []""", file=batt_file)
        main(batt_file, seed)
        print("    return o", file=batt_file)
