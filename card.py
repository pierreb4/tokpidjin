import argparse
import re
import random
import time
import inspect

from pprint import pprint

# import dsl

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

    hints = [t for var, t in global_id.__annotations__.items()]
    return hints[-1:] + hints[:-1]



def clean_call(call):
    return call.replace('(', ', ').replace(')', '')


def get_items(call):
    return call.strip('[]').split(',')


def replace_random(value, input_list):
    current_idx = input_list.index(value)
    if current_idx == 0:  # First element
        offset = 1
    elif current_idx == len(input_list) - 1:  # Last element
        offset = -1
    else:
        offset = random.choice([-1, 1])
    
    new_idx = current_idx + offset
    return input_list[new_idx]


class Code:
    def __init__(self, file, task_id=None, S=None, t_call=None, t_number=None, t_num=0, score=0):
        self.file = file
        self.task_id = task_id
        self.S = S

        if t_call is None:
            t_call = {}
        self.t_call = t_call

        if t_number is None:
            t_number = {}
        self.t_number = t_number

        self.t_num = t_num
        self.score = score


    def substitute_color(self, arg, constant_dict=COLORS):
        budget_random = 0.01

        # Get number corresponding to color constant
        # NOTE Maybe some x_n variables carry constants and could be replaced?
        if arg in constant_dict.keys():
            c = constant_dict[arg]
        elif arg in CONSTANTS.keys() and CONSTANTS[arg] in constant_dict.values():
            c = CONSTANTS[arg]
        else:
            # Probably 'Any' and not a color constant
            return arg

        S = self.S
        c_iz_l = c_iz(S, p_g)
        c_zo_l = c_zo(S, p_g)

        if c in c_iz_l and random.random() < 0.5:
            f_n = f'F{c_iz_l.index(c)}'
            return self.substitute_color_izzo('c_iz_n', f_n)
        elif c in c_zo_l and random.random() < 0.5:
            f_n = f'F{c_zo_l.index(c)}'
            return self.substitute_color_izzo('c_zo_n', f_n)
        elif random.random() < budget_random:
            # Same as usual random replacement
            return random.choice(list(constant_dict.keys()))

        # Get name corresponding to number
        constant_list = list(constant_dict.keys())
        return constant_list[c]

    def substitute_color_izzo(self, c_izzo_n, f_n):
        # Change the score at substitution time
        self.score -= 1
        t_call = self.t_call
        t_num = self.t_num

        t_call[t_num + 0] = 'identity, S'
        t_call[t_num + 1] = 'identity, p_g'
        t_call[t_num + 2] = f'rbind, get_nth_t, {f_n}'
        t_call[t_num + 3] = f'identity, t{t_num + 2}'
        t_call[t_num + 4] = f'{c_izzo_n}, t{t_num + 0}, t{t_num + 1}, t{t_num + 3}'
        self.t_num += 5

        print(f'    t{t_num + 0} = env.do_fluff({t_num + 0}, [{t_call[t_num + 0]}]) # {self.task_id} - True', file=self.file)
        print(f'    t{t_num + 1} = env.do_fluff({t_num + 1}, [{t_call[t_num + 1]}]) # {self.task_id} - True', file=self.file)
        print(f'    t{t_num + 2} = env.do_fluff({t_num + 2}, [{t_call[t_num + 2]}]) # {self.task_id} - True', file=self.file)
        print(f'    t{t_num + 3} = env.do_fluff({t_num + 3}, [{t_call[t_num + 3]}]) # {self.task_id} - True', file=self.file)
        print(f'    t{t_num + 4} = env.do_fluff({t_num + 4}, [{t_call[t_num + 4]}]) # {self.task_id} - True', file=self.file)
        return f't{t_num + 4}'


    def substitute_rank(self, arg, constant_dict):
        if arg not in constant_dict.keys():
            return arg

        budget_random = 0.01

        return (
            replace_random(arg, list(constant_dict.keys()))
            if random.random() < budget_random
            else arg
        )


    def substitute_symbol(self, arg, constant_dict):
        budget_random = 0.01

        # Substitute constants or calls
        if random.random() < budget_random:
            return random.choice(list(constant_dict.keys()))

        return arg


    def substitute_grid_angle(self, arg, constant_dict=R8_NAMES):
        budget_random = 0.01

        # Only substitute constants 
        if arg not in constant_dict.keys():
            return arg

        c = constant_dict[arg]
        S = self.S
        if c == a_mr(S) and random.random() < 0.5:
            return self.substitute_grid_angle_mr()
        elif random.random() < budget_random:
            # Same as usual random replacement
            return random.choice(list(constant_dict.keys()))

        return arg

    def substitute_grid_angle_mr(self):
        # Change the score at substitution time
        self.score -= 1
        t_call = self.t_call
        t_num = self.t_num

        t_call[t_num + 0] = 'identity, S'
        t_call[t_num + 1] = f'a_mr, t{t_num + 0}'
        self.t_num += 2

        print(f'    t{t_num + 0} = env.do_fluff({t_num + 0}, [{t_call[t_num + 0]}]) # {self.task_id} - True', file=self.file)
        print(f'    t{t_num + 1} = env.do_fluff({t_num + 1}, [{t_call[t_num + 1]}]) # {self.task_id} - True', file=self.file)
        return f't{t_num + 1}'


    def mutate(self):
        old_call = clean_call(self.t_call[self.t_num])
        self.t_call[self.t_num] = old_call

        # print_l(f'{old_call = }')

        old_items = get_items(old_call)
        old_func_name = old_items[0].strip()
        old_hints = get_hints(old_func_name)
        
        has_mutation = False
        if old_args := re.findall(r'\b(\w+)\b', old_call):
            # TODO Track t variables to get to hints
            if old_hints is None:
                call = self.t_call[self.t_num]
                print(f'    t{self.t_num} = env.do_fluff({self.t_num}, [{call}]) # {self.task_id} - {has_mutation}', file=self.file)
                return has_mutation

            for i, (old_arg, old_hint) in enumerate(zip(old_args, old_hints)):
                # First deal with t variables
                if old_arg.startswith('t') and old_arg[1:].isdigit():
                    t_n = int(old_arg[1:])

                    while random.random() < 0.9:
                        t_offset = t_n - random.randint(1, 9)
                        if t_offset > 0:
                            new_call = clean_call(self.t_call[t_offset])
                            new_items = get_items(new_call)
                            new_func_name = new_items[0].strip()
                            new_hints = get_hints(new_func_name)
                            new_hint = new_hints[0] if new_hints else None

                            if new_hint == old_hint:
                                has_mutation = True
                                self.t_call[self.t_num] = re.sub(rf'\bt{t_n}\b', f't{t_offset}', old_call)
                # Then deal with constants
                else:
                    if old_hint in ['C_']:
                        old_args[i] = self.substitute_color(old_arg)
                    elif old_hint == 'FL':
                        old_args[i] = self.substitute_rank(old_arg, FL_NAMES)
                    elif old_hint == 'F_':
                        old_args[i] = self.substitute_rank(old_arg, F_NAMES)
                    elif old_hint == 'L_':
                        old_args[i] = self.substitute_rank(old_arg, L_NAMES)
                    elif old_hint == 'R_':
                        old_args[i] = self.substitute_symbol(old_arg, R_NAMES)
                    elif old_hint == 'R4':
                        old_args[i] = self.substitute_symbol(old_arg, R4_NAMES)
                    elif old_hint == 'R8':
                        old_args[i] = self.substitute_symbol(old_arg, R8_NAMES)
                        self.score += 1
                    elif old_hint == 'A8':
                        # print_l(f'{old_args = } - {old_hints = } - {old_call = }')
                        old_args[i] = self.substitute_grid_angle(old_arg)
                    elif old_hint not in [ 'Samples', 'Grid', 'Tuple',
                            'Object', 'Objects', 'FrozenSet', 'Patch', 
                            'Callable', 'Container', 'ContainerContainer',
                            'Integer', 'IntegerSet', 'Numerical', 'Indices', 
                            'Boolean', 'IJ', 'A4', 'TupleTuple', 'Any'
                        ]:
                        print_l(f'{old_hint = }')
                    if old_args[i] != old_arg:
                        has_mutation = True
                        self.t_call[self.t_num] = re.sub(rf'\b{old_arg}\b', f'{old_args[i]}', old_call)
                    # print_l(f'{old_hint = }')
                    # print_l(f'{old_arg = }')
                    # print_l(f'{old_args[i] = }')
                    # print_l(f'{self.S = }')

        call = self.t_call[self.t_num]
        print(f'    t{self.t_num} = env.do_fluff({self.t_num}, [{call}]) # {self.task_id} - {has_mutation}', file=self.file)
        return has_mutation


