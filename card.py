import argparse
import re
import random
import time
import inspect
import hashlib

from pprint import pprint

from utils import *
from constants import *
from dsl import *

import dsl
DSL_FUNCTIONS = inspect.getmembers(dsl, inspect.isfunction)
DSL_FUNCNAMES = [name for name, func in DSL_FUNCTIONS]


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
    def __init__(self, file, task_id=None, S=None, t_call=None, t_isok=None, 
            t_number=None, t_num=0, score=0):
        self.file = file
        self.task_id = task_id
        self.S = S

        self.t_call = t_call if t_call is not None else {}
        self.t_isok = t_isok if t_isok is not None else {}
        self.t_number = t_number if t_number is not None else {}

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
            return self.substitute_color_izzo(4, 5, f_n)
        elif c in c_zo_l and random.random() < 0.5:
            f_n = f'F{c_zo_l.index(c)}'
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
        t_isok = self.t_isok
        t_num = self.t_num

        t_call[t_num + 0] = 'apply, first, S'
        t_isok[t_num + 0] = 'True'
        t_call[t_num + 1] = 'apply, second, S'
        t_isok[t_num + 1] = 'True'
        t_call[t_num + 2] = f'mapply, p_g, t{t_num + 0}.t'
        t_isok[t_num + 2] = f't{t_num + 0}.ok'
        t_call[t_num + 3] = f'mapply, p_g, t{t_num + 1}.t'
        t_isok[t_num + 3] = f't{t_num + 1}.ok'
        t_call[t_num + 4] = f'dedupe, t{t_num + 2}.t'
        t_isok[t_num + 4] = f't{t_num + 2}.ok'
        t_call[t_num + 5] = f'dedupe, t{t_num + 3}.t'
        t_isok[t_num + 5] = f't{t_num + 3}.ok'
        t_call[t_num + 6] = f'difference_tuple, t{t_num + arg_i}.t, t{t_num + arg_o}.t'
        t_isok[t_num + 6] = f't{t_num + arg_i}.ok and t{t_num + arg_o}.ok'
        t_call[t_num + 7] = f'get_nth_t, t{t_num + 6}.t, {f_n}'
        t_isok[t_num + 7] = f't{t_num + 6}.ok'
        self.t_num += 8
        for t in range(8):
            print(
                f'    t{t_num + t} = env.do_pile({t_num + t}, [{t_call[t_num + t]}], {t_isok[t_num + t]}) # {self.task_id} - True',
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
            print(f'    t{t_num + t} = env.do_pile({t_num + t}, [{t_call[t_num + t]}]) # {self.task_id} - True', file=self.file)
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
        t_isok = self.t_isok
        t_num = self.t_num

        t_call[t_num + 0] = 'identity, S'
        t_isok[t_num + 0] = 'True'
        t_call[t_num + 1] = f'a_mr, t{t_num + 0}.t'
        t_isok[t_num + 1] = f't{t_num + 0}.ok'
        self.t_num += 2

        print(f'    t{t_num + 0} = env.do_pile({t_num + 0}, [{t_call[t_num + 0]}], {t_isok[t_num + 0]}) # {self.task_id} - True', file=self.file)
        print(f'    t{t_num + 1} = env.do_pile({t_num + 1}, [{t_call[t_num + 1]}], {t_isok[t_num + 1]}) # {self.task_id} - True', file=self.file)
        return f't{t_num + 1}'


    def mutate(self, freeze=False):
        old_call = clean_call(self.t_call[self.t_num])
        self.t_call[self.t_num] = old_call

        # print_l(f'{old_call = }')

        old_items = get_items(old_call)
        old_func_name = old_items[0].strip()
        old_hints = get_hints(old_func_name)

        has_mutation = Mutation(False, None, None)
        if old_args := re.findall(r'\b(\w+)\b', old_call):
            # TODO Track t variables to get to hints
            if old_hints is None:
                old_hint = None
                for i, old_arg in enumerate(old_args):
                    # First deal with t variables
                    if re.match(r't\d+', old_arg):
                        if self.t_num not in self.t_isok:
                            self.t_isok[self.t_num] = f'{old_arg}.ok'
                        else:
                            self.t_isok[self.t_num] += f' and {old_arg}.ok'
                        if not freeze:
                            t_n = int(old_arg[1:])
                            has_mutation = self.do_offset_mutation(old_hint, old_call, t_n, has_mutation)
                    elif not freeze:
                        has_mutation = self.do_arg_substitutions(old_hint, old_call, old_args, old_arg, i, has_mutation)

                return self.file_pile(has_mutation)

            for i, (old_arg, old_hint) in enumerate(zip(old_args, old_hints)):
                # First deal with t variables
                if re.match(r't\d+', old_arg):
                    if self.t_num not in self.t_isok:
                        self.t_isok[self.t_num] =  f'{old_arg}.ok'
                    else:
                        self.t_isok[self.t_num] += f' and {old_arg}.ok'
                    if not freeze:
                        t_n = int(old_arg[1:])
                        has_mutation = self.do_offset_mutation(old_hint, old_call, t_n, has_mutation)
                elif not freeze:
                    has_mutation = self.do_arg_substitutions(old_hint, old_call, old_args, old_arg, i, has_mutation)

        return self.file_pile(has_mutation)


    def file_pile(self, has_mutation):
        t_call = self.t_call[self.t_num]
        call_list = [c.strip() for c in t_call.split(',')]
        call = [f'{c}.t' if re.match(r't\d+', c) else c for c in call_list]
        call_string = ', '.join(call)

        if self.t_num not in self.t_isok:
            self.t_isok[self.t_num] = 'True'
        isok = self.t_isok[self.t_num]
        print(f'    t{self.t_num} = env.do_pile({self.t_num}, [{call_string}], {isok}) # {self.task_id} - [{has_mutation.old}]', file=self.file)
        return has_mutation


    def do_offset_mutation(self, old_hint, old_call, t_n, has_mutation):
        while random.random() < 0.01:
            # TODO Check parameter impact on mutation numbers            
            t_offset = random.randint(1, t_n)
            if t_offset > 0:
            # if t_offset > self.last_differ_t_num:
                new_call = clean_call(self.t_call[t_offset])
                new_items = get_items(new_call)

                if random.randint(0, 1) == 0:
                    new_func_name = new_items[0].strip()

                    new_hints = get_hints(new_func_name)
                    new_hint = new_hints[0] if new_hints else None

                    if new_hint == old_hint or new_hint == 'Any' or old_hint == 'Any' or new_hint is None or old_hint is None:
                        # has_mutation = True
                        pattern = rf'\bt{t_n}\b'
                        self.t_call[self.t_num] = re.sub(pattern, f't{t_offset}', old_call)
                        has_mutation = Mutation(True, old_call, self.t_call[self.t_num])

                else:
                    # XXX Pick a random function name from dsl.py
                    #     If promising, make more structural
                    new_func_name = random.choice(DSL_FUNCNAMES)
                    # print_l(f'Random function name {new_func_name} for t{t_offset} in {old_call}')

                    new_hints = get_hints(new_func_name)
                    new_hint = new_hints[0] if new_hints else None
                    # print_l(f'{old_hint = } - {new_hints = }')

                    if new_hint == old_hint or new_hint == 'Any' or old_hint == 'Any' or new_hint is None or old_hint is None:
                        # has_mutation = True
                        pattern = rf'\bt{t_n}\b'
                        self.t_call[self.t_num] = re.sub(pattern, f't{t_offset}', old_call)
                        has_mutation = Mutation(True, old_call, self.t_call[self.t_num])
                        # print_l(f'- Mutated {old_call} to {self.t_call[self.t_num]}')

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
        elif self.t_num > 1 and random.random() < 0.01:
            if old_hint == 'Callable':
                old_args[i] = random.choice(DSL_FUNCNAMES)
            else:
                # Replace with a t variable
                t_n = self.t_num - 1
                t_offset = random.randint(1, t_n)
                old_args[i] = f't{t_offset}'
            # print_l(f'- Replacing {old_arg} with {old_args[i]} in {old_call}')

        if old_args[i] != old_arg:
            # has_mutation = True
            pattern = rf'\b{old_arg}\b'
            self.t_call[self.t_num] = re.sub(pattern, f'{old_args[i]}', old_call)
            has_mutation = Mutation(True, old_call, self.t_call[self.t_num])
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


def track_solution(t_call, t_num, done):
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
                track_solution(t_call, t_num, done)

    return done


def build_differ_body(t_call, ret_t, done):
    differ_body = ''
    for t_num in sorted(done):
        t_split = [item.strip() for item in t_call[t_num].split(',')]
        t = [s[:-2] if s.endswith('.t') else s for s in t_split]

        func = t[0]
        args = t[1:]
        differ_body += f'    t{t_num} = '
        differ_body += f'{func}('
        differ_body += ', '.join(args)
        differ_body += ')\n'
    differ_body += f'    return t{ret_t}\n'

    return differ_body


class Differs:
    # def __init__(self, freeze_differs=False, I='I'):
    def __init__(self, task_ids, freeze_differs=False):
        self.freeze_differs = freeze_differs
        self.init_equals = {}

        all_list = { 'iz': [], 'zo': [] }
        differ_list = ['differs']
        for score_type in ['iz', 'zo']:
            file_list = []
            weights = []
            for task_id in task_ids:
                differ_dir = f'differ_dir/{score_type}/solve_{task_id}/[0-9]*/[0-9]*/[0-9a-f]*.py'
                file_paths = glob.glob(differ_dir)
                if not file_paths:
                    continue
                random.shuffle(file_paths)
                for file_path in file_paths:
                    sections = file_path.split('/')
                    s_score = int(sections[3])
                    # t_score = int(sections[4])

                    file_list.append(file_path)
                    weights.append(s_score)

                if sum(weights) > 0:
                    select_differ = random.choices(file_list, weights=weights, k=1)
                else:
                    select_differ = []

                # all_list += [f[:-3] for f in file_paths if f.endswith('.py')]
                all_list[score_type] += [f[:-3] for f in select_differ if f.endswith('.py')]

            # all_list = [f[:-3] for f in os.listdir('differ_md5') if f.endswith('.py')]
            add_list = random.sample(all_list[score_type], min(32, len(all_list[score_type])))
            differ_list += add_list

        # TODO Maybe adjust get_differs to get the best differs 
        self.differs = get_differs(differ_list, best_only=True)

        for differ_name, differ in self.differs.items():
            self.init_equals[differ_name] = get_equals(differ.source)


    def sub_I(self, I='I'):

        # print_l(f'Substituting C with {C}')

        self.run_equals = {}
        for differ_name in self.init_equals.keys():
            self.run_equals[differ_name] = {}
            for x_name, x_call in self.init_equals[differ_name].items():
                self.run_equals[differ_name][x_name] = re.sub(r'\bI\b', I, x_call)

                # print_l(f'{differ_name} - {x_name} = {self.run_equals[differ_name][x_name]}')


    def add_lines(self, code, uses, task_id=None):
        # run_equals = self.run_equals.copy()
        for differ_name in self.run_equals.keys():

            # if task_id is not None:
            #     print_l(f'{task_id = } - {differ_name = } - {self.run_equals[differ_name]}')

            equals_name = self.run_equals[differ_name].copy()
            for x_name, x_call in self.run_equals[differ_name].items():
                freeze_differs = self.freeze_differs if task_id is None else True
                add_differ_line(equals_name, code, uses, task_id, freeze_differs)

            if task_id is None:
                done = track_solution(code.t_call, code.t_num, None)

                # print_l(f'{differ_name} - {done = }')

                differ_body = build_differ_body(code.t_call, code.t_num, done)
                differ_body = re.sub(r'\bt(\d+)\b', r'x\1', differ_body)

                differ_source = f'def differ(S, I, C):\n{differ_body}'
                # self.init_equals[differ_name] = get_equals(differ_source)

                inlined_source = inline_variables(differ_source)
                md5_hash = hashlib.md5(inlined_source.encode()).hexdigest()

                # NOTE Changes keys to self.run_equals !!!
                # differ_name = f'differ_{md5_hash}'
                # differ_source = f'def {differ_name}(S, I, O, C):\n{differ_body}'

                # print_l(f'{differ_name}\n{inlined_source = }')


            # print(f"    if type(t{code.t_num}.t) is int:", file=code.file)
            # print(f"        s.append(({code.t_num}, '{task_id}', '{differ_name}', t{code.t_num}.t))", file=code.file)
            print(f"    s.append(({code.t_num}, '{task_id}', '{differ_name}', t{code.t_num}))", file=code.file)

        code.last_differ_t_num = code.t_num


def add_differ_line(equals, code, uses, task_id=None, freeze_differs=False):
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
        has_mutation = code.mutate(freeze_differs)
        code.t_number[old_call] = code.t_num
    else:
        # has_mutation = False
        has_mutation = Mutation(False, None, None)

    if has_mutation.present and not freeze_differs and task_id is None:
        print_l(f'{old_name = } - {old_call = }')
        print_l(f'{code.t_call[code.t_num] = }')

    # Replace x_n with t_name[x_call] in rest of solver
    for x_name, x_call in equals.items():
        if old_name in x_call:
            uses[old_call] += 1
            equals[x_name] = re.sub(rf'\b{old_name}\b', f't{code.t_number[old_call]}', x_call)


# def append_to_o(code, last_call, has_mutation, task_id):
    # last_t = code.t_number[last_call]
def append_to_o(code, last_t, has_mutation, task_id):
    # check_t = f't{last_t}.ok and t{last_t}.t == O'
    # print(f"    o.append(({last_t}, {has_mutation}, '{task_id}', {check_t}))", file=code.file)
    # check_t = f't{last_t}.t if t{last_t}.ok else None'
    print(f"    o.append(({last_t}, {has_mutation.present}, '{task_id}', t{last_t}))", file=code.file)


def add_solver_line(equals, code, uses, task_id=None, freeze_solvers=False):
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
        has_mutation = code.mutate(freeze_solvers)
        code.t_number[old_call] = code.t_num
    else:
        # has_mutation = False
        has_mutation = Mutation(False, None, None)

    # Was the left side O?
    if old_name == 'O':
        append_to_o(code, code.t_num, has_mutation, task_id)
        # # differs = Differs(freeze_differs=True, I=f't{code.t_number[old_call]}')
        # differs.sub_I(I=f't{code.t_number[old_call]}')
        # differs.add_lines(code, uses, task_id=task_id)

    # Replace x_n with t_name[x_call] in rest of solver
    for x_name, x_call in equals.items():
        if old_name in x_call:
            uses[old_call] += 1
            equals[x_name] = re.sub(rf'\b{old_name}\b', f't{code.t_num}', x_call)

    return old_name == 'O'


def main(count=0, task_id=None, freeze_solvers=False, freeze_differs=False, batt_file_name='batt.py'):
    train_data = get_data(train=True, sort_by_size=True)
    # eval_data = get_data(train=False, sort_by_size=True)
    # total_data = {k: {**train_data[k], **eval_data[k]} for k in ['train', 'test']}
    total_data = train_data

    # Get one of best solvers if not mutating (while running main.py for instance)
    # solvers = get_solvers([solvers_dir, solvers_pre], best_only=freeze_solvers)
    pre_solvers = get_solvers([solvers_pre], best_only=freeze_solvers)
    dir_solvers = get_solvers([solvers_dir], best_only=freeze_solvers)
    all_solvers = {**dir_solvers, **pre_solvers}
    all_task_ids = list(all_solvers.keys())    

    print_l(f"{len(all_solvers) = }")

    if task_id:
        solvers = {k: all_solvers[k] for k in [task_id]}
    elif count > 0:
        # Pick random solvers, half from pre_solvers, half from dir_solvers
        # TODO Refine to pick half proven solvers and half unproven solvers
        # We can check that the score in solver_dir (solver.o_score) matches the number of samples in S
        rnd_dir_solvers = {k: dir_solvers[k] for k in random.sample(list(dir_solvers.keys()), count)}
        dir_count = len(rnd_dir_solvers)
        pre_count = count - dir_count
        rnd_pre_solvers = {k: pre_solvers[k] for k in random.sample(list(pre_solvers.keys()), pre_count)}
        # XXX Don't apply sourcery suggestion below. It breaks things!
        rnd_solvers = {**rnd_dir_solvers, **rnd_pre_solvers}
        rnd_task_ids = list(rnd_solvers.keys())

        task_sizes = []
        for task_id in rnd_task_ids:
            size = 0
            for S in total_data['train'][task_id] + total_data['test'][task_id]:
                for ex in S.values():
                    size += sum(len(inner) for inner in ex)
            task_sizes.append(size)

        # Sort solvers by task size
        weighted_tasks = list(zip(rnd_task_ids, task_sizes))
        weighted_tasks.sort(key=lambda x: x[1], reverse=True)
        solvers = {task_id: all_solvers[task_id] for task_id, _ in weighted_tasks}
    else:
        solvers = all_solvers

    task_ids = list(solvers.keys())
    pre_task_ids = [k for k in all_task_ids if k in pre_solvers]
    dir_task_ids = [k for k in all_task_ids if k in dir_solvers]
    print_l(f'{len(solvers) = } - {len(pre_solvers) = } - {len(dir_solvers) = }')
    print_l(f'{len(task_ids) = } - {len(pre_task_ids) = } - {len(dir_task_ids) = }')

    # Write pre_task_ids into file based on batt_file_name
    # Used in run_batt.py (from call import pre_task_ids)
    pre_task_ids = task_ids
    pre_file_name = batt_file_name.replace('.py', '_pre.py')
    with open(pre_file_name, 'w') as pre_file:
        print(f'{pre_task_ids = }', file=pre_file)

    task_ids = list(solvers.keys())
    differs = Differs(task_ids, freeze_differs=args.freeze_differs)

    equals = {task_id: get_equals(solver.source) for task_id, solver in solvers.items()}
    seed = time.time()
    random.seed(seed)
    with open(batt_file_name, 'w') as batt_file:
        print(
f"""# Generated by tokpidjin/card.py

from pile import *


def batt(task_id, S, I, C, log_path):
    s = []
    o = []
    env = Env({seed}, task_id, S, log_path)""", file=batt_file)

        code = Code(batt_file)
        uses = {}
        # differs = Differs(freeze_differs=freeze_differs, I='I')
        differs.sub_I(I='I')
        differs.add_lines(code, uses, task_id=None)
        # Check if we reach this limit with:
        # grep 'x999 = ' solver_md5/*.py
        # TODO Continue as long as previous round was x_n variable,
        #      as this insures that there's still variable O to read
        for _ in range(999):
            # Go through each solver
            solvers_copy = solvers.copy()
            for task_id, solver in solvers_copy.items():
                # print_l(f'Processing {task_id} - {len(solvers)} solvers left')

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

                get_O = add_solver_line(equals[task_id], code, uses, task_id=task_id, freeze_solvers=freeze_solvers)
                if get_O:
                    # XXX Big oops here, don't sub with I ?! :/
                    # differs.sub_I(I=f'I')
                    differs.sub_I(I=f't{code.t_num}')
                    differs.add_lines(code, uses, task_id=task_id)


        print("    return o, s", file=batt_file)

    # Write t_call into file based on batt_file_name
    # Used in run_batt.py (call_module.t_call)
    call_file_name = batt_file_name.replace('.py', '_call.py')
    with open(call_file_name, 'w') as call_file:
        print(f't_call = {code.t_call}', file=call_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run batt on specified tasks')
    parser.add_argument("-i", "--task_id", help="Specific task_id to test", type=str)
    parser.add_argument('-c', '--count', type=int, default=0,
                        help='Number of tasks to run (default: 0 - all tasks)')
    parser.add_argument("-fs", "--freeze_solvers", action="store_true",
                        help="Freeze solvers, don't mutate them")
    parser.add_argument("-fd", "--freeze_differs", action="store_true",
                        help="Freeze differs, don't mutate them")
    parser.add_argument("-f", "--file_name", type=str, default='batt.py',
                        help="File name to write the batt code to (default: batt.py)")
    args = parser.parse_args()

    # differs = Differs(freeze_differs=args.freeze_differs)
    differs = None

    main(args.count, args.task_id, args.freeze_solvers, args.freeze_differs, args.file_name)

