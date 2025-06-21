import inspect
import traceback
import re

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

    return [t for var, t in global_id.__annotations__.items()]


class Env:
    def __init__(self, SEED, S, score=0):
        self.SEED = SEED
        self.S = S
        self.score = 0
        # self.arg_dict = {}


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
        budget_random = 0.01

        # Only substitute constants 
        if arg not in constant_dict.keys():
            return arg
        
        if random.random() < budget_random:
            return replace_random(arg, list(constant_dict.keys()))

        return arg


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


    def do_fluff(self, t_num, t):
        func = t[0]
        args = t[1:]

        if t is None or func is None:
            return None

        hints = get_hints(func.__name__)
        # self.arg_dict[t_num] = (0, func, inspect.signature(func))
        # print_l(f'{func.__name__ = }, {args = }, {hints = }')

        # Then apply hint-based substitutions
        for i, arg in enumerate(args):
            if arg is None or hints is None or i >= len(hints):
                continue

            hint = hints[i]

            if hint in ['Any', 'C_']:
                args[i] = self.substitute_color(arg)
            elif hint == 'FL':
                args[i] = self.substitute_rank(arg, FL_NAMES)
            elif hint == 'F_':
                args[i] = self.substitute_rank(arg, F_NAMES)
            elif hint == 'L_':
                args[i] = self.substitute_rank(arg, L_NAMES)
            elif hint == 'R_':
                args[i] = self.substitute_symbol(arg, R_NAMES)
            elif hint == 'R4':
                args[i] = self.substitute_symbol(arg, R4_NAMES)
            elif hint == 'R8':
                args[i] = self.substitute_symbol(arg, R8_NAMES)
                self.score += 1
            elif hint == 'A8':
                args[i] = self.substitute_grid_angle(arg)
            elif hint not in [ 'Samples', 'Grid', 'Tuple', 
                    'Object', 'Objects', 'FrozenSet', 'Patch', 
                    'Callable', 'Container', 'ContainerContainer',
                    'Integer', 'IntegerSet', 'Numerical', 'Indices', 
                    'Boolean', 'IJ', 'A4', 
                ]:
                print_l(f'{hint = }')

            # self.arg_dict[t_num] = (i + 1, arg, hint)

            # if re.fullmatch(r't\d+', arg):
            #     print_f(f'Found t: {arg}')

        try:
            result = func(*args)
            result = run_with_timeout(func, args, timeout=0.001)
        except Exception as e:
            # show_exception("", e)
            # print("traceback: ", traceback.format_exc())
            result = None

        return result

    def print_arg_dict(self):
        print(f'{self.arg_dict = }')


    def get_seed(self):
        return self.SEED

