from utils import *
from constants import *
from dsl import *

# NOTE Variable I in differ refers to dynamic grid,
# from run, initially I, but then a t_n variable,
# typically one compared to O
# TODO Consider moving differ (and future friends)
# to their own file
# XXX Simplify to diff single (running) input
# and single (static) output. Think about
# how to make sure to not take into account
# outputs from test tasks (maybe train=True flag?)

# Flags = namedtuple('Flags', ['train', 'eval'])
#          flags: 'Flags' = Flags(True, False)
def differ_p_g_iz(
    I: 'Grid', 
    O: 'Grid', 
    flags: 'Flags'
) -> 'Integer':
    x1 = p_g(I)
    x2 = p_g(O)
    x3 = difference_tuple(x1, x2)
    x4 = get_nth_t(x3, F0)
    x5 = size(x3)
    return x5


# Flags = namedtuple('Flags', ['train', 'eval'])
#          flags: 'Flags' = Flags(True, False)
def differ_p_g_zo(
    I: 'Grid', 
    O: 'Grid', 
    flags: 'Flags'
) -> 'Integer':
    x1 = p_g(I)
    x2 = p_g(O)
    x3 = difference_tuple(x2, x1)
    x4 = get_nth_t(x3, F0)
    x5 = size(x3)
    return x5


# TODO Write more like these
# differ_p_g
# differ_o_g_size
# differ_o_g_loc
# differ_o_g_dir


# Provide seeds for pickers, to be used
# by the solvers in constant replacements
# def pickers(I, O, flags=Flags(True, False)):
#     x1 = differ_p_g_iz(I, O, flags)
#     x2 = get_nth_t(x1, F0)
#     x3 = differ_p_g_zo(I, O, flags)
#     x4 = get_nth_t(x3, F0)


# TODO Think about how to use flag further,
# interaction between train flag, test with 
# correct result and test without
# XXX Probably train and eval flags

# Flags = namedtuple('Flags', ['train', 'eval'])
#          flags: 'Flags' = Flags(True, False)
def summer(
    I: 'Grid', 
    O: 'Grid',
    flags: 'Flags'
) -> 'Integer':
    x1 = differ_p_g_iz(I, O, flags)
    x2 = differ_p_g_zo(I, O, flags)
    # More to come here
    x3 = add(x1, x2)
    return x3

