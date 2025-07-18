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
        budget_random = 0.1

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
            # return self.substitute_color_izzo('c_iz_n', f_n)
            return self.substitute_color_izzo(4, 5, f_n)
        elif c in c_zo_l and random.random() < 0.5:
            f_n = f'F{c_zo_l.index(c)}'
            # return self.substitute_color_izzo('c_zo_n', f_n)
            return self.substitute_color_izzo(5, 4, f_n)
        elif random.random() < budget_random:
            # Same as usual random replacement
            return random.choice(list(constant_dict.keys()))

        # Get name corresponding to number
        constant_list = list(constant_dict.keys())
        return constant_list[c]


    def substitute_color_izzo(self, arg_i, arg_o, f_n):
        self.score -= 1
        t_call = self.t_call
        t_num = self.t_num
        t_call[t_num + 0] = 'apply, first, S'
        t_call[t_num + 1] = 'apply, second, S'
        t_call[t_num + 2] = f'mapply, p_g, t{t_num + 0}'
        t_call[t_num + 3] = f'mapply, p_g, t{t_num + 1}'
        t_call[t_num + 4] = f'dedupe, t{t_num + 2}'
        t_call[t_num + 5] = f'dedupe, t{t_num + 3}'
        t_call[t_num + 6] = f'difference_tuple, t{t_num + arg_i}, t{t_num + arg_o}'
        t_call[t_num + 7] = f'get_nth_t, t{t_num + 6}, {f_n}'
        self.t_num += 8
        for t in range(8):
            print(
                f'    t{t_num + t} = env.do_fluff({t_num + t}, [{t_call[t_num + t]}]) # {self.task_id} - True',
                file=self.file,
            )
        return f't{t_num + 7}'


    def old_substitute_color_izzo(self, c_izzo_n, f_n):
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

        for t in range(5):
            print(f'    t{t_num + t} = env.do_fluff({t_num + t}, [{t_call[t_num + t]}]) # {self.task_id} - True', file=self.file)
        return f't{t_num + 4}'


    def substitute_rank(self, arg, constant_dict):
        if arg not in constant_dict.keys():
            return arg

        budget_random = 0.1

        return (
            replace_random(arg, list(constant_dict.keys()))
            if random.random() < budget_random
            else arg
        )


    def substitute_symbol(self, arg, constant_dict):
        budget_random = 0.1

        # Substitute constants or calls
        if random.random() < budget_random:
            return random.choice(list(constant_dict.keys()))

        return arg


    def substitute_grid_angle(self, arg, constant_dict=R8_NAMES):
        budget_random = 0.1

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


    def mutate(self, preserve=False):
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


                old_hint = None
                for i, old_arg in enumerate(old_args):
                    # First deal with t variables
                    if old_arg.startswith('t') and old_arg[1:].isdigit():
                        if not preserve:
                            t_n = int(old_arg[1:])
                            has_mutation = self.do_offset_mutation(old_hint, old_call, t_n, has_mutation)
                    elif not preserve:
                        has_mutation = self.do_arg_substitutions(old_hint, old_call, old_args, old_arg, i, has_mutation)


                return self.file_fluff(has_mutation)
            for i, (old_arg, old_hint) in enumerate(zip(old_args, old_hints)):
                # First deal with t variables
                if old_arg.startswith('t') and old_arg[1:].isdigit():
                    if not preserve:
                        t_n = int(old_arg[1:])
                        has_mutation = self.do_offset_mutation(old_hint, old_call, t_n, has_mutation)
                elif not preserve:
                    has_mutation = self.do_arg_substitutions(old_hint, old_call, old_args, old_arg, i, has_mutation)

        return self.file_fluff(has_mutation)


    def file_fluff(self, has_mutation):
        call = self.t_call[self.t_num]
        print(f'    t{self.t_num} = env.do_fluff({self.t_num}, [{call}]) # {self.task_id} - {has_mutation}', file=self.file)
        return has_mutation


    def do_offset_mutation(self, old_hint, old_call, t_n, has_mutation):
        while random.random() < 0.001:
            # TODO Check parameter impact on mutation numbers
            # t_offset = t_n - random.randint(1, 9)
            t_offset = random.randint(1, t_n)
            if t_offset > 0:
                new_call = clean_call(self.t_call[t_offset])
                new_items = get_items(new_call)
                new_func_name = new_items[0].strip()
                new_hints = get_hints(new_func_name)
                new_hint = new_hints[0] if new_hints else None

                if new_hint == old_hint or old_hint is None:
                    has_mutation = True
                    self.t_call[self.t_num] = re.sub(rf'\bt{t_n}\b', f't{t_offset}', old_call)
        return has_mutation


    def do_arg_substitutions(self, old_hint, old_call, old_args, old_arg, i, has_mutation):
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
        elif old_hint == 'A4':
            old_args[i] = self.substitute_symbol(old_arg, A4_NAMES)
        elif old_hint == 'A8':
            old_args[i] = self.substitute_grid_angle(old_arg)
        elif old_hint not in [ 'Samples', 'Grid', 'Tuple',
                'Object', 'Objects', 'FrozenSet', 'Patch', 
                'Callable', 'Container', 'ContainerContainer',
                'Integer', 'IntegerSet', 'Numerical', 'Indices', 
                'Boolean', 'IJ', 'TupleTuple', 'Any',
                None
            ]:
            print_l(f'{old_hint = }')
        if old_args[i] != old_arg:
            has_mutation = True
            self.t_call[self.t_num] = re.sub(rf'\b{old_arg}\b', f'{old_args[i]}', old_call)
        return has_mutation


