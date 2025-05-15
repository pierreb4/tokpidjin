import os
import json
import inspect

from arc_types import *
from constants_manus import *
from dsl import *
from main import *
import solvers


def second( container: Container ) -> Any:
    """ second item of container """
    iterator = iter(container)
    next(iterator)
    return next(iterator, None)


def dedupe_pair_tuple(S: SampleTuple) -> SampleTuple:
    """Remove sample pairs where input equals output"""
    return tuple((a, b) for a, b in S if a != b)


def b_iz(S: SampleTuple, function: Callable) -> Any:
    # Filter out identical pairs first
    # For now, we don't use them
    x1 = dedupe_pair_tuple(S)
    # Check that we have something left
    if not x1:
        return False, None    
    x2 = apply(first, x1)
    x3 = apply(second, x1)
    x4 = apply(function, x2)
    x5 = apply(function, x3)
    x6 = papply(difference_tuple, x4, x5)    
    x7 = dedupe(x6)
    if len(x7) == 1:
        return True, x7[0] if x7[0] != () else None
    return False, x7 if len(x7) > 0 else None


def b_iz_n(S: SampleTuple, index: int, function: Callable) -> Any:
    (ret_bool, ret_tuple) = b_iz(S, function)
    if ret_bool and ret_tuple is not None:
        return Color(ret_tuple[index]) if index < len(ret_tuple) else None
    return None


def b_zo( S: SampleTuple, function: Callable ) -> Any:
    # Filter out identical pairs first
    # For now, we don't use them
    x1 = dedupe_pair_tuple(S)
    # Check that we have something left
    if not x1:
        return False, None
    x2 = apply(first, x1)
    x3 = apply(second, x1)
    x4 = apply(function, x2)
    x5 = apply(function, x3)
    x6 = papply(difference_tuple, x5, x4)
    x7 = dedupe(x6)
    if len(x7) == 1:
        return True, x7[0] if x7[0] != () else None
    return False, x7 if len(x7) > 0 else None


def b_zo_n(S: SampleTuple, index: int, function: Callable) -> Any:
    (ret_bool, ret_tuple) = b_zo(S, function)
    if ret_bool and ret_tuple is not None:
        return ret_tuple[index] if index < len(ret_tuple) else None
    return None


def get_constant(S: SampleTuple, func_name: str, constant: str) -> Any:
    command_tuple = (
        f'{constant}',
        f'b_iz_n(S, 0, {func_name})',
        f'b_iz_n(S, 1, {func_name})',
        f'b_iz_n(S, 2, {func_name})',
        f'b_iz_n(S, 3, {func_name})',
        f'b_iz_n(S, 4, {func_name})',
        f'b_iz_n(S, 5, {func_name})',
        f'b_zo_n(S, 0, {func_name})',
        f'b_zo_n(S, 1, {func_name})',
        f'b_zo_n(S, 2, {func_name})',
        f'b_zo_n(S, 3, {func_name})',
        f'b_zo_n(S, 4, {func_name})',
        f'b_zo_n(S, 5, {func_name})',
    )
    exec_var_dict = {
        'S': S
    }

    command_ret = ()
    for command in command_tuple:
        exec_var_dict = { 'S': S }
        exec(f'O = {command}', None, exec_var_dict)
        command_ret += (exec_var_dict['O'],)

    return tuple(
        command for command, ret in zip(command_tuple, command_ret) if ret == command_ret[0]
    )


def get_return_type_name(func: Callable) -> str:
    """Get the return type name of a function."""
    ret_ann = inspect.signature(func).return_annotation
    origin = getattr(ret_ann, '__origin__', None)
    if origin is not None:
        return origin.__name__
    else:
        return str(ret_ann)


def check_frozenset():
    done_tuple = (
        (asindices, asindice_tuple),
        (asobject, asobject_tuple),
        (fgpartition, fgpartition_tuple),
        (frontiers, frontiers_tuple),
        (palette, palette_tuple),
        (partition, partition_tuple),
    )

    for (pre_func, fix_func) in done_tuple:
        # Show outputs to check that they match
        pre_func_name = pre_func.__name__
        print(f'-- {pre_func_name = } --')
        print(f'{b_iz(S, pre_func) = }')
        print(f'{b_zo(S, pre_func) = }')

        fix_func_name = fix_func.__name__
        print(f'-- {fix_func_name = } --')
        print(f'{b_iz(S, fix_func) = }')
        print(f'{b_zo(S, fix_func) = }')

    func_tuple = (
        bottomhalf, compress, dmirror, height, hmirror,
        leastcolor, lefthalf, mostcolor, numcolors, portrait,
        rot180, rot270, rot90, shape, tophalf, vmirror, width,
    )

    for func in func_tuple:
        func_name = func.__name__
        print(f'-- {func_name = } --')

        ret_type_name = get_return_type_name(func)
        print(f'{ret_type_name = }')

        if ret_type_name not in ["<class 'bool'>", "<class 'int'>", 'frozenset']:
            print(f'{b_iz(S, func) = }')
            print(f'{b_zo(S, func) = }')
        else:
            # Print when function returns a frozenset
            if ret_type_name == 'frozenset':
                assert False, f'{func_name} should not return {ret_type_name}'


