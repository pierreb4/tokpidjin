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

ALL_DSL_FUNCTIONS = inspect.getmembers(dsl, inspect.isfunction)
DSL_FUNCTIONS = [ (name, func) for name, func in ALL_DSL_FUNCTIONS \
        if not name.startswith('_') ]
DSL_FUNCTION_NAMES = [name for name, func in DSL_FUNCTIONS]
DSL_FUNCTION_DICT = dict(DSL_FUNCTIONS)

BUDGET_RANDOM = 0.01

# Borrowed from regin.py maybe can go to utils.py?
def get_hints(dsl_func_name):
    # print_l(f'Getting hints for {dsl_func_name}') if DO_PRINT else None

    if dsl_func_name not in globals():
        return None

    global_id = globals()[dsl_func_name]

    if not inspect.isfunction(global_id):
        return None

    hints = tuple(t for var, t in global_id.__annotations__.items())

    # Fix hints order to match call order
    ret_hints = hints if len(hints) <= 1 else (hints[-1],) + hints[:-1]

    # print_l(f'Getting hints for {dsl_func_name}: {ret_hints}') if DO_PRINT else None

    return ret_hints


def get_value(call_string):
    value = call_string.replace('(', ', ').replace(')', '')
    return tuple(value.split(', '))


# def clean_call(call_value):
#     # print_l(f'Cleaning call_value: {call_value}') if DO_PRINT else None
#     return call_value.replace('(', ', ').replace(')', '')


# def get_items(call_value):
#     # print_l(f'Get items from: {call_value}') if DO_PRINT else None
#     return call_value.strip('[]').split(', ')


# def is_called_as_function(call_str, var_name):
#     """Check if variable is being called as a function (has parentheses after it)"""
#     # Look for pattern: var_name followed by '('
#     pattern = rf'\b{re.escape(var_name)}\s*\('
#     return bool(re.search(pattern, call_str))


