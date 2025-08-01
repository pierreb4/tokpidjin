import argparse
import re
import random
import time
import inspect

from pprint import pprint

from utils import *
from constants import *
from dsl import *


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


    def mutate(self, freeze=False):
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
                        if not freeze:
                            t_n = int(old_arg[1:])
                            has_mutation = self.do_offset_mutation(old_hint, old_call, t_n, has_mutation)
                    elif not freeze:
                        has_mutation = self.do_arg_substitutions(old_hint, old_call, old_args, old_arg, i, has_mutation)

                return self.file_fluff(has_mutation), False
            for i, (old_arg, old_hint) in enumerate(zip(old_args, old_hints)):
                # First deal with t variables
                if old_arg.startswith('t') and old_arg[1:].isdigit():
                    if not freeze:
                        t_n = int(old_arg[1:])
                        has_mutation = self.do_offset_mutation(old_hint, old_call, t_n, has_mutation)
                elif not freeze:
                    has_mutation = self.do_arg_substitutions(old_hint, old_call, old_args, old_arg, i, has_mutation)

        get_differ = old_hints[0] == 'Grid' if old_hints else False
        return self.file_fluff(has_mutation), get_differ


    def file_fluff(self, has_mutation):
        call = self.t_call[self.t_num]
        print(f'    t{self.t_num} = env.do_fluff({self.t_num}, [{call}]) # {self.task_id} - {has_mutation}', file=self.file)
        # print("    print(f'{t" + str(self.t_num) + " = }')", file=self.file)
        return has_mutation


    def do_offset_mutation(self, old_hint, old_call, t_n, has_mutation):
        while random.random() < 0.01:
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


def get_equals(source):
    # Catalog assignments in source
    equals = {}
    for line in source.split('\n'):
        if ' = ' in line:
            parts = line.split(' = ')
            var_name = parts[0].strip()
            value = parts[1].strip()
            equals[var_name] = value
    return equals


class Differs:
    def __init__(self, file, I='I'):
        self.file = file
        self.equals = {}
        differs_module = load_module('differs')
        for name, func in inspect.getmembers(differs_module, inspect.isfunction):
            if not name.startswith('differ_'):
                continue

            source = inspect.getsource(func)
            self.equals[name] = get_equals(source)

            for var_name, value in self.equals[name].items():
                self.equals[name][var_name] = re.sub(r'\bI\b', I, value)


    def add_line(self, code, uses, task_id=None):
        for name in self.equals.keys():
            equals_name = self.equals[name].copy()
            for var_name, value in self.equals[name].items():
                add_differ_line(equals_name, code, uses, freeze_differ=True)

            print(f"    if type(t{code.t_num}) is int:", file=code.file)
            print(f"        s.append(('{task_id}', '{name}', t{code.t_num}))", file=code.file)


def add_differ_line(equals, code, uses, task_id=None, freeze_differ=False):
    # Take next assignment - x_n = call(...)
    old_name, old_call = next(iter(equals.items()))
    uses[old_call] = 0

    # Remove entry from equals
    del equals[old_name]

    # Check that right side is new
    if old_call not in code.t_number:
        # Then add it to t_call/t_number
        code.t_num += 1
        code.t_call[code.t_num] = old_call
        has_mutation, get_differ = code.mutate(freeze_differ)
        code.t_number[old_call] = code.t_num
    else:
        has_mutation = False
        get_differ = False

    # if get_differ:
    #     differs = Differs(code.file, I=f't{code.t_number[old_call]}')
    #     differs.add_line(code, uses, task_id=task_id)

    # Replace x_n with t_name[x_call] in rest of solver
    for x_name, x_call in equals.items():
        if old_name in x_call:
            uses[old_call] += 1
            equals[x_name] = re.sub(rf'\b{old_name}\b', f't{code.t_number[old_call]}', x_call)


def append_to_o(code, old_call, has_mutation, task_id):
    print(f"    if t{code.t_number[old_call]} == O:", file=code.file)
    print(f"        o.append(({code.t_number[old_call]}, {has_mutation}, '{task_id}', '-1'))", file=code.file)
    return True


