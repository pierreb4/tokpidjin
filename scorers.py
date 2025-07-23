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
def differ_p_g_iz(
    I: 'Grid', 
    O: 'Grid', 
    flags: 'Flags' = Flags(True, False)
) -> 'Integer':
    x1 = p_g(I)
    x2 = p_g(O)
    x3 = dedupe(x1)
    x4 = dedupe(x2)
    x5 = difference_tuple(x3, x4)
    x6 = get_nth_t(x5, F0)
    x7 = size(x5)
    print(f'{x7 = }')
    return x7


# def differ_p_g_iz(I, O, train=True):
#     x1 = identity(p_g)
#     x2 = apply(first, S)
#     x3 = apply(second, S)
#     x4 = mapply(x1, x2)
#     x5 = mapply(x1, x3)
#     x6 = dedupe(x4)
#     x7 = dedupe(x5)
#     x8 = difference_tuple(x4, x5)
#     return x8


# Flags = namedtuple('Flags', ['train', 'eval'])
def differ_p_g_zo(
    I: 'Grid', 
    O: 'Grid', 
    flags: 'Flags' = Flags(True, False)
) -> 'Integer':
    x1 = p_g(I)
    x2 = p_g(O)
    x3 = dedupe(x1)
    x4 = dedupe(x2)
    x5 = difference_tuple(x4, x3)
    x6 = get_nth_t(x5, F0)
    x7 = size(x5)
    print(f'{x7 = }')
    return x7


# def differ_p_g_zo(I, O, train=True):
#     x1 = identity(p_g)
#     x2 = apply(first, S)
#     x3 = apply(second, S)
#     x4 = mapply(x1, x2)
#     x5 = mapply(x1, x3)
#     x6 = dedupe(x4)
#     x7 = dedupe(x5)
#     x8 = difference_tuple(x5, x4)
#     return x8


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
def summer(
    I: 'Grid', 
    O: 'Grid', 
    flags: 'Flags' = Flags(True, False)
) -> 'Integer':
    x1 = differ_p_g_iz(I, O, flags)
    x2 = differ_p_g_zo(I, O, flags)
    # More to come here
    x3 = add(x1, x2)
    return x3