def iscompatible_hint(old_hint, new_hint):
    """Check if two hints are compatible.
    
    Returns True if:
    - Both are the same string
    - Either is 'Any'
    - Both are tuples of same length with compatible elements
    - Both are constants from overlapping ranges (using HINT_OVERLAPS)
    """
    if isinstance(old_hint, str) and old_hint == new_hint:
        return True
    
    # Check for 'Any' compatibility
    if old_hint == 'Any' or new_hint == 'Any':
        return True
    
    # Check if both are constants from overlapping ranges
    if isinstance(old_hint, str) and isinstance(new_hint, str):
        # Use centralized type definitions from constants.py
        # Check if these hints are compatible
        if new_hint in HINT_OVERLAPS.get(old_hint, set()):
            return True

        if old_hint in HINT_OVERLAPS:
            return False

        # XXX Until we refine, assume unknown types are compatible        
        return True
    
    # Check tuples
    if isinstance(old_hint, tuple) and isinstance(new_hint, tuple):
        if len(old_hint) != len(new_hint):
            return False
        for oh, nh in zip(old_hint, new_hint):
            if not iscompatible_hint(oh, nh):
                return False
        return True
    
    return False


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
    def __init__(self, file, task_id=None, S=None, t_call=None, 
            t_number=None, t_num=0, vectorized=False):
        self.file = file
        self.task_id = task_id
        self.S = S
        self.vectorized = vectorized  # GPU-friendly batch mode flag

        self.t_call = t_call if t_call is not None else {}
        self.t_number = t_number if t_number is not None else {}

        # List t_nums available for differ or solver mutation
        self.differ = {}
        self.solver = {}

        self.t_num = t_num


    def substitute_color(self, arg, constant_dict=COLORS):
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
        elif random.random() < BUDGET_RANDOM:
            # Same as usual random replacement
            return random.choice(list(constant_dict.keys()))

        # Get name corresponding to number
        constant_list = list(constant_dict.keys())
        return constant_list[c]


    def substitute_color_izzo(self, arg_i, arg_o, f_n):
        t_call = self.t_call
        t_num = self.t_num

        # GPU Batch Pattern: Sample extraction + processing
        # Lines t_num+0 to t_num+3 form a GPU-optimizable pattern
        self.t_call[t_num + 0] = HintValue(get_hints('apply'), ('apply', 'first', 'S'))
        self.file_batt(False)
        self.t_num += 1

        self.t_call[t_num + 1] = HintValue(get_hints('apply'), ('apply', 'second', 'S'))
        self.file_batt(False)
        self.t_num += 1

        self.t_call[t_num + 2] = HintValue(get_hints('mapply'), ('mapply', 'p_g', f't{t_num + 0}'))
        self.file_batt(False)
        self.t_num += 1

        self.t_call[t_num + 3] = HintValue(get_hints('mapply'), ('mapply', 'p_g', f't{t_num + 1}'))
        self.file_batt(False)
        self.t_num += 1

        self.t_call[t_num + 4] = HintValue(get_hints('dedupe'), ('dedupe', f't{t_num + 2}'))
        self.file_batt(False)
        self.t_num += 1

        self.t_call[t_num + 5] = HintValue(get_hints('dedupe'), ('dedupe', f't{t_num + 3}'))
        self.file_batt(False)
        self.t_num += 1

        self.t_call[t_num + 6] = HintValue(get_hints('difference_tuple'), ('difference_tuple', f't{t_num + arg_i}', f't{t_num + arg_o}'))
        self.file_batt(False)
        self.t_num += 1

        self.t_call[t_num + 7] = HintValue(get_hints('get_nth'), ('get_nth', f't{t_num + 6}', f'{f_n}'))
        self.file_batt(False)
        self.t_num += 1
        # self.t_num += 8
        
        # # Generate normal code for all lines
        # for t in range(8):
        #     print(f'    t{t_num + t} = {t_call[t_num + t].value}', file=self.file)
        
        return f't{t_num + 7}'


    def substitute_rank(self, arg, constant_dict):
        if arg not in constant_dict.keys():
            return arg

        return (
            replace_random(arg, list(constant_dict.keys()))
            if random.random() < BUDGET_RANDOM
            else arg
        )


    def substitute_symbol(self, arg, constant_dict):
        # Substitute constants or calls
        if random.random() < BUDGET_RANDOM:
            return random.choice(list(constant_dict.keys()))

        return arg


    def substitute_grid_angle(self, arg, constant_dict=R8_NAMES):
        # Only substitute constants 
        if arg not in constant_dict.keys():
            return arg

        c = constant_dict[arg]
        S = self.S
        if c == a_mr(S) and random.random() < 0.5:
            return self.substitute_grid_angle_mr()
        elif random.random() < BUDGET_RANDOM:
            # Same as usual random replacement
            return random.choice(list(constant_dict.keys()))

        return arg

    def substitute_grid_angle_mr(self):
        t_call = self.t_call
        t_num = self.t_num

        self.t_call[t_num + 0] = HintValue(get_hints('identity'), ('identity', 'S'))
        self.file_batt(False)
        self.t_num += 1

        self.t_call[t_num + 1] = HintValue(get_hints('a_mr'), ('a_mr', f't{t_num + 0}'))
        self.file_batt(False)
        self.t_num += 1
        # self.t_num += 2

        # for t in range(2):
        #     print(f'    t{t_num + t} = {t_call[t_num + t].value}', file=self.file)

        return f't{t_num + 1}'


    def mutate(self, is_solver, freeze=False):
        # NOTE old_call is a HintValue namedtuple
        old_call = self.t_call[self.t_num]
        differ = self.differ[self.t_num]
        solver = self.solver[self.t_num]

        print(f'    # Pre-mutate t{self.t_num}', file=self.file)
        print(f'    # -- {old_call.value = }', file=self.file)
        print(f'    # -- {old_call.hint = }', file=self.file)
 
        has_mutation = Mutation(False, None, None)

        old_args = old_call.value
        old_hints = old_call.hint

        if old_hints is None:

            # print_l(f'-- old_hints is None for {old_call}') if DO_PRINT else None

            last_hint = None
            for i, old_arg in enumerate(old_args):

                # print_l(f'-- old_call[{i}] = {old_arg}') if DO_PRINT else None

                if re.match(r't\d+', old_arg):
                    t_n = int(old_arg[1:])

                    # print_l(f'-- old_arg is t variable: {old_arg}: {self.t_call[t_n]}') if DO_PRINT else None

                    last_hint = self.t_call[t_n].hint[0] if isinstance(self.t_call[t_n].hint, tuple) else self.t_call[t_n].hint

            # TODO Check that this is the correct behavior for both legs below
            # NOTE Still better than before :)
            old_hint = last_hint

            # old_func_name is a t variable
            for i, old_arg in enumerate(old_args):
                # First deal with t variables
                if re.match(r't\d+', old_arg):
                    if not freeze:
                        t_n = int(old_arg[1:])
                        has_mutation = self.do_offset_mutation(old_hint, old_call, t_n, is_solver, has_mutation)
                elif not freeze:
                    has_mutation = self.do_arg_substitutions(old_hint, old_call, old_args, old_arg, i, is_solver, has_mutation)
        else:
            # old_func_name is a known function
            # Skip last hint (return type) and use only argument hints
            if isinstance(old_hints, str):
                arg_hints = [old_hints]
            else:
                arg_hints = old_hints[1:] if len(old_hints) > 1 else []

            for i, (old_arg, old_hint) in enumerate(zip(old_args, arg_hints)):

                if isinstance(old_hint, str) and re.match(r'^[a-z]$', old_hint):
                    print_l(f'-- {old_func_name} - {old_args} - {arg_hints}') if DO_PRINT else None
                    print_l(f'-- old_hint is {old_hint} for {old_call}') if DO_PRINT else None

                # First deal with t variables
                if re.match(r't\d+', old_arg):
                    if not freeze:
                        t_n = int(old_arg[1:])
                        has_mutation = self.do_offset_mutation(old_hint, old_call, t_n, is_solver, has_mutation)
                elif not freeze:
                    has_mutation = self.do_arg_substitutions(old_hint, old_call, old_args, old_arg, i, is_solver, has_mutation)

        return self.file_batt(has_mutation)


    def file_batt(self, has_mutation):
        # NOTE old_call is a HintValue namedtuple
        t_call = self.t_call[self.t_num]

        # call_list = [c.strip() for c in t_call.value.split(',')]
        # func_name = call_list[0]

        call_list = t_call.value
        func_name = call_list[0]

        call_string = f'{func_name}(' + ', '.join(call_list[1:]) + ')'
        
        # Wrap ALL assignments in try-except to catch bad mutations
        # (wrong function signatures, type errors, etc.)
        # Use type-aware default from _get_safe_default() helper
        # UNLESS in vectorized mode (GPU-friendly, no try/except)
        if self.vectorized:
            # Vectorized mode: direct assignment, no exception handling
            # Pre-validation happens at batch level
            print(f'    t{self.t_num} = {call_string}', file=self.file)
        else:
            # Standard mode: safe with try/except
            print('    try:', file=self.file)
            print(f'        t{self.t_num} = {call_string}', file=self.file)
            print('    except (TypeError, AttributeError, ValueError, IndexError, KeyError):', file=self.file)
            print(f'        t{self.t_num} = _get_safe_default({func_name})', file=self.file)
        return has_mutation


    def do_offset_mutation(self, old_hint, old_call, t_n, is_solver, has_mutation):
        while random.random() < BUDGET_RANDOM:
            # while True:
            for _ in range(99):
                t_offset = random.randint(1, t_n)

                if is_solver and self.solver.get(t_offset, False) or not is_solver:
                    t_name = f't{t_n}'

                    print_l(f'Considering offset mutation for {t_name} to t{t_offset}') if DO_PRINT else None
                    print_l(f'-- {t_name}: {self.t_call[t_n]}') if DO_PRINT else None
                    print_l(f'-- t{t_offset}: {self.t_call[t_offset]}') if DO_PRINT else None

                    new_hint = self.t_call[t_offset].hint

                    if random.randint(0, 1) == 0:
                        if not iscompatible_hint(old_hint, new_hint):
                            continue

                        sub_item = f't{t_offset}'
                        print_l(f'Offset: {sub_item = }') if DO_PRINT else None

                    elif old_call.value[0] == t_name:
                        # Check function compatibility
                        old_hints = old_call.hint
                        # while True:
                        for _ in range(99):
                            sub_item = random.choice(DSL_FUNCTION_NAMES)
                            new_hints = get_hints(sub_item)

                            if len(new_hints) == len(old_hints):
                                all_compatible = all(
                                    iscompatible_hint(
                                        old_arg_hint, new_arg_hint
                                    )
                                    for old_arg_hint, new_arg_hint in zip(
                                        old_hints, new_hints
                                    )
                                )
                            else:
                                sub_item = t_name

                            break

                        print_l(f'New func: {sub_item = }') if DO_PRINT else None

                    elif old_hint in INT_TYPE_RANGES:
                        sub_item = random.choice([*INT_GENERIC_CONSTANTS])
                        print_l(f'New arg: {sub_item = }') if DO_PRINT else None

                    elif old_hint in PAIR_TYPE_RANGES:
                        sub_item = random.choice([*PAIR_GENERIC_CONSTANTS])
                        print_l(f'New arg: {sub_item = }') if DO_PRINT else None

                    else:
                        sub_item = t_name
                        print_l(f'No mutation for {sub_item = } due to hint: {old_hint = }') \
                                if DO_PRINT else None

                    value = tuple(sub_item if item == t_name else item for item in old_call.value)

                    # XXX We might need old_hints here
                    self.t_call[self.t_num] = HintValue(old_hint, value)
                    has_mutation = Mutation(True, old_call, self.t_call[self.t_num])
                    break

        return has_mutation


    def do_arg_substitutions(self, old_hint, old_call, old_args, old_arg, i, is_solver, has_mutation):
        sub_arg = old_arg

        if old_hint in ('C_',):
            sub_arg = self.substitute_color(old_arg)
        elif old_hint == 'FL':
            sub_arg = self.substitute_rank(old_arg, FL_NAMES)
        elif old_hint == 'F_':
            sub_arg = self.substitute_rank(old_arg, F_NAMES)
        elif old_hint == 'L_':
            sub_arg = self.substitute_rank(old_arg, L_NAMES)
        elif old_hint == 'R_':
            sub_arg = self.substitute_symbol(old_arg, R_NAMES)
        elif old_hint == 'R4':
            sub_arg = self.substitute_symbol(old_arg, R4_NAMES)
        elif old_hint == 'R8':
            sub_arg = self.substitute_symbol(old_arg, R8_NAMES)
        elif old_hint == 'A4':
            sub_arg = self.substitute_symbol(old_arg, A4_NAMES)
        elif old_hint == 'A8':
            sub_arg = self.substitute_grid_angle(old_arg)
        elif old_hint == 'Boolean':
            sub_arg = self.substitute_symbol(old_arg, B_NAMES)
        elif old_hint in ('I_', 'J_'):
            sub_arg = self.substitute_symbol(old_arg, CONSTANTS)
        elif old_hint == 'IJ':
            sub_arg = self.substitute_symbol(old_arg, PAIR_GENERIC_CONSTANTS)
        elif old_hint not in ('Samples', 'Grid', 'Tuple',
                'Object', 'Objects', 'Patch', 'Indices',
                'Callable', 'Container', 'ContainerContainer',
                'Integer', 'Numerical', 'Colors', 'FrozenSet',
                'TupleTuple', 'TTT_iii', 'Any',
                None
         ) and not isinstance(old_hint, tuple):
            print_l(f'Unrecognised type: {old_hint = } in {old_call}') if DO_PRINT else None
        elif self.t_num > 1 and random.random() < BUDGET_RANDOM:

            # XXX We need to get in here when old_hint is a tuple type
            # XXX And adapt the code accordingly

            if old_hint == 'Callable':

                # NOTE We also need to match hints

                # Replace with random function of same arity
                old_func_name = old_args[i]

                if old_func_name not in DSL_FUNCTION_DICT:
                    print_l(f'{old_func_name = } - {old_args = }')

                old_function = DSL_FUNCTION_DICT[old_func_name] if old_func_name in DSL_FUNCTION_DICT else None
                arity = old_function.__code__.co_argcount

                # while True:
                for _ in range(99):
                    new_func_name = random.choice(DSL_FUNCTION_NAMES)
                    new_function = DSL_FUNCTION_DICT[new_func_name]
                    if new_function.__code__.co_argcount == arity:
                        break
                sub_arg = new_func_name

            elif not isinstance(old_hint, tuple):
                # Replace with a t variable
                t_n = self.t_num - 1
                # while True:
                for _ in range(99):
                    t_offset = random.randint(1, t_n)
                    if is_solver and self.solver.get(t_offset, False) or not is_solver:
                        # old_args[i] = f't{t_offset}'
                        sub_arg = f't{t_offset}'
                        break
            else:
                print_l(f'Unprocessed tuple type for substitution: {old_hint = }')

        if sub_arg != old_arg:
            # pattern = rf'\b{old_arg}\b'
            # self.t_call[self.t_num] = re.sub(pattern, f'{old_args[i]}', old_call.value)
            # Replace value
            # value = re.sub(pattern, f'{old_args[i]}', old_call.value)

            value = old_call.value[:i] + (sub_arg,) + old_call.value[i+1:]

            # XXX We might need old_hints here
            self.t_call[self.t_num] = HintValue(old_hint, value)
            has_mutation = Mutation(True, old_call, self.t_call[self.t_num])
        return has_mutation


