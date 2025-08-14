import inspect
import traceback
import re
import random

from utils import *
from constants import *
from dsl import *
from differs import *


# Borrowed from regin.py maybe can go to utils.py?
def get_hints(node_name):
    if node_name not in globals():
        return None

    global_id = globals()[node_name]
    if not inspect.isfunction(global_id):
        return None

    return [t for var, t in global_id.__annotations__.items()]


class Env:
    def __init__(self, SEED, task_id, S, log_path=None, score=0):
        self.SEED = SEED
        self.task_id = task_id
        self.S = S
        self.score = score
        self.log_path = 'fluff.log' if log_path is None else log_path
        self.exceptions = 0

    def do_fluff(self, t_num, t, isok=True):
        if t is None or isok == False:
            return OKT(False, None)

        func = t[0]
        args = t[1:]

        try:
            result = OKT(True, func(*args))

            # # Gather score here, depending on function
            # Score = namedtuple('Score', ['iz', 'zo']) 
            # if func in score_funcs:
            #     score = func(*args)
            #     self.score += score.iz + score.zo
            # else:
            #     result = func(*args)

            # Will get returned so:
            # if t32 == O:
            #     o.append((32, False, 'ed36ccf7', '0', self.score))


            # print(f'{t_num = } - {func.__name__} - {args}')
            # print(f'{result = }')
        except Exception as e:
            # TODO Log and resolve exceptions
            #      Log the first few exceptions to fluff.log
            if self.exceptions > 1:
                return OKT(False, None)
            self.exceptions += 1

            with open(self.log_path, 'w') as f:
                log_exception(f'{self.task_id} - {t_num = }', e, file=f)
                print("traceback: ", traceback.format_exc(), file=f)

                # Show the type all arguments
                for i, arg in enumerate(t):
                    print(f' -> {i} - {type(arg) = } - {str(arg)[:60]}', file=f)

                if func is not None and hasattr(func, '__name__'):
                    hints = get_hints(func.__name__)
                    if hints is not None:
                        if hints[-1] in ['FrozenSet', 'Indices', 'IndicesSet', 
                                'IntegerSet', 'Object', 'Objects', 'Patch']:
                            return OKT(True, frozenset())
                        elif hints[-1] in ['Cell', 'Grid', 'IJ', 'Samples', 'Tuple',
                                'TupleTuple']:
                            return OKT(True, ())
                        # else:
                        #     print(f'{func.__name__} -> {hints[-1]} - {t_num}', file=f)

                        # if func.__name__ == 'apply':
                        #     if type(t[2]).__name__ == 'frozenset':
                        #         return frozenset()
                        #     elif type(t[2]).__name__ == 'tuple':
                        #         return ()
                        #     else:
                        #         print(f' -> {type(t[2]).__name__}', file=f)
            result = OKT(False, None)

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


