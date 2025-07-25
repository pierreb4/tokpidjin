from utils import *
from constants import *
from dsl import *

# NOTE Variable I in differ refers to dynamic grid,
# from run, initially I, but then a t_n variable,
# typically one compared to O

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
    x1 = identity(p_g)
    x2 = x1(I)
    x3 = x1(O)
    x4 = difference_tuple(x2, x3)
    x5 = get_nth_t(x4, F0)
    x6 = size(x4)
    return x6


# Flags = namedtuple('Flags', ['train', 'eval'])
#          flags: 'Flags' = Flags(True, False)
def differ_p_g_zo(
    I: 'Grid', 
    O: 'Grid', 
    flags: 'Flags'
) -> 'Integer':
    x1 = identity(p_g)
    x2 = x1(I)
    x3 = x1(O)
    x4 = difference_tuple(x3, x2)
    x5 = get_nth_t(x4, F0)
    x6 = size(x4)
    return x6


def differ_o_g_size_iz(
    I: 'Grid', 
    O: 'Grid', 
    flags: 'Flags'
) -> 'Integer':
    x1 = rbind(o_g, R5)
    x2 = x1(I)
    x3 = x1(O)
    x4 = rbind(sizefilter, ONE)
    x5 = x4(x2)
    x6 = x4(x3)
    x7 = difference(x5, x6)
    x8 = get_nth_f(x7, F0)
    x9 = size(x7)
    return x9


def differ_o_g_size_zo(
    I: 'Grid', 
    O: 'Grid', 
    flags: 'Flags'
) -> 'Integer':
    x1 = rbind(o_g, R5)
    x2 = x1(I)
    x3 = x1(O)
    x4 = rbind(sizefilter, ONE)
    x5 = x4(x2)
    x6 = x4(x3)
    x7 = difference(x6, x5)
    x8 = get_nth_f(x7, F0)
    x9 = size(x7)
    return x9


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
# def summer(
#     I: 'Grid', 
#     O: 'Grid',
#     flags: 'Flags'
# ) -> 'Integer':
#     x1 = differ_p_g_iz(I, O, flags)
#     x2 = differ_p_g_zo(I, O, flags)
#     # More to come here
#     x3 = add(x1, x2)
#     return x3