def get_equals(source):
    # Catalog assignments in source
    # Each assignment maps x_var -> HintValue(hint, value)
    # where hint is the return type of the function being called
    equals = {}
    for line in source.split('\n'):

        # print_l(f'Processing line: {line}') if DO_PRINT else None

        if match := re.match(r'    (.+) = (([^(]+)\(.+)', line):
            x_var = match[1]
            call = match[2]
            func = match[3]

            # Check if func is an x variable (like x1, x2, etc.)
            if re.match(r'x\d+', func):
                # func is an x variable, get its hints from equals
                func_hint_value = equals.get(func)
                func_hints = func_hint_value.hint if func_hint_value else None
                if func_hints is None:
                    # x variable not yet defined - this is an error in the solver
                    print_l(f'ERROR: x variable {func} used before definition in line: {line}') if DO_PRINT else None
                    assert False, f'Unknown x variable {func} in line: {line}'
            else:
                # func is a DSL function name
                func_hints = get_hints(func)
                if func_hints is None:
                    # Unknown function - this is an error
                    print_l(f'ERROR: Unknown function {func} in line: {line}') if DO_PRINT else None
                    assert False, f'Unknown function {func} in line: {line}'
            
            top_values = get_value(call)

            # print_l(f'Processing: {line = }') if DO_PRINT else None
            # print_l(f'            {func_hints = }') if DO_PRINT else None
            # print_l(f'            {top_values = }') if DO_PRINT else None

            new_hints = ()
            for hint_count, value in enumerate(top_values):
                add_hint = ()
                if re.match(r'x\d+', value):

                    # print_l(f'Processing {hint_count = } and {value = }') if DO_PRINT else None

                    hint_value = equals.get(value)

                    # print_l(f'Found hint_value: {hint_value}') if DO_PRINT else None

                    if hint_count == 0 and hint_value:
                        new_hints = hint_value.hint[0]
                        break

                    # add_hint = (hint_value.hint[0],) if len(hint_value.hint) > 0 else () 

                # Numerical constants and DSL function names
                # NOTE We only expect function names below, for now
                else:
                    # print_l(f'Processing: {value}') if DO_PRINT else None

                    if value == 'S':
                        add_hint = ('Samples',)
                    elif value in ('I', 'C'):
                        add_hint = ('Grid',)
                    elif value in B_NAMES:
                        add_hint = ('Boolean',)    
                    elif value in F_NAMES:
                        add_hint = ('F_',)
                    elif value in FL_NAMES:
                        add_hint = ('FL',)
                    elif value in L_NAMES:
                        add_hint = ('L_',)
                    elif value in R_NAMES:
                        add_hint = ('R_',)
                    elif value in R4_NAMES:
                        add_hint = ('R4',)
                    elif value in R8_NAMES:
                        add_hint = ('R8',)
                    elif value in A4_NAMES:
                        add_hint = ('A4',)
                    elif value in A8_NAMES:
                        add_hint = ('A8',)
                    elif value in COLORS:
                        add_hint = ('C_',)
                    elif value in INT_GENERIC_CONSTANTS:
                        add_hint = ('Integer',)
                    elif value in PAIR_GENERIC_CONSTANTS:
                        add_hint = ('IJ',)

                    # Function names
                    elif value[0].islower():
                        if hint_count == 0 and value in ['identity', 'rbind', 'lbind']:

                            # print_l(f'Adjusting: {func_hints = } for: {top_values = }') if DO_PRINT else None

                            first_arg = top_values[1]

                            # Lookup first argument hints
                            if re.match(r'x\d+', first_arg):
                                hint_value = equals.get(first_arg)
                                hint_base = hint_value.hint[0] if hint_value else 'Callable'
                            else:
                                hint_base = get_hints(first_arg)

                            if value == 'identity':
                                new_hints = (hint_base,)
                                break

                            if value == 'rbind':
                                new_hints = (hint_base[:-1],)
                                break

                            if value == 'lbind':
                                new_hints = (hint_base[1:],)
                                break

                        else:
                            new_hints = get_hints(value)

                            # print_l(f'Getting {new_hints = } for {value = }') if DO_PRINT else None

                            if hint_count == 0 and func_hints:
                                add_hint = (func_hints[0], )
                                break
                            
                            if new_hints:
                                add_hint = (new_hints,)
                    else:
                        print_l(f'Could not extract hints for value: {value}') if DO_PRINT else None

                # Add hints
                if hint_count != 0:
                    new_hints += add_hint

            equals[x_var] = HintValue(new_hints, top_values)

    return equals


