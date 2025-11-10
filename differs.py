from utils import *
from constants import *
from dsl import *

# NOTE Variable I in differ refers to dynamic grid
# in run, initially I, but then any grid in t_n

# def differ_p_g_iz(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
def differ_fc9e44c913711da609a9e25126b4b296(S, I, C):
    x1 = identity(p_g)
    x2 = x1(I)
    x3 = x1(C)
    x4 = difference_tuple(x2, x3)
    x5 = size(x4)
    x6 = get_nth_t(x4, F0)
    x7 = astuple(x5, x6)
    return x7


# def differ_p_g_zo(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
def differ_c59e6ae069a9205b311cf67a15473d64(S, I, C):
    x1 = identity(p_g)
    x2 = x1(I)
    x3 = x1(C)
    x4 = difference_tuple(x3, x2)
    x5 = size(x4)
    x6 = get_nth_t(x4, F0)
    x7 = astuple(x5, x6)
    return x7


# def differ_o_g_size_iz(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
def differ_d50e4f6db9fab7b53f413af7de3a35da(S, I, C):
    x1 = rbind(o_g, R5)
    x2 = x1(I)
    x3 = x1(C)
    x4 = rbind(sizefilter, ONE)
    x5 = x4(x2)
    x6 = x4(x3)
    x7 = difference(x5, x6)
    x8 = size(x7)
    x9 = get_nth_f(x7, F0)
    x10 = astuple(x8, x9)
    return x10


# def differ_o_g_size_zo(I: 'Grid', O: 'Grid', flags: 'Flags') -> 'Integer':
def differ_f4a4346405e974b919a4b5a52f28e40c(S, I, C):
    x1 = rbind(o_g, R5)
    x2 = x1(I)
    x3 = x1(C)
    x4 = rbind(sizefilter, ONE)
    x5 = x4(x2)
    x6 = x4(x3)
    x7 = difference(x6, x5)
    x8 = size(x7)
    x9 = get_nth_f(x7, F0)
    x10 = astuple(x8, x9)
    return x10


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

