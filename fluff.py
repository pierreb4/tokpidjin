import inspect
import traceback
import re
import random

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
        self.score = score
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
        if t is None:
            return None

        func = t[0]
        args = t[1:]

        try:
            result = func(*args)
        except Exception as e:
        # except (AttributeError, IndexError, KeyError,
        #         RuntimeError,
        #         StopIteration, 
        #         TypeError, ValueError,
        #         ZeroDivisionError) as e:
            # TODO Display and resolve exceptions
            if random.random() < 0.0001:
                with open('fluff.log', 'a') as f:
                    log_exception(f'{t_num = }', e, file=f)
                    print("traceback: ", traceback.format_exc(), file=f)
            result = None

        return result

    def print_arg_dict(self):
        print(f'{self.arg_dict = }')


    def get_seed(self):
        return self.SEED


def log_exception(msg, e=None, file=None):
    frame = inspect.currentframe()
    caller_frame = frame.f_back
    file_path = caller_frame.f_code.co_filename
    file_name = os.path.basename(file_path)
    function_name = caller_frame.f_code.co_name
    line_number = caller_frame.f_lineno
    if file is not None:
        if e is not None:
            print(f"!!! EXCEPTION !!! {type(e).__name__}: {e}", file=file)
        print(f"!!! ========= !!! {file_name}:{line_number} {function_name}: {msg}", file=file)
    else:
        if e is not None:
            print(f"!!! EXCEPTION !!! {type(e).__name__}: {e}")
        print(f"!!! ========= !!! {file_name}:{line_number} {function_name}: {msg}")