def adjust_hints(equals, value, hint):
    hints = None

    if func_name == 'identity':
        func_arg = re.match(r'identity\((\w+)\)', value)[1]
        hints = get_hints(func_arg)
        hint = (hints, hints)

    return hint


def assert_message(source, value, message):
    print(source)
    print_l(f'{value = }')
    assert False, message


def track_solution(t_call, t_num, done):
    if done is None:
        done = set()

    if t_num not in done:
        done.add(t_num)

    call = t_call[t_num].value

    # if t_list := re.findall(r't(\d+)', call):
    #     for t_str in t_list:
    #         t_num = int(t_str)

    if t_list := [int(item[1:]) for item in call if re.match(r't\d+', item)]:
        for t_num in t_list:
            if t_num not in done:
                done.add(t_num)
                track_solution(t_call, t_num, done)

    return done


def build_differ_body(t_call, ret_t, done):
    differ_body = ''
    for t_num in sorted(done):
        # t_split = [item.strip() for item in t_call[t_num].value.split(',')]
        # t = [s[:-2] if s.endswith('.t') else s for s in t_split]

        t = t_call[t_num].value

        func = t[0]
        args = t[1:]
        differ_body += f'    t{t_num} = {func}({", ".join(args)})\n'
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
            for x_name, hint_value in self.init_equals[differ_name].items():
                # Extract value from HintValue namedtuple
                x_value = hint_value.value
                # Perform substitution and store back as HintValue namedtuple
                # sub_value = re.sub(r'\bI\b', I, x_value)
                sub_value = tuple(I if item == 'I' else item for item in x_value)
                self.run_equals[differ_name][x_name] = HintValue(hint_value.hint, sub_value)

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

            # XXX Not sure that we actually need this
            # We don't seem to save the differ source

            # if task_id is None:
            #     done = track_solution(code.t_call, code.t_num, None)

            #     # print_l(f'{differ_name} - {done = }')

            #     differ_body = build_differ_body(code.t_call, code.t_num, done)
            #     differ_body = re.sub(r'\bt(\d+)\b', r'x\1', differ_body)

            #     differ_source = f'def differ(S, I, C):\n{differ_body}'

            #     inlined_source = inline_variables(differ_source)
            #     md5_hash = hashlib.md5(inlined_source.encode()).hexdigest()


            # print(f"    if type(t{code.t_num}.t) is int:", file=code.file)
            # print(f"        s.append(({code.t_num}, '{task_id}', '{differ_name}', t{code.t_num}.t))", file=code.file)
            print(f"    s.append(({code.t_num}, '{task_id}', '{differ_name}', t{code.t_num}))", file=code.file)

        code.last_differ_t_num = code.t_num