def main(file, seed, count=0):
    train_data = get_data(train=True, sort_by_size=True)
    # eval_data = get_data(train=False, sort_by_size=True)
    # total_data = {k: {**train_data[k], **eval_data[k]} for k in ['train', 'test']}
    total_data = train_data

    solvers = get_solvers([solvers_dir, solvers_pre])

    print_l(f"{len(solvers) = }")

    equals = {task_id: get_equals(source) for task_id, (_, source) in solvers.items()}

    if count > 0: 
        solvers = {k: solvers[k] for k in list(solvers.keys())[:count]}

    code = Code(file)
    uses = {}
    for _ in range(999):
        # Go through each solver
        solvers_copy = solvers.copy()
        for task_id, (func_name, source) in solvers_copy.items():
            # print_l(f"-- {task_id} -----")

            if task_id not in total_data['train']:
                continue

            train_task = total_data['train'][task_id]
            S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in train_task)
            # print_l(f'{len(S) = }')
            # code = Code(file, task_id, S, t_call, t_number, t_num)
            code.S = S
            code.task_id = task_id

            # Is it empty?
            if not equals[task_id]:
                # Then remove it from solver list
                del solvers[task_id]
                continue

            # Else take next assignment - x_n = call(...)
            old_name, old_call = next(iter(equals[task_id].items()))
            uses[old_call] = 0

            # Remove entry from equals
            del equals[task_id][old_name]

            # Else is the right side new?
            has_mutation = False
            if old_call not in code.t_number.keys():
                # Then add it to t_call/t_number
                code.t_num += 1
                code.t_call[code.t_num] = old_call

                # print_l(f'{code.t_num = } - {old_call = }')

                has_mutation = code.mutate()
                code.t_number[old_call] = code.t_num

            # Was the left side O?
            if old_name == 'O':
                if len(func_name.split('_')) == 4:
                    num_sol = func_name.split('_')[-1]
                else:
                    num_sol = '0' 
                print(f"    if t{code.t_number[old_call]} == O:", file=file)
                print(f"        o.append(({code.t_number[old_call]}, {has_mutation}, '{task_id}', '{num_sol}'))", file=file)

            # Replace x_n with t_name[x_call] in rest of solver
            for x_name, x_call in equals[task_id].items():
                if old_name in x_call:
                    uses[old_call] += 1
                    equals[task_id][x_name] = re.sub(rf'\b{old_name}\b', f't{code.t_number[old_call]}', x_call)
                    # print_l(f'{x_name} = {x_call} -> t{code.t_number[old_call]} = {equals[task_id][x_name]}')
            # if uses[old_call] > 9:
            #     print(f't{code.t_number[old_call]} - {old_call = } - {uses[old_call] = }')

    # for call in code.t_number.keys():
    #     # if uses[call] > 9:
    #         print(f'{uses[call] = } - {call = } - {code.t_number[call] = }')
    # print_l(f'{len(code.t_number.keys()) = }')
        

    # Write t_call into new file call.py
    with open('call.py', 'w') as call_file:
        print(f't_call = {code.t_call}', file=call_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run batt on specified tasks')
    parser.add_argument('--count', '-c', type=int, default=0,
                        help='Number of tasks to run (default: 0 - all tasks)')
    args = parser.parse_args()


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
        main(batt_file, seed, args.count)
        print("    return o", file=batt_file)