def main(file, seed, count=0, task_id=None, preserve=False):
    train_data = get_data(train=True, sort_by_size=True)
    # eval_data = get_data(train=False, sort_by_size=True)
    # total_data = {k: {**train_data[k], **eval_data[k]} for k in ['train', 'test']}
    total_data = train_data

    # Get one of best solvers if not mutating (for performance checks)
    solvers = get_solvers([solvers_dir, solvers_pre], best_only=preserve)
    task_list = list(solvers.keys())

    print_l(f"{len(solvers) = }")

    if task_id:
        solvers = {k: solvers[k] for k in [task_id]}
    elif count > 0:
        solvers = {k: solvers[k] for k in list(solvers.keys())[:count]}

    task_sizes = []
    for task_id in task_list:
        size = 0
        for S in total_data['train'][task_id] + total_data['test'][task_id]:
            for ex in S.values():
                size += sum(len(inner) for inner in ex)
        task_sizes.append(size)

    # Sort solvers by task size
    weighted_tasks = list(zip(task_list, task_sizes))
    weighted_tasks.sort(key=lambda x: x[1], reverse=True)
    solvers = {task_id: solvers[task_id] for task_id, _ in weighted_tasks}

    equals = {task_id: get_equals(source) for task_id, (_, source) in solvers.items()}
    code = Code(file)
    uses = {}
    # Check if we reach this limit with:
    # grep 'x9999 = ' solver_md5/*.py
    # TODO Just continue as long as we've seen an x_n var previous round,
    #      as there's still variable O to read
    for _ in range(999):
        # Go through each solver
        solvers_copy = solvers.copy()
        for task_id, (func_name, source) in solvers_copy.items():
            if task_id not in total_data['train']:
                continue

            train_task = total_data['train'][task_id]
            S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in train_task)
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

                has_mutation = code.mutate(preserve)
                code.t_number[old_call] = code.t_num

            # Was the left side O?
            if old_name == 'O':
                # TODO Fix/remove num_sol, as func_name doesn't include it
                num_sol = func_name.split('_')[-1] if len(func_name.split('_')) == 4 else '0'
                print(f"    if t{code.t_number[old_call]} == O:", file=file)
                print(f"        o.append(({code.t_number[old_call]}, {has_mutation}, '{task_id}', '{num_sol}'))", file=file)

            # Replace x_n with t_name[x_call] in rest of solver
            for x_name, x_call in equals[task_id].items():
                if old_name in x_call:
                    uses[old_call] += 1
                    equals[task_id][x_name] = re.sub(rf'\b{old_name}\b', f't{code.t_number[old_call]}', x_call)

    # Write t_call into new file call.py
    with open('call.py', 'w') as call_file:
        print(f't_call = {code.t_call}', file=call_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run batt on specified tasks')
    parser.add_argument("-i", "--task_id", help="Specific task_id to test", type=str)
    parser.add_argument('--count', '-c', type=int, default=0,
                        help='Number of tasks to run (default: 0 - all tasks)')
    parser.add_argument("-p", "--preserve", action="store_true",
                        help="Preserve, don't mutate the code")
    args = parser.parse_args()

    file_name = 'batt.py'
    seed = time.time()
    random.seed(seed)
    with open(file_name, 'w') as batt_file:
        print(
f"""# Generated by tokpidjin/card.py

from fluff import *


def batt(task_id, S, I, O, log_path):
    env = Env({seed}, task_id, S, log_path)
    o = []""", file=batt_file)
        main(batt_file, seed, args.count, args.task_id, args.preserve)
        print("    return o", file=batt_file)