def add_differ_line(equals, code, uses, task_id=None, freeze_differs=False):
    # Take next assignment - x_n = HintValue(hint, call(...))
    # old_name, hint_value = next(iter(equals.items()))
    # old_call = hint_value.value


    # Now old_call is a hint_value namedtuple
    old_name, old_call = next(iter(equals.items()))

    uses[old_call.value] = 0

    # old_items = get_items(old_call.value)
    # old_func_name = old_items[0].strip()

    old_func_name = old_call.value[0]

    # Remove entry from equals
    del equals[old_name]

    # Check that right side is new
    if old_call.value not in code.t_number:
        # Then add it to t_call/t_number
        code.t_num += 1
        code.t_call[code.t_num] = old_call
        code.differ[code.t_num] = True
        # Make t_num available for solver mutation when it fills conditions
        code.solver[code.t_num] = bool(
            len(equals) == 1 and old_func_name == 'get_nth'
        )
        has_mutation = code.mutate(False, freeze_differs)
        code.t_number[old_call.value] = code.t_num
    else:
        has_mutation = Mutation(False, None, None)

    if has_mutation.present and not freeze_differs and task_id is None \
            and DO_PRINT:
        print_l(f'{old_name = } - {old_call = }')
        print_l(f'{code.t_call[code.t_num] = }')

    # Replace x_n with t_name[x_call] in rest of solver
    for x_name, x_hint_value in equals.items():
        x_call = x_hint_value.value
        if old_name in x_call:
            uses[old_call.value] += 1
            # Replace old_name with t_number[old_call] to track mutations
            # new_call = re.sub(rf'\b{old_name}\b', f't{code.t_number[old_call.value]}', x_call)

            new_call = tuple(
                f't{code.t_number[old_call.value]}' if item == old_name else item
                for item in x_call
            )

            equals[x_name] = HintValue(x_hint_value.hint, new_call)


