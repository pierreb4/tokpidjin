from utils import *
from constants import *
from dsl import *

# NOTE Variable I in differ refers to dynamic grid
# in run, initially I, but then any grid in t_n

# def differ_p_g_iz:
def differ_3f0ddb7d879771cea3fd76b3efe1f81a(S, I, C):
    x1 = identity(p_g)
    x2 = x1(I)
    x3 = x1(C)
    x4 = difference_tuple(x2, x3)
    x5 = size(x4)
    x6 = multiply(x5, HUNDRED)
    x7 = subtract(THOUSAND, x6)
    x8 = get_nth_t(x4, F0)
    x9 = astuple(x7, x8)
    return x9


# def differ_p_g_zo:
def differ_24bc869480a2b6e94edb36dde31aa952(S, I, C):
    x1 = identity(p_g)
    x2 = x1(I)
    x3 = x1(C)
    x4 = difference_tuple(x3, x2)
    x5 = size(x4)
    x6 = multiply(x5, HUNDRED)
    x7 = get_nth_t(x4, F0)
    x8 = astuple(x6, x7)
    return x8


# def differ_o_g_size_iz:
def differ_c1c647c98b030d4e84ceab659a625a86(S, I, C):
    x1 = rbind(o_g, R5)
    x2 = x1(I)
    x3 = x1(C)
    x4 = rbind(sizefilter, ONE)
    x5 = x4(x2)
    x6 = x4(x3)
    x7 = difference(x5, x6)
    x8 = size(x7)
    x9 = multiply(x8, HUNDRED)
    x10 = subtract(THOUSAND, x9)
    x11 = get_nth_f(x7, F0)
    x12 = astuple(x10, x11)
    return x12


# def differ_o_g_size_zo:
def differ_d94712356774eb0ee744182d98e136ae(S, I, C):
    x1 = rbind(o_g, R5)
    x2 = x1(I)
    x3 = x1(C)
    x4 = rbind(sizefilter, ONE)
    x5 = x4(x2)
    x6 = x4(x3)
    x7 = difference(x6, x5)
    x8 = size(x7)
    x9 = multiply(x8, HUNDRED)
    x10 = get_nth_f(x7, F0)
    x11 = astuple(x9, x10)
    return x11


# TODO Write more like these
# differ_p_g
# differ_o_g_size
# differ_o_g_loc
# differ_o_g_dir


def differ_2e60be2014891e3e081089061ca48033(S, I, C):
    """
    Count matching cells when dimensions match (Tier 2 scoring).
    Returns (total_cells, matching_cells).
    """
    x1 = cellwise(I, C, NEG_ONE)
    x2 = f_ofcolor(x1, NEG_ONE)
    x3 = size(x2)
    x4 = height_t(I)
    x5 = width_t(I)
    x6 = multiply(x4, x5)
    x7 = subtract(x6, x3)
    x8 = astuple(x6, x7)
    return x8


# Alias for readability
differ_exact_dims = differ_2e60be2014891e3e081089061ca48033