if __name__ == "__main__":
    data = get_data(train=True)

    # Get constants, solvers and dsl
    with open('constants_manus.py', 'r') as f:
        constants = [c.split(' = ')[0] for c in f.readlines() if ' = ' in c]

    definition_dict = {
        function: inspect.getsource(getattr(solvers, function)) \
            for function in get_functions(solvers.__file__)
    }
    dsl_interface = get_functions(dsl.__file__)

    count = 10
    for key in data['train'].keys():
        key_list = ['253bf280', 'dae9d2b5', '0ca9ddb6']

        if key in key_list:
            pass
        elif count > 0:
            count -= 1
        else:
            continue

        task = data['train'][key]
        print(f'-- {key = } - {len(task) = } -----')
        S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)

        # Find corresponding solver
        solver = getattr(solvers, f'solve_{key}')
        solver_name = solver.__name__
        definition = definition_dict[solver_name]
        print(f'{definition}')

        # Show palette_tuple constants
        print(f'{b_iz(S, palette_tuple) = }')
        print(f'{b_zo(S, palette_tuple) = }')

        lines = definition.split('\n')
        assert lines[0] == f'def {solver_name}(I):'
        assert lines[-1] == ''
        variables = set()
        calls = set()
        for line in lines[1:-2]:
            variable, call = line.lstrip().split(' = ')
            function, args = call.split('(')
            assert variable not in dsl_interface
            assert variable not in variables
            assert call not in calls
            variables.add(variable)
            calls.add(call)
            assert function in dsl_interface or function in variables
            assert args[-1] == ')'
            args = [args[:-1]] if ',' not in args else args[:-1].split(', ')
            for arg in args:
                if arg in constants:
                    for function in dsl_interface:
                        try:
                            constant_call = get_constant(S, function, arg)
                            if len(constant_call) > 1:
                                print(f'{constant_call = }')
                                # Replace constant_call[0] with constant_call[1]
                                # in the definition
                                definition = definition.replace(
                                    f'{variable}', f'{variable} = {constant_call[1]}\n    {variable}', 1 
                                )
                                definition = definition.replace(
                                    constant_call[0], f'{variable}', 1
                                )
                                print(f'{definition}')

                        except:
                            pass

                assert any([
                    arg in variables, arg in dsl_interface,
                    arg in constants, arg == 'I'
                ])
        for v in variables:
            if sum([
                definition.count(vs) for vs in [
                    f'({v})', f'({v}, ', f', {v})',
                    f', {v}, ', f' {v} = ', f' {v}('
                ]
            ]) == 1 and v != 'O':
                print(f'{v = }')
            assert sum([
                definition.count(vs) for vs in [
                    f'({v})', f'({v}, ', f', {v})',
                    f', {v}, ', f' {v} = ', f' {v}('
                ]
            ]) > 1 or v == 'O'


"""
    def FOUR(S: SampleTuple):
        command_tuple = tuple(
            '4',
            'b_iz_0(S, palette_tuple)',
            'b_iz_1(S, palette_tuple)',
            'b_iz_2(S, palette_tuple)',
            'b_iz_3(S, palette_tuple)',
            'b_iz_4(S, palette_tuple)',
            'b_iz_5(S, palette_tuple)',
            'b_zo_0(S, palette_tuple)',
            'b_zo_1(S, palette_tuple)',
            'b_zo_2(S, palette_tuple)',
            'b_zo_3(S, palette_tuple)',
            'b_zo_4(S, palette_tuple)',
            'b_zo_5(S, palette_tuple)',
        )
        command_ret = tuple(exec(command) for command in command_tuple)
        # Return commands for which command_ret equals command_tuple[0]
        return tuple(
            command for command, ret in zip(command_tuple, command_ret)
            if ret == command_tuple[0]
        )

def solve_dae9d2b5(I):
    x1 = lefthalf(I)
    x2 = righthalf(I)
    x3 = ofcolor(x1, FOUR)
    x4 = ofcolor(x2, THREE)
    x5 = combine(x3, x4)
    O = fill(x1, SIX, x5)
    return O

b_iz(S, palette_tuple) = (True, (3, 4))
b_iz_0(S, palette_tuple) = 3
b_zo(S, palette_tuple) = (True, (6,))
arg = 'FOUR'
arg = 'THREE'
arg = 'SIX'

x_n = b_iz(S, palette_tuple)
THREE = x_n[0]


THREE = b_iz_0(S, palette_tuple)
FOUR  = b_iz_1(S, palette_tuple)

"""