def append_to_o(code, last_t, has_mutation, task_id):
    print(f"    o.append(({last_t}, {has_mutation.present}, '{task_id}', t{last_t}))", file=code.file)


def add_solver_line(equals, code, uses, task_id=None, freeze_solvers=False):
    # Take next assignment - x_n = HintValue(hint, call(...))
    # old_name, hint_value = next(iter(equals.items()))
    # old_call = hint_value.value


    # Now old_call is a hint_value namedtuple
    old_name, old_call = next(iter(equals.items()))


    uses[old_call.value] = 0

    # Remove entry from equals
    del equals[old_name]

    # Check that right side is new
    if old_call.value not in code.t_number:
        # Then add it to t_call/t_number
        code.t_num += 1
        code.t_call[code.t_num] = old_call
        code.differ[code.t_num] = False
        code.solver[code.t_num] = True
        has_mutation = code.mutate(True, freeze_solvers)
        code.t_number[old_call.value] = code.t_num
    else:
        has_mutation = Mutation(False, None, None)

    # Was the left side O?
    if old_name == 'O':
        append_to_o(code, code.t_num, has_mutation, task_id)

    # Replace x_n with t_name[x_call] in rest of solver
    for x_name, x_hint_value in equals.items():
        x_call = x_hint_value.value
        if old_name in x_call:
            uses[old_call.value] += 1
            # new_call = re.sub(rf'\b{old_name}\b', f't{code.t_num}', x_call)

            new_call = tuple(
                f't{code.t_num}' if item == old_name else item
                for item in x_call
            )

            equals[x_name] = HintValue(x_hint_value.hint, new_call)

    return old_name == 'O'


