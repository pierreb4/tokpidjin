from utils import *
from constants import *
from dsl import *

# NOTE Variable I in differ refers to dynamic grid
# in run, initially I, but then any grid in t_n

# TODO Differentiate between train and eval,
# maybe with train and eval flags, but what level?
# This here might be too low
# XXX Keeping them as placeholders/reminders

# Flags = namedtuple('Flags', ['train', 'eval'])
#          flags: 'Flags' = Flags(True, False)
# def differ_p_g_iz(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
# def differ_207afa9ac2f8547d9e6bd57058d4206c(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
#     x1 = identity(p_g)
#     x2 = x1(I)
#     x3 = x1(O)
#     x4 = difference_tuple(x2, x3)
#     x5 = get_nth_t(x4, F0)
#     x6 = size(x4)
#     return x6


# # def differ_p_g_zo(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
# def differ_9b8e636bf6f8a4e30a0d6aa8ae396d68(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
#     x1 = identity(p_g)
#     x2 = x1(I)
#     x3 = x1(O)
#     x4 = difference_tuple(x3, x2)
#     x5 = get_nth_t(x4, F0)
#     x6 = size(x4)
#     return x6


# # def differ_o_g_size_iz(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
# def differ_089d541a66d5d39cab837ff24efc0ba6(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
#     x1 = rbind(o_g, R5)
#     x2 = x1(I)
#     x3 = x1(O)
#     x4 = rbind(sizefilter, ONE)
#     x5 = x4(x2)
#     x6 = x4(x3)
#     x7 = difference(x5, x6)
#     x8 = get_nth_f(x7, F0)
#     x9 = size(x7)
#     return x9


# # def differ_o_g_size_zo(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
# def differ_26e5f26b09a980364a8d2d36c5bfb723(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
#     x1 = rbind(o_g, R5)
#     x2 = x1(I)
#     x3 = x1(O)
#     x4 = rbind(sizefilter, ONE)
#     x5 = x4(x2)
#     x6 = x4(x3)
#     x7 = difference(x6, x5)
#     x8 = get_nth_f(x7, F0)
#     x9 = size(x7)
#     return x9


# S needs to be the list of training I/O pairs
# Then we test by setting S to test pair(s)
# So batt can take just S, not I/O as arg
# Enable mutate for training, not for testing

# Q: What's the second part of S when testing? None, or?

# def differ_p_g_iz(S, I):
def differ_d77f143df3eb9933c7395936b029b48e(S, I):
    x1 = apply(first, S)
    x2 = apply(second, S)
    x3 = mapply(p_g, x1)
    x4 = mapply(p_g, x2)
    x5 = dedupe(x3)
    x6 = dedupe(x4)
    x7 = difference_tuple(x5, x6)
    x8 = get_nth_t(x7, F0)
    x9 = size(x7)
    return x9


# def differ_p_g_zo(S, I):
def differ_e5a497998c2ee27e2075f6c719d63297(S, I):
    x1 = apply(first, S)
    x2 = apply(second, S)
    x3 = mapply(p_g, x1)
    x4 = mapply(p_g, x2)
    x5 = dedupe(x3)
    x6 = dedupe(x4)
    x7 = difference_tuple(x6, x5)
    x8 = get_nth_t(x7, F0)
    x9 = size(x7)
    return x9


# def differ_o_g_size_iz(S, I):
def differ_813b3ee28f8ced59e41d06fc4eb58700(S, I):
    x1 = rbind(o_g, R5)
    x2 = apply(first, S)
    x3 = apply(second, S)
    x4 = mapply(x1, x2)
    x5 = mapply(x1, x3)
    x6 = rbind(sizefilter, ONE)
    x7 = mapply(x6, x4)
    x8 = mapply(x6, x5)
    x9 = difference(x7, x8)
    x10 = get_nth_f(x9, F0)
    x11 = size(x9)
    return x11


# def differ_o_g_size_zo(S, I):
def differ_78619a027297b52eff7fdf1c30494b5d(S, I):
    x1 = rbind(o_g, R5)
    x2 = apply(first, S)
    x3 = apply(second, S)
    x4 = mapply(x1, x2)
    x5 = mapply(x1, x3)
    x6 = rbind(sizefilter, ONE)
    x7 = mapply(x6, x4)
    x8 = mapply(x6, x5)
    x9 = difference(x8, x7)
    x10 = get_nth_f(x9, F0)
    x11 = size(x9)
    return x11


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
# XXX Put picker bits in card.py
#     together with substitute funcs