def add_solver_line(equals, code, uses, task_id=None, freeze_solver=False):
    # Take next assignment - x_n = call(...)
    old_name, old_call = next(iter(equals.items()))
    uses[old_call] = 0

    # Remove entry from equals
    del equals[old_name]

    # Check that right side is new
    if old_call not in code.t_number:
        # Then add it to t_call/t_number
        code.t_num += 1
        code.t_call[code.t_num] = old_call
        has_mutation, get_differ = code.mutate(freeze_solver)
        code.t_number[old_call] = code.t_num
    else:
        has_mutation = False
        get_differ = False

    # Was the left side O?
    if old_name == 'O':
        get_differ = append_to_o(code, old_call, has_mutation, task_id)

    # if get_differ:
    #     differs = Differs(code.file, I=f't{code.t_number[old_call]}')
    #     differs.add_line(code, uses, task_id=task_id)

    # Replace x_n with t_name[x_call] in rest of solver
    for x_name, x_call in equals.items():
        if old_name in x_call:
            uses[old_call] += 1
            equals[x_name] = re.sub(rf'\b{old_name}\b', f't{code.t_number[old_call]}', x_call)


def main(file, seed, count=0, task_id=None, freeze_solver=False, freeze_differ=False):
    train_data = get_data(train=True, sort_by_size=True)
    # eval_data = get_data(train=False, sort_by_size=True)
    # total_data = {k: {**train_data[k], **eval_data[k]} for k in ['train', 'test']}
    total_data = train_data

    # Get one of best solvers if not mutating (for performance checks)
    solvers = get_solvers([solvers_dir, solvers_pre], best_only=freeze_solver)
    task_list = list(solvers.keys())

    print_l(f"{len(solvers) = }")

    if task_id:
        solvers = {k: solvers[k] for k in [task_id]}
    elif count > 0:
        # solvers = {k: solvers[k] for k in list(solvers.keys())[:count]}
        # Pick random solvers
        solvers = {k: solvers[k] for k in random.sample(list(solvers.keys()), count)}
        task_list = list(solvers.keys())    

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

    equals = {task_id: get_equals(solver.source) for task_id, solver in solvers.items()}
    code = Code(file)
    uses = {}
    # differs = Differs(file, I='I')
    # differs.add_line(code, uses, task_id=task_id)
    # Check if we reach this limit with:
    # grep 'x999 = ' solver_md5/*.py
    # TODO Continue as long as previous round was x_n variable,
    #      as this insures that there's still variable O to read
    for _ in range(999):
        # Go through each solver
        solvers_copy = solvers.copy()
        # for task_id, (func_name, source) in solvers_copy.items():
        for task_id, solver in solvers_copy.items():
            func_name = solver.name
            # solver_path = solver.path
            source = solver.source

            if task_id not in total_data['train']:
                continue

            train_task = total_data['train'][task_id]
            S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in train_task)
            code.S = S
            code.task_id = task_id

            # Check if equals is empty
            if not equals[task_id]:
                # Then remove it from solver list
                del solvers[task_id]
                continue

            add_solver_line(equals[task_id], code, uses, task_id=task_id, freeze_solver=freeze_solver)

    # Write t_call into new file call.py
    # Used in run_batt.py (from call import t_call)
    with open('call.py', 'w') as call_file:
        print(f't_call = {code.t_call}', file=call_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run batt on specified tasks')
    parser.add_argument("-i", "--task_id", help="Specific task_id to test", type=str)
    parser.add_argument('--count', '-c', type=int, default=0,
                        help='Number of tasks to run (default: 0 - all tasks)')
    parser.add_argument("-fs", "--freeze_solver", action="store_true",
                        help="Freeze solvers, don't mutate them")
    parser.add_argument("-fd", "--freeze_differ", action="store_true",
                        help="Freeze differs, don't mutate them")
    parser.add_argument("-f", "--file_name", type=str, default='batt.py',
                        help="File name to write the batt code to (default: batt.py)")
    args = parser.parse_args()

    seed = time.time()
    random.seed(seed)
    with open(args.file_name, 'w') as batt_file:
        print(
f"""# Generated by tokpidjin/card.py

from fluff import *


def batt(task_id, S, I, O, flags, log_path):
    s = []
    o = []
    env = Env({seed}, task_id, S, log_path)""", file=batt_file)
        main(batt_file, seed, args.count, args.task_id, args.freeze_solver, args.freeze_differ)
        print("    return o, s", file=batt_file)