def main(count=0, task_id=None, freeze_solvers=False, freeze_differs=False, batt_file_name='batt.py', vectorized=False):
    train_data = get_data(train=True, sort_by_size=True)
    # eval_data = get_data(train=False, sort_by_size=True)
    # total_data = {k: {**train_data[k], **eval_data[k]} for k in ['demo', 'test']}
    total_data = train_data

    # Get one of best solvers if not mutating (while running main.py for instance)
    all_solvers = get_solvers([solvers_dir], best_only=freeze_solvers)
    # pre_solvers = get_solvers([solvers_pre], best_only=freeze_solvers)
    # dir_solvers = get_solvers([solvers_dir], best_only=freeze_solvers)
    # all_solvers = {**dir_solvers, **pre_solvers}
    # all_solvers = {**pre_solvers, **dir_solvers}
    all_task_ids = list(all_solvers.keys())    

    print_l(f"{len(all_solvers) = }")

    if task_id:
        solvers = {k: all_solvers[k] for k in [task_id]}
    elif count > 0:
        # # Pick random solvers, half from pre_solvers, half from dir_solvers
        # # TODO Refine to pick half proven solvers and half unproven solvers
        # # We can check that the score in solver_dir (solver.o_score) matches the number of samples in S
        # rnd_dir_solvers = {k: dir_solvers[k] for k in random.sample(list(dir_solvers.keys()), count // 2)}
        # dir_count = len(rnd_dir_solvers)
        # pre_count = count - dir_count
        # rnd_pre_solvers = {k: pre_solvers[k] for k in random.sample(list(pre_solvers.keys()), pre_count)}
        # # XXX Don't apply sourcery suggestion below. It breaks things!
        # rnd_solvers = {**rnd_dir_solvers, **rnd_pre_solvers}

        assert len(all_task_ids) >= count, f'Not enough tasks to sample {count} from {len(all_task_ids)}'

        rnd_solvers = {k: all_solvers[k] for k in random.sample(all_task_ids, count)}
        rnd_task_ids = list(rnd_solvers.keys())

        task_sizes = []
        for task_id in rnd_task_ids:
            size = 0
            for S in total_data['demo'][task_id] + total_data['test'][task_id]:
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
    # pre_task_ids = [k for k in all_task_ids if k in pre_solvers]
    # dir_task_ids = [k for k in all_task_ids if k in dir_solvers]
    # print_l(f'{len(solvers) = } - {len(pre_solvers) = } - {len(dir_solvers) = }')
    # print_l(f'{len(task_ids) = } - {len(pre_task_ids) = } - {len(dir_task_ids) = }')

    # # Write mix_task_ids into file based on batt_file_name
    # # Used in run_batt.py (from call import mix_task_ids)
    # mix_task_ids = task_ids
    # mix_file_name = batt_file_name.replace('.py', '_mix.py')
    # with open(mix_file_name, 'w') as mix_file:
    #     print(f'{mix_task_ids = }', file=mix_file)

    task_ids = list(solvers.keys())
    differs = Differs(task_ids, freeze_differs=args.freeze_differs)

    equals = {task_id: get_equals(solver.source) for task_id, solver in solvers.items()}
    seed = time.time()
    random.seed(seed)

    with open(batt_file_name, 'w') as batt_file:
        print(
f"""# Generated by tokpidjin/card.py

from dsl import *
from constants import *
from safe_dsl import _get_safe_default

def batt(task_id, S, I, C, log_path):
    s = []
    o = []""", file=batt_file)

        # Pass vectorized mode to Code class
        code = Code(batt_file, vectorized=vectorized)
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
                func_name = solver.name
                # solver_path = solver.path
                source = solver.source

                if task_id not in total_data['demo']:
                    continue

                train_task = total_data['demo'][task_id]
                S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in train_task)
                code.S = S
                code.task_id = task_id

                # Check if equals is empty
                if not equals[task_id]:
                    # Then remove it from solver list
                    del solvers[task_id]
                    continue

                # if solver in pre_solvers.values():
                #     # Don't mutate pre_solvers
                #     freeze_solvers = True
                # else:
                #     freeze_solvers = freeze_solvers

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
        print("from collections import namedtuple", file=call_file)
        print("HintValue = namedtuple('HintValue', ['hint', 'value'])", file=call_file)
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
    parser.add_argument("--vectorized", action="store_true",
                        help="Generate vectorized batch-friendly version (GPU-optimized, no try/except)")
    args = parser.parse_args()

    # differs = Differs(freeze_differs=args.freeze_differs)
    differs = None

    main(args.count, args.task_id, args.freeze_solvers, args.freeze_differs, args.file_name, args.vectorized)

