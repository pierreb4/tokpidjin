import re
import random
import time
import inspect

from pprint import pprint

from utils import *
from constants import *
import dsl
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


class Code:
    def __init__(self, S, score=0):
        self.S = S
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
        c_iz = dsl.c_iz(S, p_g)
        c_zo = dsl.c_zo(S, p_g)

        if c in c_iz and random.random() < 0.5:
            # Change the score at substitution time
            self.score -= 1
            return f'c_iz_n(identity(S), identity(p_g), identity(rbind(get_nth_t, F{c_iz.index(c)})))'
        elif c in c_zo and random.random() < 0.5:
            # Change the score at substitution time
            self.score -= 1
            return f'c_zo_n(identity(S), identity(p_g), identity(rbind(get_nth_t, F{c_zo.index(c)})))'
        elif random.random() < budget_random:
            # Same as usual random replacement
            return random.choice(list(constant_dict.keys()))

        # Get name corresponding to number
        constant_list = list(constant_dict.keys())
        return constant_list[c]


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
        if c == dsl.a_mr(S) and random.random() < 0.5:
            # Change the score at substitution time
            self.score -= 1
            return 'identity(a_mr(S))'        
        elif random.random() < budget_random:
            # Same as usual random replacement
            return random.choice(list(constant_dict.keys()))
        
        return arg


    def mutate(self, t_call, t_num, has_mutation, task_id):
        old_call = clean_call(t_call[f't{t_num}'])
        ret_call = old_call

        old_items = get_items(old_call)
        old_func_name = old_items[0].strip()
        old_hints = get_hints(old_func_name)

        # if random.random() > 0.5:
        #     return ret_call
        
        if old_args := re.findall(r'\b(\w+)\b', old_call):
            # TODO Track t variables to get to hints
            if old_hints is None:
                return ret_call

            for i, (old_arg, old_hint) in enumerate(zip(old_args, old_hints)):
                # First deal with t variables
                if old_arg.startswith('t') and old_arg[1:].isdigit():
                    t_num = int(old_arg[1:])

                    while random.random() < 0.33:
                        t_offset = t_num - random.randint(1, 9)
                        if t_offset > 0:
                            new_call = clean_call(t_call[f't{t_offset}'])
                            new_items = get_items(new_call)
                            new_func_name = new_items[0].strip()
                            new_hints = get_hints(new_func_name)
                            new_hint = new_hints[0] if new_hints else None

                            if new_hint == old_hint:
                                has_mutation[task_id] = True
                                ret_call = re.sub(rf'\bt{t_num}\b', f't{t_offset}', ret_call)
                # Then deal with constants
                else:
                    if old_hint in ['Any', 'C_']:
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
                        old_args[i] = self.substitute_grid_angle(old_arg)
                    elif old_hint not in [ 'Samples', 'Grid', 'Tuple', 
                            'Object', 'Objects', 'FrozenSet', 'Patch', 
                            'Callable', 'Container', 'ContainerContainer',
                            'Integer', 'IntegerSet', 'Numerical', 'Indices', 
                            'Boolean', 'IJ', 'A4', 
                        ]:
                        print_l(f'{old_hint = }')
                    if old_args[i] != old_arg:
                        has_mutation[task_id] = True
                        ret_call = re.sub(rf'\b{old_arg}\b', f'{old_args[i]}', ret_call)
                        # XXX We need to be careful of making substitutions in this ret_call
                    # print_l(f'{old_hint = }')
                    # print_l(f'{old_arg = }')
                    # print_l(f'{old_args[i] = }')
                    # print_l(f'{self.S = }')

        return ret_call


def main(file, seed):
    train_data = get_data(train=True, sort_by_size=True)
    eval_data = get_data(train=False, sort_by_size=True)
    total_data = {k: {**train_data[k], **eval_data[k]} for k in ['train', 'test']}

    solvers = get_solvers([solvers_lnk, solvers_pre])
    equals = {task_id: get_equals(source) for task_id, source in solvers.items()}
    # print_l(f"{get_equals(solvers['a85d4709']) = }")

    # XXX Limit to first 5
    # solvers = {k: solvers[k] for k in list(solvers.keys())[:5]}

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

            train_task = total_data['train'][task_id]
            S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in train_task)
            code = Code(S)

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

                call = code.mutate(t_call, t_num, has_mutation, task_id)                                    
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
