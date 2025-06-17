from dsl import *
from constants import *


def solve_80af3007(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = upscale_t(x3, THREE)
    if x == 4:
        return x4
    x5 = hconcat(x3, x3)
    if x == 5:
        return x5
    x6 = hconcat(x5, x3)
    if x == 6:
        return x6
    x7 = vconcat(x6, x6)
    if x == 7:
        return x7
    x8 = vconcat(x7, x6)
    if x == 8:
        return x8
    x9 = cellwise(x4, x8, ZERO)
    if x == 9:
        return x9
    O = downscale(x9, THREE)
    return O

def solve_794b24be(S, I, x=0):
    x1 = canvas(ZERO, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, ONE)
    if x == 2:
        return x2
    x3 = size_f(x2)
    if x == 3:
        return x3
    x4 = equality(x3, FOUR)
    if x == 4:
        return x4
    x5 = decrement(x3)
    if x == 5:
        return x5
    x6 = tojvec(x5)
    if x == 6:
        return x6
    x7 = connect(ORIGIN, x6)
    if x == 7:
        return x7
    x8 = insert(UNITY, x7)
    if x == 8:
        return x8
    x9 = branch(x4, x8, x7)
    if x == 9:
        return x9
    O = fill(x1, TWO, x9)
    return O

def solve_7c008303(S, I, x=0):
    x1 = replace(I, THREE, ZERO)
    if x == 1:
        return x1
    x2 = replace(x1, EIGHT, ZERO)
    if x == 2:
        return x2
    x3 = compress(x2)
    if x == 3:
        return x3
    x4 = upscale_t(x3, THREE)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, THREE)
    if x == 5:
        return x5
    x6 = subgrid(x5, I)
    if x == 6:
        return x6
    x7 = f_ofcolor(x6, ZERO)
    if x == 7:
        return x7
    O = fill(x4, ZERO, x7)
    return O

def solve_56dc2b01(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = recolor_i(EIGHT, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = colorfilter(x3, THREE)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = gravitate(x1, x5)
    if x == 6:
        return x6
    x7 = sign(x6)
    if x == 7:
        return x7
    x8 = gravitate(x5, x1)
    if x == 8:
        return x8
    x9 = get_nth_f(x8, F0)
    if x == 9:
        return x9
    x10 = equality(x9, ZERO)
    if x == 10:
        return x10
    x11 = branch(x10, width_f, height_f)
    if x == 11:
        return x11
    x12 = x11(x5)
    if x == 12:
        return x12
    x13 = multiply(x7, x12)
    if x == 13:
        return x13
    x14 = crement(x13)
    if x == 14:
        return x14
    x15 = shift(x2, x14)
    if x == 15:
        return x15
    x16 = paint(I, x15)
    if x == 16:
        return x16
    O = move(x16, x5, x8)
    return O

def solve_3618c87e(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    O = move(I, x3, TWO_BY_ZERO)
    return O

def solve_045e512c(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = lbind(mapply, x3)
    if x == 4:
        return x4
    x5 = double(TEN)
    if x == 5:
        return x5
    x6 = interval(FOUR, x5, FOUR)
    if x == 6:
        return x6
    x7 = rbind(apply, x6)
    if x == 7:
        return x7
    x8 = lbind(rbind, multiply)
    if x == 8:
        return x8
    x9 = lbind(position, x2)
    if x == 9:
        return x9
    x10 = chain(x7, x8, x9)
    if x == 10:
        return x10
    x11 = compose(x4, x10)
    if x == 11:
        return x11
    x12 = fork(recolor_o, color, x11)
    if x == 12:
        return x12
    x13 = remove_f(x2, x1)
    if x == 13:
        return x13
    x14 = mapply(x12, x13)
    if x == 14:
        return x14
    O = paint(I, x14)
    return O

def solve_4258a5f9(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = mapply(neighbors, x1)
    if x == 2:
        return x2
    O = fill(I, ONE, x2)
    return O

def solve_54d82841(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    x3 = lbind(astuple, x2)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, L1)
    if x == 4:
        return x4
    x5 = compose(x4, center)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = apply(x5, x6)
    if x == 7:
        return x7
    x8 = apply(x3, x7)
    if x == 8:
        return x8
    O = fill(I, FOUR, x8)
    return O

def solve_f8a8fe49(S, I, x=0):
    x1 = replace(I, FIVE, ZERO)
    if x == 1:
        return x1
    x2 = compose(normalize, asobject)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = colorfilter(x3, TWO)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = portrait_f(x5)
    if x == 6:
        return x6
    x7 = branch(x6, hsplit, vsplit)
    if x == 7:
        return x7
    x8 = rbind(mir_rot_t, R2)
    if x == 8:
        return x8
    x9 = rbind(mir_rot_t, R0)
    if x == 9:
        return x9
    x10 = branch(x6, x8, x9)
    if x == 10:
        return x10
    x11 = f_ofcolor(I, TWO)
    if x == 11:
        return x11
    x12 = subgrid(x11, I)
    if x == 12:
        return x12
    x13 = trim(x12)
    if x == 13:
        return x13
    x14 = x10(x13)
    if x == 14:
        return x14
    x15 = x7(x14, TWO)
    if x == 15:
        return x15
    x16 = apply(x2, x15)
    if x == 16:
        return x16
    x17 = get_nth_t(x16, L1)
    if x == 17:
        return x17
    x18 = corner(x11, R0)
    if x == 18:
        return x18
    x19 = increment(x18)
    if x == 19:
        return x19
    x20 = shift(x17, x19)
    if x == 20:
        return x20
    x21 = branch(x6, tojvec, toivec)
    if x == 21:
        return x21
    x22 = compose(x21, increment)
    if x == 22:
        return x22
    x23 = branch(x6, width_f, height_f)
    if x == 23:
        return x23
    x24 = x23(x17)
    if x == 24:
        return x24
    x25 = x22(x24)
    if x == 25:
        return x25
    x26 = invert(x25)
    if x == 26:
        return x26
    x27 = shift(x20, x26)
    if x == 27:
        return x27
    x28 = paint(x1, x27)
    if x == 28:
        return x28
    x29 = get_nth_f(x16, F0)
    if x == 29:
        return x29
    x30 = shift(x29, x19)
    if x == 30:
        return x30
    x31 = double(x24)
    if x == 31:
        return x31
    x32 = x22(x31)
    if x == 32:
        return x32
    x33 = shift(x30, x32)
    if x == 33:
        return x33
    O = paint(x28, x33)
    return O

def solve_c9e6f938(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    O = hconcat(I, x1)
    return O

def solve_e509e548(S, I, x=0):
    x1 = replace(I, THREE, SIX)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = lbind(contained, THREE)
    if x == 3:
        return x3
    x4 = rbind(subgrid, I)
    if x == 4:
        return x4
    x5 = chain(palette_t, trim, x4)
    if x == 5:
        return x5
    x6 = compose(x3, x5)
    if x == 6:
        return x6
    x7 = mfilter_f(x2, x6)
    if x == 7:
        return x7
    x8 = fill(x1, TWO, x7)
    if x == 8:
        return x8
    x9 = fork(add, height_f, width_f)
    if x == 9:
        return x9
    x10 = compose(decrement, x9)
    if x == 10:
        return x10
    x11 = fork(equality, size, x10)
    if x == 11:
        return x11
    x12 = mfilter_f(x2, x11)
    if x == 12:
        return x12
    O = fill(x8, ONE, x12)
    return O

def solve_40853293(S, I, x=0):
    x1 = fork(recolor_i, color, backdrop)
    if x == 1:
        return x1
    x2 = partition(I)
    if x == 2:
        return x2
    x3 = apply(x1, x2)
    if x == 3:
        return x3
    x4 = mfilter(x3, hline_i)
    if x == 4:
        return x4
    x5 = paint(I, x4)
    if x == 5:
        return x5
    x6 = mfilter(x3, vline_i)
    if x == 6:
        return x6
    O = paint(x5, x6)
    return O

def solve_8403a5d5(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = color(x2)
    if x == 3:
        return x3
    x4 = asindices(I)
    if x == 4:
        return x4
    x5 = col_row(x2, R2)
    if x == 5:
        return x5
    x6 = interval(x5, TEN, TWO)
    if x == 6:
        return x6
    x7 = rbind(contained, x6)
    if x == 7:
        return x7
    x8 = rbind(get_nth_f, L1)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = sfilter(x4, x9)
    if x == 10:
        return x10
    x11 = fill(I, x3, x10)
    if x == 11:
        return x11
    x12 = increment(x5)
    if x == 12:
        return x12
    x13 = interval(x12, TEN, FOUR)
    if x == 13:
        return x13
    x14 = apply(tojvec, x13)
    if x == 14:
        return x14
    x15 = fill(x11, FIVE, x14)
    if x == 15:
        return x15
    x16 = lbind(astuple, NINE)
    if x == 16:
        return x16
    x17 = add(x5, THREE)
    if x == 17:
        return x17
    x18 = interval(x17, TEN, FOUR)
    if x == 18:
        return x18
    x19 = apply(x16, x18)
    if x == 19:
        return x19
    O = fill(x15, FIVE, x19)
    return O

def solve_cdecee7f(S, I, x=0):
    x1 = rbind(canvas, UNITY)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = rbind(col_row, R2)
    if x == 3:
        return x3
    x4 = order(x2, x3)
    if x == 4:
        return x4
    x5 = apply(color, x4)
    if x == 5:
        return x5
    x6 = apply(x1, x5)
    if x == 6:
        return x6
    x7 = merge_t(x6)
    if x == 7:
        return x7
    x8 = mir_rot_t(x7, R1)
    if x == 8:
        return x8
    x9 = size_f(x2)
    if x == 9:
        return x9
    x10 = subtract(NINE, x9)
    if x == 10:
        return x10
    x11 = astuple(ONE, x10)
    if x == 11:
        return x11
    x12 = canvas(ZERO, x11)
    if x == 12:
        return x12
    x13 = hconcat(x8, x12)
    if x == 13:
        return x13
    x14 = hsplit(x13, THREE)
    if x == 14:
        return x14
    x15 = merge_t(x14)
    if x == 15:
        return x15
    x16 = astuple(ONE, THREE)
    if x == 16:
        return x16
    x17 = crop(x15, ORIGIN, x16)
    if x == 17:
        return x17
    x18 = crop(x15, DOWN, x16)
    if x == 18:
        return x18
    x19 = mir_rot_t(x18, R2)
    if x == 19:
        return x19
    x20 = vconcat(x17, x19)
    if x == 20:
        return x20
    x21 = crop(x15, TWO_BY_ZERO, x16)
    if x == 21:
        return x21
    O = vconcat(x20, x21)
    return O

def solve_952a094c(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    x4 = cover(I, x3)
    if x == 4:
        return x4
    x5 = rbind(get_arg_rank, F0)
    if x == 5:
        return x5
    x6 = lbind(x5, x2)
    if x == 6:
        return x6
    x7 = lbind(rbind, manhattan)
    if x == 7:
        return x7
    x8 = chain(x6, x7, initset)
    if x == 8:
        return x8
    x9 = compose(color, x8)
    if x == 9:
        return x9
    x10 = fork(astuple, x9, identity)
    if x == 10:
        return x10
    x11 = get_arg_rank_f(x1, size, F0)
    if x == 11:
        return x11
    x12 = outbox(x11)
    if x == 12:
        return x12
    x13 = corners(x12)
    if x == 13:
        return x13
    x14 = apply(x10, x13)
    if x == 14:
        return x14
    O = paint(x4, x14)
    return O

def solve_6d0aefbc(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    O = hconcat(I, x1)
    return O

def solve_36fdfd69(S, I, x=0):
    x1 = upscale_t(I, TWO)
    if x == 1:
        return x1
    x2 = o_g(x1, R7)
    if x == 2:
        return x2
    x3 = colorfilter(x2, TWO)
    if x == 3:
        return x3
    x4 = product(x3, x3)
    if x == 4:
        return x4
    x5 = lbind(greater, FIVE)
    if x == 5:
        return x5
    x6 = rbind(get_nth_f, F0)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, L1)
    if x == 7:
        return x7
    x8 = fork(manhattan, x6, x7)
    if x == 8:
        return x8
    x9 = compose(x5, x8)
    if x == 9:
        return x9
    x10 = sfilter_f(x4, x9)
    if x == 10:
        return x10
    x11 = apply(merge, x10)
    if x == 11:
        return x11
    x12 = mapply(delta, x11)
    if x == 12:
        return x12
    x13 = fill(x1, FOUR, x12)
    if x == 13:
        return x13
    x14 = merge(x3)
    if x == 14:
        return x14
    x15 = paint(x13, x14)
    if x == 15:
        return x15
    O = downscale(x15, TWO)
    return O

def solve_88a10436(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = colorfilter(x1, FIVE)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = get_nth_f(x3, F0)
    if x == 4:
        return x4
    x5 = normalize(x4)
    if x == 5:
        return x5
    x6 = get_nth_f(x2, F0)
    if x == 6:
        return x6
    x7 = center(x6)
    if x == 7:
        return x7
    x8 = shift(x5, x7)
    if x == 8:
        return x8
    x9 = shift(x8, NEG_UNITY)
    if x == 9:
        return x9
    O = paint(I, x9)
    return O

def solve_543a7ed5(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = colorfilter(x1, SIX)
    if x == 2:
        return x2
    x3 = mapply(outbox, x2)
    if x == 3:
        return x3
    x4 = fill(I, THREE, x3)
    if x == 4:
        return x4
    x5 = mapply(delta, x2)
    if x == 5:
        return x5
    O = fill(x4, FOUR, x5)
    return O

def solve_a3df8b1e(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = shoot(x2, UP_RIGHT)
    if x == 3:
        return x3
    x4 = fill(I, ONE, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(x4, ONE)
    if x == 5:
        return x5
    x6 = corner(x5, R1)
    if x == 6:
        return x6
    x7 = shoot(x6, NEG_UNITY)
    if x == 7:
        return x7
    x8 = fill(x4, ONE, x7)
    if x == 8:
        return x8
    x9 = o_g(x8, R7)
    if x == 9:
        return x9
    x10 = get_nth_f(x9, F0)
    if x == 10:
        return x10
    x11 = subgrid(x10, x8)
    if x == 11:
        return x11
    x12 = shape_t(x11)
    if x == 12:
        return x12
    x13 = subtract(x12, DOWN)
    if x == 13:
        return x13
    x14 = crop(x11, DOWN, x13)
    if x == 14:
        return x14
    x15 = vconcat(x14, x14)
    if x == 15:
        return x15
    x16 = vconcat(x15, x15)
    if x == 16:
        return x16
    x17 = vconcat(x16, x16)
    if x == 17:
        return x17
    x18 = mir_rot_f(x17, R0)
    if x == 18:
        return x18
    x19 = shape_t(I)
    if x == 19:
        return x19
    x20 = crop(x18, ORIGIN, x19)
    if x == 20:
        return x20
    O = mir_rot_f(x20, R0)
    return O

def solve_ba97ae07(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = totuple(x1)
    if x == 2:
        return x2
    x3 = apply(color, x2)
    if x == 3:
        return x3
    x4 = get_common_rank_t(x3, F0)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, x4)
    if x == 5:
        return x5
    x6 = backdrop(x5)
    if x == 6:
        return x6
    O = fill(I, x4, x6)
    return O

def solve_94f9d214(S, I, x=0):
    x1 = astuple(FOUR, FOUR)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = tophalf(I)
    if x == 3:
        return x3
    x4 = f_ofcolor(x3, ZERO)
    if x == 4:
        return x4
    x5 = bottomhalf(I)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, ZERO)
    if x == 6:
        return x6
    x7 = intersection(x4, x6)
    if x == 7:
        return x7
    O = fill(x2, TWO, x7)
    return O

def solve_2013d3e2(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = lefthalf(x3)
    if x == 4:
        return x4
    O = tophalf(x4)
    return O

def solve_150deff5(S, I, x=0):
    x1 = canvas(FIVE, TWO_BY_TWO)
    if x == 1:
        return x1
    x2 = asobject(x1)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = occurrences(I, x2)
    if x == 4:
        return x4
    x5 = mapply(x3, x4)
    if x == 5:
        return x5
    x6 = fill(I, EIGHT, x5)
    if x == 6:
        return x6
    x7 = astuple(TWO, ONE)
    if x == 7:
        return x7
    x8 = canvas(EIGHT, x7)
    if x == 8:
        return x8
    x9 = canvas(FIVE, UNITY)
    if x == 9:
        return x9
    x10 = vconcat(x8, x9)
    if x == 10:
        return x10
    x11 = asobject(x10)
    if x == 11:
        return x11
    x12 = lbind(shift, x11)
    if x == 12:
        return x12
    x13 = occurrences(x6, x11)
    if x == 13:
        return x13
    x14 = mapply(x12, x13)
    if x == 14:
        return x14
    x15 = fill(x6, TWO, x14)
    if x == 15:
        return x15
    x16 = astuple(ONE, THREE)
    if x == 16:
        return x16
    x17 = canvas(FIVE, x16)
    if x == 17:
        return x17
    x18 = asobject(x17)
    if x == 18:
        return x18
    x19 = lbind(shift, x18)
    if x == 19:
        return x19
    x20 = occurrences(x15, x18)
    if x == 20:
        return x20
    x21 = mapply(x19, x20)
    if x == 21:
        return x21
    x22 = fill(x15, TWO, x21)
    if x == 22:
        return x22
    x23 = mir_rot_t(x10, R0)
    if x == 23:
        return x23
    x24 = asobject(x23)
    if x == 24:
        return x24
    x25 = lbind(shift, x24)
    if x == 25:
        return x25
    x26 = occurrences(x22, x24)
    if x == 26:
        return x26
    x27 = mapply(x25, x26)
    if x == 27:
        return x27
    x28 = fill(x22, TWO, x27)
    if x == 28:
        return x28
    x29 = mir_rot_t(x10, R1)
    if x == 29:
        return x29
    x30 = asobject(x29)
    if x == 30:
        return x30
    x31 = lbind(shift, x30)
    if x == 31:
        return x31
    x32 = occurrences(x28, x30)
    if x == 32:
        return x32
    x33 = mapply(x31, x32)
    if x == 33:
        return x33
    x34 = fill(x28, TWO, x33)
    if x == 34:
        return x34
    x35 = mir_rot_t(x29, R2)
    if x == 35:
        return x35
    x36 = asobject(x35)
    if x == 36:
        return x36
    x37 = lbind(shift, x36)
    if x == 37:
        return x37
    x38 = occurrences(x34, x36)
    if x == 38:
        return x38
    x39 = mapply(x37, x38)
    if x == 39:
        return x39
    O = fill(x34, TWO, x39)
    return O

def solve_22eb0ac0(S, I, x=0):
    x1 = fork(recolor_i, color, backdrop)
    if x == 1:
        return x1
    x2 = fgpartition(I)
    if x == 2:
        return x2
    x3 = apply(x1, x2)
    if x == 3:
        return x3
    x4 = mfilter_f(x3, hline_o)
    if x == 4:
        return x4
    O = paint(I, x4)
    return O

def solve_60b61512(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = mapply(delta, x1)
    if x == 2:
        return x2
    O = fill(I, SEVEN, x2)
    return O

def solve_22168020(S, I, x=0):
    x1 = lbind(prapply, connect)
    if x == 1:
        return x1
    x2 = lbind(f_ofcolor, I)
    if x == 2:
        return x2
    x3 = fork(x1, x2, x2)
    if x == 3:
        return x3
    x4 = compose(merge, x3)
    if x == 4:
        return x4
    x5 = fork(recolor_i, identity, x4)
    if x == 5:
        return x5
    x6 = palette_t(I)
    if x == 6:
        return x6
    x7 = remove(ZERO, x6)
    if x == 7:
        return x7
    x8 = mapply(x5, x7)
    if x == 8:
        return x8
    O = paint(I, x8)
    return O

def solve_8e1813be(S, I, x=0):
    x1 = replace(I, FIVE, ZERO)
    if x == 1:
        return x1
    x2 = o_g(x1, R7)
    if x == 2:
        return x2
    x3 = get_nth_f(x2, F0)
    if x == 3:
        return x3
    x4 = vline_o(x3)
    if x == 4:
        return x4
    x5 = rbind(mir_rot_t, R1)
    if x == 5:
        return x5
    x6 = branch(x4, x5, identity)
    if x == 6:
        return x6
    x7 = x6(x1)
    if x == 7:
        return x7
    x8 = o_g(x7, R7)
    if x == 8:
        return x8
    x9 = rbind(col_row, R1)
    if x == 9:
        return x9
    x10 = order(x8, x9)
    if x == 10:
        return x10
    x11 = apply(color, x10)
    if x == 11:
        return x11
    x12 = dedupe(x11)
    if x == 12:
        return x12
    x13 = size_t(x12)
    if x == 13:
        return x13
    x14 = rbind(repeat, x13)
    if x == 14:
        return x14
    x15 = apply(x14, x12)
    if x == 15:
        return x15
    O = x6(x15)
    return O

def solve_9565186b(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = canvas(FIVE, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R4)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, F0)
    if x == 4:
        return x4
    O = paint(x2, x4)
    return O

def solve_746b3537(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = chain(size, dedupe, x1)
    if x == 2:
        return x2
    x3 = x2(I)
    if x == 3:
        return x3
    x4 = equality(x3, ONE)
    if x == 4:
        return x4
    x5 = rbind(mir_rot_t, R1)
    if x == 5:
        return x5
    x6 = branch(x4, x5, identity)
    if x == 6:
        return x6
    x7 = x6(I)
    if x == 7:
        return x7
    x8 = o_g(x7, R4)
    if x == 8:
        return x8
    x9 = rbind(col_row, R2)
    if x == 9:
        return x9
    x10 = order(x8, x9)
    if x == 10:
        return x10
    x11 = apply(color, x10)
    if x == 11:
        return x11
    x12 = repeat(x11, ONE)
    if x == 12:
        return x12
    O = x6(x12)
    return O

def solve_1e32b0e9(S, I, x=0):
    x1 = asobject(I)
    if x == 1:
        return x1
    x2 = palette_f(x1)
    if x == 2:
        return x2
    x3 = height_t(I)
    if x == 3:
        return x3
    x4 = subtract(x3, TWO)
    if x == 4:
        return x4
    x5 = divide(x4, THREE)
    if x == 5:
        return x5
    x6 = astuple(x5, x5)
    if x == 6:
        return x6
    x7 = crop(I, ORIGIN, x6)
    if x == 7:
        return x7
    x8 = partition(x7)
    if x == 8:
        return x8
    x9 = matcher(color, ZERO)
    if x == 9:
        return x9
    x10 = compose(flip, x9)
    if x == 10:
        return x10
    x11 = extract(x8, x10)
    if x == 11:
        return x11
    x12 = palette_f(x11)
    if x == 12:
        return x12
    x13 = difference(x2, x12)
    if x == 13:
        return x13
    x14 = get_color_rank_t(I, F0)
    if x == 14:
        return x14
    x15 = initset(x14)
    if x == 15:
        return x15
    x16 = difference(x13, x15)
    if x == 16:
        return x16
    x17 = get_nth_f(x16, F0)
    if x == 17:
        return x17
    x18 = lbind(shift, x11)
    if x == 18:
        return x18
    x19 = lbind(multiply, x5)
    if x == 19:
        return x19
    x20 = rbind(get_nth_f, F0)
    if x == 20:
        return x20
    x21 = interval(ZERO, THREE, ONE)
    if x == 21:
        return x21
    x22 = product(x21, x21)
    if x == 22:
        return x22
    x23 = totuple(x22)
    if x == 23:
        return x23
    x24 = apply(x20, x23)
    if x == 24:
        return x24
    x25 = apply(x19, x24)
    if x == 25:
        return x25
    x26 = papply(add, x25, x24)
    if x == 26:
        return x26
    x27 = rbind(get_nth_f, L1)
    if x == 27:
        return x27
    x28 = apply(x27, x23)
    if x == 28:
        return x28
    x29 = apply(x19, x28)
    if x == 29:
        return x29
    x30 = papply(add, x29, x28)
    if x == 30:
        return x30
    x31 = papply(astuple, x26, x30)
    if x == 31:
        return x31
    x32 = mapply(x18, x31)
    if x == 32:
        return x32
    O = underfill(I, x17, x32)
    return O

def solve_941d9a10(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = apply(toindices, x2)
    if x == 3:
        return x3
    x4 = lbind(extract, x3)
    if x == 4:
        return x4
    x5 = lbind(lbind, contained)
    if x == 5:
        return x5
    x6 = compose(x4, x5)
    if x == 6:
        return x6
    x7 = x6(ORIGIN)
    if x == 7:
        return x7
    x8 = fill(I, ONE, x7)
    if x == 8:
        return x8
    x9 = shape_t(I)
    if x == 9:
        return x9
    x10 = decrement(x9)
    if x == 10:
        return x10
    x11 = x6(x10)
    if x == 11:
        return x11
    x12 = fill(x8, THREE, x11)
    if x == 12:
        return x12
    x13 = astuple(FIVE, FIVE)
    if x == 13:
        return x13
    x14 = x6(x13)
    if x == 14:
        return x14
    O = fill(x12, TWO, x14)
    return O

def solve_a78176bb(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = remove(ZERO, x1)
    if x == 2:
        return x2
    x3 = other_f(x2, FIVE)
    if x == 3:
        return x3
    x4 = rbind(shoot, UNITY)
    if x == 4:
        return x4
    x5 = rbind(shoot, NEG_UNITY)
    if x == 5:
        return x5
    x6 = fork(combine, x4, x5)
    if x == 6:
        return x6
    x7 = rbind(add, UP_RIGHT)
    if x == 7:
        return x7
    x8 = rbind(corner, R1)
    if x == 8:
        return x8
    x9 = o_g(I, R5)
    if x == 9:
        return x9
    x10 = colorfilter(x9, FIVE)
    if x == 10:
        return x10
    x11 = lbind(index, I)
    if x == 11:
        return x11
    x12 = compose(x11, x8)
    if x == 12:
        return x12
    x13 = matcher(x12, FIVE)
    if x == 13:
        return x13
    x14 = sfilter_f(x10, x13)
    if x == 14:
        return x14
    x15 = apply(x8, x14)
    if x == 15:
        return x15
    x16 = apply(x7, x15)
    if x == 16:
        return x16
    x17 = mapply(x6, x16)
    if x == 17:
        return x17
    x18 = rbind(add, DOWN_LEFT)
    if x == 18:
        return x18
    x19 = rbind(corner, R2)
    if x == 19:
        return x19
    x20 = difference(x10, x14)
    if x == 20:
        return x20
    x21 = apply(x19, x20)
    if x == 21:
        return x21
    x22 = apply(x18, x21)
    if x == 22:
        return x22
    x23 = mapply(x6, x22)
    if x == 23:
        return x23
    x24 = combine_f(x17, x23)
    if x == 24:
        return x24
    x25 = fill(I, x3, x24)
    if x == 25:
        return x25
    O = replace(x25, FIVE, ZERO)
    return O

def solve_bbc9ae5d(S, I, x=0):
    x1 = width_t(I)
    if x == 1:
        return x1
    x2 = halve(x1)
    if x == 2:
        return x2
    x3 = vupscale(I, x2)
    if x == 3:
        return x3
    x4 = palette_t(I)
    if x == 4:
        return x4
    x5 = other_f(x4, ZERO)
    if x == 5:
        return x5
    x6 = rbind(shoot, UNITY)
    if x == 6:
        return x6
    x7 = f_ofcolor(x3, x5)
    if x == 7:
        return x7
    x8 = mapply(x6, x7)
    if x == 8:
        return x8
    O = fill(x3, x5, x8)
    return O

def solve_445eab21(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = fork(multiply, height_f, width_f)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x1, x2, F0)
    if x == 3:
        return x3
    x4 = color(x3)
    if x == 4:
        return x4
    O = canvas(x4, TWO_BY_TWO)
    return O

def solve_d43fd935(S, I, x=0):
    x1 = f_ofcolor(I, THREE)
    if x == 1:
        return x1
    x2 = rbind(gravitate, x1)
    if x == 2:
        return x2
    x3 = fork(add, center, x2)
    if x == 3:
        return x3
    x4 = fork(connect, center, x3)
    if x == 4:
        return x4
    x5 = fork(recolor_i, color, x4)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = sizefilter(x6, ONE)
    if x == 7:
        return x7
    x8 = rbind(vmatching, x1)
    if x == 8:
        return x8
    x9 = rbind(hmatching, x1)
    if x == 9:
        return x9
    x10 = fork(either, x8, x9)
    if x == 10:
        return x10
    x11 = sfilter_f(x7, x10)
    if x == 11:
        return x11
    x12 = mapply(x5, x11)
    if x == 12:
        return x12
    O = paint(I, x12)
    return O

def solve_be94b721(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O

def solve_cbded52d(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = compose(color, x1)
    if x == 2:
        return x2
    x3 = compose(center, x1)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, L1)
    if x == 4:
        return x4
    x5 = compose(center, x4)
    if x == 5:
        return x5
    x6 = fork(connect, x3, x5)
    if x == 6:
        return x6
    x7 = chain(initset, center, x6)
    if x == 7:
        return x7
    x8 = fork(recolor_i, x2, x7)
    if x == 8:
        return x8
    x9 = o_g(I, R5)
    if x == 9:
        return x9
    x10 = sizefilter(x9, ONE)
    if x == 10:
        return x10
    x11 = product(x10, x10)
    if x == 11:
        return x11
    x12 = fork(vmatching, x1, x4)
    if x == 12:
        return x12
    x13 = fork(hmatching, x1, x4)
    if x == 13:
        return x13
    x14 = fork(either, x12, x13)
    if x == 14:
        return x14
    x15 = sfilter_f(x11, x14)
    if x == 15:
        return x15
    x16 = mapply(x8, x15)
    if x == 16:
        return x16
    O = paint(I, x16)
    return O

def solve_a8d7556c(S, I, x=0):
    x1 = initset(ORIGIN)
    if x == 1:
        return x1
    x2 = recolor_i(ZERO, x1)
    if x == 2:
        return x2
    x3 = upscale_f(x2, TWO)
    if x == 3:
        return x3
    x4 = lbind(shift, x3)
    if x == 4:
        return x4
    x5 = occurrences(I, x3)
    if x == 5:
        return x5
    x6 = mapply(x4, x5)
    if x == 6:
        return x6
    x7 = fill(I, TWO, x6)
    if x == 7:
        return x7
    x8 = add(SIX, SIX)
    if x == 8:
        return x8
    x9 = astuple(EIGHT, x8)
    if x == 9:
        return x9
    x10 = index(x7, x9)
    if x == 10:
        return x10
    x11 = equality(x10, TWO)
    if x == 11:
        return x11
    x12 = add(x9, DOWN)
    if x == 12:
        return x12
    x13 = initset(x9)
    if x == 13:
        return x13
    x14 = insert(x12, x13)
    if x == 14:
        return x14
    x15 = toobject(x14, I)
    if x == 15:
        return x15
    x16 = toobject(x14, x7)
    if x == 16:
        return x16
    x17 = branch(x11, x15, x16)
    if x == 17:
        return x17
    O = paint(x7, x17)
    return O

def solve_ba26e723(S, I, x=0):
    x1 = f_ofcolor(I, FOUR)
    if x == 1:
        return x1
    x2 = rbind(multiply, THREE)
    if x == 2:
        return x2
    x3 = rbind(divide, THREE)
    if x == 3:
        return x3
    x4 = compose(x2, x3)
    if x == 4:
        return x4
    x5 = fork(equality, identity, x4)
    if x == 5:
        return x5
    x6 = rbind(get_nth_f, L1)
    if x == 6:
        return x6
    x7 = compose(x5, x6)
    if x == 7:
        return x7
    x8 = sfilter_f(x1, x7)
    if x == 8:
        return x8
    O = fill(I, SIX, x8)
    return O

def solve_9aec4887(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, numcolors_f, L1)
    if x == 2:
        return x2
    x3 = other_f(x1, x2)
    if x == 3:
        return x3
    x4 = subgrid(x3, I)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, F0)
    if x == 5:
        return x5
    x6 = rbind(get_arg_rank, L1)
    if x == 6:
        return x6
    x7 = normalize_o(x3)
    if x == 7:
        return x7
    x8 = lbind(x6, x7)
    if x == 8:
        return x8
    x9 = rbind(compose, initset)
    if x == 9:
        return x9
    x10 = lbind(rbind, manhattan)
    if x == 10:
        return x10
    x11 = chain(x9, x10, initset)
    if x == 11:
        return x11
    x12 = chain(x5, x8, x11)
    if x == 12:
        return x12
    x13 = fork(astuple, x12, identity)
    if x == 13:
        return x13
    x14 = normalize_o(x2)
    if x == 14:
        return x14
    x15 = shift(x14, UNITY)
    if x == 15:
        return x15
    x16 = toindices(x15)
    if x == 16:
        return x16
    x17 = apply(x13, x16)
    if x == 17:
        return x17
    x18 = paint(x4, x17)
    if x == 18:
        return x18
    x19 = rbind(mir_rot_f, R2)
    if x == 19:
        return x19
    x20 = fork(combine, identity, x19)
    if x == 20:
        return x20
    x21 = rbind(corner, R0)
    if x == 21:
        return x21
    x22 = rbind(corner, R3)
    if x == 22:
        return x22
    x23 = fork(connect, x21, x22)
    if x == 23:
        return x23
    x24 = x23(x16)
    if x == 24:
        return x24
    x25 = x20(x24)
    if x == 25:
        return x25
    x26 = intersection(x16, x25)
    if x == 26:
        return x26
    O = fill(x18, EIGHT, x26)
    return O

def solve_72ca375d(S, I, x=0):
    x1 = rbind(subgrid, I)
    if x == 1:
        return x1
    x2 = o_g(I, R7)
    if x == 2:
        return x2
    x3 = totuple(x2)
    if x == 3:
        return x3
    x4 = apply(x1, x3)
    if x == 4:
        return x4
    x5 = rbind(mir_rot_t, R2)
    if x == 5:
        return x5
    x6 = apply(x5, x4)
    if x == 6:
        return x6
    x7 = papply(equality, x4, x6)
    if x == 7:
        return x7
    x8 = pair(x4, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_f, L1)
    if x == 9:
        return x9
    x10 = extract(x8, x9)
    if x == 10:
        return x10
    O = get_nth_t(x10, F0)
    return O

def solve_6d58a25d(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = remove_f(x2, x1)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    x5 = color(x4)
    if x == 5:
        return x5
    x6 = col_row(x2, R1)
    if x == 6:
        return x6
    x7 = increment(x6)
    if x == 7:
        return x7
    x8 = rbind(greater, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_f, F0)
    if x == 9:
        return x9
    x10 = compose(x8, x9)
    if x == 10:
        return x10
    x11 = rbind(sfilter, x10)
    if x == 11:
        return x11
    x12 = chain(x11, vfrontier, center)
    if x == 12:
        return x12
    x13 = rbind(vmatching, x2)
    if x == 13:
        return x13
    x14 = rbind(greater, x6)
    if x == 14:
        return x14
    x15 = rbind(col_row, R1)
    if x == 15:
        return x15
    x16 = compose(x14, x15)
    if x == 16:
        return x16
    x17 = fork(both, x13, x16)
    if x == 17:
        return x17
    x18 = sfilter_f(x3, x17)
    if x == 18:
        return x18
    x19 = mapply(x12, x18)
    if x == 19:
        return x19
    O = underfill(I, x5, x19)
    return O

def solve_dc433765(S, I, x=0):
    x1 = f_ofcolor(I, THREE)
    if x == 1:
        return x1
    x2 = recolor_i(THREE, x1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, FOUR)
    if x == 3:
        return x3
    x4 = get_nth_f(x3, F0)
    if x == 4:
        return x4
    x5 = get_nth_f(x1, F0)
    if x == 5:
        return x5
    x6 = subtract(x4, x5)
    if x == 6:
        return x6
    x7 = sign(x6)
    if x == 7:
        return x7
    O = move(I, x2, x7)
    return O

def solve_db93a21d(S, I, x=0):
    x1 = rbind(shoot, DOWN)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, NINE)
    if x == 2:
        return x2
    x3 = mapply(x1, x2)
    if x == 3:
        return x3
    x4 = underfill(I, ONE, x3)
    if x == 4:
        return x4
    x5 = o_g(I, R7)
    if x == 5:
        return x5
    x6 = colorfilter(x5, NINE)
    if x == 6:
        return x6
    x7 = mapply(outbox, x6)
    if x == 7:
        return x7
    x8 = fill(x4, THREE, x7)
    if x == 8:
        return x8
    x9 = power(outbox, TWO)
    if x == 9:
        return x9
    x10 = rbind(greater, ONE)
    if x == 10:
        return x10
    x11 = compose(halve, width_f)
    if x == 11:
        return x11
    x12 = compose(x10, x11)
    if x == 12:
        return x12
    x13 = sfilter_f(x6, x12)
    if x == 13:
        return x13
    x14 = mapply(x9, x13)
    if x == 14:
        return x14
    x15 = fill(x8, THREE, x14)
    if x == 15:
        return x15
    x16 = power(outbox, THREE)
    if x == 16:
        return x16
    x17 = matcher(x11, THREE)
    if x == 17:
        return x17
    x18 = sfilter_f(x6, x17)
    if x == 18:
        return x18
    x19 = mapply(x16, x18)
    if x == 19:
        return x19
    O = fill(x15, THREE, x19)
    return O

def solve_264363fd(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    x3 = cover(I, x2)
    if x == 3:
        return x3
    x4 = rbind(subgrid, x3)
    if x == 4:
        return x4
    x5 = height_f(x2)
    if x == 5:
        return x5
    x6 = equality(x5, FIVE)
    if x == 6:
        return x6
    x7 = branch(x6, UP, RIGHT)
    if x == 7:
        return x7
    x8 = center(x2)
    if x == 8:
        return x8
    x9 = add(x7, x8)
    if x == 9:
        return x9
    x10 = index(I, x9)
    if x == 10:
        return x10
    x11 = lbind(recolor_i, x10)
    if x == 11:
        return x11
    x12 = lbind(mapply, vfrontier)
    if x == 12:
        return x12
    x13 = index(I, x8)
    if x == 13:
        return x13
    x14 = astuple(x13, ORIGIN)
    if x == 14:
        return x14
    x15 = initset(x14)
    if x == 15:
        return x15
    x16 = rbind(occurrences, x15)
    if x == 16:
        return x16
    x17 = compose(x16, x4)
    if x == 17:
        return x17
    x18 = compose(x12, x17)
    if x == 18:
        return x18
    x19 = lbind(mapply, hfrontier)
    if x == 19:
        return x19
    x20 = compose(x19, x17)
    if x == 20:
        return x20
    x21 = branch(x6, x18, x20)
    if x == 21:
        return x21
    x22 = width_f(x2)
    if x == 22:
        return x22
    x23 = equality(x22, FIVE)
    if x == 23:
        return x23
    x24 = branch(x23, x20, x18)
    if x == 24:
        return x24
    x25 = fork(combine, x21, x24)
    if x == 25:
        return x25
    x26 = compose(x11, x25)
    if x == 26:
        return x26
    x27 = fork(paint, x4, x26)
    if x == 27:
        return x27
    x28 = compose(asobject, x27)
    if x == 28:
        return x28
    x29 = rbind(corner, R0)
    if x == 29:
        return x29
    x30 = fork(shift, x28, x29)
    if x == 30:
        return x30
    x31 = o_g(x3, R1)
    if x == 31:
        return x31
    x32 = mapply(x30, x31)
    if x == 32:
        return x32
    x33 = paint(x3, x32)
    if x == 33:
        return x33
    x34 = normalize(x2)
    if x == 34:
        return x34
    x35 = astuple(x6, x23)
    if x == 35:
        return x35
    x36 = add(UNITY, x35)
    if x == 36:
        return x36
    x37 = invert(x36)
    if x == 37:
        return x37
    x38 = shift(x34, x37)
    if x == 38:
        return x38
    x39 = lbind(shift, x38)
    if x == 39:
        return x39
    x40 = occurrences(x3, x15)
    if x == 40:
        return x40
    x41 = mapply(x39, x40)
    if x == 41:
        return x41
    x42 = paint(x33, x41)
    if x == 42:
        return x42
    x43 = get_color_rank_t(x3, F0)
    if x == 43:
        return x43
    x44 = f_ofcolor(x3, x43)
    if x == 44:
        return x44
    O = fill(x42, x43, x44)
    return O

def solve_bb43febb(S, I, x=0):
    x1 = compose(backdrop, inbox)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = colorfilter(x2, FIVE)
    if x == 3:
        return x3
    x4 = mapply(x1, x3)
    if x == 4:
        return x4
    O = fill(I, TWO, x4)
    return O

def solve_68b16354(S, I, x=0):
    O = mir_rot_t(I, R0)
    return O

def solve_af902bf9(S, I, x=0):
    x1 = f_ofcolor(I, FOUR)
    if x == 1:
        return x1
    x2 = prapply(connect, x1, x1)
    if x == 2:
        return x2
    x3 = fork(either, vline_i, hline_i)
    if x == 3:
        return x3
    x4 = mfilter_f(x2, x3)
    if x == 4:
        return x4
    x5 = underfill(I, NEG_ONE, x4)
    if x == 5:
        return x5
    x6 = compose(backdrop, inbox)
    if x == 6:
        return x6
    x7 = o_g(x5, R1)
    if x == 7:
        return x7
    x8 = mapply(x6, x7)
    if x == 8:
        return x8
    x9 = fill(x5, TWO, x8)
    if x == 9:
        return x9
    O = replace(x9, NEG_ONE, ZERO)
    return O

def solve_8e5a5113(S, I, x=0):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = mir_rot_t(x1, R4)
    if x == 2:
        return x2
    x3 = mir_rot_t(x1, R5)
    if x == 3:
        return x3
    x4 = astuple(x2, x3)
    if x == 4:
        return x4
    x5 = apply(asobject, x4)
    if x == 5:
        return x5
    x6 = astuple(FOUR, EIGHT)
    if x == 6:
        return x6
    x7 = apply(tojvec, x6)
    if x == 7:
        return x7
    x8 = mpapply(shift, x5, x7)
    if x == 8:
        return x8
    O = paint(I, x8)
    return O

def solve_8be77c9e(S, I, x=0):
    x1 = mir_rot_t(I, R0)
    if x == 1:
        return x1
    O = vconcat(I, x1)
    return O

def solve_1b60fb0c(S, I, x=0):
    x1 = mir_rot_t(I, R4)
    if x == 1:
        return x1
    x2 = f_ofcolor(x1, ONE)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = neighbors(ORIGIN)
    if x == 4:
        return x4
    x5 = mapply(neighbors, x4)
    if x == 5:
        return x5
    x6 = apply(x3, x5)
    if x == 6:
        return x6
    x7 = f_ofcolor(I, ONE)
    if x == 7:
        return x7
    x8 = lbind(intersection, x7)
    if x == 8:
        return x8
    x9 = compose(size, x8)
    if x == 9:
        return x9
    x10 = get_arg_rank_f(x6, x9, F0)
    if x == 10:
        return x10
    O = underfill(I, TWO, x10)
    return O

def solve_6fa7a44f(S, I, x=0):
    x1 = mir_rot_t(I, R0)
    if x == 1:
        return x1
    O = vconcat(I, x1)
    return O

def solve_7468f01a(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    O = mir_rot_t(x3, R2)
    return O

def solve_98cf29f8(S, I, x=0):
    x1 = fgpartition(I)
    if x == 1:
        return x1
    x2 = fork(multiply, height_f, width_f)
    if x == 2:
        return x2
    x3 = fork(equality, size, x2)
    if x == 3:
        return x3
    x4 = extract(x1, x3)
    if x == 4:
        return x4
    x5 = other_f(x1, x4)
    if x == 5:
        return x5
    x6 = cover(I, x5)
    if x == 6:
        return x6
    x7 = color(x5)
    if x == 7:
        return x7
    x8 = rbind(greater, THREE)
    if x == 8:
        return x8
    x9 = rbind(colorcount_f, x7)
    if x == 9:
        return x9
    x10 = rbind(toobject, I)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, L1)
    if x == 11:
        return x11
    x12 = chain(x10, ineighbors, x11)
    if x == 12:
        return x12
    x13 = chain(x8, x9, x12)
    if x == 13:
        return x13
    x14 = sfilter_f(x5, x13)
    if x == 14:
        return x14
    x15 = outbox(x14)
    if x == 15:
        return x15
    x16 = backdrop(x15)
    if x == 16:
        return x16
    x17 = gravitate(x16, x4)
    if x == 17:
        return x17
    x18 = shift(x16, x17)
    if x == 18:
        return x18
    O = fill(x6, x7, x18)
    return O

def solve_de1cd16c(S, I, x=0):
    x1 = rbind(subgrid, I)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = sizefilter(x2, ONE)
    if x == 3:
        return x3
    x4 = difference(x2, x3)
    if x == 4:
        return x4
    x5 = apply(x1, x4)
    if x == 5:
        return x5
    x6 = get_color_rank_t(I, L1)
    if x == 6:
        return x6
    x7 = rbind(colorcount_t, x6)
    if x == 7:
        return x7
    x8 = get_arg_rank_f(x5, x7, F0)
    if x == 8:
        return x8
    x9 = get_color_rank_t(x8, F0)
    if x == 9:
        return x9
    O = canvas(x9, UNITY)
    return O

def solve_b548a754(S, I, x=0):
    x1 = replace(I, EIGHT, ZERO)
    if x == 1:
        return x1
    x2 = get_color_rank_t(x1, L1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    x5 = backdrop(x4)
    if x == 5:
        return x5
    x6 = fill(I, x2, x5)
    if x == 6:
        return x6
    x7 = replace(x1, x2, ZERO)
    if x == 7:
        return x7
    x8 = get_color_rank_t(x7, L1)
    if x == 8:
        return x8
    x9 = box(x4)
    if x == 9:
        return x9
    O = fill(x6, x8, x9)
    return O

def solve_e5062a87(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = recolor_i(ZERO, x1)
    if x == 2:
        return x2
    x3 = normalize(x2)
    if x == 3:
        return x3
    x4 = lbind(shift, x3)
    if x == 4:
        return x4
    x5 = occurrences(I, x2)
    if x == 5:
        return x5
    x6 = apply(x4, x5)
    if x == 6:
        return x6
    x7 = astuple(TWO, SIX)
    if x == 7:
        return x7
    x8 = astuple(FIVE, ONE)
    if x == 8:
        return x8
    x9 = astuple(ONE, THREE)
    if x == 9:
        return x9
    x10 = initset(x9)
    if x == 10:
        return x10
    x11 = insert(x8, x10)
    if x == 11:
        return x11
    x12 = insert(x7, x11)
    if x == 12:
        return x12
    x13 = rbind(contained, x12)
    if x == 13:
        return x13
    x14 = rbind(corner, R0)
    if x == 14:
        return x14
    x15 = chain(flip, x13, x14)
    if x == 15:
        return x15
    x16 = sfilter_f(x6, x15)
    if x == 16:
        return x16
    x17 = merge_f(x16)
    if x == 17:
        return x17
    x18 = recolor_o(TWO, x17)
    if x == 18:
        return x18
    O = paint(I, x18)
    return O

def solve_46f33fce(S, I, x=0):
    x1 = mir_rot_t(I, R5)
    if x == 1:
        return x1
    x2 = downscale(x1, TWO)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R5)
    if x == 3:
        return x3
    O = upscale_t(x3, FOUR)
    return O

def solve_178fcbfb(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = mapply(vfrontier, x1)
    if x == 2:
        return x2
    x3 = fill(I, TWO, x2)
    if x == 3:
        return x3
    x4 = compose(hfrontier, center)
    if x == 4:
        return x4
    x5 = fork(recolor_i, color, x4)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = colorfilter(x6, TWO)
    if x == 7:
        return x7
    x8 = difference(x6, x7)
    if x == 8:
        return x8
    x9 = mapply(x5, x8)
    if x == 9:
        return x9
    O = paint(x3, x9)
    return O

def solve_7b7f7511(S, I, x=0):
    x1 = portrait_t(I)
    if x == 1:
        return x1
    x2 = branch(x1, tophalf, lefthalf)
    if x == 2:
        return x2
    O = x2(I)
    return O

def solve_5521c0d9(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = cover(I, x2)
    if x == 3:
        return x3
    x4 = chain(toivec, invert, height_f)
    if x == 4:
        return x4
    x5 = fork(shift, identity, x4)
    if x == 5:
        return x5
    x6 = mapply(x5, x1)
    if x == 6:
        return x6
    O = paint(x3, x6)
    return O

def solve_29ec7d0e(S, I, x=0):
    x1 = partition(I)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = merge(x3)
    if x == 4:
        return x4
    x5 = lbind(shift, x4)
    if x == 5:
        return x5
    x6 = height_t(I)
    if x == 6:
        return x6
    x7 = decrement(x6)
    if x == 7:
        return x7
    x8 = tojvec(x7)
    if x == 8:
        return x8
    x9 = astuple(x6, ONE)
    if x == 9:
        return x9
    x10 = crop(I, x8, x9)
    if x == 10:
        return x10
    x11 = asobject(x10)
    if x == 11:
        return x11
    x12 = vperiod(x11)
    if x == 12:
        return x12
    x13 = width_t(I)
    if x == 13:
        return x13
    x14 = decrement(x13)
    if x == 14:
        return x14
    x15 = toivec(x14)
    if x == 15:
        return x15
    x16 = astuple(ONE, x13)
    if x == 16:
        return x16
    x17 = crop(I, x15, x16)
    if x == 17:
        return x17
    x18 = asobject(x17)
    if x == 18:
        return x18
    x19 = hperiod(x18)
    if x == 19:
        return x19
    x20 = astuple(x12, x19)
    if x == 20:
        return x20
    x21 = lbind(multiply, x20)
    if x == 21:
        return x21
    x22 = neighbors(ORIGIN)
    if x == 22:
        return x22
    x23 = mapply(neighbors, x22)
    if x == 23:
        return x23
    x24 = apply(x21, x23)
    if x == 24:
        return x24
    x25 = mapply(x5, x24)
    if x == 25:
        return x25
    O = paint(I, x25)
    return O

def solve_6cf79266(S, I, x=0):
    x1 = astuple(ZERO, ORIGIN)
    if x == 1:
        return x1
    x2 = initset(x1)
    if x == 2:
        return x2
    x3 = upscale_f(x2, THREE)
    if x == 3:
        return x3
    x4 = toindices(x3)
    if x == 4:
        return x4
    x5 = lbind(shift, x4)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, ZERO)
    if x == 6:
        return x6
    x7 = rbind(difference, x6)
    if x == 7:
        return x7
    x8 = chain(size, x7, x5)
    if x == 8:
        return x8
    x9 = matcher(x8, ZERO)
    if x == 9:
        return x9
    x10 = lbind(add, NEG_UNITY)
    if x == 10:
        return x10
    x11 = chain(flip, x9, x10)
    if x == 11:
        return x11
    x12 = fork(both, x9, x11)
    if x == 12:
        return x12
    x13 = sfilter_f(x6, x12)
    if x == 13:
        return x13
    x14 = mapply(x5, x13)
    if x == 14:
        return x14
    O = fill(I, ONE, x14)
    return O

def solve_97a05b5b(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = lbind(lbind, shift)
    if x == 4:
        return x4
    x5 = compose(x4, normalize)
    if x == 5:
        return x5
    x6 = lbind(rbind, subtract)
    if x == 6:
        return x6
    x7 = rbind(corner, R0)
    if x == 7:
        return x7
    x8 = compose(x6, x7)
    if x == 8:
        return x8
    x9 = lbind(recolor_o, ZERO)
    if x == 9:
        return x9
    x10 = rbind(get_nth_f, F0)
    if x == 10:
        return x10
    x11 = matcher(x10, TWO)
    if x == 11:
        return x11
    x12 = compose(flip, x11)
    if x == 12:
        return x12
    x13 = rbind(sfilter, x12)
    if x == 13:
        return x13
    x14 = compose(x9, x13)
    if x == 14:
        return x14
    x15 = rbind(sfilter, x11)
    if x == 15:
        return x15
    x16 = fork(combine, x14, x15)
    if x == 16:
        return x16
    x17 = chain(x8, x16, normalize)
    if x == 17:
        return x17
    x18 = compose(positive, size)
    if x == 18:
        return x18
    x19 = switch(x3, TWO, ZERO)
    if x == 19:
        return x19
    x20 = o_g(x19, R7)
    if x == 20:
        return x20
    x21 = apply(toindices, x20)
    if x == 21:
        return x21
    x22 = lbind(sfilter, x21)
    if x == 22:
        return x22
    x23 = lbind(lbind, contained)
    if x == 23:
        return x23
    x24 = chain(x18, x22, x23)
    if x == 24:
        return x24
    x25 = rbind(sfilter, x24)
    if x == 25:
        return x25
    x26 = lbind(occurrences, x19)
    if x == 26:
        return x26
    x27 = chain(x26, x16, normalize)
    if x == 27:
        return x27
    x28 = compose(x25, x27)
    if x == 28:
        return x28
    x29 = chain(size, x10, x22)
    if x == 29:
        return x29
    x30 = compose(x29, x23)
    if x == 30:
        return x30
    x31 = rbind(compose, x30)
    if x == 31:
        return x31
    x32 = lbind(rbind, equality)
    if x == 32:
        return x32
    x33 = rbind(colorcount_f, TWO)
    if x == 33:
        return x33
    x34 = chain(x31, x32, x33)
    if x == 34:
        return x34
    x35 = fork(sfilter, x28, x34)
    if x == 35:
        return x35
    x36 = fork(apply, x17, x35)
    if x == 36:
        return x36
    x37 = fork(mapply, x5, x36)
    if x == 37:
        return x37
    x38 = rbind(get_nth_f, L1)
    if x == 38:
        return x38
    x39 = fork(compose, x10, x38)
    if x == 39:
        return x39
    x40 = rbind(mir_rot_f, R3)
    if x == 40:
        return x40
    x41 = rbind(mir_rot_f, R1)
    if x == 41:
        return x41
    x42 = astuple(x40, x41)
    if x == 42:
        return x42
    x43 = rbind(mir_rot_f, R0)
    if x == 43:
        return x43
    x44 = rbind(mir_rot_f, R2)
    if x == 44:
        return x44
    x45 = astuple(x43, x44)
    if x == 45:
        return x45
    x46 = combine(x42, x45)
    if x == 46:
        return x46
    x47 = product(x46, x46)
    if x == 47:
        return x47
    x48 = apply(x39, x47)
    if x == 48:
        return x48
    x49 = lbind(rapply, x48)
    if x == 49:
        return x49
    x50 = rbind(greater, ONE)
    if x == 50:
        return x50
    x51 = compose(x50, numcolors_f)
    if x == 51:
        return x51
    x52 = sfilter_f(x1, x51)
    if x == 52:
        return x52
    x53 = mapply(x49, x52)
    if x == 53:
        return x53
    x54 = mapply(x37, x53)
    if x == 54:
        return x54
    x55 = paint(x3, x54)
    if x == 55:
        return x55
    x56 = fork(apply, x17, x27)
    if x == 56:
        return x56
    x57 = fork(mapply, x5, x56)
    if x == 57:
        return x57
    x58 = lbind(remove, TWO)
    if x == 58:
        return x58
    x59 = palette_t(x54)
    if x == 59:
        return x59
    x60 = x58(x59)
    if x == 60:
        return x60
    x61 = rbind(contained, x60)
    if x == 61:
        return x61
    x62 = chain(x10, x58, palette_f)
    if x == 62:
        return x62
    x63 = chain(flip, x61, x62)
    if x == 63:
        return x63
    x64 = sfilter_f(x52, x63)
    if x == 64:
        return x64
    x65 = mapply(x49, x64)
    if x == 65:
        return x65
    x66 = mapply(x57, x65)
    if x == 66:
        return x66
    O = paint(x55, x66)
    return O

def solve_5ad4f10b(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = get_color_rank_t(x3, L1)
    if x == 4:
        return x4
    x5 = replace(x3, x4, ZERO)
    if x == 5:
        return x5
    x6 = color(x2)
    if x == 6:
        return x6
    x7 = replace(x5, x6, x4)
    if x == 7:
        return x7
    x8 = height_t(x7)
    if x == 8:
        return x8
    x9 = divide(x8, THREE)
    if x == 9:
        return x9
    O = downscale(x7, x9)
    return O

def solve_c909285e(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O

def solve_bd4472b8(S, I, x=0):
    x1 = width_t(I)
    if x == 1:
        return x1
    x2 = astuple(TWO, x1)
    if x == 2:
        return x2
    x3 = crop(I, ORIGIN, x2)
    if x == 3:
        return x3
    x4 = tophalf(x3)
    if x == 4:
        return x4
    x5 = mir_rot_t(x4, R1)
    if x == 5:
        return x5
    x6 = hupscale(x5, x1)
    if x == 6:
        return x6
    x7 = repeat(x6, TWO)
    if x == 7:
        return x7
    x8 = merge_t(x7)
    if x == 8:
        return x8
    O = vconcat(x3, x8)
    return O

def solve_aabf363d(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = replace(I, x1, ZERO)
    if x == 2:
        return x2
    x3 = get_color_rank_t(x2, L1)
    if x == 3:
        return x3
    O = replace(x2, x3, x1)
    return O

def solve_f8ff0b80(S, I, x=0):
    x1 = rbind(canvas, UNITY)
    if x == 1:
        return x1
    x2 = o_g(I, R7)
    if x == 2:
        return x2
    x3 = order(x2, size)
    if x == 3:
        return x3
    x4 = apply(color, x3)
    if x == 4:
        return x4
    x5 = apply(x1, x4)
    if x == 5:
        return x5
    x6 = merge_t(x5)
    if x == 6:
        return x6
    O = mir_rot_t(x6, R0)
    return O

def solve_dbc1a6ce(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = fork(connect, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, ONE)
    if x == 4:
        return x4
    x5 = product(x4, x4)
    if x == 5:
        return x5
    x6 = apply(x3, x5)
    if x == 6:
        return x6
    x7 = fork(either, vline_i, hline_i)
    if x == 7:
        return x7
    x8 = mfilter_f(x6, x7)
    if x == 8:
        return x8
    O = underfill(I, EIGHT, x8)
    return O

def solve_6f8cd79b(S, I, x=0):
    x1 = asindices(I)
    if x == 1:
        return x1
    x2 = apply(initset, x1)
    if x == 2:
        return x2
    x3 = rbind(bordering, I)
    if x == 3:
        return x3
    x4 = mfilter_f(x2, x3)
    if x == 4:
        return x4
    O = fill(I, EIGHT, x4)
    return O

def solve_5c0a986e(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = corner(x1, R3)
    if x == 2:
        return x2
    x3 = shoot(x2, UNITY)
    if x == 3:
        return x3
    x4 = fill(I, TWO, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, ONE)
    if x == 5:
        return x5
    x6 = corner(x5, R0)
    if x == 6:
        return x6
    x7 = shoot(x6, NEG_UNITY)
    if x == 7:
        return x7
    O = fill(x4, ONE, x7)
    return O

def solve_db3e9e38(S, I, x=0):
    x1 = rbind(shoot, UP)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, SEVEN)
    if x == 2:
        return x2
    x3 = corner(x2, R3)
    if x == 3:
        return x3
    x4 = shoot(x3, UP_RIGHT)
    if x == 4:
        return x4
    x5 = shoot(x3, NEG_UNITY)
    if x == 5:
        return x5
    x6 = combine(x4, x5)
    if x == 6:
        return x6
    x7 = mapply(x1, x6)
    if x == 7:
        return x7
    x8 = fill(I, EIGHT, x7)
    if x == 8:
        return x8
    x9 = get_nth_t(x3, L1)
    if x == 9:
        return x9
    x10 = rbind(subtract, x9)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, L1)
    if x == 11:
        return x11
    x12 = chain(even, x10, x11)
    if x == 12:
        return x12
    x13 = sfilter_f(x7, x12)
    if x == 13:
        return x13
    O = fill(x8, SEVEN, x13)
    return O

def solve_d9fac9be(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = remove(ZERO, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, F0)
    if x == 4:
        return x4
    x5 = color(x4)
    if x == 5:
        return x5
    x6 = other_f(x2, x5)
    if x == 6:
        return x6
    O = canvas(x6, UNITY)
    return O

def solve_72322fa7(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = compose(x1, normalize)
    if x == 2:
        return x2
    x3 = lbind(occurrences, I)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, F0)
    if x == 4:
        return x4
    x5 = lbind(matcher, x4)
    if x == 5:
        return x5
    x6 = rbind(get_color_rank_f, F0)
    if x == 6:
        return x6
    x7 = compose(x5, x6)
    if x == 7:
        return x7
    x8 = fork(sfilter, identity, x7)
    if x == 8:
        return x8
    x9 = compose(x3, x8)
    if x == 9:
        return x9
    x10 = fork(mapply, x2, x9)
    if x == 10:
        return x10
    x11 = o_g(I, R3)
    if x == 11:
        return x11
    x12 = matcher(numcolors_f, ONE)
    if x == 12:
        return x12
    x13 = sfilter_f(x11, x12)
    if x == 13:
        return x13
    x14 = difference(x11, x13)
    if x == 14:
        return x14
    x15 = mapply(x10, x14)
    if x == 15:
        return x15
    x16 = paint(I, x15)
    if x == 16:
        return x16
    x17 = lbind(rbind, add)
    if x == 17:
        return x17
    x18 = rbind(corner, R0)
    if x == 18:
        return x18
    x19 = fork(difference, identity, x8)
    if x == 19:
        return x19
    x20 = compose(x18, x19)
    if x == 20:
        return x20
    x21 = fork(subtract, x18, x20)
    if x == 21:
        return x21
    x22 = compose(x17, x21)
    if x == 22:
        return x22
    x23 = compose(x3, x19)
    if x == 23:
        return x23
    x24 = fork(apply, x22, x23)
    if x == 24:
        return x24
    x25 = fork(mapply, x2, x24)
    if x == 25:
        return x25
    x26 = mapply(x25, x14)
    if x == 26:
        return x26
    O = paint(x16, x26)
    return O

def solve_23b5c85d(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O

def solve_6e02f1e3(S, I, x=0):
    x1 = canvas(ZERO, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = numcolors_t(I)
    if x == 2:
        return x2
    x3 = equality(x2, THREE)
    if x == 3:
        return x3
    x4 = branch(x3, TWO_BY_ZERO, ORIGIN)
    if x == 4:
        return x4
    x5 = equality(x2, TWO)
    if x == 5:
        return x5
    x6 = branch(x5, TWO_BY_TWO, ZERO_BY_TWO)
    if x == 6:
        return x6
    x7 = connect(x4, x6)
    if x == 7:
        return x7
    O = fill(x1, FIVE, x7)
    return O

def solve_681b3aeb(S, I, x=0):
    x1 = mir_rot_t(I, R6)
    if x == 1:
        return x1
    x2 = o_g(x1, R5)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x2, size, L1)
    if x == 3:
        return x3
    x4 = color(x3)
    if x == 4:
        return x4
    x5 = canvas(x4, THREE_BY_THREE)
    if x == 5:
        return x5
    x6 = get_arg_rank_f(x2, size, F0)
    if x == 6:
        return x6
    x7 = normalize(x6)
    if x == 7:
        return x7
    x8 = paint(x5, x7)
    if x == 8:
        return x8
    O = mir_rot_t(x8, R4)
    return O

def solve_2204b7a8(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = lbind(sfilter, x1)
    if x == 2:
        return x2
    x3 = compose(size, x2)
    if x == 3:
        return x3
    x4 = x3(vline_o)
    if x == 4:
        return x4
    x5 = x3(hline_o)
    if x == 5:
        return x5
    x6 = greater(x4, x5)
    if x == 6:
        return x6
    x7 = branch(x6, hconcat, vconcat)
    if x == 7:
        return x7
    x8 = branch(x6, lefthalf, tophalf)
    if x == 8:
        return x8
    x9 = x8(I)
    if x == 9:
        return x9
    x10 = index(x9, ORIGIN)
    if x == 10:
        return x10
    x11 = replace(x9, THREE, x10)
    if x == 11:
        return x11
    x12 = branch(x6, righthalf, bottomhalf)
    if x == 12:
        return x12
    x13 = x12(I)
    if x == 13:
        return x13
    x14 = shape_t(x13)
    if x == 14:
        return x14
    x15 = decrement(x14)
    if x == 15:
        return x15
    x16 = index(x13, x15)
    if x == 16:
        return x16
    x17 = replace(x13, THREE, x16)
    if x == 17:
        return x17
    O = x7(x11, x17)
    return O

def solve_56ff96f3(S, I, x=0):
    x1 = fork(recolor_i, color, backdrop)
    if x == 1:
        return x1
    x2 = fgpartition(I)
    if x == 2:
        return x2
    x3 = mapply(x1, x2)
    if x == 3:
        return x3
    O = paint(I, x3)
    return O

def solve_44d8ac46(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = apply(delta, x1)
    if x == 2:
        return x2
    x3 = mfilter_f(x2, square_f)
    if x == 3:
        return x3
    O = fill(I, TWO, x3)
    return O

def solve_2bcee788(S, I, x=0):
    x1 = get_color_rank_t(I, F0)
    if x == 1:
        return x1
    x2 = replace(I, x1, THREE)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, L1)
    if x == 4:
        return x4
    x5 = hline_o(x4)
    if x == 5:
        return x5
    x6 = get_arg_rank_f(x3, size, F0)
    if x == 6:
        return x6
    x7 = subgrid(x6, x2)
    if x == 7:
        return x7
    x8 = mir_rot_t(x7, R0)
    if x == 8:
        return x8
    x9 = mir_rot_t(x7, R2)
    if x == 9:
        return x9
    x10 = branch(x5, x8, x9)
    if x == 10:
        return x10
    x11 = asobject(x10)
    if x == 11:
        return x11
    x12 = rbind(get_nth_f, F0)
    if x == 12:
        return x12
    x13 = matcher(x12, THREE)
    if x == 13:
        return x13
    x14 = compose(flip, x13)
    if x == 14:
        return x14
    x15 = sfilter_f(x11, x14)
    if x == 15:
        return x15
    x16 = corner(x6, R0)
    if x == 16:
        return x16
    x17 = shape_f(x6)
    if x == 17:
        return x17
    x18 = position(x6, x4)
    if x == 18:
        return x18
    x19 = get_nth_t(x18, F0)
    if x == 19:
        return x19
    x20 = branch(x5, x19, ZERO)
    if x == 20:
        return x20
    x21 = get_nth_t(x18, L1)
    if x == 21:
        return x21
    x22 = branch(x5, ZERO, x21)
    if x == 22:
        return x22
    x23 = astuple(x20, x22)
    if x == 23:
        return x23
    x24 = multiply(x17, x23)
    if x == 24:
        return x24
    x25 = add(x16, x24)
    if x == 25:
        return x25
    x26 = shift(x15, x25)
    if x == 26:
        return x26
    O = paint(x2, x26)
    return O

def solve_a65b410d(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = corner(x1, R1)
    if x == 2:
        return x2
    x3 = shoot(x2, UP_RIGHT)
    if x == 3:
        return x3
    x4 = underfill(I, THREE, x3)
    if x == 4:
        return x4
    x5 = shoot(x2, DOWN_LEFT)
    if x == 5:
        return x5
    x6 = underfill(x4, ONE, x5)
    if x == 6:
        return x6
    x7 = rbind(shoot, LEFT)
    if x == 7:
        return x7
    x8 = mapply(x7, x5)
    if x == 8:
        return x8
    x9 = underfill(x6, ONE, x8)
    if x == 9:
        return x9
    x10 = mapply(x7, x3)
    if x == 10:
        return x10
    O = underfill(x9, THREE, x10)
    return O

def solve_6773b310(S, I, x=0):
    x1 = compress(I)
    if x == 1:
        return x1
    x2 = rbind(toobject, x1)
    if x == 2:
        return x2
    x3 = fork(insert, identity, neighbors)
    if x == 3:
        return x3
    x4 = rbind(multiply, THREE)
    if x == 4:
        return x4
    x5 = neighbors(ORIGIN)
    if x == 5:
        return x5
    x6 = insert(ORIGIN, x5)
    if x == 6:
        return x6
    x7 = apply(x4, x6)
    if x == 7:
        return x7
    x8 = astuple(FOUR, FOUR)
    if x == 8:
        return x8
    x9 = shift(x7, x8)
    if x == 9:
        return x9
    x10 = apply(x3, x9)
    if x == 10:
        return x10
    x11 = apply(x2, x10)
    if x == 11:
        return x11
    x12 = rbind(colorcount_f, SIX)
    if x == 12:
        return x12
    x13 = matcher(x12, TWO)
    if x == 13:
        return x13
    x14 = mfilter(x11, x13)
    if x == 14:
        return x14
    x15 = fill(x1, ONE, x14)
    if x == 15:
        return x15
    x16 = replace(x15, SIX, ZERO)
    if x == 16:
        return x16
    O = downscale(x16, THREE)
    return O

def solve_3e980e27(S, I, x=0):
    x1 = rbind(compose, center)
    if x == 1:
        return x1
    x2 = lbind(lbind, shift)
    if x == 2:
        return x2
    x3 = rbind(corner, R0)
    if x == 3:
        return x3
    x4 = compose(invert, x3)
    if x == 4:
        return x4
    x5 = lbind(compose, x4)
    if x == 5:
        return x5
    x6 = lbind(rbind, sfilter)
    if x == 6:
        return x6
    x7 = compose(x5, x6)
    if x == 7:
        return x7
    x8 = lbind(contained, TWO)
    if x == 8:
        return x8
    x9 = x7(x8)
    if x == 9:
        return x9
    x10 = fork(shift, identity, x9)
    if x == 10:
        return x10
    x11 = chain(x1, x2, x10)
    if x == 11:
        return x11
    x12 = astuple(TEN, TEN)
    if x == 12:
        return x12
    x13 = invert(x12)
    if x == 13:
        return x13
    x14 = astuple(THREE, x13)
    if x == 14:
        return x14
    x15 = astuple(TWO, x13)
    if x == 15:
        return x15
    x16 = initset(x15)
    if x == 16:
        return x16
    x17 = insert(x14, x16)
    if x == 17:
        return x17
    x18 = o_g(I, R3)
    if x == 18:
        return x18
    x19 = insert(x17, x18)
    if x == 19:
        return x19
    x20 = compose(x8, palette_f)
    if x == 20:
        return x20
    x21 = sfilter_f(x19, x20)
    if x == 21:
        return x21
    x22 = get_arg_rank_f(x21, size, F0)
    if x == 22:
        return x22
    x23 = mir_rot_f(x22, R2)
    if x == 23:
        return x23
    x24 = x11(x23)
    if x == 24:
        return x24
    x25 = remove_f(x22, x21)
    if x == 25:
        return x25
    x26 = mapply(x24, x25)
    if x == 26:
        return x26
    x27 = lbind(contained, THREE)
    if x == 27:
        return x27
    x28 = x7(x27)
    if x == 28:
        return x28
    x29 = fork(shift, identity, x28)
    if x == 29:
        return x29
    x30 = chain(x1, x2, x29)
    if x == 30:
        return x30
    x31 = compose(x27, palette_f)
    if x == 31:
        return x31
    x32 = sfilter_f(x19, x31)
    if x == 32:
        return x32
    x33 = get_arg_rank_f(x32, size, F0)
    if x == 33:
        return x33
    x34 = x30(x33)
    if x == 34:
        return x34
    x35 = remove_f(x33, x32)
    if x == 35:
        return x35
    x36 = mapply(x34, x35)
    if x == 36:
        return x36
    x37 = combine_f(x26, x36)
    if x == 37:
        return x37
    O = paint(I, x37)
    return O

def solve_67a3c6ac(S, I, x=0):
    O = mir_rot_t(I, R2)
    return O

def solve_ea786f4a(S, I, x=0):
    x1 = shoot(ORIGIN, UNITY)
    if x == 1:
        return x1
    x2 = width_t(I)
    if x == 2:
        return x2
    x3 = decrement(x2)
    if x == 3:
        return x3
    x4 = tojvec(x3)
    if x == 4:
        return x4
    x5 = shoot(x4, DOWN_LEFT)
    if x == 5:
        return x5
    x6 = combine(x1, x5)
    if x == 6:
        return x6
    O = fill(I, ZERO, x6)
    return O

def solve_3c9b0459(S, I, x=0):
    O = mir_rot_t(I, R5)
    return O

def solve_1f85a75f(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O

def solve_780d0b14(S, I, x=0):
    x1 = asindices(I)
    if x == 1:
        return x1
    x2 = fill(I, ZERO, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R7)
    if x == 3:
        return x3
    x4 = rbind(greater, TWO)
    if x == 4:
        return x4
    x5 = compose(x4, size)
    if x == 5:
        return x5
    x6 = sfilter(x3, x5)
    if x == 6:
        return x6
    x7 = totuple(x6)
    if x == 7:
        return x7
    x8 = apply(color, x7)
    if x == 8:
        return x8
    x9 = apply(center, x7)
    if x == 9:
        return x9
    x10 = pair(x8, x9)
    if x == 10:
        return x10
    x11 = paint(x2, x10)
    if x == 11:
        return x11
    x12 = rbind(greater, ONE)
    if x == 12:
        return x12
    x13 = compose(dedupe, totuple)
    if x == 13:
        return x13
    x14 = chain(x12, size, x13)
    if x == 14:
        return x14
    x15 = sfilter(x11, x14)
    if x == 15:
        return x15
    x16 = mir_rot_t(x15, R4)
    if x == 16:
        return x16
    x17 = sfilter(x16, x14)
    if x == 17:
        return x17
    O = mir_rot_t(x17, R6)
    return O

def solve_4290ef0e(S, I, x=0):
    x1 = get_color_rank_t(I, F0)
    if x == 1:
        return x1
    x2 = fgpartition(I)
    if x == 2:
        return x2
    x3 = apply(size, x2)
    if x == 3:
        return x3
    x4 = contained(ONE, x3)
    if x == 4:
        return x4
    x5 = size_f(x2)
    if x == 5:
        return x5
    x6 = increment(x5)
    if x == 6:
        return x6
    x7 = branch(x4, x5, x6)
    if x == 7:
        return x7
    x8 = double(x7)
    if x == 8:
        return x8
    x9 = decrement(x8)
    if x == 9:
        return x9
    x10 = astuple(x9, x9)
    if x == 10:
        return x10
    x11 = canvas(x1, x10)
    if x == 11:
        return x11
    x12 = rbind(get_arg_rank, L1)
    if x == 12:
        return x12
    x13 = rbind(x12, centerofmass)
    if x == 13:
        return x13
    x14 = rbind(mir_rot_f, R0)
    if x == 14:
        return x14
    x15 = rbind(mir_rot_f, R3)
    if x == 15:
        return x15
    x16 = rbind(mir_rot_f, R1)
    if x == 16:
        return x16
    x17 = rbind(mir_rot_f, R2)
    if x == 17:
        return x17
    x18 = compose(initset, x17)
    if x == 18:
        return x18
    x19 = fork(insert, x16, x18)
    if x == 19:
        return x19
    x20 = fork(insert, x15, x19)
    if x == 20:
        return x20
    x21 = fork(insert, x14, x20)
    if x == 21:
        return x21
    x22 = compose(x13, x21)
    if x == 22:
        return x22
    x23 = rbind(branch, NEG_TWO)
    if x == 23:
        return x23
    x24 = fork(x23, positive, decrement)
    if x == 24:
        return x24
    x25 = rbind(get_rank, L1)
    if x == 25:
        return x25
    x26 = lbind(remove, ZERO)
    if x == 26:
        return x26
    x27 = lbind(prapply, manhattan)
    if x == 27:
        return x27
    x28 = fork(x27, identity, identity)
    if x == 28:
        return x28
    x29 = compose(x26, x28)
    if x == 29:
        return x29
    x30 = chain(x24, x25, x29)
    if x == 30:
        return x30
    x31 = rbind(get_val_rank, F0)
    if x == 31:
        return x31
    x32 = rbind(x31, width_f)
    if x == 32:
        return x32
    x33 = compose(double, x32)
    if x == 33:
        return x33
    x34 = fork(add, x30, x33)
    if x == 34:
        return x34
    x35 = o_g(I, R5)
    if x == 35:
        return x35
    x36 = lbind(colorfilter, x35)
    if x == 36:
        return x36
    x37 = compose(x36, color)
    if x == 37:
        return x37
    x38 = compose(x34, x37)
    if x == 38:
        return x38
    x39 = compose(invert, x38)
    if x == 39:
        return x39
    x40 = order(x2, x39)
    if x == 40:
        return x40
    x41 = apply(x22, x40)
    if x == 41:
        return x41
    x42 = apply(normalize, x41)
    if x == 42:
        return x42
    x43 = interval(ZERO, x7, ONE)
    if x == 43:
        return x43
    x44 = pair(x43, x43)
    if x == 44:
        return x44
    x45 = mpapply(shift, x42, x44)
    if x == 45:
        return x45
    x46 = paint(x11, x45)
    if x == 46:
        return x46
    x47 = mir_rot_t(x46, R4)
    if x == 47:
        return x47
    x48 = paint(x47, x45)
    if x == 48:
        return x48
    x49 = mir_rot_t(x48, R4)
    if x == 49:
        return x49
    x50 = paint(x49, x45)
    if x == 50:
        return x50
    x51 = mir_rot_t(x50, R4)
    if x == 51:
        return x51
    O = paint(x51, x45)
    return O

def solve_776ffc46(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = colorfilter(x1, FIVE)
    if x == 2:
        return x2
    x3 = fork(equality, toindices, box)
    if x == 3:
        return x3
    x4 = extract(x2, x3)
    if x == 4:
        return x4
    x5 = inbox(x4)
    if x == 5:
        return x5
    x6 = subgrid(x5, I)
    if x == 6:
        return x6
    x7 = asobject(x6)
    if x == 7:
        return x7
    x8 = rbind(get_nth_f, F0)
    if x == 8:
        return x8
    x9 = matcher(x8, ZERO)
    if x == 9:
        return x9
    x10 = compose(flip, x9)
    if x == 10:
        return x10
    x11 = sfilter_f(x7, x10)
    if x == 11:
        return x11
    x12 = normalize(x11)
    if x == 12:
        return x12
    x13 = color(x12)
    if x == 13:
        return x13
    x14 = compose(toindices, normalize)
    if x == 14:
        return x14
    x15 = toindices(x12)
    if x == 15:
        return x15
    x16 = matcher(x14, x15)
    if x == 16:
        return x16
    x17 = mfilter_f(x1, x16)
    if x == 17:
        return x17
    O = fill(I, x13, x17)
    return O

def solve_cce03e0d(S, I, x=0):
    x1 = hconcat(I, I)
    if x == 1:
        return x1
    x2 = hconcat(x1, I)
    if x == 2:
        return x2
    x3 = vconcat(x2, x2)
    if x == 3:
        return x3
    x4 = vconcat(x3, x2)
    if x == 4:
        return x4
    x5 = upscale_t(I, THREE)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, ZERO)
    if x == 6:
        return x6
    x7 = f_ofcolor(x5, ONE)
    if x == 7:
        return x7
    x8 = combine_f(x6, x7)
    if x == 8:
        return x8
    O = fill(x4, ZERO, x8)
    return O

def solve_e40b9e2f(S, I, x=0):
    x1 = rbind(mir_rot_f, R0)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_f, R2)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R3)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = x3(x5)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = neighbors(ORIGIN)
    if x == 8:
        return x8
    x9 = mapply(neighbors, x8)
    if x == 9:
        return x9
    x10 = apply(x7, x9)
    if x == 10:
        return x10
    x11 = lbind(intersection, x5)
    if x == 11:
        return x11
    x12 = get_arg_rank_f(x10, x11, F0)
    if x == 12:
        return x12
    x13 = paint(I, x12)
    if x == 13:
        return x13
    x14 = rbind(mir_rot_f, R1)
    if x == 14:
        return x14
    x15 = compose(x2, x14)
    if x == 15:
        return x15
    x16 = o_g(x13, R3)
    if x == 16:
        return x16
    x17 = get_nth_f(x16, F0)
    if x == 17:
        return x17
    x18 = x15(x17)
    if x == 18:
        return x18
    x19 = lbind(shift, x18)
    if x == 19:
        return x19
    x20 = apply(x19, x9)
    if x == 20:
        return x20
    x21 = compose(size, x11)
    if x == 21:
        return x21
    x22 = get_arg_rank_f(x20, x21, F0)
    if x == 22:
        return x22
    O = paint(x13, x22)
    return O

def solve_49d1d64f(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = add(x1, TWO)
    if x == 2:
        return x2
    x3 = canvas(ZERO, x2)
    if x == 3:
        return x3
    x4 = asobject(I)
    if x == 4:
        return x4
    x5 = shift(x4, UNITY)
    if x == 5:
        return x5
    x6 = paint(x3, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, F0)
    if x == 7:
        return x7
    x8 = rbind(get_arg_rank, L1)
    if x == 8:
        return x8
    x9 = lbind(x8, x5)
    if x == 9:
        return x9
    x10 = rbind(compose, initset)
    if x == 10:
        return x10
    x11 = lbind(lbind, manhattan)
    if x == 11:
        return x11
    x12 = chain(x10, x11, initset)
    if x == 12:
        return x12
    x13 = chain(x7, x9, x12)
    if x == 13:
        return x13
    x14 = fork(astuple, x13, identity)
    if x == 14:
        return x14
    x15 = fork(difference, box, corners)
    if x == 15:
        return x15
    x16 = asindices(x3)
    if x == 16:
        return x16
    x17 = x15(x16)
    if x == 17:
        return x17
    x18 = apply(x14, x17)
    if x == 18:
        return x18
    O = paint(x6, x18)
    return O

def solve_a2fd1cf0(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = col_row(x1, R1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, THREE)
    if x == 3:
        return x3
    x4 = col_row(x3, R1)
    if x == 4:
        return x4
    x5 = astuple(x2, x4)
    if x == 5:
        return x5
    x6 = get_rank(x5, L1)
    if x == 6:
        return x6
    x7 = col_row(x3, R2)
    if x == 7:
        return x7
    x8 = astuple(x6, x7)
    if x == 8:
        return x8
    x9 = get_rank(x5, F0)
    if x == 9:
        return x9
    x10 = astuple(x9, x7)
    if x == 10:
        return x10
    x11 = connect(x8, x10)
    if x == 11:
        return x11
    x12 = col_row(x1, R2)
    if x == 12:
        return x12
    x13 = astuple(x12, x7)
    if x == 13:
        return x13
    x14 = get_rank(x13, L1)
    if x == 14:
        return x14
    x15 = astuple(x2, x14)
    if x == 15:
        return x15
    x16 = get_rank(x13, F0)
    if x == 16:
        return x16
    x17 = astuple(x2, x16)
    if x == 17:
        return x17
    x18 = connect(x15, x17)
    if x == 18:
        return x18
    x19 = combine_f(x11, x18)
    if x == 19:
        return x19
    O = underfill(I, EIGHT, x19)
    return O

def solve_5168d44c(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = recolor_i(TWO, x1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, THREE)
    if x == 3:
        return x3
    x4 = height_f(x3)
    if x == 4:
        return x4
    x5 = equality(x4, ONE)
    if x == 5:
        return x5
    x6 = branch(x5, ZERO_BY_TWO, TWO_BY_ZERO)
    if x == 6:
        return x6
    O = move(I, x2, x6)
    return O

def solve_25d8a9c8(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = sizefilter(x1, THREE)
    if x == 2:
        return x2
    x3 = mfilter_f(x2, hline_o)
    if x == 3:
        return x3
    x4 = toindices(x3)
    if x == 4:
        return x4
    x5 = fill(I, FIVE, x4)
    if x == 5:
        return x5
    x6 = asindices(I)
    if x == 6:
        return x6
    x7 = difference(x6, x4)
    if x == 7:
        return x7
    O = fill(x5, ZERO, x7)
    return O

def solve_ae4f1146(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = rbind(colorcount_f, ONE)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x1, x2, F0)
    if x == 3:
        return x3
    O = subgrid(x3, I)
    return O

def solve_90f3ed37(S, I, x=0):
    x1 = rbind(get_arg_rank, F0)
    if x == 1:
        return x1
    x2 = interval(TWO, NEG_ONE, NEG_ONE)
    if x == 2:
        return x2
    x3 = apply(tojvec, x2)
    if x == 3:
        return x3
    x4 = rbind(apply, x3)
    if x == 4:
        return x4
    x5 = lbind(lbind, shift)
    if x == 5:
        return x5
    x6 = o_g(I, R7)
    if x == 6:
        return x6
    x7 = rbind(col_row, R1)
    if x == 7:
        return x7
    x8 = order(x6, x7)
    if x == 8:
        return x8
    x9 = get_nth_t(x8, F0)
    if x == 9:
        return x9
    x10 = normalize(x9)
    if x == 10:
        return x10
    x11 = lbind(shift, x10)
    if x == 11:
        return x11
    x12 = rbind(corner, R0)
    if x == 12:
        return x12
    x13 = compose(x11, x12)
    if x == 13:
        return x13
    x14 = chain(x4, x5, x13)
    if x == 14:
        return x14
    x15 = lbind(compose, size)
    if x == 15:
        return x15
    x16 = lbind(lbind, intersection)
    if x == 16:
        return x16
    x17 = compose(x15, x16)
    if x == 17:
        return x17
    x18 = fork(x1, x14, x17)
    if x == 18:
        return x18
    x19 = remove_f(x9, x8)
    if x == 19:
        return x19
    x20 = mapply(x18, x19)
    if x == 20:
        return x20
    O = underfill(I, ONE, x20)
    return O

def solve_1f642eb9(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = get_nth_f(x3, F0)
    if x == 4:
        return x4
    x5 = rbind(gravitate, x4)
    if x == 5:
        return x5
    x6 = compose(crement, x5)
    if x == 6:
        return x6
    x7 = fork(shift, identity, x6)
    if x == 7:
        return x7
    x8 = mapply(x7, x2)
    if x == 8:
        return x8
    O = paint(I, x8)
    return O

def solve_d0f5fe59(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = size_f(x1)
    if x == 2:
        return x2
    x3 = astuple(x2, x2)
    if x == 3:
        return x3
    x4 = canvas(ZERO, x3)
    if x == 4:
        return x4
    x5 = shoot(ORIGIN, UNITY)
    if x == 5:
        return x5
    O = fill(x4, EIGHT, x5)
    return O

def solve_fcc82909(S, I, x=0):
    x1 = rbind(add, DOWN)
    if x == 1:
        return x1
    x2 = rbind(corner, R2)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = rbind(corner, R3)
    if x == 4:
        return x4
    x5 = compose(toivec, numcolors_f)
    if x == 5:
        return x5
    x6 = fork(add, x4, x5)
    if x == 6:
        return x6
    x7 = fork(astuple, x3, x6)
    if x == 7:
        return x7
    x8 = compose(box, x7)
    if x == 8:
        return x8
    x9 = o_g(I, R3)
    if x == 9:
        return x9
    x10 = mapply(x8, x9)
    if x == 10:
        return x10
    O = fill(I, THREE, x10)
    return O

def solve_93b581b8(S, I, x=0):
    x1 = rbind(mir_rot_f, R3)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_f, R1)
    if x == 2:
        return x2
    x3 = chain(x1, x2, merge)
    if x == 3:
        return x3
    x4 = fgpartition(I)
    if x == 4:
        return x4
    x5 = x3(x4)
    if x == 5:
        return x5
    x6 = upscale_f(x5, THREE)
    if x == 6:
        return x6
    x7 = astuple(NEG_TWO, NEG_TWO)
    if x == 7:
        return x7
    x8 = shift(x6, x7)
    if x == 8:
        return x8
    x9 = underpaint(I, x8)
    if x == 9:
        return x9
    x10 = fork(combine, hfrontier, vfrontier)
    if x == 10:
        return x10
    x11 = toindices(x5)
    if x == 11:
        return x11
    x12 = mapply(x10, x11)
    if x == 12:
        return x12
    x13 = difference(x12, x11)
    if x == 13:
        return x13
    O = fill(x9, ZERO, x13)
    return O

def solve_31aa019c(S, I, x=0):
    x1 = astuple(TEN, TEN)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = get_color_rank_t(I, L1)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, x3)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = initset(x5)
    if x == 6:
        return x6
    x7 = fill(x2, x3, x6)
    if x == 7:
        return x7
    x8 = neighbors(x5)
    if x == 8:
        return x8
    O = fill(x7, TWO, x8)
    return O

def solve_b2862040(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ONE)
    if x == 2:
        return x2
    x3 = colorfilter(x1, NINE)
    if x == 3:
        return x3
    x4 = rbind(bordering, I)
    if x == 4:
        return x4
    x5 = compose(flip, x4)
    if x == 5:
        return x5
    x6 = mfilter_f(x3, x5)
    if x == 6:
        return x6
    x7 = rbind(adjacent, x6)
    if x == 7:
        return x7
    x8 = mfilter_f(x2, x7)
    if x == 8:
        return x8
    O = fill(I, EIGHT, x8)
    return O

def solve_1a07d186(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    x4 = cover(I, x3)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, F0)
    if x == 5:
        return x5
    x6 = difference(x1, x2)
    if x == 6:
        return x6
    x7 = lbind(colorfilter, x6)
    if x == 7:
        return x7
    x8 = chain(x5, x7, color)
    if x == 8:
        return x8
    x9 = fork(gravitate, identity, x8)
    if x == 9:
        return x9
    x10 = fork(shift, identity, x9)
    if x == 10:
        return x10
    x11 = apply(color, x6)
    if x == 11:
        return x11
    x12 = rbind(contained, x11)
    if x == 12:
        return x12
    x13 = compose(x12, color)
    if x == 13:
        return x13
    x14 = sfilter_f(x2, x13)
    if x == 14:
        return x14
    x15 = mapply(x10, x14)
    if x == 15:
        return x15
    O = paint(x4, x15)
    return O

def solve_1190e5a7(S, I, x=0):
    x1 = get_color_rank_t(I, F0)
    if x == 1:
        return x1
    x2 = frontiers(I)
    if x == 2:
        return x2
    x3 = sfilter_f(x2, vline_o)
    if x == 3:
        return x3
    x4 = difference(x2, x3)
    if x == 4:
        return x4
    x5 = astuple(x4, x3)
    if x == 5:
        return x5
    x6 = apply(size, x5)
    if x == 6:
        return x6
    x7 = increment(x6)
    if x == 7:
        return x7
    O = canvas(x1, x7)
    return O

def solve_8eb1be9a(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = height_f(x2)
    if x == 4:
        return x4
    x5 = rbind(multiply, x4)
    if x == 5:
        return x5
    x6 = interval(NEG_TWO, FOUR, ONE)
    if x == 6:
        return x6
    x7 = apply(x5, x6)
    if x == 7:
        return x7
    x8 = apply(toivec, x7)
    if x == 8:
        return x8
    x9 = mapply(x3, x8)
    if x == 9:
        return x9
    O = paint(I, x9)
    return O

def solve_b94a9452(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = get_color_rank_t(x3, L1)
    if x == 4:
        return x4
    x5 = get_color_rank_t(x3, F0)
    if x == 5:
        return x5
    O = switch(x3, x4, x5)
    return O

def solve_8731374e(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = height_t(x3)
    if x == 4:
        return x4
    x5 = vsplit(x3, x4)
    if x == 5:
        return x5
    x6 = lbind(greater, FOUR)
    if x == 6:
        return x6
    x7 = compose(x6, numcolors_t)
    if x == 7:
        return x7
    x8 = sfilter_t(x5, x7)
    if x == 8:
        return x8
    x9 = merge(x8)
    if x == 9:
        return x9
    x10 = mir_rot_t(x9, R4)
    if x == 10:
        return x10
    x11 = width_t(x3)
    if x == 11:
        return x11
    x12 = vsplit(x10, x11)
    if x == 12:
        return x12
    x13 = sfilter_t(x12, x7)
    if x == 13:
        return x13
    x14 = merge(x13)
    if x == 14:
        return x14
    x15 = mir_rot_t(x14, R6)
    if x == 15:
        return x15
    x16 = get_color_rank_t(x15, L1)
    if x == 16:
        return x16
    x17 = fork(combine, vfrontier, hfrontier)
    if x == 17:
        return x17
    x18 = f_ofcolor(x15, x16)
    if x == 18:
        return x18
    x19 = mapply(x17, x18)
    if x == 19:
        return x19
    O = fill(x15, x16, x19)
    return O

def solve_4522001f(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = toindices(x2)
    if x == 3:
        return x3
    x4 = contained(TWO_BY_ZERO, x3)
    if x == 4:
        return x4
    x5 = astuple(NINE, NINE)
    if x == 5:
        return x5
    x6 = canvas(ZERO, x5)
    if x == 6:
        return x6
    x7 = astuple(THREE, ORIGIN)
    if x == 7:
        return x7
    x8 = initset(x7)
    if x == 8:
        return x8
    x9 = upscale_f(x8, TWO)
    if x == 9:
        return x9
    x10 = upscale_f(x9, TWO)
    if x == 10:
        return x10
    x11 = shape_f(x10)
    if x == 11:
        return x11
    x12 = shift(x10, x11)
    if x == 12:
        return x12
    x13 = combine(x10, x12)
    if x == 13:
        return x13
    x14 = paint(x6, x13)
    if x == 14:
        return x14
    x15 = mir_rot_t(x14, R6)
    if x == 15:
        return x15
    x16 = contained(TWO_BY_TWO, x3)
    if x == 16:
        return x16
    x17 = mir_rot_t(x14, R5)
    if x == 17:
        return x17
    x18 = contained(ZERO_BY_TWO, x3)
    if x == 18:
        return x18
    x19 = mir_rot_t(x14, R4)
    if x == 19:
        return x19
    x20 = branch(x18, x19, x14)
    if x == 20:
        return x20
    x21 = branch(x16, x17, x20)
    if x == 21:
        return x21
    O = branch(x4, x15, x21)
    return O

def solve_7df24a62(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = rbind(shift, NEG_UNITY)
    if x == 2:
        return x2
    x3 = rbind(f_ofcolor, ONE)
    if x == 3:
        return x3
    x4 = compose(normalize, x3)
    if x == 4:
        return x4
    x5 = chain(x1, x2, x4)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, ONE)
    if x == 6:
        return x6
    x7 = subgrid(x6, I)
    if x == 7:
        return x7
    x8 = mir_rot_t(x7, R4)
    if x == 8:
        return x8
    x9 = astuple(x7, x8)
    if x == 9:
        return x9
    x10 = mir_rot_t(x7, R5)
    if x == 10:
        return x10
    x11 = mir_rot_t(x7, R6)
    if x == 11:
        return x11
    x12 = astuple(x10, x11)
    if x == 12:
        return x12
    x13 = combine(x9, x12)
    if x == 13:
        return x13
    x14 = apply(x5, x13)
    if x == 14:
        return x14
    x15 = rbind(interval, ONE)
    if x == 15:
        return x15
    x16 = lbind(x15, ZERO)
    if x == 16:
        return x16
    x17 = height_t(I)
    if x == 17:
        return x17
    x18 = lbind(subtract, x17)
    if x == 18:
        return x18
    x19 = chain(increment, x18, height_f)
    if x == 19:
        return x19
    x20 = compose(x16, x19)
    if x == 20:
        return x20
    x21 = width_t(I)
    if x == 21:
        return x21
    x22 = lbind(subtract, x21)
    if x == 22:
        return x22
    x23 = chain(increment, x22, width_f)
    if x == 23:
        return x23
    x24 = compose(x16, x23)
    if x == 24:
        return x24
    x25 = fork(product, x20, x24)
    if x == 25:
        return x25
    x26 = corner(x6, R0)
    if x == 26:
        return x26
    x27 = rbind(shift, x26)
    if x == 27:
        return x27
    x28 = rbind(f_ofcolor, FOUR)
    if x == 28:
        return x28
    x29 = compose(x27, x28)
    if x == 29:
        return x29
    x30 = apply(x29, x13)
    if x == 30:
        return x30
    x31 = apply(normalize, x30)
    if x == 31:
        return x31
    x32 = apply(x25, x31)
    if x == 32:
        return x32
    x33 = matcher(size, ZERO)
    if x == 33:
        return x33
    x34 = lbind(compose, x33)
    if x == 34:
        return x34
    x35 = lbind(rbind, difference)
    if x == 35:
        return x35
    x36 = f_ofcolor(I, FOUR)
    if x == 36:
        return x36
    x37 = lbind(difference, x36)
    if x == 37:
        return x37
    x38 = apply(x37, x30)
    if x == 38:
        return x38
    x39 = apply(x35, x38)
    if x == 39:
        return x39
    x40 = apply(x1, x31)
    if x == 40:
        return x40
    x41 = papply(compose, x39, x40)
    if x == 41:
        return x41
    x42 = apply(x34, x41)
    if x == 42:
        return x42
    x43 = papply(sfilter, x32, x42)
    if x == 43:
        return x43
    x44 = mpapply(mapply, x14, x43)
    if x == 44:
        return x44
    O = fill(I, ONE, x44)
    return O

def solve_d13f3404(S, I, x=0):
    x1 = astuple(SIX, SIX)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = rbind(shoot, UNITY)
    if x == 3:
        return x3
    x4 = compose(x3, center)
    if x == 4:
        return x4
    x5 = fork(recolor_i, color, x4)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = mapply(x5, x6)
    if x == 7:
        return x7
    O = paint(x2, x7)
    return O

def solve_3631a71a(S, I, x=0):
    x1 = rbind(get_rank, F0)
    if x == 1:
        return x1
    x2 = lbind(apply, x1)
    if x == 2:
        return x2
    x3 = replace(I, NINE, ZERO)
    if x == 3:
        return x3
    x4 = mir_rot_t(x3, R1)
    if x == 4:
        return x4
    x5 = papply(pair, x3, x4)
    if x == 5:
        return x5
    x6 = apply(x2, x5)
    if x == 6:
        return x6
    x7 = shape_t(I)
    if x == 7:
        return x7
    x8 = subtract(x7, TWO_BY_TWO)
    if x == 8:
        return x8
    x9 = crop(x6, TWO_BY_TWO, x8)
    if x == 9:
        return x9
    x10 = mir_rot_t(x9, R2)
    if x == 10:
        return x10
    x11 = o_g(x10, R5)
    if x == 11:
        return x11
    x12 = merge(x11)
    if x == 12:
        return x12
    x13 = shift(x12, TWO_BY_TWO)
    if x == 13:
        return x13
    O = paint(x6, x13)
    return O

def solve_253bf280(S, I, x=0):
    x1 = f_ofcolor(I, EIGHT)
    if x == 1:
        return x1
    x2 = prapply(connect, x1, x1)
    if x == 2:
        return x2
    x3 = rbind(greater, ONE)
    if x == 3:
        return x3
    x4 = compose(x3, size)
    if x == 4:
        return x4
    x5 = sfilter_f(x2, x4)
    if x == 5:
        return x5
    x6 = fork(either, vline_i, hline_i)
    if x == 6:
        return x6
    x7 = mfilter_f(x5, x6)
    if x == 7:
        return x7
    x8 = fill(I, THREE, x7)
    if x == 8:
        return x8
    O = fill(x8, EIGHT, x1)
    return O

def solve_a61f2674(S, I, x=0):
    x1 = replace(I, FIVE, ZERO)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x2, size, F0)
    if x == 3:
        return x3
    x4 = recolor_o(ONE, x3)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x2, size, L1)
    if x == 5:
        return x5
    x6 = recolor_o(TWO, x5)
    if x == 6:
        return x6
    x7 = combine_f(x4, x6)
    if x == 7:
        return x7
    O = paint(x1, x7)
    return O

def solve_ec883f72(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = remove(ZERO, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R7)
    if x == 3:
        return x3
    x4 = fork(multiply, height_f, width_f)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x3, x4, F0)
    if x == 5:
        return x5
    x6 = color(x5)
    if x == 6:
        return x6
    x7 = other_f(x2, x6)
    if x == 7:
        return x7
    x8 = corner(x5, R3)
    if x == 8:
        return x8
    x9 = shoot(x8, UNITY)
    if x == 9:
        return x9
    x10 = corner(x5, R2)
    if x == 10:
        return x10
    x11 = shoot(x10, DOWN_LEFT)
    if x == 11:
        return x11
    x12 = combine(x9, x11)
    if x == 12:
        return x12
    x13 = corner(x5, R1)
    if x == 13:
        return x13
    x14 = shoot(x13, UP_RIGHT)
    if x == 14:
        return x14
    x15 = corner(x5, R0)
    if x == 15:
        return x15
    x16 = shoot(x15, NEG_UNITY)
    if x == 16:
        return x16
    x17 = combine(x14, x16)
    if x == 17:
        return x17
    x18 = combine(x12, x17)
    if x == 18:
        return x18
    O = underfill(I, x7, x18)
    return O

def solve_0b148d64(S, I, x=0):
    x1 = partition(I)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O

def solve_25d487eb(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = center(x2)
    if x == 3:
        return x3
    x4 = o_g(I, R5)
    if x == 4:
        return x4
    x5 = merge_f(x4)
    if x == 5:
        return x5
    x6 = center(x5)
    if x == 6:
        return x6
    x7 = subtract(x6, x3)
    if x == 7:
        return x7
    x8 = shoot(x3, x7)
    if x == 8:
        return x8
    O = underfill(I, x1, x8)
    return O

def solve_9f236235(S, I, x=0):
    x1 = compress(I)
    if x == 1:
        return x1
    x2 = mir_rot_t(x1, R2)
    if x == 2:
        return x2
    x3 = o_g(I, R4)
    if x == 3:
        return x3
    x4 = get_val_rank_f(x3, width_f, L1)
    if x == 4:
        return x4
    O = downscale(x2, x4)
    return O

def solve_a48eeaf7(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = cover(I, x1)
    if x == 2:
        return x2
    x3 = rbind(get_arg_rank, L1)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, TWO)
    if x == 4:
        return x4
    x5 = outbox(x4)
    if x == 5:
        return x5
    x6 = apply(initset, x5)
    if x == 6:
        return x6
    x7 = lbind(x3, x6)
    if x == 7:
        return x7
    x8 = lbind(lbind, manhattan)
    if x == 8:
        return x8
    x9 = compose(x8, initset)
    if x == 9:
        return x9
    x10 = compose(x7, x9)
    if x == 10:
        return x10
    x11 = mapply(x10, x1)
    if x == 11:
        return x11
    O = fill(x2, FIVE, x11)
    return O

def solve_9d9215db(S, I, x=0):
    x1 = rbind(get_rank, F0)
    if x == 1:
        return x1
    x2 = lbind(apply, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(I, R6)
    if x == 3:
        return x3
    x4 = mir_rot_t(I, R5)
    if x == 4:
        return x4
    x5 = mir_rot_t(I, R4)
    if x == 5:
        return x5
    x6 = initset(I)
    if x == 6:
        return x6
    x7 = insert(x5, x6)
    if x == 7:
        return x7
    x8 = insert(x4, x7)
    if x == 8:
        return x8
    x9 = insert(x3, x8)
    if x == 9:
        return x9
    x10 = chain(numcolors_t, lefthalf, tophalf)
    if x == 10:
        return x10
    x11 = get_arg_rank_f(x9, x10, F0)
    if x == 11:
        return x11
    x12 = mir_rot_t(x11, R2)
    if x == 12:
        return x12
    x13 = papply(pair, x11, x12)
    if x == 13:
        return x13
    x14 = apply(x2, x13)
    if x == 14:
        return x14
    x15 = rbind(corner, R2)
    if x == 15:
        return x15
    x16 = partition(x14)
    if x == 16:
        return x16
    x17 = sizefilter(x16, FOUR)
    if x == 17:
        return x17
    x18 = apply(x15, x17)
    if x == 18:
        return x18
    x19 = rbind(corner, R3)
    if x == 19:
        return x19
    x20 = apply(x19, x17)
    if x == 20:
        return x20
    x21 = combine_f(x18, x20)
    if x == 21:
        return x21
    x22 = cover(x14, x21)
    if x == 22:
        return x22
    x23 = rbind(get_nth_f, L1)
    if x == 23:
        return x23
    x24 = compose(even, x23)
    if x == 24:
        return x24
    x25 = rbind(sfilter, x24)
    if x == 25:
        return x25
    x26 = rbind(add, ZERO_BY_TWO)
    if x == 26:
        return x26
    x27 = rbind(corner, R0)
    if x == 27:
        return x27
    x28 = compose(x26, x27)
    if x == 28:
        return x28
    x29 = tojvec(NEG_TWO)
    if x == 29:
        return x29
    x30 = rbind(add, x29)
    if x == 30:
        return x30
    x31 = rbind(corner, R1)
    if x == 31:
        return x31
    x32 = compose(x30, x31)
    if x == 32:
        return x32
    x33 = fork(connect, x28, x32)
    if x == 33:
        return x33
    x34 = chain(normalize, x25, x33)
    if x == 34:
        return x34
    x35 = fork(shift, x34, x28)
    if x == 35:
        return x35
    x36 = fork(recolor_i, color, x35)
    if x == 36:
        return x36
    x37 = mapply(x36, x17)
    if x == 37:
        return x37
    x38 = paint(x22, x37)
    if x == 38:
        return x38
    x39 = mir_rot_t(x38, R4)
    if x == 39:
        return x39
    x40 = papply(pair, x38, x39)
    if x == 40:
        return x40
    x41 = apply(x2, x40)
    if x == 41:
        return x41
    x42 = mir_rot_t(x38, R5)
    if x == 42:
        return x42
    x43 = papply(pair, x41, x42)
    if x == 43:
        return x43
    x44 = apply(x2, x43)
    if x == 44:
        return x44
    x45 = mir_rot_t(x38, R6)
    if x == 45:
        return x45
    x46 = papply(pair, x44, x45)
    if x == 46:
        return x46
    O = apply(x2, x46)
    return O

def solve_b7249182(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = portrait_f(x2)
    if x == 3:
        return x3
    x4 = rbind(mir_rot_t, R1)
    if x == 4:
        return x4
    x5 = branch(x3, identity, x4)
    if x == 5:
        return x5
    x6 = x5(I)
    if x == 6:
        return x6
    x7 = o_g(x6, R5)
    if x == 7:
        return x7
    x8 = rbind(col_row, R1)
    if x == 8:
        return x8
    x9 = order(x7, x8)
    if x == 9:
        return x9
    x10 = get_nth_t(x9, L1)
    if x == 10:
        return x10
    x11 = color(x10)
    if x == 11:
        return x11
    x12 = rbind(get_nth_f, F0)
    if x == 12:
        return x12
    x13 = compose(x12, toindices)
    if x == 13:
        return x13
    x14 = get_nth_f(x9, F0)
    if x == 14:
        return x14
    x15 = x13(x14)
    if x == 15:
        return x15
    x16 = x13(x10)
    if x == 16:
        return x16
    x17 = connect(x15, x16)
    if x == 17:
        return x17
    x18 = fill(x6, x11, x17)
    if x == 18:
        return x18
    x19 = color(x14)
    if x == 19:
        return x19
    x20 = centerofmass(x17)
    if x == 20:
        return x20
    x21 = connect(x15, x20)
    if x == 21:
        return x21
    x22 = fill(x18, x19, x21)
    if x == 22:
        return x22
    x23 = add(x20, DOWN)
    if x == 23:
        return x23
    x24 = initset(x20)
    if x == 24:
        return x24
    x25 = insert(x23, x24)
    if x == 25:
        return x25
    x26 = toobject(x25, x22)
    if x == 26:
        return x26
    x27 = shift(x26, ZERO_BY_TWO)
    if x == 27:
        return x27
    x28 = astuple(ZERO, NEG_TWO)
    if x == 28:
        return x28
    x29 = shift(x26, x28)
    if x == 29:
        return x29
    x30 = combine_f(x27, x29)
    if x == 30:
        return x30
    x31 = paint(x22, x30)
    if x == 31:
        return x31
    x32 = corner(x30, R0)
    if x == 32:
        return x32
    x33 = corner(x30, R1)
    if x == 33:
        return x33
    x34 = connect(x32, x33)
    if x == 34:
        return x34
    x35 = shift(x34, UP)
    if x == 35:
        return x35
    x36 = fill(x31, x19, x35)
    if x == 36:
        return x36
    x37 = corner(x30, R2)
    if x == 37:
        return x37
    x38 = corner(x30, R3)
    if x == 38:
        return x38
    x39 = connect(x37, x38)
    if x == 39:
        return x39
    x40 = shift(x39, DOWN)
    if x == 40:
        return x40
    x41 = fill(x36, x11, x40)
    if x == 41:
        return x41
    x42 = cover(x41, x25)
    if x == 42:
        return x42
    O = x5(x42)
    return O

def solve_f9012d9b(S, I, x=0):
    x1 = f_ofcolor(I, ZERO)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = lbind(contained, ZERO)
    if x == 3:
        return x3
    x4 = chain(flip, x3, palette_t)
    if x == 4:
        return x4
    x5 = mfilter_f(x2, x4)
    if x == 5:
        return x5
    x6 = lbind(shift, x5)
    if x == 6:
        return x6
    x7 = vsplit(I, TWO)
    if x == 7:
        return x7
    x8 = extract(x7, x4)
    if x == 8:
        return x8
    x9 = asobject(x8)
    if x == 9:
        return x9
    x10 = vperiod(x9)
    if x == 10:
        return x10
    x11 = hsplit(I, TWO)
    if x == 11:
        return x11
    x12 = extract(x11, x4)
    if x == 12:
        return x12
    x13 = asobject(x12)
    if x == 13:
        return x13
    x14 = hperiod(x13)
    if x == 14:
        return x14
    x15 = astuple(x10, x14)
    if x == 15:
        return x15
    x16 = rbind(multiply, x15)
    if x == 16:
        return x16
    x17 = neighbors(ORIGIN)
    if x == 17:
        return x17
    x18 = mapply(neighbors, x17)
    if x == 18:
        return x18
    x19 = apply(x16, x18)
    if x == 19:
        return x19
    x20 = mapply(x6, x19)
    if x == 20:
        return x20
    x21 = paint(I, x20)
    if x == 21:
        return x21
    O = subgrid(x1, x21)
    return O

def solve_1fad071e(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ONE)
    if x == 2:
        return x2
    x3 = sizefilter(x2, FOUR)
    if x == 3:
        return x3
    x4 = size_f(x3)
    if x == 4:
        return x4
    x5 = astuple(ONE, x4)
    if x == 5:
        return x5
    x6 = canvas(ONE, x5)
    if x == 6:
        return x6
    x7 = subtract(FIVE, x4)
    if x == 7:
        return x7
    x8 = astuple(ONE, x7)
    if x == 8:
        return x8
    x9 = canvas(ZERO, x8)
    if x == 9:
        return x9
    O = hconcat(x6, x9)
    return O

def solve_67a423a3(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_color_rank_t(I, L1)
    if x == 2:
        return x2
    x3 = colorfilter(x1, x2)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    x5 = delta(x4)
    if x == 5:
        return x5
    x6 = get_nth_f(x5, F0)
    if x == 6:
        return x6
    x7 = neighbors(x6)
    if x == 7:
        return x7
    O = fill(I, FOUR, x7)
    return O

def solve_77fdfe62(S, I, x=0):
    x1 = replace(I, EIGHT, ZERO)
    if x == 1:
        return x1
    x2 = replace(x1, ONE, ZERO)
    if x == 2:
        return x2
    x3 = compress(x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = subgrid(x4, I)
    if x == 5:
        return x5
    x6 = width_t(x5)
    if x == 6:
        return x6
    x7 = halve(x6)
    if x == 7:
        return x7
    x8 = upscale_t(x3, x7)
    if x == 8:
        return x8
    x9 = f_ofcolor(x5, ZERO)
    if x == 9:
        return x9
    O = fill(x8, ZERO, x9)
    return O

def solve_e9afcf9a(S, I, x=0):
    x1 = astuple(TWO, ONE)
    if x == 1:
        return x1
    x2 = crop(I, ORIGIN, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R0)
    if x == 3:
        return x3
    x4 = hconcat(x2, x3)
    if x == 4:
        return x4
    x5 = hconcat(x4, x4)
    if x == 5:
        return x5
    O = hconcat(x5, x4)
    return O

def solve_91413438(S, I, x=0):
    x1 = colorcount_t(I, ZERO)
    if x == 1:
        return x1
    x2 = multiply(x1, THREE)
    if x == 2:
        return x2
    x3 = multiply(x2, x1)
    if x == 3:
        return x3
    x4 = subtract(x3, THREE)
    if x == 4:
        return x4
    x5 = astuple(THREE, x4)
    if x == 5:
        return x5
    x6 = canvas(ZERO, x5)
    if x == 6:
        return x6
    x7 = hconcat(I, x6)
    if x == 7:
        return x7
    x8 = o_g(x7, R7)
    if x == 8:
        return x8
    x9 = get_nth_f(x8, F0)
    if x == 9:
        return x9
    x10 = lbind(shift, x9)
    if x == 10:
        return x10
    x11 = compose(x10, tojvec)
    if x == 11:
        return x11
    x12 = rbind(multiply, THREE)
    if x == 12:
        return x12
    x13 = subtract(NINE, x1)
    if x == 13:
        return x13
    x14 = interval(ZERO, x13, ONE)
    if x == 14:
        return x14
    x15 = apply(x12, x14)
    if x == 15:
        return x15
    x16 = mapply(x11, x15)
    if x == 16:
        return x16
    x17 = paint(x7, x16)
    if x == 17:
        return x17
    x18 = hsplit(x17, x1)
    if x == 18:
        return x18
    O = merge_t(x18)
    return O

def solve_d4f3cd78(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = delta(x1)
    if x == 2:
        return x2
    x3 = fill(I, EIGHT, x2)
    if x == 3:
        return x3
    x4 = box(x1)
    if x == 4:
        return x4
    x5 = difference(x4, x1)
    if x == 5:
        return x5
    x6 = get_nth_f(x5, F0)
    if x == 6:
        return x6
    x7 = position(x4, x5)
    if x == 7:
        return x7
    x8 = shoot(x6, x7)
    if x == 8:
        return x8
    O = fill(x3, EIGHT, x8)
    return O

def solve_d23f8c26(S, I, x=0):
    x1 = asindices(I)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = width_t(I)
    if x == 3:
        return x3
    x4 = halve(x3)
    if x == 4:
        return x4
    x5 = matcher(x2, x4)
    if x == 5:
        return x5
    x6 = compose(flip, x5)
    if x == 6:
        return x6
    x7 = sfilter_f(x1, x6)
    if x == 7:
        return x7
    O = fill(I, ZERO, x7)
    return O

def solve_995c5fa3(S, I, x=0):
    x1 = rbind(canvas, UNITY)
    if x == 1:
        return x1
    x2 = rbind(f_ofcolor, ZERO)
    if x == 2:
        return x2
    x3 = compose(size, x2)
    if x == 3:
        return x3
    x4 = matcher(x3, ZERO)
    if x == 4:
        return x4
    x5 = compose(double, x4)
    if x == 5:
        return x5
    x6 = power(double, TWO)
    if x == 6:
        return x6
    x7 = rbind(corner, R0)
    if x == 7:
        return x7
    x8 = compose(x7, x2)
    if x == 8:
        return x8
    x9 = matcher(x8, UNITY)
    if x == 9:
        return x9
    x10 = chain(x6, double, x9)
    if x == 10:
        return x10
    x11 = fork(add, x5, x10)
    if x == 11:
        return x11
    x12 = rbind(multiply, THREE)
    if x == 12:
        return x12
    x13 = matcher(x8, DOWN)
    if x == 13:
        return x13
    x14 = compose(x12, x13)
    if x == 14:
        return x14
    x15 = astuple(TWO, ONE)
    if x == 15:
        return x15
    x16 = matcher(x8, x15)
    if x == 16:
        return x16
    x17 = compose(x6, x16)
    if x == 17:
        return x17
    x18 = fork(add, x14, x17)
    if x == 18:
        return x18
    x19 = fork(add, x11, x18)
    if x == 19:
        return x19
    x20 = compose(x1, x19)
    if x == 20:
        return x20
    x21 = hsplit(I, THREE)
    if x == 21:
        return x21
    x22 = apply(x20, x21)
    if x == 22:
        return x22
    x23 = merge_t(x22)
    if x == 23:
        return x23
    O = hupscale(x23, THREE)
    return O

def solve_d687bc17(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    x4 = cover(I, x3)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, F0)
    if x == 5:
        return x5
    x6 = difference(x1, x2)
    if x == 6:
        return x6
    x7 = lbind(colorfilter, x6)
    if x == 7:
        return x7
    x8 = chain(x5, x7, color)
    if x == 8:
        return x8
    x9 = fork(gravitate, identity, x8)
    if x == 9:
        return x9
    x10 = fork(shift, identity, x9)
    if x == 10:
        return x10
    x11 = apply(color, x6)
    if x == 11:
        return x11
    x12 = rbind(contained, x11)
    if x == 12:
        return x12
    x13 = compose(x12, color)
    if x == 13:
        return x13
    x14 = sfilter_f(x2, x13)
    if x == 14:
        return x14
    x15 = mapply(x10, x14)
    if x == 15:
        return x15
    O = paint(x4, x15)
    return O

def solve_57aa92db(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = lbind(remove, ZERO)
    if x == 2:
        return x2
    x3 = chain(x1, x2, palette_f)
    if x == 3:
        return x3
    x4 = rbind(toobject, I)
    if x == 4:
        return x4
    x5 = chain(x3, x4, outbox)
    if x == 5:
        return x5
    x6 = o_g(I, R3)
    if x == 6:
        return x6
    x7 = rbind(get_rank, F0)
    if x == 7:
        return x7
    x8 = lbind(lbind, colorcount_f)
    if x == 8:
        return x8
    x9 = fork(apply, x8, palette_f)
    if x == 9:
        return x9
    x10 = compose(x7, x9)
    if x == 10:
        return x10
    x11 = rbind(get_rank, L1)
    if x == 11:
        return x11
    x12 = compose(x11, x9)
    if x == 12:
        return x12
    x13 = fork(subtract, x10, x12)
    if x == 13:
        return x13
    x14 = get_arg_rank_f(x6, x13, F0)
    if x == 14:
        return x14
    x15 = normalize_o(x14)
    if x == 15:
        return x15
    x16 = lbind(shift, x15)
    if x == 16:
        return x16
    x17 = rbind(corner, R0)
    if x == 17:
        return x17
    x18 = get_color_rank_f(x14, L1)
    if x == 18:
        return x18
    x19 = matcher(x1, x18)
    if x == 19:
        return x19
    x20 = sfilter_f(x15, x19)
    if x == 20:
        return x20
    x21 = corner(x20, R0)
    if x == 21:
        return x21
    x22 = lbind(multiply, x21)
    if x == 22:
        return x22
    x23 = compose(x22, width_f)
    if x == 23:
        return x23
    x24 = fork(subtract, x17, x23)
    if x == 24:
        return x24
    x25 = compose(x16, x24)
    if x == 25:
        return x25
    x26 = fork(upscale_f, x25, width_f)
    if x == 26:
        return x26
    x27 = fork(recolor_o, x5, x26)
    if x == 27:
        return x27
    x28 = o_g(I, R5)
    if x == 28:
        return x28
    x29 = colorfilter(x28, x18)
    if x == 29:
        return x29
    x30 = mapply(x27, x29)
    if x == 30:
        return x30
    x31 = paint(I, x30)
    if x == 31:
        return x31
    x32 = merge_f(x28)
    if x == 32:
        return x32
    O = paint(x31, x32)
    return O

def solve_ea32f347(S, I, x=0):
    x1 = replace(I, FIVE, FOUR)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x2, size, F0)
    if x == 3:
        return x3
    x4 = fill(x1, ONE, x3)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x2, size, L1)
    if x == 5:
        return x5
    O = fill(x4, TWO, x5)
    return O

def solve_c444b776(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x2, size, L1)
    if x == 3:
        return x3
    x4 = backdrop(x3)
    if x == 4:
        return x4
    x5 = toobject(x4, I)
    if x == 5:
        return x5
    x6 = normalize(x5)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = rbind(corner, R0)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = mapply(x9, x2)
    if x == 10:
        return x10
    O = paint(I, x10)
    return O

def solve_3de23699(S, I, x=0):
    x1 = fgpartition(I)
    if x == 1:
        return x1
    x2 = sizefilter(x1, FOUR)
    if x == 2:
        return x2
    x3 = get_nth_f(x2, F0)
    if x == 3:
        return x3
    x4 = subgrid(x3, I)
    if x == 4:
        return x4
    x5 = trim(x4)
    if x == 5:
        return x5
    x6 = difference(x1, x2)
    if x == 6:
        return x6
    x7 = get_nth_f(x6, F0)
    if x == 7:
        return x7
    x8 = color(x7)
    if x == 8:
        return x8
    x9 = color(x3)
    if x == 9:
        return x9
    O = replace(x5, x8, x9)
    return O

def solve_36d67576(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = compose(x1, normalize)
    if x == 2:
        return x2
    x3 = lbind(rbind, subtract)
    if x == 3:
        return x3
    x4 = rbind(corner, R0)
    if x == 4:
        return x4
    x5 = compose(x3, x4)
    if x == 5:
        return x5
    x6 = astuple(TWO, FOUR)
    if x == 6:
        return x6
    x7 = rbind(contained, x6)
    if x == 7:
        return x7
    x8 = rbind(get_nth_f, F0)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = rbind(sfilter, x9)
    if x == 10:
        return x10
    x11 = chain(x5, x10, normalize)
    if x == 11:
        return x11
    x12 = lbind(occurrences, I)
    if x == 12:
        return x12
    x13 = chain(x12, x10, normalize)
    if x == 13:
        return x13
    x14 = fork(apply, x11, x13)
    if x == 14:
        return x14
    x15 = fork(mapply, x2, x14)
    if x == 15:
        return x15
    x16 = rbind(mir_rot_f, R3)
    if x == 16:
        return x16
    x17 = rbind(mir_rot_f, R1)
    if x == 17:
        return x17
    x18 = astuple(x16, x17)
    if x == 18:
        return x18
    x19 = rbind(mir_rot_f, R0)
    if x == 19:
        return x19
    x20 = rbind(mir_rot_f, R2)
    if x == 20:
        return x20
    x21 = astuple(x19, x20)
    if x == 21:
        return x21
    x22 = combine(x18, x21)
    if x == 22:
        return x22
    x23 = rbind(get_nth_f, L1)
    if x == 23:
        return x23
    x24 = fork(compose, x8, x23)
    if x == 24:
        return x24
    x25 = product(x22, x22)
    if x == 25:
        return x25
    x26 = apply(x24, x25)
    if x == 26:
        return x26
    x27 = totuple(x26)
    if x == 27:
        return x27
    x28 = combine(x22, x27)
    if x == 28:
        return x28
    x29 = o_g(I, R1)
    if x == 29:
        return x29
    x30 = get_arg_rank_f(x29, numcolors_f, F0)
    if x == 30:
        return x30
    x31 = rapply_t(x28, x30)
    if x == 31:
        return x31
    x32 = mapply(x15, x31)
    if x == 32:
        return x32
    O = paint(I, x32)
    return O

def solve_3906de3d(S, I, x=0):
    x1 = rbind(order, identity)
    if x == 1:
        return x1
    x2 = mir_rot_t(I, R6)
    if x == 2:
        return x2
    x3 = switch(x2, ONE, TWO)
    if x == 3:
        return x3
    x4 = apply(x1, x3)
    if x == 4:
        return x4
    x5 = switch(x4, ONE, TWO)
    if x == 5:
        return x5
    O = mir_rot_t(x5, R3)
    return O

def solve_c3f564a4(S, I, x=0):
    x1 = rbind(get_rank, F0)
    if x == 1:
        return x1
    x2 = lbind(apply, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(I, R1)
    if x == 3:
        return x3
    x4 = papply(pair, I, x3)
    if x == 4:
        return x4
    x5 = apply(x2, x4)
    if x == 5:
        return x5
    x6 = asindices(I)
    if x == 6:
        return x6
    x7 = f_ofcolor(x5, ZERO)
    if x == 7:
        return x7
    x8 = difference(x6, x7)
    if x == 8:
        return x8
    x9 = toobject(x8, x5)
    if x == 9:
        return x9
    x10 = lbind(shift, x9)
    if x == 10:
        return x10
    x11 = invert(NINE)
    if x == 11:
        return x11
    x12 = interval(x11, NINE, ONE)
    if x == 12:
        return x12
    x13 = interval(NINE, x11, NEG_ONE)
    if x == 13:
        return x13
    x14 = pair(x12, x13)
    if x == 14:
        return x14
    x15 = mapply(x10, x14)
    if x == 15:
        return x15
    O = paint(x5, x15)
    return O

def solve_b775ac94(S, I, x=0):
    x1 = lbind(index, I)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = lbind(compose, toindices)
    if x == 3:
        return x3
    x4 = rbind(compose, x2)
    if x == 4:
        return x4
    x5 = lbind(rbind, equality)
    if x == 5:
        return x5
    x6 = rbind(get_color_rank_f, F0)
    if x == 6:
        return x6
    x7 = chain(x4, x5, x6)
    if x == 7:
        return x7
    x8 = fork(sfilter, identity, x7)
    if x == 8:
        return x8
    x9 = rbind(compose, initset)
    if x == 9:
        return x9
    x10 = lbind(rbind, adjacent)
    if x == 10:
        return x10
    x11 = fork(difference, identity, x8)
    if x == 11:
        return x11
    x12 = chain(x9, x10, x11)
    if x == 12:
        return x12
    x13 = fork(extract, x8, x12)
    if x == 13:
        return x13
    x14 = fork(insert, x13, x11)
    if x == 14:
        return x14
    x15 = lbind(recolor_i, ZERO)
    if x == 15:
        return x15
    x16 = chain(x15, delta, x14)
    if x == 16:
        return x16
    x17 = fork(combine, x14, x16)
    if x == 17:
        return x17
    x18 = x3(x17)
    if x == 18:
        return x18
    x19 = lbind(compose, x8)
    if x == 19:
        return x19
    x20 = rbind(mir_rot_f, R0)
    if x == 20:
        return x20
    x21 = fork(position, x8, x11)
    if x == 21:
        return x21
    x22 = chain(toivec, x2, x21)
    if x == 22:
        return x22
    x23 = fork(multiply, shape_f, x22)
    if x == 23:
        return x23
    x24 = fork(shift, x20, x23)
    if x == 24:
        return x24
    x25 = x19(x24)
    if x == 25:
        return x25
    x26 = compose(crement, invert)
    if x == 26:
        return x26
    x27 = lbind(compose, x26)
    if x == 27:
        return x27
    x28 = x27(x22)
    if x == 28:
        return x28
    x29 = fork(shift, x25, x28)
    if x == 29:
        return x29
    x30 = x3(x29)
    if x == 30:
        return x30
    x31 = fork(intersection, x18, x30)
    if x == 31:
        return x31
    x32 = chain(x1, x2, x31)
    if x == 32:
        return x32
    x33 = fork(recolor_o, x32, x29)
    if x == 33:
        return x33
    x34 = o_g(I, R3)
    if x == 34:
        return x34
    x35 = mapply(x33, x34)
    if x == 35:
        return x35
    x36 = paint(I, x35)
    if x == 36:
        return x36
    x37 = rbind(mir_rot_f, R2)
    if x == 37:
        return x37
    x38 = rbind(get_nth_f, L1)
    if x == 38:
        return x38
    x39 = chain(tojvec, x38, x21)
    if x == 39:
        return x39
    x40 = fork(multiply, shape_f, x39)
    if x == 40:
        return x40
    x41 = fork(shift, x37, x40)
    if x == 41:
        return x41
    x42 = x19(x41)
    if x == 42:
        return x42
    x43 = x27(x39)
    if x == 43:
        return x43
    x44 = fork(shift, x42, x43)
    if x == 44:
        return x44
    x45 = x3(x44)
    if x == 45:
        return x45
    x46 = fork(intersection, x18, x45)
    if x == 46:
        return x46
    x47 = chain(x1, x2, x46)
    if x == 47:
        return x47
    x48 = fork(recolor_o, x47, x44)
    if x == 48:
        return x48
    x49 = mapply(x48, x34)
    if x == 49:
        return x49
    x50 = paint(x36, x49)
    if x == 50:
        return x50
    x51 = compose(x20, x37)
    if x == 51:
        return x51
    x52 = fork(multiply, shape_f, x21)
    if x == 52:
        return x52
    x53 = fork(shift, x51, x52)
    if x == 53:
        return x53
    x54 = x19(x53)
    if x == 54:
        return x54
    x55 = x27(x21)
    if x == 55:
        return x55
    x56 = fork(shift, x54, x55)
    if x == 56:
        return x56
    x57 = x3(x56)
    if x == 57:
        return x57
    x58 = fork(intersection, x18, x57)
    if x == 58:
        return x58
    x59 = chain(x1, x2, x58)
    if x == 59:
        return x59
    x60 = fork(recolor_o, x59, x56)
    if x == 60:
        return x60
    x61 = mapply(x60, x34)
    if x == 61:
        return x61
    O = paint(x50, x61)
    return O

def solve_3eda0437(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = lbind(occurrences, I)
    if x == 2:
        return x2
    x3 = fork(apply, x1, x2)
    if x == 3:
        return x3
    x4 = lbind(canvas, ZERO)
    if x == 4:
        return x4
    x5 = chain(x3, asobject, x4)
    if x == 5:
        return x5
    x6 = interval(TWO, TEN, ONE)
    if x == 6:
        return x6
    x7 = prapply(astuple, x6, x6)
    if x == 7:
        return x7
    x8 = mapply(x5, x7)
    if x == 8:
        return x8
    x9 = get_arg_rank_f(x8, size, F0)
    if x == 9:
        return x9
    O = fill(I, SIX, x9)
    return O

def solve_484b58aa(S, I, x=0):
    x1 = partition(I)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = merge(x3)
    if x == 4:
        return x4
    x5 = lbind(shift, x4)
    if x == 5:
        return x5
    x6 = power(decrement, TWO)
    if x == 6:
        return x6
    x7 = height_t(I)
    if x == 7:
        return x7
    x8 = x6(x7)
    if x == 8:
        return x8
    x9 = tojvec(x8)
    if x == 9:
        return x9
    x10 = astuple(x7, TWO)
    if x == 10:
        return x10
    x11 = crop(I, x9, x10)
    if x == 11:
        return x11
    x12 = asobject(x11)
    if x == 12:
        return x12
    x13 = vperiod(x12)
    if x == 13:
        return x13
    x14 = width_t(I)
    if x == 14:
        return x14
    x15 = x6(x14)
    if x == 15:
        return x15
    x16 = toivec(x15)
    if x == 16:
        return x16
    x17 = astuple(TWO, x14)
    if x == 17:
        return x17
    x18 = crop(I, x16, x17)
    if x == 18:
        return x18
    x19 = asobject(x18)
    if x == 19:
        return x19
    x20 = hperiod(x19)
    if x == 20:
        return x20
    x21 = astuple(x13, x20)
    if x == 21:
        return x21
    x22 = lbind(multiply, x21)
    if x == 22:
        return x22
    x23 = neighbors(ORIGIN)
    if x == 23:
        return x23
    x24 = mapply(neighbors, x23)
    if x == 24:
        return x24
    x25 = apply(x22, x24)
    if x == 25:
        return x25
    x26 = mapply(x5, x25)
    if x == 26:
        return x26
    O = paint(I, x26)
    return O

def solve_f8c80d96(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x2, width_f, L1)
    if x == 3:
        return x3
    x4 = size_f(x3)
    if x == 4:
        return x4
    x5 = equality(x4, ONE)
    if x == 5:
        return x5
    x6 = branch(x5, identity, outbox)
    if x == 6:
        return x6
    x7 = chain(outbox, outbox, x6)
    if x == 7:
        return x7
    x8 = colorfilter(x2, x1)
    if x == 8:
        return x8
    x9 = get_arg_rank_f(x8, size, F0)
    if x == 9:
        return x9
    x10 = x7(x9)
    if x == 10:
        return x10
    x11 = fill(I, x1, x10)
    if x == 11:
        return x11
    x12 = power(x7, TWO)
    if x == 12:
        return x12
    x13 = x12(x9)
    if x == 13:
        return x13
    x14 = fill(x11, x1, x13)
    if x == 14:
        return x14
    x15 = power(x7, THREE)
    if x == 15:
        return x15
    x16 = x15(x9)
    if x == 16:
        return x16
    x17 = fill(x14, x1, x16)
    if x == 17:
        return x17
    O = replace(x17, ZERO, FIVE)
    return O

def solve_28bf18c6(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    O = hconcat(x3, x3)
    return O

def solve_d90796e8(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = sizefilter(x1, TWO)
    if x == 2:
        return x2
    x3 = lbind(contained, TWO)
    if x == 3:
        return x3
    x4 = compose(x3, palette_f)
    if x == 4:
        return x4
    x5 = mfilter_f(x2, x4)
    if x == 5:
        return x5
    x6 = cover(I, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, F0)
    if x == 7:
        return x7
    x8 = matcher(x7, THREE)
    if x == 8:
        return x8
    x9 = sfilter_f(x5, x8)
    if x == 9:
        return x9
    O = fill(x6, EIGHT, x9)
    return O

def solve_1bfc4729(S, I, x=0):
    x1 = tophalf(I)
    if x == 1:
        return x1
    x2 = get_color_rank_t(x1, L1)
    if x == 2:
        return x2
    x3 = hfrontier(TWO_BY_ZERO)
    if x == 3:
        return x3
    x4 = asindices(I)
    if x == 4:
        return x4
    x5 = box(x4)
    if x == 5:
        return x5
    x6 = combine(x3, x5)
    if x == 6:
        return x6
    x7 = fill(x1, x2, x6)
    if x == 7:
        return x7
    x8 = mir_rot_t(x7, R0)
    if x == 8:
        return x8
    x9 = bottomhalf(I)
    if x == 9:
        return x9
    x10 = get_color_rank_t(x9, L1)
    if x == 10:
        return x10
    x11 = replace(x8, x2, x10)
    if x == 11:
        return x11
    O = vconcat(x7, x11)
    return O

def solve_7837ac64(S, I, x=0):
    x1 = rbind(mir_rot_t, R1)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = lbind(apply, x2)
    if x == 3:
        return x3
    x4 = fgpartition(I)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x4, size, F0)
    if x == 5:
        return x5
    x6 = remove_f(x5, x4)
    if x == 6:
        return x6
    x7 = merge_f(x6)
    if x == 7:
        return x7
    x8 = subgrid(x7, I)
    if x == 8:
        return x8
    x9 = height_t(x8)
    if x == 9:
        return x9
    x10 = o_g(x8, R4)
    if x == 10:
        return x10
    x11 = colorfilter(x10, ZERO)
    if x == 11:
        return x11
    x12 = get_nth_f(x11, F0)
    if x == 12:
        return x12
    x13 = height_f(x12)
    if x == 13:
        return x13
    x14 = increment(x13)
    if x == 14:
        return x14
    x15 = interval(ZERO, x9, x14)
    if x == 15:
        return x15
    x16 = rbind(contained, x15)
    if x == 16:
        return x16
    x17 = rbind(get_nth_f, L1)
    if x == 17:
        return x17
    x18 = chain(flip, x16, x17)
    if x == 18:
        return x18
    x19 = rbind(sfilter, x18)
    if x == 19:
        return x19
    x20 = interval(ZERO, x9, ONE)
    if x == 20:
        return x20
    x21 = rbind(pair, x20)
    if x == 21:
        return x21
    x22 = chain(x3, x19, x21)
    if x == 22:
        return x22
    x23 = compose(x1, x22)
    if x == 23:
        return x23
    x24 = power(x23, TWO)
    if x == 24:
        return x24
    x25 = rbind(toobject, x8)
    if x == 25:
        return x25
    x26 = chain(x25, corners, outbox)
    if x == 26:
        return x26
    x27 = compose(color, x26)
    if x == 27:
        return x27
    x28 = fork(recolor_o, x27, identity)
    if x == 28:
        return x28
    x29 = chain(color, merge, frontiers)
    if x == 29:
        return x29
    x30 = x29(I)
    if x == 30:
        return x30
    x31 = lbind(contained, x30)
    if x == 31:
        return x31
    x32 = chain(x31, palette_f, x26)
    if x == 32:
        return x32
    x33 = compose(flip, x32)
    if x == 33:
        return x33
    x34 = compose(numcolors_f, x26)
    if x == 34:
        return x34
    x35 = matcher(x34, ONE)
    if x == 35:
        return x35
    x36 = fork(both, x33, x35)
    if x == 36:
        return x36
    x37 = sfilter(x11, x36)
    if x == 37:
        return x37
    x38 = mapply(x28, x37)
    if x == 38:
        return x38
    x39 = paint(x8, x38)
    if x == 39:
        return x39
    x40 = x24(x39)
    if x == 40:
        return x40
    O = downscale(x40, x13)
    return O

def solve_8efcae92(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ONE)
    if x == 2:
        return x2
    x3 = compose(size, delta)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x2, x3, F0)
    if x == 4:
        return x4
    O = subgrid(x4, I)
    return O

def solve_6e19193c(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = compose(x2, delta)
    if x == 3:
        return x3
    x4 = rbind(colorcount_f, x1)
    if x == 4:
        return x4
    x5 = matcher(x4, TWO)
    if x == 5:
        return x5
    x6 = rbind(toobject, I)
    if x == 6:
        return x6
    x7 = chain(x5, x6, dneighbors)
    if x == 7:
        return x7
    x8 = rbind(sfilter, x7)
    if x == 8:
        return x8
    x9 = chain(x2, x8, toindices)
    if x == 9:
        return x9
    x10 = fork(subtract, x3, x9)
    if x == 10:
        return x10
    x11 = fork(shoot, x3, x10)
    if x == 11:
        return x11
    x12 = o_g(I, R5)
    if x == 12:
        return x12
    x13 = mapply(x11, x12)
    if x == 13:
        return x13
    x14 = fill(I, x1, x13)
    if x == 14:
        return x14
    x15 = mapply(delta, x12)
    if x == 15:
        return x15
    O = fill(x14, ZERO, x15)
    return O

def solve_39e1d7f9(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = fgpartition(I)
    if x == 2:
        return x2
    x3 = order(x2, height_f)
    if x == 3:
        return x3
    x4 = get_nth_t(x3, L1)
    if x == 4:
        return x4
    x5 = remove_f(x4, x3)
    if x == 5:
        return x5
    x6 = get_nth_t(x5, L1)
    if x == 6:
        return x6
    x7 = color(x6)
    if x == 7:
        return x7
    x8 = colorfilter(x1, x7)
    if x == 8:
        return x8
    x9 = get_color_rank_t(I, F0)
    if x == 9:
        return x9
    x10 = lbind(remove, x9)
    if x == 10:
        return x10
    x11 = chain(size, x10, palette_t)
    if x == 11:
        return x11
    x12 = rbind(toobject, I)
    if x == 12:
        return x12
    x13 = power(outbox, TWO)
    if x == 13:
        return x13
    x14 = chain(x11, x12, x13)
    if x == 14:
        return x14
    x15 = get_arg_rank_f(x8, x14, F0)
    if x == 15:
        return x15
    x16 = corner(x15, R0)
    if x == 16:
        return x16
    x17 = shape_f(x15)
    if x == 17:
        return x17
    x18 = subtract(x16, x17)
    if x == 18:
        return x18
    x19 = decrement(x18)
    if x == 19:
        return x19
    x20 = multiply(x17, THREE)
    if x == 20:
        return x20
    x21 = add(x20, TWO_BY_TWO)
    if x == 21:
        return x21
    x22 = crop(I, x19, x21)
    if x == 22:
        return x22
    x23 = asobject(x22)
    if x == 23:
        return x23
    x24 = lbind(shift, x23)
    if x == 24:
        return x24
    x25 = increment(x17)
    if x == 25:
        return x25
    x26 = rbind(subtract, x25)
    if x == 26:
        return x26
    x27 = rbind(corner, R0)
    if x == 27:
        return x27
    x28 = apply(x27, x8)
    if x == 28:
        return x28
    x29 = apply(x26, x28)
    if x == 29:
        return x29
    x30 = mapply(x24, x29)
    if x == 30:
        return x30
    O = paint(I, x30)
    return O

def solve_e73095fd(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = fork(equality, toindices, backdrop)
    if x == 3:
        return x3
    x4 = sfilter_f(x2, x3)
    if x == 4:
        return x4
    x5 = matcher(size, ZERO)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, FIVE)
    if x == 6:
        return x6
    x7 = rbind(intersection, x6)
    if x == 7:
        return x7
    x8 = lbind(mapply, dneighbors)
    if x == 8:
        return x8
    x9 = chain(x8, corners, outbox)
    if x == 9:
        return x9
    x10 = fork(difference, x9, outbox)
    if x == 10:
        return x10
    x11 = chain(x5, x7, x10)
    if x == 11:
        return x11
    x12 = mfilter_f(x4, x11)
    if x == 12:
        return x12
    O = fill(I, FOUR, x12)
    return O

def solve_9172f3a0(S, I, x=0):
    O = upscale_t(I, THREE)
    return O

def solve_a8c38be5(S, I, x=0):
    x1 = astuple(NINE, NINE)
    if x == 1:
        return x1
    x2 = canvas(FIVE, x1)
    if x == 2:
        return x2
    x3 = rbind(corner, R0)
    if x == 3:
        return x3
    x4 = asindices(x2)
    if x == 4:
        return x4
    x5 = box(x4)
    if x == 5:
        return x5
    x6 = chain(outbox, outbox, initset)
    if x == 6:
        return x6
    x7 = corners(x4)
    if x == 7:
        return x7
    x8 = mapply(x6, x7)
    if x == 8:
        return x8
    x9 = difference(x5, x8)
    if x == 9:
        return x9
    x10 = inbox(x5)
    if x == 10:
        return x10
    x11 = lbind(contained, ZERO)
    if x == 11:
        return x11
    x12 = center(x4)
    if x == 12:
        return x12
    x13 = rbind(subtract, x12)
    if x == 13:
        return x13
    x14 = compose(x11, x13)
    if x == 14:
        return x14
    x15 = sfilter_f(x10, x14)
    if x == 15:
        return x15
    x16 = combine(x9, x15)
    if x == 16:
        return x16
    x17 = fill(x2, ONE, x16)
    if x == 17:
        return x17
    x18 = o_g(x17, R5)
    if x == 18:
        return x18
    x19 = apply(toindices, x18)
    if x == 19:
        return x19
    x20 = lbind(extract, x19)
    if x == 20:
        return x20
    x21 = lbind(matcher, normalize)
    if x == 21:
        return x21
    x22 = chain(x3, x20, x21)
    if x == 22:
        return x22
    x23 = compose(x22, toindices)
    if x == 23:
        return x23
    x24 = fork(shift, identity, x23)
    if x == 24:
        return x24
    x25 = replace(I, FIVE, ZERO)
    if x == 25:
        return x25
    x26 = o_g(x25, R5)
    if x == 26:
        return x26
    x27 = apply(normalize, x26)
    if x == 27:
        return x27
    x28 = mapply(x24, x27)
    if x == 28:
        return x28
    O = paint(x2, x28)
    return O

def solve_90c28cc7(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = dedupe(x3)
    if x == 4:
        return x4
    x5 = mir_rot_t(x4, R4)
    if x == 5:
        return x5
    x6 = dedupe(x5)
    if x == 6:
        return x6
    O = mir_rot_t(x6, R6)
    return O

def solve_444801d8(S, I, x=0):
    x1 = rbind(get_color_rank_f, L1)
    if x == 1:
        return x1
    x2 = rbind(toobject, I)
    if x == 2:
        return x2
    x3 = chain(x1, x2, delta)
    if x == 3:
        return x3
    x4 = rbind(shift, UP)
    if x == 4:
        return x4
    x5 = compose(x4, backdrop)
    if x == 5:
        return x5
    x6 = fork(recolor_i, x3, x5)
    if x == 6:
        return x6
    x7 = o_g(I, R5)
    if x == 7:
        return x7
    x8 = colorfilter(x7, ONE)
    if x == 8:
        return x8
    x9 = mapply(x6, x8)
    if x == 9:
        return x9
    O = underpaint(I, x9)
    return O

def solve_88a62173(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = tophalf(x1)
    if x == 2:
        return x2
    x3 = righthalf(I)
    if x == 3:
        return x3
    x4 = tophalf(x3)
    if x == 4:
        return x4
    x5 = astuple(x2, x4)
    if x == 5:
        return x5
    x6 = bottomhalf(x1)
    if x == 6:
        return x6
    x7 = bottomhalf(x3)
    if x == 7:
        return x7
    x8 = astuple(x6, x7)
    if x == 8:
        return x8
    x9 = combine_t(x5, x8)
    if x == 9:
        return x9
    O = get_common_rank_t(x9, L1)
    return O

def solve_2dc579da(S, I, x=0):
    x1 = rbind(hsplit, TWO)
    if x == 1:
        return x1
    x2 = vsplit(I, TWO)
    if x == 2:
        return x2
    x3 = mapply(x1, x2)
    if x == 3:
        return x3
    O = get_arg_rank_t(x3, numcolors_t, F0)
    return O

def solve_aedd82e4(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, TWO)
    if x == 2:
        return x2
    x3 = sizefilter(x2, ONE)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    O = fill(I, ONE, x4)
    return O

def solve_8f2ea7aa(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = upscale_t(x3, THREE)
    if x == 4:
        return x4
    x5 = hconcat(x3, x3)
    if x == 5:
        return x5
    x6 = hconcat(x5, x3)
    if x == 6:
        return x6
    x7 = vconcat(x6, x6)
    if x == 7:
        return x7
    x8 = vconcat(x7, x6)
    if x == 8:
        return x8
    O = cellwise(x4, x8, ZERO)
    return O

def solve_ddf7fa4f(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = compose(color, x1)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, L1)
    if x == 3:
        return x3
    x4 = fork(recolor_o, x2, x3)
    if x == 4:
        return x4
    x5 = o_g(I, R5)
    if x == 5:
        return x5
    x6 = sizefilter(x5, ONE)
    if x == 6:
        return x6
    x7 = colorfilter(x5, FIVE)
    if x == 7:
        return x7
    x8 = product(x6, x7)
    if x == 8:
        return x8
    x9 = fork(vmatching, x1, x3)
    if x == 9:
        return x9
    x10 = sfilter_f(x8, x9)
    if x == 10:
        return x10
    x11 = mapply(x4, x10)
    if x == 11:
        return x11
    O = paint(I, x11)
    return O

def solve_28e73c20(S, I, x=0):
    x1 = canvas(THREE, UNITY)
    if x == 1:
        return x1
    x2 = lbind(hupscale, x1)
    if x == 2:
        return x2
    x3 = compose(x2, height_t)
    if x == 3:
        return x3
    x4 = rbind(hconcat, x1)
    if x == 4:
        return x4
    x5 = canvas(ZERO, UNITY)
    if x == 5:
        return x5
    x6 = lbind(hupscale, x5)
    if x == 6:
        return x6
    x7 = chain(x6, decrement, height_t)
    if x == 7:
        return x7
    x8 = compose(x4, x7)
    if x == 8:
        return x8
    x9 = rbind(mir_rot_t, R4)
    if x == 9:
        return x9
    x10 = fork(vconcat, x8, x9)
    if x == 10:
        return x10
    x11 = fork(vconcat, x3, x10)
    if x == 11:
        return x11
    x12 = width_t(I)
    if x == 12:
        return x12
    x13 = subtract(x12, FOUR)
    if x == 13:
        return x13
    x14 = power(x11, x13)
    if x == 14:
        return x14
    x15 = even(x12)
    if x == 15:
        return x15
    x16 = upscale_t(x1, FOUR)
    if x == 16:
        return x16
    x17 = astuple(TWO, TWO)
    if x == 17:
        return x17
    x18 = astuple(ONE, TWO)
    if x == 18:
        return x18
    x19 = initset(DOWN)
    if x == 19:
        return x19
    x20 = insert(UNITY, x19)
    if x == 20:
        return x20
    x21 = insert(x18, x20)
    if x == 21:
        return x21
    x22 = insert(x17, x21)
    if x == 22:
        return x22
    x23 = fill(x16, ZERO, x22)
    if x == 23:
        return x23
    x24 = vupscale(x1, FIVE)
    if x == 24:
        return x24
    x25 = hupscale(x24, THREE)
    if x == 25:
        return x25
    x26 = astuple(THREE, ONE)
    if x == 26:
        return x26
    x27 = astuple(TWO, ONE)
    if x == 27:
        return x27
    x28 = insert(x27, x20)
    if x == 28:
        return x28
    x29 = insert(x26, x28)
    if x == 29:
        return x29
    x30 = fill(x25, ZERO, x29)
    if x == 30:
        return x30
    x31 = branch(x15, x23, x30)
    if x == 31:
        return x31
    O = x14(x31)
    return O

def solve_d406998b(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = f_ofcolor(x1, FIVE)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, L1)
    if x == 3:
        return x3
    x4 = compose(even, x3)
    if x == 4:
        return x4
    x5 = sfilter_f(x2, x4)
    if x == 5:
        return x5
    x6 = fill(x1, THREE, x5)
    if x == 6:
        return x6
    O = mir_rot_t(x6, R2)
    return O

def solve_95990924(S, I, x=0):
    x1 = rbind(corner, R0)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = apply(outbox, x2)
    if x == 3:
        return x3
    x4 = apply(x1, x3)
    if x == 4:
        return x4
    x5 = fill(I, ONE, x4)
    if x == 5:
        return x5
    x6 = rbind(corner, R1)
    if x == 6:
        return x6
    x7 = apply(x6, x3)
    if x == 7:
        return x7
    x8 = fill(x5, TWO, x7)
    if x == 8:
        return x8
    x9 = rbind(corner, R2)
    if x == 9:
        return x9
    x10 = apply(x9, x3)
    if x == 10:
        return x10
    x11 = fill(x8, THREE, x10)
    if x == 11:
        return x11
    x12 = rbind(corner, R3)
    if x == 12:
        return x12
    x13 = apply(x12, x3)
    if x == 13:
        return x13
    O = fill(x11, FOUR, x13)
    return O

def solve_dae9d2b5(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = f_ofcolor(x1, FOUR)
    if x == 2:
        return x2
    x3 = righthalf(I)
    if x == 3:
        return x3
    x4 = f_ofcolor(x3, THREE)
    if x == 4:
        return x4
    x5 = combine_f(x2, x4)
    if x == 5:
        return x5
    O = fill(x1, SIX, x5)
    return O

def solve_868de0fa(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = sfilter_f(x1, square_f)
    if x == 2:
        return x2
    x3 = compose(even, height_f)
    if x == 3:
        return x3
    x4 = sfilter_f(x2, x3)
    if x == 4:
        return x4
    x5 = merge_f(x4)
    if x == 5:
        return x5
    x6 = fill(I, TWO, x5)
    if x == 6:
        return x6
    x7 = difference(x2, x4)
    if x == 7:
        return x7
    x8 = merge_f(x7)
    if x == 8:
        return x8
    O = fill(x6, SEVEN, x8)
    return O

def solve_c8cbb738(S, I, x=0):
    x1 = get_color_rank_t(I, F0)
    if x == 1:
        return x1
    x2 = fgpartition(I)
    if x == 2:
        return x2
    x3 = get_val_rank_f(x2, shape_f, F0)
    if x == 3:
        return x3
    x4 = canvas(x1, x3)
    if x == 4:
        return x4
    x5 = lbind(subtract, x3)
    if x == 5:
        return x5
    x6 = chain(halve, x5, shape_f)
    if x == 6:
        return x6
    x7 = fork(shift, identity, x6)
    if x == 7:
        return x7
    x8 = apply(normalize, x2)
    if x == 8:
        return x8
    x9 = mapply(x7, x8)
    if x == 9:
        return x9
    O = paint(x4, x9)
    return O

def solve_d2abd087(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = matcher(size, SIX)
    if x == 2:
        return x2
    x3 = mfilter_f(x1, x2)
    if x == 3:
        return x3
    x4 = fill(I, TWO, x3)
    if x == 4:
        return x4
    x5 = compose(flip, x2)
    if x == 5:
        return x5
    x6 = mfilter_f(x1, x5)
    if x == 6:
        return x6
    O = fill(x4, ONE, x6)
    return O

def solve_5614dbcf(S, I, x=0):
    x1 = replace(I, FIVE, ZERO)
    if x == 1:
        return x1
    O = downscale(x1, THREE)
    return O

def solve_a416b8f3(S, I, x=0):
    O = hconcat(I, I)
    return O

def solve_27a28665(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = get_val_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = equality(x2, FIVE)
    if x == 3:
        return x3
    x4 = equality(x2, FOUR)
    if x == 4:
        return x4
    x5 = equality(x2, ONE)
    if x == 5:
        return x5
    x6 = branch(x5, TWO, ONE)
    if x == 6:
        return x6
    x7 = branch(x4, THREE, x6)
    if x == 7:
        return x7
    x8 = branch(x3, SIX, x7)
    if x == 8:
        return x8
    O = canvas(x8, UNITY)
    return O

def solve_e48d4e1a(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, FIVE)
    if x == 3:
        return x3
    x4 = fill(I, ZERO, x3)
    if x == 4:
        return x4
    x5 = get_color_rank_t(x4, L1)
    if x == 5:
        return x5
    x6 = fork(combine, vfrontier, hfrontier)
    if x == 6:
        return x6
    x7 = size_f(x3)
    if x == 7:
        return x7
    x8 = multiply(DOWN_LEFT, x7)
    if x == 8:
        return x8
    x9 = f_ofcolor(I, x5)
    if x == 9:
        return x9
    x10 = rbind(colorcount_f, x5)
    if x == 10:
        return x10
    x11 = rbind(toobject, I)
    if x == 11:
        return x11
    x12 = chain(x10, x11, dneighbors)
    if x == 12:
        return x12
    x13 = matcher(x12, FOUR)
    if x == 13:
        return x13
    x14 = extract(x9, x13)
    if x == 14:
        return x14
    x15 = add(x8, x14)
    if x == 15:
        return x15
    x16 = x6(x15)
    if x == 16:
        return x16
    O = fill(x2, x5, x16)
    return O

def solve_272f95fa(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = apply(toindices, x2)
    if x == 3:
        return x3
    x4 = rbind(bordering, I)
    if x == 4:
        return x4
    x5 = compose(flip, x4)
    if x == 5:
        return x5
    x6 = extract(x3, x5)
    if x == 6:
        return x6
    x7 = fill(I, SIX, x6)
    if x == 7:
        return x7
    x8 = remove_f(x6, x3)
    if x == 8:
        return x8
    x9 = lbind(vmatching, x6)
    if x == 9:
        return x9
    x10 = sfilter_f(x8, x9)
    if x == 10:
        return x10
    x11 = rbind(col_row, R1)
    if x == 11:
        return x11
    x12 = get_arg_rank_f(x10, x11, L1)
    if x == 12:
        return x12
    x13 = fill(x7, TWO, x12)
    if x == 13:
        return x13
    x14 = get_arg_rank_f(x10, x11, F0)
    if x == 14:
        return x14
    x15 = fill(x13, ONE, x14)
    if x == 15:
        return x15
    x16 = lbind(hmatching, x6)
    if x == 16:
        return x16
    x17 = sfilter_f(x8, x16)
    if x == 17:
        return x17
    x18 = rbind(col_row, R2)
    if x == 18:
        return x18
    x19 = get_arg_rank_f(x17, x18, L1)
    if x == 19:
        return x19
    x20 = fill(x15, FOUR, x19)
    if x == 20:
        return x20
    x21 = get_arg_rank_f(x17, x18, F0)
    if x == 21:
        return x21
    O = fill(x20, THREE, x21)
    return O

def solve_447fd412(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = lbind(apply, increment)
    if x == 2:
        return x2
    x3 = lbind(rbind, subtract)
    if x == 3:
        return x3
    x4 = rbind(corner, R0)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, F0)
    if x == 5:
        return x5
    x6 = lbind(matcher, x5)
    if x == 6:
        return x6
    x7 = rbind(get_color_rank_f, F0)
    if x == 7:
        return x7
    x8 = compose(x6, x7)
    if x == 8:
        return x8
    x9 = fork(sfilter, identity, x8)
    if x == 9:
        return x9
    x10 = fork(difference, identity, x9)
    if x == 10:
        return x10
    x11 = chain(x3, x4, x10)
    if x == 11:
        return x11
    x12 = lbind(occurrences, I)
    if x == 12:
        return x12
    x13 = lbind(recolor_i, ZERO)
    if x == 13:
        return x13
    x14 = compose(x13, outbox)
    if x == 14:
        return x14
    x15 = fork(combine, identity, x14)
    if x == 15:
        return x15
    x16 = chain(x12, x15, x10)
    if x == 16:
        return x16
    x17 = fork(apply, x11, x16)
    if x == 17:
        return x17
    x18 = compose(x2, x17)
    if x == 18:
        return x18
    x19 = fork(mapply, x1, x18)
    if x == 19:
        return x19
    x20 = lbind(rbind, upscale_f)
    if x == 20:
        return x20
    x21 = interval(ONE, FOUR, ONE)
    if x == 21:
        return x21
    x22 = apply(x20, x21)
    if x == 22:
        return x22
    x23 = o_g(I, R3)
    if x == 23:
        return x23
    x24 = get_arg_rank_f(x23, numcolors_f, F0)
    if x == 24:
        return x24
    x25 = normalize(x24)
    if x == 25:
        return x25
    x26 = rapply_t(x22, x25)
    if x == 26:
        return x26
    x27 = mapply(x19, x26)
    if x == 27:
        return x27
    O = paint(I, x27)
    return O

def solve_1caeab9d(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = cover(I, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, ONE)
    if x == 4:
        return x4
    x5 = col_row(x4, R0)
    if x == 5:
        return x5
    x6 = lbind(subtract, x5)
    if x == 6:
        return x6
    x7 = rbind(col_row, R0)
    if x == 7:
        return x7
    x8 = chain(toivec, x6, x7)
    if x == 8:
        return x8
    x9 = fork(shift, identity, x8)
    if x == 9:
        return x9
    x10 = mapply(x9, x1)
    if x == 10:
        return x10
    O = paint(x3, x10)
    return O

def solve_06df4c85(S, I, x=0):
    x1 = rbind(get_nth_f, L1)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = power(x1, TWO)
    if x == 4:
        return x4
    x5 = fork(connect, x3, x4)
    if x == 5:
        return x5
    x6 = fork(recolor_i, color, x5)
    if x == 6:
        return x6
    x7 = partition(I)
    if x == 7:
        return x7
    x8 = get_arg_rank_f(x7, size, F0)
    if x == 8:
        return x8
    x9 = colorfilter(x7, ZERO)
    if x == 9:
        return x9
    x10 = difference(x7, x9)
    if x == 10:
        return x10
    x11 = remove_f(x8, x10)
    if x == 11:
        return x11
    x12 = merge_f(x11)
    if x == 12:
        return x12
    x13 = product(x12, x12)
    if x == 13:
        return x13
    x14 = power(x2, TWO)
    if x == 14:
        return x14
    x15 = compose(x2, x1)
    if x == 15:
        return x15
    x16 = fork(equality, x14, x15)
    if x == 16:
        return x16
    x17 = sfilter_f(x13, x16)
    if x == 17:
        return x17
    x18 = apply(x6, x17)
    if x == 18:
        return x18
    x19 = fork(either, vline_o, hline_o)
    if x == 19:
        return x19
    x20 = mfilter_f(x18, x19)
    if x == 20:
        return x20
    x21 = paint(I, x20)
    if x == 21:
        return x21
    x22 = get_color_rank_t(I, F0)
    if x == 22:
        return x22
    x23 = f_ofcolor(I, x22)
    if x == 23:
        return x23
    O = fill(x21, x22, x23)
    return O

def solve_f1cefba8(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = remove(ZERO, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R1)
    if x == 3:
        return x3
    x4 = get_nth_f(x3, F0)
    if x == 4:
        return x4
    x5 = subgrid(x4, I)
    if x == 5:
        return x5
    x6 = power(trim, TWO)
    if x == 6:
        return x6
    x7 = x6(x5)
    if x == 7:
        return x7
    x8 = asindices(x7)
    if x == 8:
        return x8
    x9 = shift(x8, TWO_BY_TWO)
    if x == 9:
        return x9
    x10 = fill(x5, ZERO, x9)
    if x == 10:
        return x10
    x11 = get_color_rank_t(x10, L1)
    if x == 11:
        return x11
    x12 = other_f(x2, x11)
    if x == 12:
        return x12
    x13 = f_ofcolor(x10, x11)
    if x == 13:
        return x13
    x14 = corner(x4, R0)
    if x == 14:
        return x14
    x15 = shift(x13, x14)
    if x == 15:
        return x15
    x16 = rbind(get_nth_f, F0)
    if x == 16:
        return x16
    x17 = f_ofcolor(I, x11)
    if x == 17:
        return x17
    x18 = col_row(x17, R1)
    if x == 18:
        return x18
    x19 = matcher(x16, x18)
    if x == 19:
        return x19
    x20 = col_row(x17, R0)
    if x == 20:
        return x20
    x21 = matcher(x16, x20)
    if x == 21:
        return x21
    x22 = fork(either, x19, x21)
    if x == 22:
        return x22
    x23 = sfilter_f(x15, x22)
    if x == 23:
        return x23
    x24 = mapply(vfrontier, x23)
    if x == 24:
        return x24
    x25 = difference(x15, x23)
    if x == 25:
        return x25
    x26 = mapply(hfrontier, x25)
    if x == 26:
        return x26
    x27 = combine_f(x24, x26)
    if x == 27:
        return x27
    x28 = fill(I, x12, x27)
    if x == 28:
        return x28
    x29 = f_ofcolor(I, ZERO)
    if x == 29:
        return x29
    x30 = intersection(x29, x27)
    if x == 30:
        return x30
    O = fill(x28, x11, x30)
    return O

def solve_0962bcdd(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = replace(I, ZERO, x1)
    if x == 2:
        return x2
    x3 = get_color_rank_t(x2, L1)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, x3)
    if x == 4:
        return x4
    x5 = mapply(dneighbors, x4)
    if x == 5:
        return x5
    x6 = fill(I, x3, x5)
    if x == 6:
        return x6
    x7 = rbind(corner, R0)
    if x == 7:
        return x7
    x8 = rbind(corner, R3)
    if x == 8:
        return x8
    x9 = fork(connect, x7, x8)
    if x == 9:
        return x9
    x10 = rbind(corner, R2)
    if x == 10:
        return x10
    x11 = rbind(corner, R1)
    if x == 11:
        return x11
    x12 = fork(connect, x10, x11)
    if x == 12:
        return x12
    x13 = fork(combine, x9, x12)
    if x == 13:
        return x13
    x14 = o_g(x6, R3)
    if x == 14:
        return x14
    x15 = mapply(x13, x14)
    if x == 15:
        return x15
    O = fill(x6, x1, x15)
    return O

def solve_834ec97d(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = fill(I, ZERO, x2)
    if x == 3:
        return x3
    x4 = shift(x2, DOWN)
    if x == 4:
        return x4
    x5 = paint(x3, x4)
    if x == 5:
        return x5
    x6 = asindices(I)
    if x == 6:
        return x6
    x7 = col_row(x4, R1)
    if x == 7:
        return x7
    x8 = lbind(greater, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_f, F0)
    if x == 9:
        return x9
    x10 = compose(x8, x9)
    if x == 10:
        return x10
    x11 = sfilter_f(x6, x10)
    if x == 11:
        return x11
    x12 = col_row(x4, R2)
    if x == 12:
        return x12
    x13 = subtract(x12, TEN)
    if x == 13:
        return x13
    x14 = add(x12, TEN)
    if x == 14:
        return x14
    x15 = interval(x13, x14, TWO)
    if x == 15:
        return x15
    x16 = rbind(contained, x15)
    if x == 16:
        return x16
    x17 = rbind(get_nth_f, L1)
    if x == 17:
        return x17
    x18 = compose(x16, x17)
    if x == 18:
        return x18
    x19 = sfilter_f(x11, x18)
    if x == 19:
        return x19
    O = fill(x5, FOUR, x19)
    return O

def solve_f2829549(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = shape_t(x1)
    if x == 2:
        return x2
    x3 = canvas(ZERO, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(x1, ZERO)
    if x == 4:
        return x4
    x5 = righthalf(I)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, ZERO)
    if x == 6:
        return x6
    x7 = intersection(x4, x6)
    if x == 7:
        return x7
    O = fill(x3, THREE, x7)
    return O

def solve_63613498(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = compose(toindices, normalize)
    if x == 2:
        return x2
    x3 = crop(I, ORIGIN, THREE_BY_THREE)
    if x == 3:
        return x3
    x4 = asindices(x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(x3, ZERO)
    if x == 5:
        return x5
    x6 = difference(x4, x5)
    if x == 6:
        return x6
    x7 = normalize(x6)
    if x == 7:
        return x7
    x8 = matcher(x2, x7)
    if x == 8:
        return x8
    x9 = mfilter_f(x1, x8)
    if x == 9:
        return x9
    x10 = fill(I, FIVE, x9)
    if x == 10:
        return x10
    x11 = asobject(x3)
    if x == 11:
        return x11
    O = paint(x10, x11)
    return O

def solve_b91ae062(S, I, x=0):
    x1 = numcolors_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    O = upscale_t(I, x2)
    return O

def solve_f25fbde4(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    O = upscale_t(x3, TWO)
    return O

def solve_3f7978a0(S, I, x=0):
    x1 = fgpartition(I)
    if x == 1:
        return x1
    x2 = matcher(color, FIVE)
    if x == 2:
        return x2
    x3 = extract(x1, x2)
    if x == 3:
        return x3
    x4 = corner(x3, R0)
    if x == 4:
        return x4
    x5 = subtract(x4, DOWN)
    if x == 5:
        return x5
    x6 = shape_f(x3)
    if x == 6:
        return x6
    x7 = add(x6, TWO_BY_ZERO)
    if x == 7:
        return x7
    O = crop(I, x5, x7)
    return O

def solve_137eaa0f(S, I, x=0):
    x1 = canvas(ZERO, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = matcher(x2, FIVE)
    if x == 3:
        return x3
    x4 = rbind(sfilter, x3)
    if x == 4:
        return x4
    x5 = chain(invert, center, x4)
    if x == 5:
        return x5
    x6 = fork(shift, identity, x5)
    if x == 6:
        return x6
    x7 = o_g(I, R3)
    if x == 7:
        return x7
    x8 = mapply(x6, x7)
    if x == 8:
        return x8
    x9 = shift(x8, UNITY)
    if x == 9:
        return x9
    O = paint(x1, x9)
    return O

def solve_321b1fc6(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = colorfilter(x1, EIGHT)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = get_nth_f(x3, F0)
    if x == 4:
        return x4
    x5 = cover(I, x4)
    if x == 5:
        return x5
    x6 = normalize(x4)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = rbind(corner, R0)
    if x == 8:
        return x8
    x9 = apply(x8, x2)
    if x == 9:
        return x9
    x10 = mapply(x7, x9)
    if x == 10:
        return x10
    O = paint(x5, x10)
    return O

def solve_c0f76784(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = sfilter_f(x2, square_f)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    x5 = fill(I, SEVEN, x4)
    if x == 5:
        return x5
    x6 = get_arg_rank_f(x3, size, F0)
    if x == 6:
        return x6
    x7 = fill(x5, EIGHT, x6)
    if x == 7:
        return x7
    x8 = sizefilter(x3, ONE)
    if x == 8:
        return x8
    x9 = merge_f(x8)
    if x == 9:
        return x9
    O = fill(x7, SIX, x9)
    return O

def solve_0d3d703e(S, I, x=0):
    x1 = switch(I, THREE, FOUR)
    if x == 1:
        return x1
    x2 = switch(x1, EIGHT, NINE)
    if x == 2:
        return x2
    x3 = switch(x2, TWO, SIX)
    if x == 3:
        return x3
    O = switch(x3, ONE, FIVE)
    return O

def solve_b60334d2(S, I, x=0):
    x1 = replace(I, FIVE, ZERO)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, FIVE)
    if x == 2:
        return x2
    x3 = mapply(dneighbors, x2)
    if x == 3:
        return x3
    x4 = fill(x1, ONE, x3)
    if x == 4:
        return x4
    x5 = mapply(ineighbors, x2)
    if x == 5:
        return x5
    O = fill(x4, FIVE, x5)
    return O

def solve_25ff71a9(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    O = move(I, x2, DOWN)
    return O

def solve_67385a82(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, THREE)
    if x == 2:
        return x2
    x3 = sizefilter(x2, ONE)
    if x == 3:
        return x3
    x4 = difference(x2, x3)
    if x == 4:
        return x4
    x5 = merge_f(x4)
    if x == 5:
        return x5
    O = fill(I, EIGHT, x5)
    return O

def solve_3befdf3e(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = palette_t(I)
    if x == 2:
        return x2
    x3 = remove(ZERO, x2)
    if x == 3:
        return x3
    x4 = other_f(x3, x1)
    if x == 4:
        return x4
    x5 = switch(I, x1, x4)
    if x == 5:
        return x5
    x6 = rbind(get_nth_f, F0)
    if x == 6:
        return x6
    x7 = lbind(power, outbox)
    if x == 7:
        return x7
    x8 = compose(width_f, inbox)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = initset(x9)
    if x == 10:
        return x10
    x11 = lbind(rapply, x10)
    if x == 11:
        return x11
    x12 = chain(initset, x6, x11)
    if x == 12:
        return x12
    x13 = fork(rapply, x12, identity)
    if x == 13:
        return x13
    x14 = compose(x6, x13)
    if x == 14:
        return x14
    x15 = compose(backdrop, x14)
    if x == 15:
        return x15
    x16 = o_g(I, R1)
    if x == 16:
        return x16
    x17 = mapply(x15, x16)
    if x == 17:
        return x17
    x18 = underfill(x5, x4, x17)
    if x == 18:
        return x18
    x19 = lbind(chain, backdrop)
    if x == 19:
        return x19
    x20 = lbind(x19, inbox)
    if x == 20:
        return x20
    x21 = compose(x20, x9)
    if x == 21:
        return x21
    x22 = lbind(apply, initset)
    if x == 22:
        return x22
    x23 = chain(x22, corners, x15)
    if x == 23:
        return x23
    x24 = fork(mapply, x21, x23)
    if x == 24:
        return x24
    x25 = fork(intersection, x15, x24)
    if x == 25:
        return x25
    x26 = mapply(x25, x16)
    if x == 26:
        return x26
    O = fill(x18, ZERO, x26)
    return O

def solve_dc0a314f(S, I, x=0):
    x1 = f_ofcolor(I, THREE)
    if x == 1:
        return x1
    x2 = rbind(get_rank, F0)
    if x == 2:
        return x2
    x3 = lbind(apply, x2)
    if x == 3:
        return x3
    x4 = replace(I, THREE, ZERO)
    if x == 4:
        return x4
    x5 = mir_rot_t(x4, R1)
    if x == 5:
        return x5
    x6 = papply(pair, x4, x5)
    if x == 6:
        return x6
    x7 = apply(x3, x6)
    if x == 7:
        return x7
    x8 = mir_rot_t(x7, R3)
    if x == 8:
        return x8
    x9 = papply(pair, x7, x8)
    if x == 9:
        return x9
    x10 = apply(x3, x9)
    if x == 10:
        return x10
    O = subgrid(x1, x10)
    return O

def solve_0a938d79(S, I, x=0):
    x1 = portrait_t(I)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_t, R1)
    if x == 2:
        return x2
    x3 = branch(x1, x2, identity)
    if x == 3:
        return x3
    x4 = x3(I)
    if x == 4:
        return x4
    x5 = compose(vfrontier, tojvec)
    if x == 5:
        return x5
    x6 = lbind(mapply, x5)
    if x == 6:
        return x6
    x7 = chain(double, decrement, width_f)
    if x == 7:
        return x7
    x8 = fgpartition(x4)
    if x == 8:
        return x8
    x9 = merge(x8)
    if x == 9:
        return x9
    x10 = x7(x9)
    if x == 10:
        return x10
    x11 = rbind(interval, x10)
    if x == 11:
        return x11
    x12 = width_t(x4)
    if x == 12:
        return x12
    x13 = rbind(x11, x12)
    if x == 13:
        return x13
    x14 = rbind(col_row, R2)
    if x == 14:
        return x14
    x15 = chain(x6, x13, x14)
    if x == 15:
        return x15
    x16 = fork(recolor_i, color, x15)
    if x == 16:
        return x16
    x17 = mapply(x16, x8)
    if x == 17:
        return x17
    x18 = paint(x4, x17)
    if x == 18:
        return x18
    O = x3(x18)
    return O

def solve_694f12f3(S, I, x=0):
    x1 = compose(backdrop, inbox)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = colorfilter(x2, FOUR)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, L1)
    if x == 4:
        return x4
    x5 = x1(x4)
    if x == 5:
        return x5
    x6 = fill(I, ONE, x5)
    if x == 6:
        return x6
    x7 = get_arg_rank_f(x3, size, F0)
    if x == 7:
        return x7
    x8 = x1(x7)
    if x == 8:
        return x8
    O = fill(x6, TWO, x8)
    return O

def solve_bda2d7a6(S, I, x=0):
    x1 = partition(I)
    if x == 1:
        return x1
    x2 = order(x1, size)
    if x == 2:
        return x2
    x3 = apply(color, x2)
    if x == 3:
        return x3
    x4 = get_nth_t(x2, L1)
    if x == 4:
        return x4
    x5 = repeat(x4, ONE)
    if x == 5:
        return x5
    x6 = remove_f(x4, x2)
    if x == 6:
        return x6
    x7 = combine_t(x5, x6)
    if x == 7:
        return x7
    x8 = mpapply(recolor_o, x3, x7)
    if x == 8:
        return x8
    O = paint(I, x8)
    return O

def solve_239be575(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = lbind(contained, TWO)
    if x == 2:
        return x2
    x3 = compose(x2, palette_f)
    if x == 3:
        return x3
    x4 = sfilter_f(x1, x3)
    if x == 4:
        return x4
    x5 = size_f(x4)
    if x == 5:
        return x5
    x6 = greater(x5, ONE)
    if x == 6:
        return x6
    x7 = branch(x6, ZERO, EIGHT)
    if x == 7:
        return x7
    O = canvas(x7, UNITY)
    return O

def solve_ae3edfdc(S, I, x=0):
    x1 = replace(I, THREE, ZERO)
    if x == 1:
        return x1
    x2 = replace(x1, SEVEN, ZERO)
    if x == 2:
        return x2
    x3 = lbind(rbind, gravitate)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, F0)
    if x == 4:
        return x4
    x5 = o_g(I, R5)
    if x == 5:
        return x5
    x6 = lbind(colorfilter, x5)
    if x == 6:
        return x6
    x7 = chain(x3, x4, x6)
    if x == 7:
        return x7
    x8 = x7(TWO)
    if x == 8:
        return x8
    x9 = fork(shift, identity, x8)
    if x == 9:
        return x9
    x10 = x6(THREE)
    if x == 10:
        return x10
    x11 = mapply(x9, x10)
    if x == 11:
        return x11
    x12 = paint(x2, x11)
    if x == 12:
        return x12
    x13 = x7(ONE)
    if x == 13:
        return x13
    x14 = fork(shift, identity, x13)
    if x == 14:
        return x14
    x15 = x6(SEVEN)
    if x == 15:
        return x15
    x16 = mapply(x14, x15)
    if x == 16:
        return x16
    O = paint(x12, x16)
    return O

def solve_4612dd53(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = box(x1)
    if x == 2:
        return x2
    x3 = fill(I, TWO, x2)
    if x == 3:
        return x3
    x4 = subgrid(x1, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(x4, ONE)
    if x == 5:
        return x5
    x6 = mapply(vfrontier, x5)
    if x == 6:
        return x6
    x7 = size_f(x6)
    if x == 7:
        return x7
    x8 = mapply(hfrontier, x5)
    if x == 8:
        return x8
    x9 = size_f(x8)
    if x == 9:
        return x9
    x10 = greater(x7, x9)
    if x == 10:
        return x10
    x11 = branch(x10, x8, x6)
    if x == 11:
        return x11
    x12 = fill(x4, TWO, x11)
    if x == 12:
        return x12
    x13 = f_ofcolor(x12, TWO)
    if x == 13:
        return x13
    x14 = corner(x1, R0)
    if x == 14:
        return x14
    x15 = shift(x13, x14)
    if x == 15:
        return x15
    O = underfill(I, TWO, x15)
    return O

def solve_1c786137(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, height_f, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    O = trim(x3)
    return O

def solve_0520fde7(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = lefthalf(x1)
    if x == 2:
        return x2
    x3 = righthalf(x1)
    if x == 3:
        return x3
    x4 = mir_rot_t(x3, R2)
    if x == 4:
        return x4
    x5 = cellwise(x2, x4, ZERO)
    if x == 5:
        return x5
    O = replace(x5, ONE, TWO)
    return O

def solve_54d9e175(S, I, x=0):
    x1 = compose(neighbors, center)
    if x == 1:
        return x1
    x2 = fork(recolor_i, color, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = sizefilter(x3, ONE)
    if x == 4:
        return x4
    x5 = mapply(x2, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = replace(x6, ONE, SIX)
    if x == 7:
        return x7
    x8 = replace(x7, TWO, SEVEN)
    if x == 8:
        return x8
    x9 = replace(x8, THREE, EIGHT)
    if x == 9:
        return x9
    O = replace(x9, FOUR, NINE)
    return O

def solve_44f52bb0(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = equality(x1, I)
    if x == 2:
        return x2
    x3 = branch(x2, ONE, SEVEN)
    if x == 3:
        return x3
    O = canvas(x3, UNITY)
    return O

def solve_1e0a9b12(S, I, x=0):
    x1 = rbind(order, identity)
    if x == 1:
        return x1
    x2 = mir_rot_t(I, R6)
    if x == 2:
        return x2
    x3 = apply(x1, x2)
    if x == 3:
        return x3
    O = mir_rot_t(x3, R4)
    return O

def solve_eb5a1d5d(S, I, x=0):
    x1 = rbind(mir_rot_t, R0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = fork(remove, x2, identity)
    if x == 3:
        return x3
    x4 = compose(x1, x3)
    if x == 4:
        return x4
    x5 = fork(vconcat, identity, x4)
    if x == 5:
        return x5
    x6 = rbind(mir_rot_t, R1)
    if x == 6:
        return x6
    x7 = compose(x6, dedupe)
    if x == 7:
        return x7
    x8 = x7(I)
    if x == 8:
        return x8
    x9 = x7(x8)
    if x == 9:
        return x9
    x10 = x5(x9)
    if x == 10:
        return x10
    x11 = mir_rot_t(x10, R1)
    if x == 11:
        return x11
    O = x5(x11)
    return O

def solve_7e0986d6(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = replace(I, x1, ZERO)
    if x == 2:
        return x2
    x3 = get_color_rank_t(x2, L1)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, x1)
    if x == 4:
        return x4
    x5 = rbind(colorcount_f, x3)
    if x == 5:
        return x5
    x6 = chain(positive, decrement, x5)
    if x == 6:
        return x6
    x7 = rbind(toobject, x2)
    if x == 7:
        return x7
    x8 = chain(x6, x7, dneighbors)
    if x == 8:
        return x8
    x9 = sfilter_f(x4, x8)
    if x == 9:
        return x9
    O = fill(x2, x3, x9)
    return O

def solve_5daaa586(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = rbind(bordering, I)
    if x == 3:
        return x3
    x4 = compose(flip, x3)
    if x == 4:
        return x4
    x5 = extract(x2, x4)
    if x == 5:
        return x5
    x6 = outbox(x5)
    if x == 6:
        return x6
    x7 = subgrid(x6, I)
    if x == 7:
        return x7
    x8 = fgpartition(x7)
    if x == 8:
        return x8
    x9 = get_arg_rank_f(x8, size, F0)
    if x == 9:
        return x9
    x10 = color(x9)
    if x == 10:
        return x10
    x11 = toindices(x9)
    if x == 11:
        return x11
    x12 = prapply(connect, x11, x11)
    if x == 12:
        return x12
    x13 = mfilter_f(x12, vline_i)
    if x == 13:
        return x13
    x14 = size_f(x13)
    if x == 14:
        return x14
    x15 = mfilter_f(x12, hline_i)
    if x == 15:
        return x15
    x16 = size_f(x15)
    if x == 16:
        return x16
    x17 = greater(x14, x16)
    if x == 17:
        return x17
    x18 = branch(x17, x13, x15)
    if x == 18:
        return x18
    O = fill(x7, x10, x18)
    return O

def solve_85c4e7cd(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = compose(invert, size)
    if x == 2:
        return x2
    x3 = order(x1, x2)
    if x == 3:
        return x3
    x4 = apply(color, x3)
    if x == 4:
        return x4
    x5 = order(x1, size)
    if x == 5:
        return x5
    x6 = mpapply(recolor_o, x4, x5)
    if x == 6:
        return x6
    O = paint(I, x6)
    return O

def solve_32597951(S, I, x=0):
    x1 = f_ofcolor(I, EIGHT)
    if x == 1:
        return x1
    x2 = delta(x1)
    if x == 2:
        return x2
    O = fill(I, THREE, x2)
    return O

def solve_2dd70a9a(S, I, x=0):
    x1 = f_ofcolor(I, THREE)
    if x == 1:
        return x1
    x2 = vline_i(x1)
    if x == 2:
        return x2
    x3 = rbind(col_row, R1)
    if x == 3:
        return x3
    x4 = rbind(col_row, R3)
    if x == 4:
        return x4
    x5 = branch(x2, x3, x4)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, TWO)
    if x == 6:
        return x6
    x7 = x5(x6)
    if x == 7:
        return x7
    x8 = x5(x1)
    if x == 8:
        return x8
    x9 = greater(x7, x8)
    if x == 9:
        return x9
    x10 = both(x2, x9)
    if x == 10:
        return x10
    x11 = rbind(col_row, R0)
    if x == 11:
        return x11
    x12 = branch(x10, x11, x3)
    if x == 12:
        return x12
    x13 = x12(x1)
    if x == 13:
        return x13
    x14 = rbind(col_row, R2)
    if x == 14:
        return x14
    x15 = branch(x2, x14, x4)
    if x == 15:
        return x15
    x16 = x15(x1)
    if x == 16:
        return x16
    x17 = astuple(x13, x16)
    if x == 17:
        return x17
    x18 = other_f(x1, x17)
    if x == 18:
        return x18
    x19 = subtract(x17, x18)
    if x == 19:
        return x19
    x20 = shoot(x17, x19)
    if x == 20:
        return x20
    x21 = underfill(I, ONE, x20)
    if x == 21:
        return x21
    x22 = o_g(x21, R4)
    if x == 22:
        return x22
    x23 = colorfilter(x22, ONE)
    if x == 23:
        return x23
    x24 = rbind(adjacent, x1)
    if x == 24:
        return x24
    x25 = sfilter_f(x23, x24)
    if x == 25:
        return x25
    x26 = difference(x23, x25)
    if x == 26:
        return x26
    x27 = merge_f(x26)
    if x == 27:
        return x27
    x28 = cover(x21, x27)
    if x == 28:
        return x28
    x29 = f_ofcolor(x28, ONE)
    if x == 29:
        return x29
    x30 = initset(x17)
    if x == 30:
        return x30
    x31 = rbind(manhattan, x30)
    if x == 31:
        return x31
    x32 = compose(x31, initset)
    if x == 32:
        return x32
    x33 = get_arg_rank_f(x29, x32, F0)
    if x == 33:
        return x33
    x34 = initset(x33)
    if x == 34:
        return x34
    x35 = vline_i(x6)
    if x == 35:
        return x35
    x36 = center(x6)
    if x == 36:
        return x36
    x37 = shoot(x36, DOWN)
    if x == 37:
        return x37
    x38 = shoot(x36, UP)
    if x == 38:
        return x38
    x39 = combine(x37, x38)
    if x == 39:
        return x39
    x40 = shoot(x36, LEFT)
    if x == 40:
        return x40
    x41 = shoot(x36, RIGHT)
    if x == 41:
        return x41
    x42 = combine(x40, x41)
    if x == 42:
        return x42
    x43 = branch(x35, x39, x42)
    if x == 43:
        return x43
    x44 = gravitate(x34, x43)
    if x == 44:
        return x44
    x45 = crement(x44)
    if x == 45:
        return x45
    x46 = add(x33, x45)
    if x == 46:
        return x46
    x47 = connect(x33, x46)
    if x == 47:
        return x47
    x48 = fill(x28, ONE, x47)
    if x == 48:
        return x48
    x49 = connect(x46, x36)
    if x == 49:
        return x49
    x50 = underfill(x48, ONE, x49)
    if x == 50:
        return x50
    O = replace(x50, ONE, THREE)
    return O

def solve_4938f0c2(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = size_f(x1)
    if x == 2:
        return x2
    x3 = greater(x2, FOUR)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, TWO)
    if x == 4:
        return x4
    x5 = mir_rot_f(x4, R2)
    if x == 5:
        return x5
    x6 = width_f(x4)
    if x == 6:
        return x6
    x7 = tojvec(x6)
    if x == 7:
        return x7
    x8 = add(x7, ZERO_BY_TWO)
    if x == 8:
        return x8
    x9 = shift(x5, x8)
    if x == 9:
        return x9
    x10 = fill(I, TWO, x9)
    if x == 10:
        return x10
    x11 = f_ofcolor(x10, TWO)
    if x == 11:
        return x11
    x12 = mir_rot_f(x11, R0)
    if x == 12:
        return x12
    x13 = height_f(x4)
    if x == 13:
        return x13
    x14 = toivec(x13)
    if x == 14:
        return x14
    x15 = add(x14, TWO_BY_ZERO)
    if x == 15:
        return x15
    x16 = shift(x12, x15)
    if x == 16:
        return x16
    x17 = fill(x10, TWO, x16)
    if x == 17:
        return x17
    O = branch(x3, I, x17)
    return O

def solve_4be741c5(S, I, x=0):
    x1 = portrait_t(I)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_t, R1)
    if x == 2:
        return x2
    x3 = branch(x1, x2, identity)
    if x == 3:
        return x3
    x4 = x3(I)
    if x == 4:
        return x4
    x5 = branch(x1, height_t, width_t)
    if x == 5:
        return x5
    x6 = x5(I)
    if x == 6:
        return x6
    x7 = astuple(ONE, x6)
    if x == 7:
        return x7
    x8 = crop(x4, ORIGIN, x7)
    if x == 8:
        return x8
    x9 = apply(dedupe, x8)
    if x == 9:
        return x9
    O = x3(x9)
    return O

def solve_d631b094(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = other_f(x1, ZERO)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, x2)
    if x == 3:
        return x3
    x4 = size_f(x3)
    if x == 4:
        return x4
    x5 = astuple(ONE, x4)
    if x == 5:
        return x5
    O = canvas(x2, x5)
    return O

def solve_c3e719e8(S, I, x=0):
    x1 = hconcat(I, I)
    if x == 1:
        return x1
    x2 = hconcat(x1, I)
    if x == 2:
        return x2
    x3 = vconcat(x2, x2)
    if x == 3:
        return x3
    x4 = vconcat(x3, x2)
    if x == 4:
        return x4
    x5 = upscale_t(I, THREE)
    if x == 5:
        return x5
    x6 = asindices(x5)
    if x == 6:
        return x6
    x7 = get_color_rank_t(I, F0)
    if x == 7:
        return x7
    x8 = f_ofcolor(x5, x7)
    if x == 8:
        return x8
    x9 = difference(x6, x8)
    if x == 9:
        return x9
    O = fill(x4, ZERO, x9)
    return O

def solve_a3325580(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_val_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = astuple(ONE, x2)
    if x == 3:
        return x3
    x4 = rbind(canvas, x3)
    if x == 4:
        return x4
    x5 = sizefilter(x1, x2)
    if x == 5:
        return x5
    x6 = rbind(col_row, R2)
    if x == 6:
        return x6
    x7 = order(x5, x6)
    if x == 7:
        return x7
    x8 = apply(color, x7)
    if x == 8:
        return x8
    x9 = apply(x4, x8)
    if x == 9:
        return x9
    x10 = merge_t(x9)
    if x == 10:
        return x10
    O = mir_rot_t(x10, R1)
    return O

def solve_e9614598(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = fork(add, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, ONE)
    if x == 4:
        return x4
    x5 = x3(x4)
    if x == 5:
        return x5
    x6 = halve(x5)
    if x == 6:
        return x6
    x7 = dneighbors(x6)
    if x == 7:
        return x7
    x8 = insert(x6, x7)
    if x == 8:
        return x8
    O = fill(I, THREE, x8)
    return O

def solve_05269061(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = rbind(multiply, THREE)
    if x == 4:
        return x4
    x5 = neighbors(ORIGIN)
    if x == 5:
        return x5
    x6 = mapply(neighbors, x5)
    if x == 6:
        return x6
    x7 = apply(x4, x6)
    if x == 7:
        return x7
    x8 = mapply(x3, x7)
    if x == 8:
        return x8
    x9 = paint(I, x8)
    if x == 9:
        return x9
    x10 = shift(x8, UP_RIGHT)
    if x == 10:
        return x10
    x11 = paint(x9, x10)
    if x == 11:
        return x11
    x12 = shift(x8, DOWN_LEFT)
    if x == 12:
        return x12
    O = paint(x11, x12)
    return O

def solve_ed36ccf7(S, I, x=0):
    O = mir_rot_t(I, R6)
    return O

def solve_f25ffba3(S, I, x=0):
    x1 = bottomhalf(I)
    if x == 1:
        return x1
    x2 = mir_rot_t(x1, R0)
    if x == 2:
        return x2
    O = vconcat(x2, x1)
    return O

def solve_caa06a1f(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    x3 = index(I, x2)
    if x == 3:
        return x3
    x4 = double(x1)
    if x == 4:
        return x4
    x5 = canvas(x3, x4)
    if x == 5:
        return x5
    x6 = asobject(I)
    if x == 6:
        return x6
    x7 = paint(x5, x6)
    if x == 7:
        return x7
    x8 = o_g(x7, R1)
    if x == 8:
        return x8
    x9 = get_nth_f(x8, F0)
    if x == 9:
        return x9
    x10 = shift(x9, LEFT)
    if x == 10:
        return x10
    x11 = lbind(shift, x10)
    if x == 11:
        return x11
    x12 = vperiod(x10)
    if x == 12:
        return x12
    x13 = hperiod(x10)
    if x == 13:
        return x13
    x14 = astuple(x12, x13)
    if x == 14:
        return x14
    x15 = lbind(multiply, x14)
    if x == 15:
        return x15
    x16 = lbind(mapply, neighbors)
    if x == 16:
        return x16
    x17 = power(x16, TWO)
    if x == 17:
        return x17
    x18 = neighbors(ORIGIN)
    if x == 18:
        return x18
    x19 = x17(x18)
    if x == 19:
        return x19
    x20 = apply(x15, x19)
    if x == 20:
        return x20
    x21 = mapply(x11, x20)
    if x == 21:
        return x21
    O = paint(I, x21)
    return O

def solve_1b2d62fb(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = replace(x1, NINE, ZERO)
    if x == 2:
        return x2
    x3 = f_ofcolor(x1, ZERO)
    if x == 3:
        return x3
    x4 = righthalf(I)
    if x == 4:
        return x4
    x5 = f_ofcolor(x4, ZERO)
    if x == 5:
        return x5
    x6 = intersection(x3, x5)
    if x == 6:
        return x6
    O = fill(x2, EIGHT, x6)
    return O

def solve_6150a2bd(S, I, x=0):
    O = mir_rot_t(I, R5)
    return O

def solve_0dfd9992(S, I, x=0):
    x1 = partition(I)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = merge(x3)
    if x == 4:
        return x4
    x5 = lbind(shift, x4)
    if x == 5:
        return x5
    x6 = height_t(I)
    if x == 6:
        return x6
    x7 = decrement(x6)
    if x == 7:
        return x7
    x8 = tojvec(x7)
    if x == 8:
        return x8
    x9 = astuple(x6, ONE)
    if x == 9:
        return x9
    x10 = crop(I, x8, x9)
    if x == 10:
        return x10
    x11 = asobject(x10)
    if x == 11:
        return x11
    x12 = vperiod(x11)
    if x == 12:
        return x12
    x13 = width_t(I)
    if x == 13:
        return x13
    x14 = decrement(x13)
    if x == 14:
        return x14
    x15 = toivec(x14)
    if x == 15:
        return x15
    x16 = astuple(ONE, x13)
    if x == 16:
        return x16
    x17 = crop(I, x15, x16)
    if x == 17:
        return x17
    x18 = asobject(x17)
    if x == 18:
        return x18
    x19 = hperiod(x18)
    if x == 19:
        return x19
    x20 = astuple(x12, x19)
    if x == 20:
        return x20
    x21 = lbind(multiply, x20)
    if x == 21:
        return x21
    x22 = neighbors(ORIGIN)
    if x == 22:
        return x22
    x23 = mapply(neighbors, x22)
    if x == 23:
        return x23
    x24 = apply(x21, x23)
    if x == 24:
        return x24
    x25 = mapply(x5, x24)
    if x == 25:
        return x25
    O = paint(I, x25)
    return O

def solve_3428a4f5(S, I, x=0):
    x1 = astuple(SIX, FIVE)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = tophalf(I)
    if x == 3:
        return x3
    x4 = f_ofcolor(x3, TWO)
    if x == 4:
        return x4
    x5 = bottomhalf(I)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, TWO)
    if x == 6:
        return x6
    x7 = combine_f(x4, x6)
    if x == 7:
        return x7
    x8 = intersection(x4, x6)
    if x == 8:
        return x8
    x9 = difference(x7, x8)
    if x == 9:
        return x9
    O = fill(x2, THREE, x9)
    return O

def solve_53b68214(S, I, x=0):
    x1 = width_t(I)
    if x == 1:
        return x1
    x2 = astuple(x1, x1)
    if x == 2:
        return x2
    x3 = canvas(ZERO, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R7)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = paint(x3, x5)
    if x == 6:
        return x6
    x7 = portrait_f(x5)
    if x == 7:
        return x7
    x8 = lbind(shift, x5)
    if x == 8:
        return x8
    x9 = vperiod(x5)
    if x == 9:
        return x9
    x10 = toivec(x9)
    if x == 10:
        return x10
    x11 = lbind(multiply, x10)
    if x == 11:
        return x11
    x12 = interval(ZERO, NINE, ONE)
    if x == 12:
        return x12
    x13 = apply(x11, x12)
    if x == 13:
        return x13
    x14 = mapply(x8, x13)
    if x == 14:
        return x14
    x15 = shape_f(x5)
    if x == 15:
        return x15
    x16 = add(DOWN, x15)
    if x == 16:
        return x16
    x17 = decrement(x16)
    if x == 17:
        return x17
    x18 = shift(x5, x17)
    if x == 18:
        return x18
    x19 = branch(x7, x14, x18)
    if x == 19:
        return x19
    O = paint(x6, x19)
    return O

def solve_62c24649(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = hconcat(I, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R0)
    if x == 3:
        return x3
    O = vconcat(x2, x3)
    return O

def solve_ce9e57f2(S, I, x=0):
    x1 = rbind(corner, R0)
    if x == 1:
        return x1
    x2 = fork(connect, x1, centerofmass)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = mapply(x2, x3)
    if x == 4:
        return x4
    x5 = fill(I, EIGHT, x4)
    if x == 5:
        return x5
    O = switch(x5, EIGHT, TWO)
    return O

def solve_025d127b(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = rbind(get_arg_rank, F0)
    if x == 3:
        return x3
    x4 = rbind(col_row, R3)
    if x == 4:
        return x4
    x5 = rbind(x3, x4)
    if x == 5:
        return x5
    x6 = lbind(colorfilter, x1)
    if x == 6:
        return x6
    x7 = compose(x5, x6)
    if x == 7:
        return x7
    x8 = apply(color, x1)
    if x == 8:
        return x8
    x9 = mapply(x7, x8)
    if x == 9:
        return x9
    x10 = difference(x2, x9)
    if x == 10:
        return x10
    O = move(I, x10, RIGHT)
    return O

def solve_47c1f68c(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = get_color_rank_t(I, L1)
    if x == 2:
        return x2
    x3 = cellwise(I, x1, x2)
    if x == 3:
        return x3
    x4 = mir_rot_t(x3, R0)
    if x == 4:
        return x4
    x5 = cellwise(x3, x4, x2)
    if x == 5:
        return x5
    x6 = compress(x5)
    if x == 6:
        return x6
    x7 = o_g(I, R7)
    if x == 7:
        return x7
    x8 = merge_f(x7)
    if x == 8:
        return x8
    x9 = get_color_rank_f(x8, F0)
    if x == 9:
        return x9
    O = replace(x6, x2, x9)
    return O

def solve_ac0a08a4(S, I, x=0):
    x1 = colorcount_t(I, ZERO)
    if x == 1:
        return x1
    x2 = subtract(NINE, x1)
    if x == 2:
        return x2
    O = upscale_t(I, x2)
    return O

def solve_cf98881b(S, I, x=0):
    x1 = hsplit(I, THREE)
    if x == 1:
        return x1
    x2 = get_nth_t(x1, F0)
    if x == 2:
        return x2
    x3 = remove_t(x2, x1)
    if x == 3:
        return x3
    x4 = get_nth_t(x3, L1)
    if x == 4:
        return x4
    x5 = get_nth_t(x3, F0)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, NINE)
    if x == 6:
        return x6
    x7 = fill(x4, NINE, x6)
    if x == 7:
        return x7
    x8 = f_ofcolor(x2, FOUR)
    if x == 8:
        return x8
    O = fill(x7, FOUR, x8)
    return O

def solve_b0c4d837(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = height_f(x1)
    if x == 2:
        return x2
    x3 = decrement(x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = height_f(x4)
    if x == 5:
        return x5
    x6 = subtract(x3, x5)
    if x == 6:
        return x6
    x7 = astuple(ONE, x6)
    if x == 7:
        return x7
    x8 = canvas(EIGHT, x7)
    if x == 8:
        return x8
    x9 = subtract(SIX, x6)
    if x == 9:
        return x9
    x10 = astuple(ONE, x9)
    if x == 10:
        return x10
    x11 = canvas(ZERO, x10)
    if x == 11:
        return x11
    x12 = hconcat(x8, x11)
    if x == 12:
        return x12
    x13 = hsplit(x12, TWO)
    if x == 13:
        return x13
    x14 = get_nth_t(x13, F0)
    if x == 14:
        return x14
    x15 = get_nth_t(x13, L1)
    if x == 15:
        return x15
    x16 = mir_rot_t(x15, R2)
    if x == 16:
        return x16
    x17 = vconcat(x14, x16)
    if x == 17:
        return x17
    x18 = astuple(ONE, THREE)
    if x == 18:
        return x18
    x19 = canvas(ZERO, x18)
    if x == 19:
        return x19
    O = vconcat(x17, x19)
    return O

def solve_d06dbe63(S, I, x=0):
    x1 = connect(ORIGIN, DOWN)
    if x == 1:
        return x1
    x2 = connect(ORIGIN, ZERO_BY_TWO)
    if x == 2:
        return x2
    x3 = combine(x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = center(x4)
    if x == 5:
        return x5
    x6 = subtract(x5, TWO_BY_ZERO)
    if x == 6:
        return x6
    x7 = shift(x3, x6)
    if x == 7:
        return x7
    x8 = lbind(shift, x7)
    if x == 8:
        return x8
    x9 = astuple(NEG_TWO, TWO)
    if x == 9:
        return x9
    x10 = lbind(multiply, x9)
    if x == 10:
        return x10
    x11 = interval(ZERO, FIVE, ONE)
    if x == 11:
        return x11
    x12 = apply(x10, x11)
    if x == 12:
        return x12
    x13 = mapply(x8, x12)
    if x == 13:
        return x13
    x14 = fill(I, FIVE, x13)
    if x == 14:
        return x14
    x15 = mir_rot_t(x14, R5)
    if x == 15:
        return x15
    x16 = f_ofcolor(x15, EIGHT)
    if x == 16:
        return x16
    x17 = center(x16)
    if x == 17:
        return x17
    x18 = subtract(x17, x6)
    if x == 18:
        return x18
    x19 = shift(x13, x18)
    if x == 19:
        return x19
    x20 = toivec(NEG_TWO)
    if x == 20:
        return x20
    x21 = shift(x19, x20)
    if x == 21:
        return x21
    x22 = fill(x15, FIVE, x21)
    if x == 22:
        return x22
    O = mir_rot_t(x22, R5)
    return O

def solve_c9f8e694(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = astuple(x1, ONE)
    if x == 2:
        return x2
    x3 = crop(I, ORIGIN, x2)
    if x == 3:
        return x3
    x4 = width_t(I)
    if x == 4:
        return x4
    x5 = hupscale(x3, x4)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, ZERO)
    if x == 6:
        return x6
    O = fill(x5, ZERO, x6)
    return O

def solve_6cdd2623(S, I, x=0):
    x1 = fgpartition(I)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = cover(I, x2)
    if x == 3:
        return x3
    x4 = get_color_rank_t(I, L1)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, x4)
    if x == 5:
        return x5
    x6 = prapply(connect, x5, x5)
    if x == 6:
        return x6
    x7 = fork(either, hline_i, vline_i)
    if x == 7:
        return x7
    x8 = box(x2)
    if x == 8:
        return x8
    x9 = rbind(difference, x8)
    if x == 9:
        return x9
    x10 = chain(positive, size, x9)
    if x == 10:
        return x10
    x11 = fork(both, x7, x10)
    if x == 11:
        return x11
    x12 = mfilter_f(x6, x11)
    if x == 12:
        return x12
    O = fill(x3, x4, x12)
    return O

def solve_3af2c5a8(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = hconcat(I, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R0)
    if x == 3:
        return x3
    O = vconcat(x2, x3)
    return O

def solve_5c2c9af4(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = center(x2)
    if x == 3:
        return x3
    x4 = corner(x2, R0)
    if x == 4:
        return x4
    x5 = subtract(x3, x4)
    if x == 5:
        return x5
    x6 = lbind(multiply, x5)
    if x == 6:
        return x6
    x7 = interval(ZERO, NINE, ONE)
    if x == 7:
        return x7
    x8 = apply(x6, x7)
    if x == 8:
        return x8
    x9 = multiply(NEG_ONE, NINE)
    if x == 9:
        return x9
    x10 = interval(ZERO, x9, NEG_ONE)
    if x == 10:
        return x10
    x11 = apply(x6, x10)
    if x == 11:
        return x11
    x12 = pair(x8, x11)
    if x == 12:
        return x12
    x13 = mapply(box, x12)
    if x == 13:
        return x13
    x14 = shift(x13, x3)
    if x == 14:
        return x14
    O = fill(I, x1, x14)
    return O

def solve_b190f7f5(S, I, x=0):
    x1 = portrait_t(I)
    if x == 1:
        return x1
    x2 = branch(x1, vsplit, hsplit)
    if x == 2:
        return x2
    x3 = x2(I, TWO)
    if x == 3:
        return x3
    x4 = get_arg_rank_t(x3, numcolors_t, F0)
    if x == 4:
        return x4
    x5 = width_t(x4)
    if x == 5:
        return x5
    x6 = upscale_t(x4, x5)
    if x == 6:
        return x6
    x7 = rbind(mir_rot_t, R1)
    if x == 7:
        return x7
    x8 = rbind(repeat, x5)
    if x == 8:
        return x8
    x9 = chain(x7, merge, x8)
    if x == 9:
        return x9
    x10 = get_arg_rank_t(x3, numcolors_t, L1)
    if x == 10:
        return x10
    x11 = x9(x10)
    if x == 11:
        return x11
    x12 = x9(x11)
    if x == 12:
        return x12
    x13 = f_ofcolor(x12, ZERO)
    if x == 13:
        return x13
    O = fill(x6, ZERO, x13)
    return O

def solve_d4469b4b(S, I, x=0):
    x1 = canvas(ZERO, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = fork(combine, vfrontier, hfrontier)
    if x == 2:
        return x2
    x3 = palette_t(I)
    if x == 3:
        return x3
    x4 = other_f(x3, ZERO)
    if x == 4:
        return x4
    x5 = equality(x4, TWO)
    if x == 5:
        return x5
    x6 = equality(x4, ONE)
    if x == 6:
        return x6
    x7 = branch(x6, UNITY, TWO_BY_TWO)
    if x == 7:
        return x7
    x8 = branch(x5, RIGHT, x7)
    if x == 8:
        return x8
    x9 = x2(x8)
    if x == 9:
        return x9
    O = fill(x1, FIVE, x9)
    return O

def solve_913fb3ed(S, I, x=0):
    x1 = f_ofcolor(I, THREE)
    if x == 1:
        return x1
    x2 = mapply(neighbors, x1)
    if x == 2:
        return x2
    x3 = fill(I, SIX, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = mapply(neighbors, x4)
    if x == 5:
        return x5
    x6 = fill(x3, FOUR, x5)
    if x == 6:
        return x6
    x7 = f_ofcolor(I, TWO)
    if x == 7:
        return x7
    x8 = mapply(neighbors, x7)
    if x == 8:
        return x8
    O = fill(x6, ONE, x8)
    return O

def solve_67e8384a(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = hconcat(I, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R0)
    if x == 3:
        return x3
    O = vconcat(x2, x3)
    return O

def solve_22233c11(S, I, x=0):
    x1 = rbind(upscale_f, TWO)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_f, R2)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = chain(invert, halve, shape_f)
    if x == 4:
        return x4
    x5 = fork(shift, x3, x4)
    if x == 5:
        return x5
    x6 = compose(toindices, x5)
    if x == 6:
        return x6
    x7 = fork(combine, hfrontier, vfrontier)
    if x == 7:
        return x7
    x8 = lbind(mapply, x7)
    if x == 8:
        return x8
    x9 = compose(x8, toindices)
    if x == 9:
        return x9
    x10 = fork(difference, x6, x9)
    if x == 10:
        return x10
    x11 = o_g(I, R7)
    if x == 11:
        return x11
    x12 = mapply(x10, x11)
    if x == 12:
        return x12
    O = fill(I, EIGHT, x12)
    return O

def solve_82819916(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_arg_rank, L1)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, L1)
    if x == 3:
        return x3
    x4 = compose(x3, x3)
    if x == 4:
        return x4
    x5 = rbind(x2, x4)
    if x == 5:
        return x5
    x6 = compose(x1, x5)
    if x == 6:
        return x6
    x7 = o_g(I, R3)
    if x == 7:
        return x7
    x8 = get_arg_rank_f(x7, size, F0)
    if x == 8:
        return x8
    x9 = normalize(x8)
    if x == 9:
        return x9
    x10 = x6(x9)
    if x == 10:
        return x10
    x11 = matcher(x1, x10)
    if x == 11:
        return x11
    x12 = sfilter_f(x9, x11)
    if x == 12:
        return x12
    x13 = lbind(shift, x12)
    if x == 13:
        return x13
    x14 = rbind(col_row, R1)
    if x == 14:
        return x14
    x15 = compose(toivec, x14)
    if x == 15:
        return x15
    x16 = compose(x13, x15)
    if x == 16:
        return x16
    x17 = fork(recolor_o, x6, x16)
    if x == 17:
        return x17
    x18 = fork(other, palette_f, x6)
    if x == 18:
        return x18
    x19 = difference(x9, x12)
    if x == 19:
        return x19
    x20 = lbind(shift, x19)
    if x == 20:
        return x20
    x21 = compose(x20, x15)
    if x == 21:
        return x21
    x22 = fork(recolor_o, x18, x21)
    if x == 22:
        return x22
    x23 = fork(combine, x17, x22)
    if x == 23:
        return x23
    x24 = remove_f(x8, x7)
    if x == 24:
        return x24
    x25 = mapply(x23, x24)
    if x == 25:
        return x25
    O = paint(I, x25)
    return O

def solve_d89b689b(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    x4 = cover(I, x3)
    if x == 4:
        return x4
    x5 = rbind(get_arg_rank, L1)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, EIGHT)
    if x == 6:
        return x6
    x7 = apply(initset, x6)
    if x == 7:
        return x7
    x8 = lbind(x5, x7)
    if x == 8:
        return x8
    x9 = lbind(rbind, manhattan)
    if x == 9:
        return x9
    x10 = compose(x8, x9)
    if x == 10:
        return x10
    x11 = fork(recolor_i, color, x10)
    if x == 11:
        return x11
    x12 = mapply(x11, x2)
    if x == 12:
        return x12
    O = paint(x4, x12)
    return O

def solve_e98196ab(S, I, x=0):
    x1 = bottomhalf(I)
    if x == 1:
        return x1
    x2 = tophalf(I)
    if x == 2:
        return x2
    x3 = o_g(x2, R5)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    O = paint(x1, x4)
    return O

def solve_673ef223(S, I, x=0):
    x1 = replace(I, EIGHT, FOUR)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = rbind(col_row, R1)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x2, x3, L1)
    if x == 4:
        return x4
    x5 = col_row(x4, R2)
    if x == 5:
        return x5
    x6 = equality(x5, ZERO)
    if x == 6:
        return x6
    x7 = branch(x6, LEFT, RIGHT)
    if x == 7:
        return x7
    x8 = rbind(shoot, x7)
    if x == 8:
        return x8
    x9 = f_ofcolor(I, EIGHT)
    if x == 9:
        return x9
    x10 = mapply(x8, x9)
    if x == 10:
        return x10
    x11 = underfill(x1, EIGHT, x10)
    if x == 11:
        return x11
    x12 = rbind(get_rank, F0)
    if x == 12:
        return x12
    x13 = rbind(get_rank, L1)
    if x == 13:
        return x13
    x14 = fork(subtract, x12, x13)
    if x == 14:
        return x14
    x15 = colorfilter(x2, TWO)
    if x == 15:
        return x15
    x16 = apply(x3, x15)
    if x == 16:
        return x16
    x17 = x14(x16)
    if x == 17:
        return x17
    x18 = toivec(x17)
    if x == 18:
        return x18
    x19 = shift(x9, x18)
    if x == 19:
        return x19
    x20 = mapply(hfrontier, x19)
    if x == 20:
        return x20
    O = underfill(x11, EIGHT, x20)
    return O

def solve_10fcaaa3(S, I, x=0):
    x1 = hconcat(I, I)
    if x == 1:
        return x1
    x2 = vconcat(x1, x1)
    if x == 2:
        return x2
    x3 = get_color_rank_t(I, L1)
    if x == 3:
        return x3
    x4 = f_ofcolor(x2, x3)
    if x == 4:
        return x4
    x5 = mapply(ineighbors, x4)
    if x == 5:
        return x5
    O = underfill(x2, EIGHT, x5)
    return O

def solve_1cf80156(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O

def solve_50cb2852(S, I, x=0):
    x1 = compose(backdrop, inbox)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = mapply(x1, x2)
    if x == 3:
        return x3
    O = fill(I, EIGHT, x3)
    return O

def solve_d6ad076f(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x1, size, F0)
    if x == 3:
        return x3
    x4 = vmatching(x2, x3)
    if x == 4:
        return x4
    x5 = branch(x4, DOWN, RIGHT)
    if x == 5:
        return x5
    x6 = rbind(col_row, R1)
    if x == 6:
        return x6
    x7 = rbind(col_row, R2)
    if x == 7:
        return x7
    x8 = branch(x4, x6, x7)
    if x == 8:
        return x8
    x9 = get_val_rank_f(x1, x8, F0)
    if x == 9:
        return x9
    x10 = x8(x2)
    if x == 10:
        return x10
    x11 = equality(x9, x10)
    if x == 11:
        return x11
    x12 = branch(x11, NEG_ONE, ONE)
    if x == 12:
        return x12
    x13 = multiply(x5, x12)
    if x == 13:
        return x13
    x14 = rbind(shoot, x13)
    if x == 14:
        return x14
    x15 = inbox(x2)
    if x == 15:
        return x15
    x16 = mapply(x14, x15)
    if x == 16:
        return x16
    x17 = underfill(I, EIGHT, x16)
    if x == 17:
        return x17
    x18 = o_g(x17, R5)
    if x == 18:
        return x18
    x19 = colorfilter(x18, EIGHT)
    if x == 19:
        return x19
    x20 = rbind(bordering, I)
    if x == 20:
        return x20
    x21 = mfilter_f(x19, x20)
    if x == 21:
        return x21
    O = cover(x17, x21)
    return O

def solve_5117e062(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = matcher(numcolors_f, TWO)
    if x == 2:
        return x2
    x3 = extract(x1, x2)
    if x == 3:
        return x3
    x4 = subgrid(x3, I)
    if x == 4:
        return x4
    x5 = get_color_rank_f(x3, F0)
    if x == 5:
        return x5
    O = replace(x4, EIGHT, x5)
    return O

def solve_8d5021e8(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = hconcat(x1, I)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R0)
    if x == 3:
        return x3
    x4 = vconcat(x2, x3)
    if x == 4:
        return x4
    x5 = vconcat(x4, x2)
    if x == 5:
        return x5
    O = mir_rot_t(x5, R0)
    return O

def solve_d9f24cd1(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, FIVE)
    if x == 2:
        return x2
    x3 = prapply(connect, x1, x2)
    if x == 3:
        return x3
    x4 = mfilter_f(x3, vline_i)
    if x == 4:
        return x4
    x5 = underfill(I, TWO, x4)
    if x == 5:
        return x5
    x6 = rbind(shoot, UP)
    if x == 6:
        return x6
    x7 = rbind(corner, R1)
    if x == 7:
        return x7
    x8 = o_g(x5, R1)
    if x == 8:
        return x8
    x9 = matcher(numcolors_f, TWO)
    if x == 9:
        return x9
    x10 = sfilter_f(x8, x9)
    if x == 10:
        return x10
    x11 = apply(x7, x10)
    if x == 11:
        return x11
    x12 = shift(x11, UNITY)
    if x == 12:
        return x12
    x13 = mapply(x6, x12)
    if x == 13:
        return x13
    x14 = fill(x5, TWO, x13)
    if x == 14:
        return x14
    x15 = difference(x8, x10)
    if x == 15:
        return x15
    x16 = colorfilter(x15, TWO)
    if x == 16:
        return x16
    x17 = mapply(toindices, x16)
    if x == 17:
        return x17
    x18 = mapply(vfrontier, x17)
    if x == 18:
        return x18
    O = fill(x14, TWO, x18)
    return O

def solve_50846271(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = prapply(connect, x1, x1)
    if x == 2:
        return x2
    x3 = lbind(greater, SIX)
    if x == 3:
        return x3
    x4 = compose(x3, size)
    if x == 4:
        return x4
    x5 = fork(either, vline_i, hline_i)
    if x == 5:
        return x5
    x6 = fork(both, x4, x5)
    if x == 6:
        return x6
    x7 = mfilter_f(x2, x6)
    if x == 7:
        return x7
    x8 = fill(I, TWO, x7)
    if x == 8:
        return x8
    x9 = o_g(x8, R4)
    if x == 9:
        return x9
    x10 = colorfilter(x9, TWO)
    if x == 10:
        return x10
    x11 = get_val_rank_f(x10, width_f, F0)
    if x == 11:
        return x11
    x12 = halve(x11)
    if x == 12:
        return x12
    x13 = toivec(x12)
    if x == 13:
        return x13
    x14 = rbind(add, x13)
    if x == 14:
        return x14
    x15 = rbind(subtract, x13)
    if x == 15:
        return x15
    x16 = fork(connect, x14, x15)
    if x == 16:
        return x16
    x17 = tojvec(x12)
    if x == 17:
        return x17
    x18 = rbind(add, x17)
    if x == 18:
        return x18
    x19 = rbind(subtract, x17)
    if x == 19:
        return x19
    x20 = fork(connect, x18, x19)
    if x == 20:
        return x20
    x21 = fork(combine, x16, x20)
    if x == 21:
        return x21
    x22 = rbind(get_arg_rank, F0)
    if x == 22:
        return x22
    x23 = rbind(colorcount_f, TWO)
    if x == 23:
        return x23
    x24 = rbind(toobject, x8)
    if x == 24:
        return x24
    x25 = rbind(subtract, TWO_BY_ZERO)
    if x == 25:
        return x25
    x26 = rbind(subtract, ZERO_BY_TWO)
    if x == 26:
        return x26
    x27 = rbind(add, TWO_BY_ZERO)
    if x == 27:
        return x27
    x28 = rbind(add, ZERO_BY_TWO)
    if x == 28:
        return x28
    x29 = compose(initset, x28)
    if x == 29:
        return x29
    x30 = fork(insert, x27, x29)
    if x == 30:
        return x30
    x31 = fork(insert, x26, x30)
    if x == 31:
        return x31
    x32 = fork(insert, x25, x31)
    if x == 32:
        return x32
    x33 = fork(combine, dneighbors, x32)
    if x == 33:
        return x33
    x34 = chain(x23, x24, x33)
    if x == 34:
        return x34
    x35 = rbind(x22, x34)
    if x == 35:
        return x35
    x36 = compose(x35, toindices)
    if x == 36:
        return x36
    x37 = apply(x36, x10)
    if x == 37:
        return x37
    x38 = mapply(x21, x37)
    if x == 38:
        return x38
    x39 = fill(x8, EIGHT, x38)
    if x == 39:
        return x39
    O = fill(x39, TWO, x1)
    return O

def solve_41e4d17e(S, I, x=0):
    x1 = fork(combine, vfrontier, hfrontier)
    if x == 1:
        return x1
    x2 = compose(x1, center)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = mapply(x2, x3)
    if x == 4:
        return x4
    O = underfill(I, SIX, x4)
    return O

def solve_6aa20dc0(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = lbind(occurrences, I)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, F0)
    if x == 3:
        return x3
    x4 = lbind(matcher, x3)
    if x == 4:
        return x4
    x5 = rbind(get_color_rank_f, F0)
    if x == 5:
        return x5
    x6 = compose(x4, x5)
    if x == 6:
        return x6
    x7 = fork(sfilter, identity, x6)
    if x == 7:
        return x7
    x8 = fork(difference, identity, x7)
    if x == 8:
        return x8
    x9 = compose(x2, x8)
    if x == 9:
        return x9
    x10 = fork(mapply, x1, x9)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, L1)
    if x == 11:
        return x11
    x12 = fork(compose, x3, x11)
    if x == 12:
        return x12
    x13 = rbind(mir_rot_f, R1)
    if x == 13:
        return x13
    x14 = rbind(mir_rot_f, R3)
    if x == 14:
        return x14
    x15 = rbind(mir_rot_f, R0)
    if x == 15:
        return x15
    x16 = rbind(mir_rot_f, R2)
    if x == 16:
        return x16
    x17 = initset(identity)
    if x == 17:
        return x17
    x18 = insert(x16, x17)
    if x == 18:
        return x18
    x19 = insert(x15, x18)
    if x == 19:
        return x19
    x20 = insert(x14, x19)
    if x == 20:
        return x20
    x21 = insert(x13, x20)
    if x == 21:
        return x21
    x22 = lbind(rbind, upscale_f)
    if x == 22:
        return x22
    x23 = interval(ONE, FOUR, ONE)
    if x == 23:
        return x23
    x24 = apply(x22, x23)
    if x == 24:
        return x24
    x25 = product(x21, x24)
    if x == 25:
        return x25
    x26 = apply(x12, x25)
    if x == 26:
        return x26
    x27 = o_g(I, R3)
    if x == 27:
        return x27
    x28 = get_arg_rank_f(x27, numcolors_f, F0)
    if x == 28:
        return x28
    x29 = normalize(x28)
    if x == 29:
        return x29
    x30 = rapply_f(x26, x29)
    if x == 30:
        return x30
    x31 = mapply(x10, x30)
    if x == 31:
        return x31
    O = paint(I, x31)
    return O

def solve_39a8645d(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = totuple(x1)
    if x == 2:
        return x2
    x3 = apply(color, x2)
    if x == 3:
        return x3
    x4 = get_common_rank_t(x3, F0)
    if x == 4:
        return x4
    x5 = matcher(color, x4)
    if x == 5:
        return x5
    x6 = extract(x1, x5)
    if x == 6:
        return x6
    O = subgrid(x6, I)
    return O

def solve_5bd6f4ac(S, I, x=0):
    x1 = tojvec(SIX)
    if x == 1:
        return x1
    O = crop(I, x1, THREE_BY_THREE)
    return O

def solve_8d510a79(S, I, x=0):
    x1 = chain(toivec, decrement, double)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, FIVE)
    if x == 2:
        return x2
    x3 = col_row(x2, R1)
    if x == 3:
        return x3
    x4 = lbind(greater, x3)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, F0)
    if x == 5:
        return x5
    x6 = compose(x4, x5)
    if x == 6:
        return x6
    x7 = compose(x1, x6)
    if x == 7:
        return x7
    x8 = fork(shoot, identity, x7)
    if x == 8:
        return x8
    x9 = lbind(matcher, x6)
    if x == 9:
        return x9
    x10 = compose(x9, x6)
    if x == 10:
        return x10
    x11 = fork(sfilter, x8, x10)
    if x == 11:
        return x11
    x12 = f_ofcolor(I, TWO)
    if x == 12:
        return x12
    x13 = mapply(x11, x12)
    if x == 13:
        return x13
    x14 = underfill(I, TWO, x13)
    if x == 14:
        return x14
    x15 = chain(invert, x1, x6)
    if x == 15:
        return x15
    x16 = fork(shoot, identity, x15)
    if x == 16:
        return x16
    x17 = f_ofcolor(I, ONE)
    if x == 17:
        return x17
    x18 = mapply(x16, x17)
    if x == 18:
        return x18
    O = fill(x14, ONE, x18)
    return O

def solve_234bbc79(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = lbind(add, RIGHT)
    if x == 4:
        return x4
    x5 = rbind(get_arg_rank, L1)
    if x == 5:
        return x5
    x6 = compose(x2, x2)
    if x == 6:
        return x6
    x7 = lbind(matcher, x6)
    if x == 7:
        return x7
    x8 = rbind(col_row, R3)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = fork(sfilter, identity, x9)
    if x == 10:
        return x10
    x11 = compose(dneighbors, x2)
    if x == 11:
        return x11
    x12 = rbind(chain, x11)
    if x == 12:
        return x12
    x13 = lbind(x12, size)
    if x == 13:
        return x13
    x14 = lbind(rbind, intersection)
    if x == 14:
        return x14
    x15 = chain(x13, x14, toindices)
    if x == 15:
        return x15
    x16 = fork(x5, x10, x15)
    if x == 16:
        return x16
    x17 = compose(x2, x16)
    if x == 17:
        return x17
    x18 = compose(x17, x1)
    if x == 18:
        return x18
    x19 = rbind(col_row, R2)
    if x == 19:
        return x19
    x20 = compose(x7, x19)
    if x == 20:
        return x20
    x21 = fork(sfilter, identity, x20)
    if x == 21:
        return x21
    x22 = fork(x5, x21, x15)
    if x == 22:
        return x22
    x23 = compose(x2, x22)
    if x == 23:
        return x23
    x24 = chain(x23, x1, x2)
    if x == 24:
        return x24
    x25 = fork(subtract, x18, x24)
    if x == 25:
        return x25
    x26 = compose(x4, x25)
    if x == 26:
        return x26
    x27 = fork(shift, x3, x26)
    if x == 27:
        return x27
    x28 = fork(combine, x1, x27)
    if x == 28:
        return x28
    x29 = fork(remove, x3, x2)
    if x == 29:
        return x29
    x30 = fork(astuple, x28, x29)
    if x == 30:
        return x30
    x31 = o_g(I, R1)
    if x == 31:
        return x31
    x32 = size_f(x31)
    if x == 32:
        return x32
    x33 = power(x30, x32)
    if x == 33:
        return x33
    x34 = astuple(ZERO, DOWN_LEFT)
    if x == 34:
        return x34
    x35 = initset(x34)
    if x == 35:
        return x35
    x36 = rbind(other, FIVE)
    if x == 36:
        return x36
    x37 = compose(x36, palette_f)
    if x == 37:
        return x37
    x38 = fork(recolor_o, x37, identity)
    if x == 38:
        return x38
    x39 = apply(x38, x31)
    if x == 39:
        return x39
    x40 = order(x39, x19)
    if x == 40:
        return x40
    x41 = astuple(x35, x40)
    if x == 41:
        return x41
    x42 = x33(x41)
    if x == 42:
        return x42
    x43 = get_nth_f(x42, F0)
    if x == 43:
        return x43
    x44 = width_f(x43)
    if x == 44:
        return x44
    x45 = decrement(x44)
    if x == 45:
        return x45
    x46 = astuple(THREE, x45)
    if x == 46:
        return x46
    x47 = canvas(ZERO, x46)
    if x == 47:
        return x47
    O = paint(x47, x43)
    return O

def solve_feca6190(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = size_f(x1)
    if x == 2:
        return x2
    x3 = multiply(x2, FIVE)
    if x == 3:
        return x3
    x4 = astuple(x3, x3)
    if x == 4:
        return x4
    x5 = canvas(ZERO, x4)
    if x == 5:
        return x5
    x6 = rbind(shoot, UNITY)
    if x == 6:
        return x6
    x7 = compose(x6, center)
    if x == 7:
        return x7
    x8 = fork(recolor_i, color, x7)
    if x == 8:
        return x8
    x9 = mapply(x8, x1)
    if x == 9:
        return x9
    x10 = paint(x5, x9)
    if x == 10:
        return x10
    O = mir_rot_t(x10, R0)
    return O

def solve_b230c067(S, I, x=0):
    x1 = replace(I, EIGHT, ONE)
    if x == 1:
        return x1
    x2 = o_g(I, R7)
    if x == 2:
        return x2
    x3 = totuple(x2)
    if x == 3:
        return x3
    x4 = apply(normalize, x3)
    if x == 4:
        return x4
    x5 = get_common_rank_t(x4, L1)
    if x == 5:
        return x5
    x6 = matcher(normalize, x5)
    if x == 6:
        return x6
    x7 = extract(x2, x6)
    if x == 7:
        return x7
    O = fill(x1, TWO, x7)
    return O

def solve_91714a58(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, F0)
    if x == 4:
        return x4
    x5 = paint(x2, x4)
    if x == 5:
        return x5
    x6 = asindices(I)
    if x == 6:
        return x6
    x7 = lbind(greater, THREE)
    if x == 7:
        return x7
    x8 = get_color_rank_f(x4, F0)
    if x == 8:
        return x8
    x9 = rbind(colorcount_f, x8)
    if x == 9:
        return x9
    x10 = rbind(toobject, x5)
    if x == 10:
        return x10
    x11 = chain(x9, x10, neighbors)
    if x == 11:
        return x11
    x12 = compose(x7, x11)
    if x == 12:
        return x12
    x13 = sfilter_f(x6, x12)
    if x == 13:
        return x13
    O = fill(x5, ZERO, x13)
    return O

def solve_ce602527(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = fgpartition(x1)
    if x == 2:
        return x2
    x3 = order(x2, size)
    if x == 3:
        return x3
    x4 = get_nth_t(x3, L1)
    if x == 4:
        return x4
    x5 = remove_f(x4, x3)
    if x == 5:
        return x5
    x6 = compose(toindices, normalize)
    if x == 6:
        return x6
    x7 = x6(x4)
    if x == 7:
        return x7
    x8 = rbind(intersection, x7)
    if x == 8:
        return x8
    x9 = rbind(upscale_f, TWO)
    if x == 9:
        return x9
    x10 = chain(toindices, x9, normalize)
    if x == 10:
        return x10
    x11 = chain(size, x8, x10)
    if x == 11:
        return x11
    x12 = get_arg_rank_t(x5, x11, F0)
    if x == 12:
        return x12
    x13 = subgrid(x12, x1)
    if x == 13:
        return x13
    O = mir_rot_t(x13, R2)
    return O

def solve_b1948b0a(S, I, x=0):
    O = replace(I, SIX, TWO)
    return O

def solve_aba27056(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = mapply(toindices, x1)
    if x == 2:
        return x2
    x3 = delta(x2)
    if x == 3:
        return x3
    x4 = fill(I, FOUR, x3)
    if x == 4:
        return x4
    x5 = box(x2)
    if x == 5:
        return x5
    x6 = difference(x5, x2)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = position(x3, x6)
    if x == 8:
        return x8
    x9 = lbind(multiply, x8)
    if x == 9:
        return x9
    x10 = interval(ZERO, NINE, ONE)
    if x == 10:
        return x10
    x11 = apply(x9, x10)
    if x == 11:
        return x11
    x12 = mapply(x7, x11)
    if x == 12:
        return x12
    x13 = fill(x4, FOUR, x12)
    if x == 13:
        return x13
    x14 = rbind(get_nth_f, F0)
    if x == 14:
        return x14
    x15 = rbind(get_nth_f, L1)
    if x == 15:
        return x15
    x16 = fork(subtract, x15, x14)
    if x == 16:
        return x16
    x17 = fork(shoot, x14, x16)
    if x == 17:
        return x17
    x18 = corners(x6)
    if x == 18:
        return x18
    x19 = f_ofcolor(x13, ZERO)
    if x == 19:
        return x19
    x20 = rbind(colorcount_f, ZERO)
    if x == 20:
        return x20
    x21 = rbind(toobject, x13)
    if x == 21:
        return x21
    x22 = chain(x20, x21, dneighbors)
    if x == 22:
        return x22
    x23 = matcher(x22, TWO)
    if x == 23:
        return x23
    x24 = sfilter_f(x19, x23)
    if x == 24:
        return x24
    x25 = rbind(adjacent, x2)
    if x == 25:
        return x25
    x26 = rbind(adjacent, x12)
    if x == 26:
        return x26
    x27 = fork(both, x25, x26)
    if x == 27:
        return x27
    x28 = compose(x27, initset)
    if x == 28:
        return x28
    x29 = sfilter_f(x24, x28)
    if x == 29:
        return x29
    x30 = product(x18, x29)
    if x == 30:
        return x30
    x31 = mapply(x17, x30)
    if x == 31:
        return x31
    O = fill(x13, FOUR, x31)
    return O

def solve_7447852a(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = colorfilter(x2, ZERO)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, L1)
    if x == 4:
        return x4
    x5 = compose(x4, center)
    if x == 5:
        return x5
    x6 = order(x3, x5)
    if x == 6:
        return x6
    x7 = size_t(x6)
    if x == 7:
        return x7
    x8 = interval(ZERO, x7, ONE)
    if x == 8:
        return x8
    x9 = pair(x6, x8)
    if x == 9:
        return x9
    x10 = interval(ZERO, x7, THREE)
    if x == 10:
        return x10
    x11 = rbind(contained, x10)
    if x == 11:
        return x11
    x12 = compose(x11, x4)
    if x == 12:
        return x12
    x13 = sfilter_t(x9, x12)
    if x == 13:
        return x13
    x14 = mapply(x1, x13)
    if x == 14:
        return x14
    O = fill(I, FOUR, x14)
    return O

def solve_ded97339(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = fork(connect, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = product(x4, x4)
    if x == 5:
        return x5
    x6 = apply(x3, x5)
    if x == 6:
        return x6
    x7 = fork(either, vline_i, hline_i)
    if x == 7:
        return x7
    x8 = mfilter_f(x6, x7)
    if x == 8:
        return x8
    O = underfill(I, EIGHT, x8)
    return O

def solve_d22278a0(S, I, x=0):
    x1 = asindices(I)
    if x == 1:
        return x1
    x2 = lbind(sfilter, x1)
    if x == 2:
        return x2
    x3 = rbind(get_rank, F0)
    if x == 3:
        return x3
    x4 = fork(multiply, sign, identity)
    if x == 4:
        return x4
    x5 = lbind(apply, x4)
    if x == 5:
        return x5
    x6 = chain(even, x3, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, F0)
    if x == 7:
        return x7
    x8 = rbind(get_nth_f, L1)
    if x == 8:
        return x8
    x9 = compose(center, x8)
    if x == 9:
        return x9
    x10 = fork(subtract, x7, x9)
    if x == 10:
        return x10
    x11 = compose(x6, x10)
    if x == 11:
        return x11
    x12 = lbind(compose, x11)
    if x == 12:
        return x12
    x13 = lbind(rbind, astuple)
    if x == 13:
        return x13
    x14 = chain(x2, x12, x13)
    if x == 14:
        return x14
    x15 = rbind(get_arg_rank, L1)
    if x == 15:
        return x15
    x16 = o_g(I, R5)
    if x == 16:
        return x16
    x17 = lbind(x15, x16)
    if x == 17:
        return x17
    x18 = fork(add, x7, x8)
    if x == 18:
        return x18
    x19 = chain(x18, x5, x10)
    if x == 19:
        return x19
    x20 = lbind(compose, x19)
    if x == 20:
        return x20
    x21 = lbind(lbind, astuple)
    if x == 21:
        return x21
    x22 = compose(x20, x21)
    if x == 22:
        return x22
    x23 = compose(x17, x22)
    if x == 23:
        return x23
    x24 = rbind(compose, x23)
    if x == 24:
        return x24
    x25 = lbind(rbind, equality)
    if x == 25:
        return x25
    x26 = chain(x2, x24, x25)
    if x == 26:
        return x26
    x27 = fork(intersection, x14, x26)
    if x == 27:
        return x27
    x28 = lbind(fork, greater)
    if x == 28:
        return x28
    x29 = rbind(compose, x22)
    if x == 29:
        return x29
    x30 = rbind(get_val_rank, L1)
    if x == 30:
        return x30
    x31 = lbind(lbind, x30)
    if x == 31:
        return x31
    x32 = rbind(remove, x16)
    if x == 32:
        return x32
    x33 = chain(x29, x31, x32)
    if x == 33:
        return x33
    x34 = compose(x20, x13)
    if x == 34:
        return x34
    x35 = fork(x28, x33, x34)
    if x == 35:
        return x35
    x36 = compose(x2, x35)
    if x == 36:
        return x36
    x37 = fork(intersection, x27, x36)
    if x == 37:
        return x37
    x38 = fork(recolor_i, color, x37)
    if x == 38:
        return x38
    x39 = mapply(x38, x16)
    if x == 39:
        return x39
    O = paint(I, x39)
    return O

def solve_e6721834(S, I, x=0):
    x1 = portrait_t(I)
    if x == 1:
        return x1
    x2 = branch(x1, vsplit, hsplit)
    if x == 2:
        return x2
    x3 = x2(I, TWO)
    if x == 3:
        return x3
    x4 = order(x3, numcolors_t)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = rbind(get_nth_f, F0)
    if x == 6:
        return x6
    x7 = lbind(occurrences, x5)
    if x == 7:
        return x7
    x8 = get_nth_t(x4, L1)
    if x == 8:
        return x8
    x9 = o_g(x8, R1)
    if x == 9:
        return x9
    x10 = merge_f(x9)
    if x == 10:
        return x10
    x11 = get_color_rank_f(x10, F0)
    if x == 11:
        return x11
    x12 = matcher(x6, x11)
    if x == 12:
        return x12
    x13 = compose(flip, x12)
    if x == 13:
        return x13
    x14 = rbind(sfilter, x13)
    if x == 14:
        return x14
    x15 = chain(x6, x7, x14)
    if x == 15:
        return x15
    x16 = rbind(corner, R0)
    if x == 16:
        return x16
    x17 = compose(x16, x14)
    if x == 17:
        return x17
    x18 = fork(subtract, x15, x17)
    if x == 18:
        return x18
    x19 = fork(shift, identity, x18)
    if x == 19:
        return x19
    x20 = compose(x7, x14)
    if x == 20:
        return x20
    x21 = chain(positive, size, x20)
    if x == 21:
        return x21
    x22 = sfilter_f(x9, x21)
    if x == 22:
        return x22
    x23 = apply(x19, x22)
    if x == 23:
        return x23
    x24 = compose(decrement, width_f)
    if x == 24:
        return x24
    x25 = chain(positive, decrement, x24)
    if x == 25:
        return x25
    x26 = mfilter_f(x23, x25)
    if x == 26:
        return x26
    O = paint(x5, x26)
    return O

def solve_6855a6e4(S, I, x=0):
    x1 = fgpartition(I)
    if x == 1:
        return x1
    x2 = colorfilter(x1, TWO)
    if x == 2:
        return x2
    x3 = get_nth_f(x2, F0)
    if x == 3:
        return x3
    x4 = portrait_f(x3)
    if x == 4:
        return x4
    x5 = mir_rot_t(I, R4)
    if x == 5:
        return x5
    x6 = branch(x4, I, x5)
    if x == 6:
        return x6
    x7 = o_g(x6, R5)
    if x == 7:
        return x7
    x8 = colorfilter(x7, FIVE)
    if x == 8:
        return x8
    x9 = merge_f(x8)
    if x == 9:
        return x9
    x10 = cover(x6, x9)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, F0)
    if x == 11:
        return x11
    x12 = compose(x11, center)
    if x == 12:
        return x12
    x13 = apply(center, x8)
    if x == 13:
        return x13
    x14 = get_val_rank_f(x13, x11, L1)
    if x == 14:
        return x14
    x15 = matcher(x12, x14)
    if x == 15:
        return x15
    x16 = extract(x8, x15)
    if x == 16:
        return x16
    x17 = subgrid(x16, x6)
    if x == 17:
        return x17
    x18 = mir_rot_t(x17, R0)
    if x == 18:
        return x18
    x19 = f_ofcolor(x18, FIVE)
    if x == 19:
        return x19
    x20 = recolor_i(FIVE, x19)
    if x == 20:
        return x20
    x21 = corner(x16, R0)
    if x == 21:
        return x21
    x22 = height_f(x20)
    if x == 22:
        return x22
    x23 = add(THREE, x22)
    if x == 23:
        return x23
    x24 = toivec(x23)
    if x == 24:
        return x24
    x25 = add(x21, x24)
    if x == 25:
        return x25
    x26 = shift(x20, x25)
    if x == 26:
        return x26
    x27 = paint(x10, x26)
    if x == 27:
        return x27
    x28 = compose(flip, x15)
    if x == 28:
        return x28
    x29 = extract(x8, x28)
    if x == 29:
        return x29
    x30 = subgrid(x29, x6)
    if x == 30:
        return x30
    x31 = mir_rot_t(x30, R0)
    if x == 31:
        return x31
    x32 = f_ofcolor(x31, FIVE)
    if x == 32:
        return x32
    x33 = recolor_i(FIVE, x32)
    if x == 33:
        return x33
    x34 = corner(x29, R0)
    if x == 34:
        return x34
    x35 = height_f(x33)
    if x == 35:
        return x35
    x36 = add(THREE, x35)
    if x == 36:
        return x36
    x37 = toivec(x36)
    if x == 37:
        return x37
    x38 = subtract(x34, x37)
    if x == 38:
        return x38
    x39 = shift(x33, x38)
    if x == 39:
        return x39
    x40 = paint(x27, x39)
    if x == 40:
        return x40
    x41 = mir_rot_t(x40, R6)
    if x == 41:
        return x41
    O = branch(x4, x40, x41)
    return O

def solve_846bdb03(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = rbind(colorcount_f, FOUR)
    if x == 2:
        return x2
    x3 = matcher(x2, ZERO)
    if x == 3:
        return x3
    x4 = extract(x1, x3)
    if x == 4:
        return x4
    x5 = remove_f(x4, x1)
    if x == 5:
        return x5
    x6 = merge_f(x5)
    if x == 6:
        return x6
    x7 = subgrid(x6, I)
    if x == 7:
        return x7
    x8 = index(x7, DOWN)
    if x == 8:
        return x8
    x9 = subgrid(x4, I)
    if x == 9:
        return x9
    x10 = lefthalf(x9)
    if x == 10:
        return x10
    x11 = palette_t(x10)
    if x == 11:
        return x11
    x12 = other_f(x11, ZERO)
    if x == 12:
        return x12
    x13 = equality(x8, x12)
    if x == 13:
        return x13
    x14 = rbind(mir_rot_f, R2)
    if x == 14:
        return x14
    x15 = branch(x13, identity, x14)
    if x == 15:
        return x15
    x16 = x15(x4)
    if x == 16:
        return x16
    x17 = normalize(x16)
    if x == 17:
        return x17
    x18 = shift(x17, UNITY)
    if x == 18:
        return x18
    O = paint(x7, x18)
    return O

def solve_00d62c1b(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = rbind(bordering, I)
    if x == 3:
        return x3
    x4 = compose(flip, x3)
    if x == 4:
        return x4
    x5 = mfilter_f(x2, x4)
    if x == 5:
        return x5
    O = fill(I, FOUR, x5)
    return O

def solve_b9b7f026(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    x3 = remove_f(x2, x1)
    if x == 3:
        return x3
    x4 = rbind(adjacent, x2)
    if x == 4:
        return x4
    x5 = extract(x3, x4)
    if x == 5:
        return x5
    x6 = color(x5)
    if x == 6:
        return x6
    O = canvas(x6, UNITY)
    return O

def solve_e8593010(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    x4 = fill(I, THREE, x3)
    if x == 4:
        return x4
    x5 = sizefilter(x1, TWO)
    if x == 5:
        return x5
    x6 = merge_f(x5)
    if x == 6:
        return x6
    x7 = fill(x4, TWO, x6)
    if x == 7:
        return x7
    O = replace(x7, ZERO, ONE)
    return O

def solve_2bee17df(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = interval(ZERO, x1, ONE)
    if x == 2:
        return x2
    x3 = rbind(colorcount_t, ZERO)
    if x == 3:
        return x3
    x4 = subtract(x1, TWO)
    if x == 4:
        return x4
    x5 = matcher(x3, x4)
    if x == 5:
        return x5
    x6 = lbind(apply, x5)
    if x == 6:
        return x6
    x7 = rbind(vsplit, x1)
    if x == 7:
        return x7
    x8 = compose(x6, x7)
    if x == 8:
        return x8
    x9 = x8(I)
    if x == 9:
        return x9
    x10 = pair(x2, x9)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, L1)
    if x == 11:
        return x11
    x12 = sfilter_t(x10, x11)
    if x == 12:
        return x12
    x13 = mapply(hfrontier, x12)
    if x == 13:
        return x13
    x14 = mir_rot_t(I, R4)
    if x == 14:
        return x14
    x15 = x8(x14)
    if x == 15:
        return x15
    x16 = pair(x15, x2)
    if x == 16:
        return x16
    x17 = rbind(get_nth_f, F0)
    if x == 17:
        return x17
    x18 = sfilter_t(x16, x17)
    if x == 18:
        return x18
    x19 = mapply(vfrontier, x18)
    if x == 19:
        return x19
    x20 = astuple(x13, x19)
    if x == 20:
        return x20
    x21 = merge_t(x20)
    if x == 21:
        return x21
    O = underfill(I, THREE, x21)
    return O

def solve_0e206a2e(S, I, x=0):
    x1 = lbind(lbind, shift)
    if x == 1:
        return x1
    x2 = compose(x1, normalize)
    if x == 2:
        return x2
    x3 = lbind(rbind, subtract)
    if x == 3:
        return x3
    x4 = rbind(corner, R0)
    if x == 4:
        return x4
    x5 = compose(x3, x4)
    if x == 5:
        return x5
    x6 = palette_t(I)
    if x == 6:
        return x6
    x7 = remove(ZERO, x6)
    if x == 7:
        return x7
    x8 = lbind(colorcount_t, I)
    if x == 8:
        return x8
    x9 = get_arg_rank_f(x7, x8, F0)
    if x == 9:
        return x9
    x10 = remove(x9, x7)
    if x == 10:
        return x10
    x11 = rbind(contained, x10)
    if x == 11:
        return x11
    x12 = rbind(get_nth_f, F0)
    if x == 12:
        return x12
    x13 = compose(x11, x12)
    if x == 13:
        return x13
    x14 = rbind(sfilter, x13)
    if x == 14:
        return x14
    x15 = chain(x5, x14, normalize)
    if x == 15:
        return x15
    x16 = lbind(occurrences, I)
    if x == 16:
        return x16
    x17 = chain(x16, x14, normalize)
    if x == 17:
        return x17
    x18 = fork(apply, x15, x17)
    if x == 18:
        return x18
    x19 = fork(mapply, x2, x18)
    if x == 19:
        return x19
    x20 = rbind(mir_rot_f, R3)
    if x == 20:
        return x20
    x21 = rbind(mir_rot_f, R1)
    if x == 21:
        return x21
    x22 = astuple(x20, x21)
    if x == 22:
        return x22
    x23 = rbind(mir_rot_f, R0)
    if x == 23:
        return x23
    x24 = rbind(mir_rot_f, R2)
    if x == 24:
        return x24
    x25 = astuple(x23, x24)
    if x == 25:
        return x25
    x26 = combine(x22, x25)
    if x == 26:
        return x26
    x27 = rbind(get_nth_f, L1)
    if x == 27:
        return x27
    x28 = fork(compose, x12, x27)
    if x == 28:
        return x28
    x29 = product(x26, x26)
    if x == 29:
        return x29
    x30 = apply(x28, x29)
    if x == 30:
        return x30
    x31 = totuple(x30)
    if x == 31:
        return x31
    x32 = combine(x26, x31)
    if x == 32:
        return x32
    x33 = lbind(rapply, x32)
    if x == 33:
        return x33
    x34 = o_g(I, R1)
    if x == 34:
        return x34
    x35 = rbind(greater, ONE)
    if x == 35:
        return x35
    x36 = compose(x35, numcolors_f)
    if x == 36:
        return x36
    x37 = sfilter(x34, x36)
    if x == 37:
        return x37
    x38 = mapply(x33, x37)
    if x == 38:
        return x38
    x39 = mapply(x19, x38)
    if x == 39:
        return x39
    x40 = paint(I, x39)
    if x == 40:
        return x40
    x41 = merge_f(x37)
    if x == 41:
        return x41
    O = cover(x40, x41)
    return O

def solve_1f876c06(S, I, x=0):
    x1 = rbind(get_nth_f, L1)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = power(x1, TWO)
    if x == 4:
        return x4
    x5 = fork(connect, x3, x4)
    if x == 5:
        return x5
    x6 = fork(recolor_i, color, x5)
    if x == 6:
        return x6
    x7 = fgpartition(I)
    if x == 7:
        return x7
    x8 = mapply(x6, x7)
    if x == 8:
        return x8
    O = paint(I, x8)
    return O

def solve_4c5c2cf0(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = mir_rot_t(x3, R0)
    if x == 4:
        return x4
    x5 = o_g(x4, R3)
    if x == 5:
        return x5
    x6 = get_nth_f(x5, F0)
    if x == 6:
        return x6
    x7 = o_g(I, R7)
    if x == 7:
        return x7
    x8 = rbind(mir_rot_t, R4)
    if x == 8:
        return x8
    x9 = fork(equality, identity, x8)
    if x == 9:
        return x9
    x10 = rbind(subgrid, I)
    if x == 10:
        return x10
    x11 = compose(x9, x10)
    if x == 11:
        return x11
    x12 = extract(x7, x11)
    if x == 12:
        return x12
    x13 = center(x12)
    if x == 13:
        return x13
    x14 = o_g(x4, R7)
    if x == 14:
        return x14
    x15 = rbind(subgrid, x4)
    if x == 15:
        return x15
    x16 = compose(x9, x15)
    if x == 16:
        return x16
    x17 = extract(x14, x16)
    if x == 17:
        return x17
    x18 = center(x17)
    if x == 18:
        return x18
    x19 = subtract(x13, x18)
    if x == 19:
        return x19
    x20 = shift(x6, x19)
    if x == 20:
        return x20
    x21 = paint(I, x20)
    if x == 21:
        return x21
    x22 = o_g(x21, R3)
    if x == 22:
        return x22
    x23 = get_nth_f(x22, F0)
    if x == 23:
        return x23
    x24 = subgrid(x23, x21)
    if x == 24:
        return x24
    x25 = mir_rot_t(x24, R2)
    if x == 25:
        return x25
    x26 = o_g(x25, R3)
    if x == 26:
        return x26
    x27 = get_nth_f(x26, F0)
    if x == 27:
        return x27
    x28 = o_g(x25, R7)
    if x == 28:
        return x28
    x29 = color(x12)
    if x == 29:
        return x29
    x30 = matcher(color, x29)
    if x == 30:
        return x30
    x31 = extract(x28, x30)
    if x == 31:
        return x31
    x32 = center(x31)
    if x == 32:
        return x32
    x33 = subtract(x13, x32)
    if x == 33:
        return x33
    x34 = shift(x27, x33)
    if x == 34:
        return x34
    O = paint(x21, x34)
    return O

def solve_d5d6de2d(S, I, x=0):
    x1 = replace(I, TWO, ZERO)
    if x == 1:
        return x1
    x2 = compose(backdrop, inbox)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = sfilter_f(x3, square_f)
    if x == 4:
        return x4
    x5 = difference(x3, x4)
    if x == 5:
        return x5
    x6 = mapply(x2, x5)
    if x == 6:
        return x6
    O = fill(x1, THREE, x6)
    return O

def solve_46442a0e(S, I, x=0):
    x1 = mir_rot_t(I, R4)
    if x == 1:
        return x1
    x2 = hconcat(I, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(I, R6)
    if x == 3:
        return x3
    x4 = mir_rot_t(I, R5)
    if x == 4:
        return x4
    x5 = hconcat(x3, x4)
    if x == 5:
        return x5
    O = vconcat(x2, x5)
    return O

def solve_29c11459(S, I, x=0):
    x1 = compose(hfrontier, center)
    if x == 1:
        return x1
    x2 = fork(recolor_i, color, x1)
    if x == 2:
        return x2
    x3 = righthalf(I)
    if x == 3:
        return x3
    x4 = o_g(x3, R5)
    if x == 4:
        return x4
    x5 = mapply(x2, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = lefthalf(I)
    if x == 7:
        return x7
    x8 = o_g(x7, R5)
    if x == 8:
        return x8
    x9 = mapply(x2, x8)
    if x == 9:
        return x9
    x10 = paint(x7, x9)
    if x == 10:
        return x10
    x11 = o_g(x10, R5)
    if x == 11:
        return x11
    x12 = merge_f(x11)
    if x == 12:
        return x12
    x13 = paint(x6, x12)
    if x == 13:
        return x13
    x14 = rbind(corner, R1)
    if x == 14:
        return x14
    x15 = apply(x14, x11)
    if x == 15:
        return x15
    x16 = shift(x15, RIGHT)
    if x == 16:
        return x16
    O = fill(x13, FIVE, x16)
    return O

def solve_508bd3b6(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    x3 = corner(x2, R0)
    if x == 3:
        return x3
    x4 = index(I, x3)
    if x == 4:
        return x4
    x5 = equality(x4, EIGHT)
    if x == 5:
        return x5
    x6 = corner(x2, R1)
    if x == 6:
        return x6
    x7 = branch(x5, x3, x6)
    if x == 7:
        return x7
    x8 = branch(x5, UNITY, DOWN_LEFT)
    if x == 8:
        return x8
    x9 = width_t(I)
    if x == 9:
        return x9
    x10 = multiply(x8, x9)
    if x == 10:
        return x10
    x11 = double(x10)
    if x == 11:
        return x11
    x12 = add(x7, x11)
    if x == 12:
        return x12
    x13 = subtract(x7, x11)
    if x == 13:
        return x13
    x14 = connect(x12, x13)
    if x == 14:
        return x14
    x15 = fill(I, THREE, x14)
    if x == 15:
        return x15
    x16 = get_arg_rank_f(x1, size, F0)
    if x == 16:
        return x16
    x17 = paint(x15, x16)
    if x == 17:
        return x17
    x18 = o_g(x17, R5)
    if x == 18:
        return x18
    x19 = rbind(adjacent, x16)
    if x == 19:
        return x19
    x20 = extract(x18, x19)
    if x == 20:
        return x20
    x21 = get_nth_f(x20, F0)
    if x == 21:
        return x21
    x22 = get_nth_t(x21, L1)
    if x == 22:
        return x22
    x23 = flip(x5)
    if x == 23:
        return x23
    x24 = branch(x23, UNITY, DOWN_LEFT)
    if x == 24:
        return x24
    x25 = multiply(x24, x9)
    if x == 25:
        return x25
    x26 = double(x25)
    if x == 26:
        return x26
    x27 = add(x22, x26)
    if x == 27:
        return x27
    x28 = subtract(x22, x26)
    if x == 28:
        return x28
    x29 = connect(x27, x28)
    if x == 29:
        return x29
    x30 = fill(x17, THREE, x29)
    if x == 30:
        return x30
    x31 = paint(x30, x2)
    if x == 31:
        return x31
    O = paint(x31, x16)
    return O

def solve_4093f84a(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = portrait_f(x1)
    if x == 2:
        return x2
    x3 = rbind(mir_rot_t, R1)
    if x == 3:
        return x3
    x4 = branch(x2, identity, x3)
    if x == 4:
        return x4
    x5 = rbind(order, identity)
    if x == 5:
        return x5
    x6 = get_color_rank_t(I, L1)
    if x == 6:
        return x6
    x7 = replace(I, x6, FIVE)
    if x == 7:
        return x7
    x8 = x4(x7)
    if x == 8:
        return x8
    x9 = lefthalf(x8)
    if x == 9:
        return x9
    x10 = apply(x5, x9)
    if x == 10:
        return x10
    x11 = rbind(order, invert)
    if x == 11:
        return x11
    x12 = righthalf(x8)
    if x == 12:
        return x12
    x13 = apply(x11, x12)
    if x == 13:
        return x13
    x14 = hconcat(x10, x13)
    if x == 14:
        return x14
    O = x4(x14)
    return O

def solve_29623171(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = rbind(interval, ONE)
    if x == 2:
        return x2
    x3 = rbind(add, THREE)
    if x == 3:
        return x3
    x4 = fork(x2, identity, x3)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, F0)
    if x == 5:
        return x5
    x6 = compose(x4, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, L1)
    if x == 7:
        return x7
    x8 = compose(x4, x7)
    if x == 8:
        return x8
    x9 = fork(product, x6, x8)
    if x == 9:
        return x9
    x10 = interval(ZERO, NINE, FOUR)
    if x == 10:
        return x10
    x11 = product(x10, x10)
    if x == 11:
        return x11
    x12 = apply(x9, x11)
    if x == 12:
        return x12
    x13 = rbind(colorcount_f, x1)
    if x == 13:
        return x13
    x14 = rbind(toobject, I)
    if x == 14:
        return x14
    x15 = compose(x13, x14)
    if x == 15:
        return x15
    x16 = get_val_rank_f(x12, x15, F0)
    if x == 16:
        return x16
    x17 = matcher(x15, x16)
    if x == 17:
        return x17
    x18 = mfilter_f(x12, x17)
    if x == 18:
        return x18
    x19 = fill(I, x1, x18)
    if x == 19:
        return x19
    x20 = compose(flip, x17)
    if x == 20:
        return x20
    x21 = mfilter_f(x12, x20)
    if x == 21:
        return x21
    O = fill(x19, ZERO, x21)
    return O

def solve_e26a3af2(S, I, x=0):
    x1 = compose(size, dedupe)
    if x == 1:
        return x1
    x2 = rbind(get_common_rank, F0)
    if x == 2:
        return x2
    x3 = mir_rot_t(I, R4)
    if x == 3:
        return x3
    x4 = apply(x2, x3)
    if x == 4:
        return x4
    x5 = x1(x4)
    if x == 5:
        return x5
    x6 = apply(x2, I)
    if x == 6:
        return x6
    x7 = x1(x6)
    if x == 7:
        return x7
    x8 = greater(x5, x7)
    if x == 8:
        return x8
    x9 = branch(x8, vupscale, hupscale)
    if x == 9:
        return x9
    x10 = repeat(x4, ONE)
    if x == 10:
        return x10
    x11 = repeat(x6, ONE)
    if x == 11:
        return x11
    x12 = mir_rot_t(x11, R4)
    if x == 12:
        return x12
    x13 = branch(x8, x10, x12)
    if x == 13:
        return x13
    x14 = branch(x8, height_t, width_t)
    if x == 14:
        return x14
    x15 = x14(I)
    if x == 15:
        return x15
    O = x9(x13, x15)
    return O

def solve_6d0160f0(S, I, x=0):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = asindices(x1)
    if x == 2:
        return x2
    x3 = recolor_i(ZERO, x2)
    if x == 3:
        return x3
    x4 = lbind(shift, x3)
    if x == 4:
        return x4
    x5 = initset(ZERO)
    if x == 5:
        return x5
    x6 = insert(FOUR, x5)
    if x == 6:
        return x6
    x7 = insert(EIGHT, x6)
    if x == 7:
        return x7
    x8 = product(x7, x7)
    if x == 8:
        return x8
    x9 = mapply(x4, x8)
    if x == 9:
        return x9
    x10 = paint(I, x9)
    if x == 10:
        return x10
    x11 = f_ofcolor(I, FOUR)
    if x == 11:
        return x11
    x12 = get_nth_f(x11, F0)
    if x == 12:
        return x12
    x13 = get_nth_f(x12, F0)
    if x == 13:
        return x13
    x14 = greater(x13, SEVEN)
    if x == 14:
        return x14
    x15 = greater(x13, THREE)
    if x == 15:
        return x15
    x16 = branch(x15, FOUR, ZERO)
    if x == 16:
        return x16
    x17 = branch(x14, EIGHT, x16)
    if x == 17:
        return x17
    x18 = get_nth_t(x12, L1)
    if x == 18:
        return x18
    x19 = greater(x18, SEVEN)
    if x == 19:
        return x19
    x20 = greater(x18, THREE)
    if x == 20:
        return x20
    x21 = branch(x20, FOUR, ZERO)
    if x == 21:
        return x21
    x22 = branch(x19, EIGHT, x21)
    if x == 22:
        return x22
    x23 = astuple(x17, x22)
    if x == 23:
        return x23
    x24 = crop(I, x23, THREE_BY_THREE)
    if x == 24:
        return x24
    x25 = replace(x24, FIVE, ZERO)
    if x == 25:
        return x25
    x26 = asindices(x25)
    if x == 26:
        return x26
    x27 = toobject(x26, x25)
    if x == 27:
        return x27
    x28 = f_ofcolor(x25, FOUR)
    if x == 28:
        return x28
    x29 = get_nth_f(x28, F0)
    if x == 29:
        return x29
    x30 = multiply(x29, FOUR)
    if x == 30:
        return x30
    x31 = shift(x27, x30)
    if x == 31:
        return x31
    O = paint(x10, x31)
    return O

def solve_a85d4709(S, I, x=0):
    x1 = lbind(mapply, hfrontier)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, FIVE)
    if x == 2:
        return x2
    x3 = lbind(sfilter, x2)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, L1)
    if x == 4:
        return x4
    x5 = lbind(matcher, x4)
    if x == 5:
        return x5
    x6 = chain(x1, x3, x5)
    if x == 6:
        return x6
    x7 = x6(ZERO)
    if x == 7:
        return x7
    x8 = fill(I, TWO, x7)
    if x == 8:
        return x8
    x9 = x6(TWO)
    if x == 9:
        return x9
    x10 = fill(x8, THREE, x9)
    if x == 10:
        return x10
    x11 = x6(ONE)
    if x == 11:
        return x11
    O = fill(x10, FOUR, x11)
    return O

def solve_3ac3eb23(S, I, x=0):
    x1 = rbind(get_nth_f, L1)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = chain(ineighbors, x1, x2)
    if x == 3:
        return x3
    x4 = fork(recolor_i, color, x3)
    if x == 4:
        return x4
    x5 = o_g(I, R5)
    if x == 5:
        return x5
    x6 = mapply(x4, x5)
    if x == 6:
        return x6
    x7 = paint(I, x6)
    if x == 7:
        return x7
    x8 = vsplit(x7, THREE)
    if x == 8:
        return x8
    x9 = get_nth_f(x8, F0)
    if x == 9:
        return x9
    x10 = vconcat(x9, x9)
    if x == 10:
        return x10
    O = vconcat(x9, x10)
    return O

def solve_b27ca6d3(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, TWO)
    if x == 2:
        return x2
    x3 = mapply(outbox, x2)
    if x == 3:
        return x3
    O = fill(I, THREE, x3)
    return O

def solve_2281f1f4(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = corner(x1, R1)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, F0)
    if x == 3:
        return x3
    x4 = power(x3, TWO)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, L1)
    if x == 5:
        return x5
    x6 = power(x5, TWO)
    if x == 6:
        return x6
    x7 = fork(astuple, x4, x6)
    if x == 7:
        return x7
    x8 = product(x1, x1)
    if x == 8:
        return x8
    x9 = apply(x7, x8)
    if x == 9:
        return x9
    x10 = remove_t(x2, x9)
    if x == 10:
        return x10
    O = underfill(I, TWO, x10)
    return O

def solve_d364b489(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = shift(x1, DOWN)
    if x == 2:
        return x2
    x3 = fill(I, EIGHT, x2)
    if x == 3:
        return x3
    x4 = shift(x1, UP)
    if x == 4:
        return x4
    x5 = fill(x3, TWO, x4)
    if x == 5:
        return x5
    x6 = shift(x1, RIGHT)
    if x == 6:
        return x6
    x7 = fill(x5, SIX, x6)
    if x == 7:
        return x7
    x8 = shift(x1, LEFT)
    if x == 8:
        return x8
    O = fill(x7, SEVEN, x8)
    return O

def solve_007bbfb7(S, I, x=0):
    x1 = hupscale(I, THREE)
    if x == 1:
        return x1
    x2 = vupscale(x1, THREE)
    if x == 2:
        return x2
    x3 = hconcat(I, I)
    if x == 3:
        return x3
    x4 = hconcat(x3, I)
    if x == 4:
        return x4
    x5 = vconcat(x4, x4)
    if x == 5:
        return x5
    x6 = vconcat(x5, x4)
    if x == 6:
        return x6
    O = cellwise(x2, x6, ZERO)
    return O

def solve_a9f96cdd(S, I, x=0):
    x1 = replace(I, TWO, ZERO)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, TWO)
    if x == 2:
        return x2
    x3 = shift(x2, NEG_UNITY)
    if x == 3:
        return x3
    x4 = fill(x1, THREE, x3)
    if x == 4:
        return x4
    x5 = shift(x2, UP_RIGHT)
    if x == 5:
        return x5
    x6 = fill(x4, SIX, x5)
    if x == 6:
        return x6
    x7 = shift(x2, DOWN_LEFT)
    if x == 7:
        return x7
    x8 = fill(x6, EIGHT, x7)
    if x == 8:
        return x8
    x9 = shift(x2, UNITY)
    if x == 9:
        return x9
    O = fill(x8, SEVEN, x9)
    return O

def solve_760b3cac(S, I, x=0):
    x1 = f_ofcolor(I, EIGHT)
    if x == 1:
        return x1
    x2 = mir_rot_f(x1, R2)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, FOUR)
    if x == 3:
        return x3
    x4 = corner(x3, R0)
    if x == 4:
        return x4
    x5 = index(I, x4)
    if x == 5:
        return x5
    x6 = equality(x5, FOUR)
    if x == 6:
        return x6
    x7 = branch(x6, NEG_ONE, ONE)
    if x == 7:
        return x7
    x8 = multiply(x7, THREE)
    if x == 8:
        return x8
    x9 = tojvec(x8)
    if x == 9:
        return x9
    x10 = shift(x2, x9)
    if x == 10:
        return x10
    O = fill(I, EIGHT, x10)
    return O

def solve_a699fb00(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = shift(x1, RIGHT)
    if x == 2:
        return x2
    x3 = shift(x1, LEFT)
    if x == 3:
        return x3
    x4 = intersection(x2, x3)
    if x == 4:
        return x4
    O = fill(I, TWO, x4)
    return O

def solve_890034e9(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = normalize(x2)
    if x == 3:
        return x3
    x4 = shift(x3, NEG_UNITY)
    if x == 4:
        return x4
    x5 = lbind(shift, x4)
    if x == 5:
        return x5
    x6 = inbox(x2)
    if x == 6:
        return x6
    x7 = recolor_i(ZERO, x6)
    if x == 7:
        return x7
    x8 = occurrences(I, x7)
    if x == 8:
        return x8
    x9 = mapply(x5, x8)
    if x == 9:
        return x9
    O = fill(I, x1, x9)
    return O

def solve_ce4f8723(S, I, x=0):
    x1 = astuple(FOUR, FOUR)
    if x == 1:
        return x1
    x2 = canvas(THREE, x1)
    if x == 2:
        return x2
    x3 = tophalf(I)
    if x == 3:
        return x3
    x4 = f_ofcolor(x3, ZERO)
    if x == 4:
        return x4
    x5 = bottomhalf(I)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, ZERO)
    if x == 6:
        return x6
    x7 = intersection(x4, x6)
    if x == 7:
        return x7
    O = fill(x2, ZERO, x7)
    return O

def solve_3bdb4ada(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = compose(x2, x1)
    if x == 3:
        return x3
    x4 = power(x2, TWO)
    if x == 4:
        return x4
    x5 = fork(subtract, x3, x4)
    if x == 5:
        return x5
    x6 = compose(even, x5)
    if x == 6:
        return x6
    x7 = lbind(compose, x6)
    if x == 7:
        return x7
    x8 = lbind(rbind, astuple)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = fork(sfilter, x1, x9)
    if x == 10:
        return x10
    x11 = rbind(corner, R0)
    if x == 11:
        return x11
    x12 = compose(increment, x11)
    if x == 12:
        return x12
    x13 = o_g(I, R5)
    if x == 13:
        return x13
    x14 = totuple(x13)
    if x == 14:
        return x14
    x15 = apply(x12, x14)
    if x == 15:
        return x15
    x16 = rbind(corner, R3)
    if x == 16:
        return x16
    x17 = compose(decrement, x16)
    if x == 17:
        return x17
    x18 = apply(x17, x14)
    if x == 18:
        return x18
    x19 = papply(connect, x15, x18)
    if x == 19:
        return x19
    x20 = apply(x2, x15)
    if x == 20:
        return x20
    x21 = pair(x19, x20)
    if x == 21:
        return x21
    x22 = mapply(x10, x21)
    if x == 22:
        return x22
    O = fill(I, ZERO, x22)
    return O

def solve_2c608aff(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x2, size, F0)
    if x == 3:
        return x3
    x4 = toindices(x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, x1)
    if x == 5:
        return x5
    x6 = prapply(connect, x4, x5)
    if x == 6:
        return x6
    x7 = fork(either, vline_i, hline_i)
    if x == 7:
        return x7
    x8 = mfilter_f(x6, x7)
    if x == 8:
        return x8
    O = underfill(I, x1, x8)
    return O

def solve_a79310a0(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = move(I, x2, DOWN)
    if x == 3:
        return x3
    O = replace(x3, EIGHT, TWO)
    return O

def solve_f76d97a5(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = get_nth_f(x1, L1)
    if x == 3:
        return x3
    x4 = switch(I, x2, x3)
    if x == 4:
        return x4
    O = replace(x4, FIVE, ZERO)
    return O

def solve_ff28f65a(S, I, x=0):
    x1 = astuple(ONE, NINE)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = size_f(x3)
    if x == 4:
        return x4
    x5 = double(x4)
    if x == 5:
        return x5
    x6 = interval(ZERO, x5, TWO)
    if x == 6:
        return x6
    x7 = apply(tojvec, x6)
    if x == 7:
        return x7
    x8 = fill(x2, ONE, x7)
    if x == 8:
        return x8
    x9 = hsplit(x8, THREE)
    if x == 9:
        return x9
    O = merge_t(x9)
    return O

def solve_963e52fc(S, I, x=0):
    x1 = asobject(I)
    if x == 1:
        return x1
    x2 = corner(x1, R0)
    if x == 2:
        return x2
    x3 = height_f(x1)
    if x == 3:
        return x3
    x4 = hperiod(x1)
    if x == 4:
        return x4
    x5 = astuple(x3, x4)
    if x == 5:
        return x5
    x6 = crop(I, x2, x5)
    if x == 6:
        return x6
    x7 = mir_rot_t(x6, R4)
    if x == 7:
        return x7
    x8 = width_t(I)
    if x == 8:
        return x8
    x9 = double(x8)
    if x == 9:
        return x9
    x10 = divide(x9, x4)
    if x == 10:
        return x10
    x11 = increment(x10)
    if x == 11:
        return x11
    x12 = repeat(x7, x11)
    if x == 12:
        return x12
    x13 = merge_t(x12)
    if x == 13:
        return x13
    x14 = mir_rot_t(x13, R6)
    if x == 14:
        return x14
    x15 = astuple(x3, x9)
    if x == 15:
        return x15
    O = crop(x14, ORIGIN, x15)
    return O

def solve_3aa6fb7a(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = mapply(corners, x1)
    if x == 2:
        return x2
    O = underfill(I, ONE, x2)
    return O

def solve_4c4377d9(S, I, x=0):
    x1 = mir_rot_t(I, R0)
    if x == 1:
        return x1
    O = vconcat(x1, I)
    return O

def solve_d4a91cb9(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = get_nth_f(x2, F0)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = get_nth_t(x5, L1)
    if x == 6:
        return x6
    x7 = astuple(x3, x6)
    if x == 7:
        return x7
    x8 = connect(x7, x5)
    if x == 8:
        return x8
    x9 = connect(x7, x2)
    if x == 9:
        return x9
    x10 = combine_f(x8, x9)
    if x == 10:
        return x10
    O = underfill(I, FOUR, x10)
    return O

def solve_05f2a901(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = colorfilter(x1, TWO)
    if x == 2:
        return x2
    x3 = get_nth_f(x2, F0)
    if x == 3:
        return x3
    x4 = colorfilter(x1, EIGHT)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = gravitate(x3, x5)
    if x == 6:
        return x6
    O = move(I, x3, x6)
    return O

def solve_855e0971(S, I, x=0):
    x1 = frontiers(I)
    if x == 1:
        return x1
    x2 = sfilter_f(x1, hline_o)
    if x == 2:
        return x2
    x3 = size_f(x2)
    if x == 3:
        return x3
    x4 = positive(x3)
    if x == 4:
        return x4
    x5 = rbind(mir_rot_t, R1)
    if x == 5:
        return x5
    x6 = branch(x4, identity, x5)
    if x == 6:
        return x6
    x7 = x6(I)
    if x == 7:
        return x7
    x8 = lbind(mapply, vfrontier)
    if x == 8:
        return x8
    x9 = rbind(f_ofcolor, ZERO)
    if x == 9:
        return x9
    x10 = rbind(subgrid, x7)
    if x == 10:
        return x10
    x11 = chain(x8, x9, x10)
    if x == 11:
        return x11
    x12 = rbind(corner, R0)
    if x == 12:
        return x12
    x13 = fork(shift, x11, x12)
    if x == 13:
        return x13
    x14 = fork(intersection, toindices, x13)
    if x == 14:
        return x14
    x15 = partition(x7)
    if x == 15:
        return x15
    x16 = matcher(color, ZERO)
    if x == 16:
        return x16
    x17 = compose(flip, x16)
    if x == 17:
        return x17
    x18 = sfilter_f(x15, x17)
    if x == 18:
        return x18
    x19 = mapply(x14, x18)
    if x == 19:
        return x19
    x20 = fill(x7, ZERO, x19)
    if x == 20:
        return x20
    O = x6(x20)
    return O

def solve_ef135b50(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = fork(connect, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, TWO)
    if x == 4:
        return x4
    x5 = product(x4, x4)
    if x == 5:
        return x5
    x6 = power(x1, TWO)
    if x == 6:
        return x6
    x7 = compose(x1, x2)
    if x == 7:
        return x7
    x8 = fork(equality, x6, x7)
    if x == 8:
        return x8
    x9 = sfilter_f(x5, x8)
    if x == 9:
        return x9
    x10 = mapply(x3, x9)
    if x == 10:
        return x10
    x11 = f_ofcolor(I, ZERO)
    if x == 11:
        return x11
    x12 = intersection(x10, x11)
    if x == 12:
        return x12
    x13 = fill(I, NINE, x12)
    if x == 13:
        return x13
    x14 = trim(x13)
    if x == 14:
        return x14
    x15 = asobject(x14)
    if x == 15:
        return x15
    x16 = shift(x15, UNITY)
    if x == 16:
        return x16
    O = paint(I, x16)
    return O

def solve_228f6490(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = compose(normalize, toindices)
    if x == 4:
        return x4
    x5 = rbind(bordering, I)
    if x == 5:
        return x5
    x6 = compose(flip, x5)
    if x == 6:
        return x6
    x7 = sfilter_f(x2, x6)
    if x == 7:
        return x7
    x8 = get_nth_f(x7, F0)
    if x == 8:
        return x8
    x9 = x4(x8)
    if x == 9:
        return x9
    x10 = matcher(x4, x9)
    if x == 10:
        return x10
    x11 = extract(x3, x10)
    if x == 11:
        return x11
    x12 = corner(x8, R0)
    if x == 12:
        return x12
    x13 = corner(x11, R0)
    if x == 13:
        return x13
    x14 = subtract(x12, x13)
    if x == 14:
        return x14
    x15 = move(I, x11, x14)
    if x == 15:
        return x15
    x16 = get_nth_f(x7, L1)
    if x == 16:
        return x16
    x17 = x4(x16)
    if x == 17:
        return x17
    x18 = matcher(x4, x17)
    if x == 18:
        return x18
    x19 = extract(x3, x18)
    if x == 19:
        return x19
    x20 = corner(x16, R0)
    if x == 20:
        return x20
    x21 = corner(x19, R0)
    if x == 21:
        return x21
    x22 = subtract(x20, x21)
    if x == 22:
        return x22
    O = move(x15, x19, x22)
    return O

def solve_6ecd11f4(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x1, size, F0)
    if x == 4:
        return x4
    x5 = subgrid(x4, I)
    if x == 5:
        return x5
    x6 = width_t(x5)
    if x == 6:
        return x6
    x7 = width_t(x3)
    if x == 7:
        return x7
    x8 = divide(x6, x7)
    if x == 8:
        return x8
    x9 = downscale(x5, x8)
    if x == 9:
        return x9
    x10 = f_ofcolor(x9, ZERO)
    if x == 10:
        return x10
    O = fill(x3, ZERO, x10)
    return O

def solve_6e82a1ae(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = lbind(sizefilter, x1)
    if x == 2:
        return x2
    x3 = compose(merge, x2)
    if x == 3:
        return x3
    x4 = x3(TWO)
    if x == 4:
        return x4
    x5 = fill(I, THREE, x4)
    if x == 5:
        return x5
    x6 = x3(THREE)
    if x == 6:
        return x6
    x7 = fill(x5, TWO, x6)
    if x == 7:
        return x7
    x8 = x3(FOUR)
    if x == 8:
        return x8
    O = fill(x7, ONE, x8)
    return O

def solve_3bd67248(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    x3 = decrement(x2)
    if x == 3:
        return x3
    x4 = astuple(x3, ONE)
    if x == 4:
        return x4
    x5 = shoot(x4, UP_RIGHT)
    if x == 5:
        return x5
    x6 = fill(I, TWO, x5)
    if x == 6:
        return x6
    x7 = astuple(x2, ONE)
    if x == 7:
        return x7
    x8 = shoot(x7, RIGHT)
    if x == 8:
        return x8
    O = fill(x6, FOUR, x8)
    return O

def solve_d511f180(S, I, x=0):
    O = switch(I, FIVE, EIGHT)
    return O

def solve_017c7c7b(S, I, x=0):
    x1 = tophalf(I)
    if x == 1:
        return x1
    x2 = bottomhalf(I)
    if x == 2:
        return x2
    x3 = equality(x1, x2)
    if x == 3:
        return x3
    x4 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    if x == 4:
        return x4
    x5 = branch(x3, x2, x4)
    if x == 5:
        return x5
    x6 = vconcat(I, x5)
    if x == 6:
        return x6
    O = replace(x6, ONE, TWO)
    return O

def solve_e8dc4411(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, ZERO)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = rbind(corner, R0)
    if x == 4:
        return x4
    x5 = rbind(corner, R3)
    if x == 5:
        return x5
    x6 = fork(connect, x4, x5)
    if x == 6:
        return x6
    x7 = x6(x2)
    if x == 7:
        return x7
    x8 = intersection(x2, x7)
    if x == 8:
        return x8
    x9 = equality(x7, x8)
    if x == 9:
        return x9
    x10 = fork(subtract, identity, crement)
    if x == 10:
        return x10
    x11 = fork(add, identity, x10)
    if x == 11:
        return x11
    x12 = branch(x9, identity, x11)
    if x == 12:
        return x12
    x13 = shape_f(x2)
    if x == 13:
        return x13
    x14 = f_ofcolor(I, x1)
    if x == 14:
        return x14
    x15 = position(x2, x14)
    if x == 15:
        return x15
    x16 = multiply(x13, x15)
    if x == 16:
        return x16
    x17 = apply(x12, x16)
    if x == 17:
        return x17
    x18 = lbind(multiply, x17)
    if x == 18:
        return x18
    x19 = interval(ONE, FIVE, ONE)
    if x == 19:
        return x19
    x20 = apply(x18, x19)
    if x == 20:
        return x20
    x21 = mapply(x3, x20)
    if x == 21:
        return x21
    O = fill(I, x1, x21)
    return O

def solve_7ddcd7ec(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = get_nth_f(x3, F0)
    if x == 4:
        return x4
    x5 = color(x4)
    if x == 5:
        return x5
    x6 = lbind(position, x4)
    if x == 6:
        return x6
    x7 = fork(shoot, center, x6)
    if x == 7:
        return x7
    x8 = mapply(x7, x2)
    if x == 8:
        return x8
    O = fill(I, x5, x8)
    return O

def solve_beb8660c(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = compose(invert, size)
    if x == 4:
        return x4
    x5 = order(x3, x4)
    if x == 5:
        return x5
    x6 = apply(normalize, x5)
    if x == 6:
        return x6
    x7 = size(x6)
    if x == 7:
        return x7
    x8 = interval(ZERO, x7, ONE)
    if x == 8:
        return x8
    x9 = apply(toivec, x8)
    if x == 9:
        return x9
    x10 = mpapply(shift, x6, x9)
    if x == 10:
        return x10
    x11 = paint(x2, x10)
    if x == 11:
        return x11
    O = mir_rot_t(x11, R5)
    return O

def solve_75b8110e(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = tophalf(x1)
    if x == 2:
        return x2
    x3 = rbind(f_ofcolor, ZERO)
    if x == 3:
        return x3
    x4 = fork(difference, asindices, x3)
    if x == 4:
        return x4
    x5 = fork(toobject, x4, identity)
    if x == 5:
        return x5
    x6 = righthalf(I)
    if x == 6:
        return x6
    x7 = bottomhalf(x6)
    if x == 7:
        return x7
    x8 = x5(x7)
    if x == 8:
        return x8
    x9 = paint(x2, x8)
    if x == 9:
        return x9
    x10 = bottomhalf(x1)
    if x == 10:
        return x10
    x11 = x5(x10)
    if x == 11:
        return x11
    x12 = paint(x9, x11)
    if x == 12:
        return x12
    x13 = tophalf(x6)
    if x == 13:
        return x13
    x14 = x5(x13)
    if x == 14:
        return x14
    O = paint(x12, x14)
    return O

def solve_7fe24cdd(S, I, x=0):
    x1 = mir_rot_t(I, R4)
    if x == 1:
        return x1
    x2 = hconcat(I, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(I, R6)
    if x == 3:
        return x3
    x4 = mir_rot_t(I, R5)
    if x == 4:
        return x4
    x5 = hconcat(x3, x4)
    if x == 5:
        return x5
    O = vconcat(x2, x5)
    return O

def solve_7f4411dc(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = rbind(greater, TWO)
    if x == 3:
        return x3
    x4 = rbind(difference, x2)
    if x == 4:
        return x4
    x5 = chain(x3, size, x4)
    if x == 5:
        return x5
    x6 = compose(x5, dneighbors)
    if x == 6:
        return x6
    x7 = sfilter_f(x2, x6)
    if x == 7:
        return x7
    O = fill(I, ZERO, x7)
    return O

def solve_469497ad(S, I, x=0):
    x1 = numcolors_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    x3 = upscale_t(I, x2)
    if x == 3:
        return x3
    x4 = o_g(x3, R1)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x4, size, L1)
    if x == 5:
        return x5
    x6 = corner(x5, R0)
    if x == 6:
        return x6
    x7 = shoot(x6, NEG_UNITY)
    if x == 7:
        return x7
    x8 = shoot(x6, UNITY)
    if x == 8:
        return x8
    x9 = combine(x7, x8)
    if x == 9:
        return x9
    x10 = corner(x5, R2)
    if x == 10:
        return x10
    x11 = shoot(x10, DOWN_LEFT)
    if x == 11:
        return x11
    x12 = shoot(x10, UP_RIGHT)
    if x == 12:
        return x12
    x13 = combine(x11, x12)
    if x == 13:
        return x13
    x14 = combine(x9, x13)
    if x == 14:
        return x14
    x15 = underfill(x3, TWO, x14)
    if x == 15:
        return x15
    x16 = o_g(x15, R5)
    if x == 16:
        return x16
    x17 = rbind(corner, R3)
    if x == 17:
        return x17
    x18 = get_arg_rank_f(x16, x17, F0)
    if x == 18:
        return x18
    O = paint(x15, x18)
    return O

def solve_c1d99e64(S, I, x=0):
    x1 = frontiers(I)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    O = fill(I, TWO, x2)
    return O

def solve_e3497940(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = righthalf(I)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R2)
    if x == 3:
        return x3
    x4 = o_g(x3, R5)
    if x == 4:
        return x4
    x5 = merge_f(x4)
    if x == 5:
        return x5
    O = paint(x1, x5)
    return O

def solve_810b9b61(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = apply(toindices, x1)
    if x == 2:
        return x2
    x3 = fork(either, vline_i, hline_i)
    if x == 3:
        return x3
    x4 = sfilter_f(x2, x3)
    if x == 4:
        return x4
    x5 = difference(x2, x4)
    if x == 5:
        return x5
    x6 = fork(equality, identity, box)
    if x == 6:
        return x6
    x7 = mfilter_f(x5, x6)
    if x == 7:
        return x7
    O = fill(I, THREE, x7)
    return O

def solve_8a004b2b(S, I, x=0):
    x1 = f_ofcolor(I, FOUR)
    if x == 1:
        return x1
    x2 = subgrid(x1, I)
    if x == 2:
        return x2
    x3 = o_g(I, R3)
    if x == 3:
        return x3
    x4 = rbind(col_row, R0)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x3, x4, F0)
    if x == 5:
        return x5
    x6 = normalize_o(x5)
    if x == 6:
        return x6
    x7 = replace(x2, FOUR, ZERO)
    if x == 7:
        return x7
    x8 = o_g(x7, R5)
    if x == 8:
        return x8
    x9 = merge_f(x8)
    if x == 9:
        return x9
    x10 = width_f(x9)
    if x == 10:
        return x10
    x11 = width_f(x5)
    if x == 11:
        return x11
    x12 = divide(x10, x11)
    if x == 12:
        return x12
    x13 = upscale_f(x6, x12)
    if x == 13:
        return x13
    x14 = corner(x9, R0)
    if x == 14:
        return x14
    x15 = shift(x13, x14)
    if x == 15:
        return x15
    O = paint(x2, x15)
    return O

def solve_11852cab(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = mir_rot_f(x2, R0)
    if x == 3:
        return x3
    x4 = paint(I, x3)
    if x == 4:
        return x4
    x5 = mir_rot_f(x2, R2)
    if x == 5:
        return x5
    x6 = paint(x4, x5)
    if x == 6:
        return x6
    x7 = mir_rot_f(x2, R1)
    if x == 7:
        return x7
    x8 = paint(x6, x7)
    if x == 8:
        return x8
    x9 = mir_rot_f(x2, R3)
    if x == 9:
        return x9
    O = paint(x8, x9)
    return O

def solve_3345333e(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = cover(I, x2)
    if x == 3:
        return x3
    x4 = get_color_rank_t(x3, L1)
    if x == 4:
        return x4
    x5 = f_ofcolor(x3, x4)
    if x == 5:
        return x5
    x6 = mir_rot_f(x5, R2)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = neighbors(ORIGIN)
    if x == 8:
        return x8
    x9 = mapply(neighbors, x8)
    if x == 9:
        return x9
    x10 = apply(x7, x9)
    if x == 10:
        return x10
    x11 = rbind(intersection, x5)
    if x == 11:
        return x11
    x12 = compose(size, x11)
    if x == 12:
        return x12
    x13 = get_arg_rank_f(x10, x12, F0)
    if x == 13:
        return x13
    O = fill(x3, x4, x13)
    return O

def solve_0ca9ddb6(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = mapply(dneighbors, x1)
    if x == 2:
        return x2
    x3 = fill(I, SEVEN, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, TWO)
    if x == 4:
        return x4
    x5 = mapply(ineighbors, x4)
    if x == 5:
        return x5
    O = fill(x3, FOUR, x5)
    return O

def solve_99b1bc43(S, I, x=0):
    x1 = tophalf(I)
    if x == 1:
        return x1
    x2 = shape_t(x1)
    if x == 2:
        return x2
    x3 = canvas(ZERO, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(x1, ZERO)
    if x == 4:
        return x4
    x5 = bottomhalf(I)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, ZERO)
    if x == 6:
        return x6
    x7 = combine_f(x4, x6)
    if x == 7:
        return x7
    x8 = intersection(x4, x6)
    if x == 8:
        return x8
    x9 = difference(x7, x8)
    if x == 9:
        return x9
    O = fill(x3, THREE, x9)
    return O

def solve_363442ee(S, I, x=0):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = asobject(x1)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = compose(x3, decrement)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, ONE)
    if x == 5:
        return x5
    x6 = mapply(x4, x5)
    if x == 6:
        return x6
    O = paint(I, x6)
    return O

def solve_23581191(S, I, x=0):
    x1 = fork(combine, vfrontier, hfrontier)
    if x == 1:
        return x1
    x2 = compose(x1, center)
    if x == 2:
        return x2
    x3 = fork(recolor_i, color, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R7)
    if x == 4:
        return x4
    x5 = mapply(x3, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, F0)
    if x == 7:
        return x7
    x8 = rbind(get_nth_f, L1)
    if x == 8:
        return x8
    x9 = fork(intersection, x7, x8)
    if x == 9:
        return x9
    x10 = apply(x2, x4)
    if x == 10:
        return x10
    x11 = x9(x10)
    if x == 11:
        return x11
    O = fill(x6, TWO, x11)
    return O

def solve_623ea044(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = color(x2)
    if x == 3:
        return x3
    x4 = center(x2)
    if x == 4:
        return x4
    x5 = lbind(shoot, x4)
    if x == 5:
        return x5
    x6 = astuple(UNITY, NEG_UNITY)
    if x == 6:
        return x6
    x7 = astuple(UP_RIGHT, DOWN_LEFT)
    if x == 7:
        return x7
    x8 = combine(x6, x7)
    if x == 8:
        return x8
    x9 = mapply(x5, x8)
    if x == 9:
        return x9
    O = fill(I, x3, x9)
    return O

def solve_b782dc8a(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = colorfilter(x2, ZERO)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, x1)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = dneighbors(x5)
    if x == 6:
        return x6
    x7 = toobject(x6, I)
    if x == 7:
        return x7
    x8 = get_color_rank_f(x7, F0)
    if x == 8:
        return x8
    x9 = f_ofcolor(I, x8)
    if x == 9:
        return x9
    x10 = rbind(adjacent, x9)
    if x == 10:
        return x10
    x11 = mfilter_f(x3, x10)
    if x == 11:
        return x11
    x12 = toindices(x11)
    if x == 12:
        return x12
    x13 = rbind(manhattan, x4)
    if x == 13:
        return x13
    x14 = chain(even, x13, initset)
    if x == 14:
        return x14
    x15 = sfilter_f(x12, x14)
    if x == 15:
        return x15
    x16 = fill(I, x1, x15)
    if x == 16:
        return x16
    x17 = difference(x12, x15)
    if x == 17:
        return x17
    O = fill(x16, x8, x17)
    return O

def solve_fafffa47(S, I, x=0):
    x1 = bottomhalf(I)
    if x == 1:
        return x1
    x2 = shape_t(x1)
    if x == 2:
        return x2
    x3 = canvas(ZERO, x2)
    if x == 3:
        return x3
    x4 = tophalf(I)
    if x == 4:
        return x4
    x5 = f_ofcolor(x4, ZERO)
    if x == 5:
        return x5
    x6 = f_ofcolor(x1, ZERO)
    if x == 6:
        return x6
    x7 = intersection(x5, x6)
    if x == 7:
        return x7
    O = fill(x3, TWO, x7)
    return O

def solve_7b6016b9(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = rbind(bordering, I)
    if x == 2:
        return x2
    x3 = compose(flip, x2)
    if x == 3:
        return x3
    x4 = mfilter_f(x1, x3)
    if x == 4:
        return x4
    x5 = fill(I, TWO, x4)
    if x == 5:
        return x5
    O = replace(x5, ZERO, THREE)
    return O

def solve_09629e4f(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_arg_rank(x1, numcolors_f, L1)
    if x == 2:
        return x2
    x3 = normalize(x2)
    if x == 3:
        return x3
    x4 = upscale_f(x3, FOUR)
    if x == 4:
        return x4
    x5 = paint(I, x4)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, FIVE)
    if x == 6:
        return x6
    O = fill(x5, FIVE, x6)
    return O

def solve_5582e5ca(S, I, x=0):
    x1 = get_color_rank_t(I, F0)
    if x == 1:
        return x1
    O = canvas(x1, THREE_BY_THREE)
    return O

def solve_c59eb873(S, I, x=0):
    O = upscale_t(I, TWO)
    return O

def solve_e179c5f4(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = shoot(x2, UP_RIGHT)
    if x == 3:
        return x3
    x4 = fill(I, ONE, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(x4, ONE)
    if x == 5:
        return x5
    x6 = corner(x5, R1)
    if x == 6:
        return x6
    x7 = shoot(x6, NEG_UNITY)
    if x == 7:
        return x7
    x8 = fill(x4, ONE, x7)
    if x == 8:
        return x8
    x9 = f_ofcolor(x8, ONE)
    if x == 9:
        return x9
    x10 = corner(x9, R0)
    if x == 10:
        return x10
    x11 = subgrid(x9, x8)
    if x == 11:
        return x11
    x12 = height_t(x11)
    if x == 12:
        return x12
    x13 = decrement(x12)
    if x == 13:
        return x13
    x14 = width_t(x11)
    if x == 14:
        return x14
    x15 = astuple(x13, x14)
    if x == 15:
        return x15
    x16 = crop(x8, x10, x15)
    if x == 16:
        return x16
    x17 = repeat(x16, NINE)
    if x == 17:
        return x17
    x18 = merge(x17)
    if x == 18:
        return x18
    x19 = height_t(I)
    if x == 19:
        return x19
    x20 = astuple(x19, x14)
    if x == 20:
        return x20
    x21 = crop(x18, ORIGIN, x20)
    if x == 21:
        return x21
    x22 = mir_rot_t(x21, R0)
    if x == 22:
        return x22
    O = replace(x22, ZERO, EIGHT)
    return O

def solve_73251a56(S, I, x=0):
    x1 = rbind(get_rank, F0)
    if x == 1:
        return x1
    x2 = lbind(apply, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(I, R1)
    if x == 3:
        return x3
    x4 = papply(pair, I, x3)
    if x == 4:
        return x4
    x5 = apply(x2, x4)
    if x == 5:
        return x5
    x6 = get_color_rank_t(x5, F0)
    if x == 6:
        return x6
    x7 = replace(x5, ZERO, x6)
    if x == 7:
        return x7
    x8 = index(x7, ORIGIN)
    if x == 8:
        return x8
    x9 = shoot(ORIGIN, UNITY)
    if x == 9:
        return x9
    O = fill(x7, x8, x9)
    return O

def solve_6a1e5592(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = colorfilter(x1, FIVE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    x4 = cover(I, x3)
    if x == 4:
        return x4
    x5 = rbind(get_arg_rank, F0)
    if x == 5:
        return x5
    x6 = rbind(multiply, TEN)
    if x == 6:
        return x6
    x7 = width_t(I)
    if x == 7:
        return x7
    x8 = astuple(FIVE, x7)
    if x == 8:
        return x8
    x9 = crop(I, ORIGIN, x8)
    if x == 9:
        return x9
    x10 = asindices(x9)
    if x == 10:
        return x10
    x11 = rbind(intersection, x10)
    if x == 11:
        return x11
    x12 = chain(x6, size, x11)
    if x == 12:
        return x12
    x13 = f_ofcolor(x9, TWO)
    if x == 13:
        return x13
    x14 = rbind(intersection, x13)
    if x == 14:
        return x14
    x15 = chain(x6, size, x14)
    if x == 15:
        return x15
    x16 = compose(invert, x15)
    if x == 16:
        return x16
    x17 = fork(add, x12, x16)
    if x == 17:
        return x17
    x18 = f_ofcolor(x9, ZERO)
    if x == 18:
        return x18
    x19 = rbind(intersection, x18)
    if x == 19:
        return x19
    x20 = chain(size, x19, outbox)
    if x == 20:
        return x20
    x21 = fork(subtract, x17, x20)
    if x == 21:
        return x21
    x22 = rbind(multiply, FIVE)
    if x == 22:
        return x22
    x23 = rbind(col_row, R1)
    if x == 23:
        return x23
    x24 = compose(x22, x23)
    if x == 24:
        return x24
    x25 = fork(subtract, x21, x24)
    if x == 25:
        return x25
    x26 = chain(size, x19, delta)
    if x == 26:
        return x26
    x27 = fork(subtract, x25, x26)
    if x == 27:
        return x27
    x28 = rbind(x5, x27)
    if x == 28:
        return x28
    x29 = rbind(apply, x10)
    if x == 29:
        return x29
    x30 = lbind(lbind, shift)
    if x == 30:
        return x30
    x31 = chain(x28, x29, x30)
    if x == 31:
        return x31
    x32 = compose(toindices, normalize)
    if x == 32:
        return x32
    x33 = apply(x32, x2)
    if x == 33:
        return x33
    x34 = mapply(x31, x33)
    if x == 34:
        return x34
    O = fill(x4, ONE, x34)
    return O

def solve_6b9890af(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = subgrid(x1, I)
    if x == 2:
        return x2
    x3 = o_g(I, R7)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, L1)
    if x == 4:
        return x4
    x5 = width_t(x2)
    if x == 5:
        return x5
    x6 = divide(x5, THREE)
    if x == 6:
        return x6
    x7 = upscale_f(x4, x6)
    if x == 7:
        return x7
    x8 = normalize(x7)
    if x == 8:
        return x8
    x9 = shift(x8, UNITY)
    if x == 9:
        return x9
    O = paint(x2, x9)
    return O

def solve_f15e1fac(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = portrait_f(x1)
    if x == 2:
        return x2
    x3 = rbind(mir_rot_t, R1)
    if x == 3:
        return x3
    x4 = branch(x2, identity, x3)
    if x == 4:
        return x4
    x5 = col_row(x1, R2)
    if x == 5:
        return x5
    x6 = equality(x5, ZERO)
    if x == 6:
        return x6
    x7 = rbind(mir_rot_t, R2)
    if x == 7:
        return x7
    x8 = branch(x6, identity, x7)
    if x == 8:
        return x8
    x9 = x4(I)
    if x == 9:
        return x9
    x10 = x8(x9)
    if x == 10:
        return x10
    x11 = f_ofcolor(x10, EIGHT)
    if x == 11:
        return x11
    x12 = col_row(x11, R1)
    if x == 12:
        return x12
    x13 = equality(x12, ZERO)
    if x == 13:
        return x13
    x14 = rbind(mir_rot_t, R0)
    if x == 14:
        return x14
    x15 = branch(x13, identity, x14)
    if x == 15:
        return x15
    x16 = chain(x4, x8, x15)
    if x == 16:
        return x16
    x17 = x15(x10)
    if x == 17:
        return x17
    x18 = rbind(shoot, DOWN)
    if x == 18:
        return x18
    x19 = f_ofcolor(x17, EIGHT)
    if x == 19:
        return x19
    x20 = mapply(x18, x19)
    if x == 20:
        return x20
    x21 = lbind(sfilter, x20)
    if x == 21:
        return x21
    x22 = rbind(get_nth_f, F0)
    if x == 22:
        return x22
    x23 = rbind(get_nth_f, L1)
    if x == 23:
        return x23
    x24 = compose(x22, x23)
    if x == 24:
        return x24
    x25 = chain(decrement, x22, x22)
    if x == 25:
        return x25
    x26 = fork(greater, x24, x25)
    if x == 26:
        return x26
    x27 = chain(increment, x23, x22)
    if x == 27:
        return x27
    x28 = fork(greater, x27, x24)
    if x == 28:
        return x28
    x29 = fork(both, x26, x28)
    if x == 29:
        return x29
    x30 = lbind(compose, x29)
    if x == 30:
        return x30
    x31 = lbind(lbind, astuple)
    if x == 31:
        return x31
    x32 = chain(x21, x30, x31)
    if x == 32:
        return x32
    x33 = f_ofcolor(x17, TWO)
    if x == 33:
        return x33
    x34 = apply(x22, x33)
    if x == 34:
        return x34
    x35 = insert(ZERO, x34)
    if x == 35:
        return x35
    x36 = order(x35, identity)
    if x == 36:
        return x36
    x37 = height_t(x17)
    if x == 37:
        return x37
    x38 = insert(x37, x34)
    if x == 38:
        return x38
    x39 = apply(decrement, x38)
    if x == 39:
        return x39
    x40 = order(x39, identity)
    if x == 40:
        return x40
    x41 = pair(x36, x40)
    if x == 41:
        return x41
    x42 = apply(x32, x41)
    if x == 42:
        return x42
    x43 = size_f(x33)
    if x == 43:
        return x43
    x44 = increment(x43)
    if x == 44:
        return x44
    x45 = interval(ZERO, x44, ONE)
    if x == 45:
        return x45
    x46 = apply(tojvec, x45)
    if x == 46:
        return x46
    x47 = papply(shift, x42, x46)
    if x == 47:
        return x47
    x48 = merge(x47)
    if x == 48:
        return x48
    x49 = fill(x17, EIGHT, x48)
    if x == 49:
        return x49
    O = x16(x49)
    return O

def solve_83302e8f(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = sfilter_f(x2, square_f)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    x5 = recolor_o(THREE, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = difference(x2, x3)
    if x == 7:
        return x7
    x8 = merge_f(x7)
    if x == 8:
        return x8
    x9 = recolor_o(FOUR, x8)
    if x == 9:
        return x9
    O = paint(x6, x9)
    return O

def solve_662c240a(S, I, x=0):
    x1 = vsplit(I, THREE)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_t, R1)
    if x == 2:
        return x2
    x3 = fork(equality, x2, identity)
    if x == 3:
        return x3
    x4 = compose(flip, x3)
    if x == 4:
        return x4
    O = extract(x1, x4)
    return O

def solve_99fa7670(S, I, x=0):
    x1 = rbind(shoot, RIGHT)
    if x == 1:
        return x1
    x2 = compose(x1, center)
    if x == 2:
        return x2
    x3 = fork(recolor_i, color, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R5)
    if x == 4:
        return x4
    x5 = mapply(x3, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, F0)
    if x == 7:
        return x7
    x8 = compose(color, x7)
    if x == 8:
        return x8
    x9 = rbind(corner, R3)
    if x == 9:
        return x9
    x10 = compose(x9, x7)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, L1)
    if x == 11:
        return x11
    x12 = compose(x9, x11)
    if x == 12:
        return x12
    x13 = fork(connect, x10, x12)
    if x == 13:
        return x13
    x14 = fork(recolor_i, x8, x13)
    if x == 14:
        return x14
    x15 = shape_t(I)
    if x == 15:
        return x15
    x16 = add(x15, DOWN_LEFT)
    if x == 16:
        return x16
    x17 = initset(x16)
    if x == 17:
        return x17
    x18 = recolor_i(ZERO, x17)
    if x == 18:
        return x18
    x19 = o_g(x6, R5)
    if x == 19:
        return x19
    x20 = insert(x18, x19)
    if x == 20:
        return x20
    x21 = rbind(col_row, R1)
    if x == 21:
        return x21
    x22 = order(x20, x21)
    if x == 22:
        return x22
    x23 = remove_f(x18, x22)
    if x == 23:
        return x23
    x24 = get_nth_t(x22, F0)
    if x == 24:
        return x24
    x25 = remove_f(x24, x22)
    if x == 25:
        return x25
    x26 = pair(x23, x25)
    if x == 26:
        return x26
    x27 = mapply(x14, x26)
    if x == 27:
        return x27
    O = underpaint(x6, x27)
    return O

def solve_6455b5f5(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = recolor_o(ONE, x2)
    if x == 3:
        return x3
    x4 = paint(I, x3)
    if x == 4:
        return x4
    x5 = colorfilter(x1, ZERO)
    if x == 5:
        return x5
    x6 = get_val_rank_f(x1, size, L1)
    if x == 6:
        return x6
    x7 = sizefilter(x5, x6)
    if x == 7:
        return x7
    x8 = merge_f(x7)
    if x == 8:
        return x8
    O = fill(x4, EIGHT, x8)
    return O

def solve_a1570a43(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = recolor_i(TWO, x1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, THREE)
    if x == 3:
        return x3
    x4 = corner(x3, R0)
    if x == 4:
        return x4
    x5 = corner(x1, R0)
    if x == 5:
        return x5
    x6 = subtract(x4, x5)
    if x == 6:
        return x6
    x7 = increment(x6)
    if x == 7:
        return x7
    O = move(I, x2, x7)
    return O

def solve_b527c5c6(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = matcher(x1, TWO)
    if x == 2:
        return x2
    x3 = rbind(sfilter, x2)
    if x == 3:
        return x3
    x4 = compose(center, x3)
    if x == 4:
        return x4
    x5 = rbind(col_row, R1)
    if x == 5:
        return x5
    x6 = compose(x5, x3)
    if x == 6:
        return x6
    x7 = fork(equality, x6, x5)
    if x == 7:
        return x7
    x8 = compose(invert, x7)
    if x == 8:
        return x8
    x9 = rbind(col_row, R0)
    if x == 9:
        return x9
    x10 = compose(x9, x3)
    if x == 10:
        return x10
    x11 = fork(equality, x10, x9)
    if x == 11:
        return x11
    x12 = fork(add, x8, x11)
    if x == 12:
        return x12
    x13 = rbind(col_row, R2)
    if x == 13:
        return x13
    x14 = compose(x13, x3)
    if x == 14:
        return x14
    x15 = fork(equality, x14, x13)
    if x == 15:
        return x15
    x16 = compose(invert, x15)
    if x == 16:
        return x16
    x17 = rbind(col_row, R3)
    if x == 17:
        return x17
    x18 = compose(x17, x3)
    if x == 18:
        return x18
    x19 = fork(equality, x18, x17)
    if x == 19:
        return x19
    x20 = fork(add, x16, x19)
    if x == 20:
        return x20
    x21 = fork(astuple, x12, x20)
    if x == 21:
        return x21
    x22 = fork(shoot, x4, x21)
    if x == 22:
        return x22
    x23 = o_g(I, R1)
    if x == 23:
        return x23
    x24 = mapply(x22, x23)
    if x == 24:
        return x24
    x25 = fill(I, TWO, x24)
    if x == 25:
        return x25
    x26 = lbind(lbind, shift)
    if x == 26:
        return x26
    x27 = compose(x26, x22)
    if x == 27:
        return x27
    x28 = lbind(apply, toivec)
    if x == 28:
        return x28
    x29 = rbind(interval, ONE)
    if x == 29:
        return x29
    x30 = rbind(get_rank, L1)
    if x == 30:
        return x30
    x31 = chain(decrement, x30, shape_f)
    if x == 31:
        return x31
    x32 = compose(invert, x31)
    if x == 32:
        return x32
    x33 = compose(increment, x31)
    if x == 33:
        return x33
    x34 = fork(x29, x32, x33)
    if x == 34:
        return x34
    x35 = compose(x28, x34)
    if x == 35:
        return x35
    x36 = fork(mapply, x27, x35)
    if x == 36:
        return x36
    x37 = compose(vline_i, x22)
    if x == 37:
        return x37
    x38 = sfilter_f(x23, x37)
    if x == 38:
        return x38
    x39 = difference(x23, x38)
    if x == 39:
        return x39
    x40 = mapply(x36, x39)
    if x == 40:
        return x40
    x41 = lbind(apply, tojvec)
    if x == 41:
        return x41
    x42 = compose(x41, x34)
    if x == 42:
        return x42
    x43 = fork(mapply, x27, x42)
    if x == 43:
        return x43
    x44 = mapply(x43, x38)
    if x == 44:
        return x44
    x45 = combine_f(x40, x44)
    if x == 45:
        return x45
    O = underfill(x25, THREE, x45)
    return O

def solve_b8cdaf2b(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = shift(x2, UP)
    if x == 3:
        return x3
    x4 = corner(x3, R0)
    if x == 4:
        return x4
    x5 = shoot(x4, NEG_UNITY)
    if x == 5:
        return x5
    x6 = corner(x3, R1)
    if x == 6:
        return x6
    x7 = shoot(x6, UP_RIGHT)
    if x == 7:
        return x7
    x8 = combine(x5, x7)
    if x == 8:
        return x8
    O = underfill(I, x1, x8)
    return O

def solve_f8b3ba0a(S, I, x=0):
    x1 = rbind(canvas, UNITY)
    if x == 1:
        return x1
    x2 = compress(I)
    if x == 2:
        return x2
    x3 = palette_t(x2)
    if x == 3:
        return x3
    x4 = lbind(colorcount_t, x2)
    if x == 4:
        return x4
    x5 = compose(invert, x4)
    if x == 5:
        return x5
    x6 = order(x3, x5)
    if x == 6:
        return x6
    x7 = apply(x1, x6)
    if x == 7:
        return x7
    x8 = merge_t(x7)
    if x == 8:
        return x8
    x9 = astuple(THREE, ONE)
    if x == 9:
        return x9
    O = crop(x8, DOWN, x9)
    return O

def solve_48d8fb45(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = matcher(size, ONE)
    if x == 2:
        return x2
    x3 = extract(x1, x2)
    if x == 3:
        return x3
    x4 = lbind(adjacent, x3)
    if x == 4:
        return x4
    x5 = extract(x1, x4)
    if x == 5:
        return x5
    O = subgrid(x5, I)
    return O

def solve_a5f85a15(S, I, x=0):
    x1 = interval(ONE, NINE, ONE)
    if x == 1:
        return x1
    x2 = apply(double, x1)
    if x == 2:
        return x2
    x3 = apply(decrement, x2)
    if x == 3:
        return x3
    x4 = papply(astuple, x3, x3)
    if x == 4:
        return x4
    x5 = lbind(shift, x4)
    if x == 5:
        return x5
    x6 = rbind(corner, R0)
    if x == 6:
        return x6
    x7 = o_g(I, R7)
    if x == 7:
        return x7
    x8 = apply(x6, x7)
    if x == 8:
        return x8
    x9 = mapply(x5, x8)
    if x == 9:
        return x9
    O = fill(I, FOUR, x9)
    return O

def solve_6430c8c4(S, I, x=0):
    x1 = astuple(FOUR, FOUR)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = tophalf(I)
    if x == 3:
        return x3
    x4 = f_ofcolor(x3, ZERO)
    if x == 4:
        return x4
    x5 = bottomhalf(I)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, ZERO)
    if x == 6:
        return x6
    x7 = intersection(x4, x6)
    if x == 7:
        return x7
    O = fill(x2, THREE, x7)
    return O

def solve_e50d258f(S, I, x=0):
    x1 = width_t(I)
    if x == 1:
        return x1
    x2 = astuple(NINE, x1)
    if x == 2:
        return x2
    x3 = canvas(ZERO, x2)
    if x == 3:
        return x3
    x4 = vconcat(I, x3)
    if x == 4:
        return x4
    x5 = o_g(x4, R1)
    if x == 5:
        return x5
    x6 = rbind(colorcount_f, TWO)
    if x == 6:
        return x6
    x7 = get_arg_rank_f(x5, x6, F0)
    if x == 7:
        return x7
    O = subgrid(x7, I)
    return O

def solve_9dfd6313(S, I, x=0):
    O = mir_rot_t(I, R1)
    return O

def solve_bdad9b1f(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = center(x1)
    if x == 2:
        return x2
    x3 = hfrontier(x2)
    if x == 3:
        return x3
    x4 = fill(I, TWO, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, EIGHT)
    if x == 5:
        return x5
    x6 = center(x5)
    if x == 6:
        return x6
    x7 = vfrontier(x6)
    if x == 7:
        return x7
    x8 = fill(x4, EIGHT, x7)
    if x == 8:
        return x8
    x9 = intersection(x3, x7)
    if x == 9:
        return x9
    O = fill(x8, FOUR, x9)
    return O

def solve_ce22a75a(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = apply(outbox, x1)
    if x == 2:
        return x2
    x3 = mapply(backdrop, x2)
    if x == 3:
        return x3
    O = fill(I, ONE, x3)
    return O

def solve_9edfc990(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, ONE)
    if x == 3:
        return x3
    x4 = rbind(adjacent, x3)
    if x == 4:
        return x4
    x5 = mfilter_f(x2, x4)
    if x == 5:
        return x5
    x6 = recolor_o(ONE, x5)
    if x == 6:
        return x6
    O = paint(I, x6)
    return O

def solve_9af7a82c(S, I, x=0):
    x1 = rbind(mir_rot_t, R3)
    if x == 1:
        return x1
    x2 = rbind(astuple, ONE)
    if x == 2:
        return x2
    x3 = compose(x2, size)
    if x == 3:
        return x3
    x4 = fork(canvas, color, x3)
    if x == 4:
        return x4
    x5 = lbind(canvas, ZERO)
    if x == 5:
        return x5
    x6 = o_g(I, R4)
    if x == 6:
        return x6
    x7 = get_val_rank_f(x6, size, F0)
    if x == 7:
        return x7
    x8 = lbind(subtract, x7)
    if x == 8:
        return x8
    x9 = chain(x2, x8, size)
    if x == 9:
        return x9
    x10 = compose(x5, x9)
    if x == 10:
        return x10
    x11 = fork(vconcat, x4, x10)
    if x == 11:
        return x11
    x12 = compose(x1, x11)
    if x == 12:
        return x12
    x13 = order(x6, size)
    if x == 13:
        return x13
    x14 = apply(x12, x13)
    if x == 14:
        return x14
    x15 = merge_t(x14)
    if x == 15:
        return x15
    O = mir_rot_t(x15, R3)
    return O

def solve_1f0c79e5(S, I, x=0):
    x1 = replace(I, TWO, ZERO)
    if x == 1:
        return x1
    x2 = get_color_rank_t(x1, L1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, TWO)
    if x == 3:
        return x3
    x4 = f_ofcolor(x1, x2)
    if x == 4:
        return x4
    x5 = combine_f(x3, x4)
    if x == 5:
        return x5
    x6 = recolor_i(x2, x5)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = compose(decrement, double)
    if x == 8:
        return x8
    x9 = corner(x5, R0)
    if x == 9:
        return x9
    x10 = invert(x9)
    if x == 10:
        return x10
    x11 = shift(x3, x10)
    if x == 11:
        return x11
    x12 = apply(x8, x11)
    if x == 12:
        return x12
    x13 = interval(ZERO, NINE, ONE)
    if x == 13:
        return x13
    x14 = prapply(multiply, x12, x13)
    if x == 14:
        return x14
    x15 = mapply(x7, x14)
    if x == 15:
        return x15
    O = paint(I, x15)
    return O

def solve_a68b268e(S, I, x=0):
    x1 = bottomhalf(I)
    if x == 1:
        return x1
    x2 = righthalf(x1)
    if x == 2:
        return x2
    x3 = lefthalf(x1)
    if x == 3:
        return x3
    x4 = f_ofcolor(x3, EIGHT)
    if x == 4:
        return x4
    x5 = fill(x2, EIGHT, x4)
    if x == 5:
        return x5
    x6 = tophalf(I)
    if x == 6:
        return x6
    x7 = righthalf(x6)
    if x == 7:
        return x7
    x8 = f_ofcolor(x7, FOUR)
    if x == 8:
        return x8
    x9 = fill(x5, FOUR, x8)
    if x == 9:
        return x9
    x10 = lefthalf(x6)
    if x == 10:
        return x10
    x11 = f_ofcolor(x10, SEVEN)
    if x == 11:
        return x11
    O = fill(x9, SEVEN, x11)
    return O

def solve_496994bd(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = halve(x1)
    if x == 2:
        return x2
    x3 = width_t(I)
    if x == 3:
        return x3
    x4 = astuple(x2, x3)
    if x == 4:
        return x4
    x5 = crop(I, ORIGIN, x4)
    if x == 5:
        return x5
    x6 = mir_rot_t(x5, R0)
    if x == 6:
        return x6
    O = vconcat(x5, x6)
    return O

def solve_b8825c91(S, I, x=0):
    x1 = rbind(get_rank, F0)
    if x == 1:
        return x1
    x2 = lbind(apply, x1)
    if x == 2:
        return x2
    x3 = replace(I, FOUR, ZERO)
    if x == 3:
        return x3
    x4 = mir_rot_t(x3, R1)
    if x == 4:
        return x4
    x5 = papply(pair, x3, x4)
    if x == 5:
        return x5
    x6 = apply(x2, x5)
    if x == 6:
        return x6
    x7 = mir_rot_t(x6, R3)
    if x == 7:
        return x7
    x8 = papply(pair, x6, x7)
    if x == 8:
        return x8
    x9 = apply(x2, x8)
    if x == 9:
        return x9
    O = mir_rot_t(x9, R3)
    return O

def solve_d037b0a7(S, I, x=0):
    x1 = rbind(shoot, DOWN)
    if x == 1:
        return x1
    x2 = compose(x1, center)
    if x == 2:
        return x2
    x3 = fork(recolor_i, color, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R5)
    if x == 4:
        return x4
    x5 = mapply(x3, x4)
    if x == 5:
        return x5
    O = paint(I, x5)
    return O

def solve_a5313dff(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = rbind(bordering, I)
    if x == 3:
        return x3
    x4 = compose(flip, x3)
    if x == 4:
        return x4
    x5 = mfilter_f(x2, x4)
    if x == 5:
        return x5
    O = fill(I, ONE, x5)
    return O

def solve_e76a88a6(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, numcolors_f, F0)
    if x == 2:
        return x2
    x3 = normalize(x2)
    if x == 3:
        return x3
    x4 = lbind(shift, x3)
    if x == 4:
        return x4
    x5 = rbind(corner, R0)
    if x == 5:
        return x5
    x6 = remove_f(x2, x1)
    if x == 6:
        return x6
    x7 = apply(x5, x6)
    if x == 7:
        return x7
    x8 = mapply(x4, x7)
    if x == 8:
        return x8
    O = paint(I, x8)
    return O

def solve_539a4f51(S, I, x=0):
    x1 = index(I, ORIGIN)
    if x == 1:
        return x1
    x2 = multiply(UNITY, TEN)
    if x == 2:
        return x2
    x3 = canvas(x1, x2)
    if x == 3:
        return x3
    x4 = colorcount_t(I, ZERO)
    if x == 4:
        return x4
    x5 = positive(x4)
    if x == 5:
        return x5
    x6 = shape_t(I)
    if x == 6:
        return x6
    x7 = decrement(x6)
    if x == 7:
        return x7
    x8 = branch(x5, x7, x6)
    if x == 8:
        return x8
    x9 = crop(I, ORIGIN, x8)
    if x == 9:
        return x9
    x10 = width_t(x9)
    if x == 10:
        return x10
    x11 = astuple(ONE, x10)
    if x == 11:
        return x11
    x12 = crop(x9, ORIGIN, x11)
    if x == 12:
        return x12
    x13 = vupscale(x12, x10)
    if x == 13:
        return x13
    x14 = hconcat(x9, x13)
    if x == 14:
        return x14
    x15 = mir_rot_t(x13, R1)
    if x == 15:
        return x15
    x16 = hconcat(x15, x9)
    if x == 16:
        return x16
    x17 = vconcat(x14, x16)
    if x == 17:
        return x17
    x18 = asobject(x17)
    if x == 18:
        return x18
    O = paint(x3, x18)
    return O

def solve_c8f0f002(S, I, x=0):
    O = replace(I, SEVEN, FIVE)
    return O

def solve_9ecd008a(S, I, x=0):
    x1 = f_ofcolor(I, ZERO)
    if x == 1:
        return x1
    x2 = mir_rot_t(I, R2)
    if x == 2:
        return x2
    O = subgrid(x1, x2)
    return O

def solve_928ad970(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = subgrid(x1, I)
    if x == 2:
        return x2
    x3 = trim(x2)
    if x == 3:
        return x3
    x4 = get_color_rank_t(x3, L1)
    if x == 4:
        return x4
    x5 = inbox(x1)
    if x == 5:
        return x5
    O = fill(I, x4, x5)
    return O

def solve_bc1d5164(S, I, x=0):
    x1 = canvas(ZERO, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = get_color_rank_t(I, L1)
    if x == 2:
        return x2
    x3 = rbind(f_ofcolor, x2)
    if x == 3:
        return x3
    x4 = crop(I, ORIGIN, THREE_BY_THREE)
    if x == 4:
        return x4
    x5 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    if x == 5:
        return x5
    x6 = astuple(x4, x5)
    if x == 6:
        return x6
    x7 = tojvec(FOUR)
    if x == 7:
        return x7
    x8 = crop(I, x7, THREE_BY_THREE)
    if x == 8:
        return x8
    x9 = astuple(TWO, FOUR)
    if x == 9:
        return x9
    x10 = crop(I, x9, THREE_BY_THREE)
    if x == 10:
        return x10
    x11 = astuple(x8, x10)
    if x == 11:
        return x11
    x12 = combine_t(x6, x11)
    if x == 12:
        return x12
    x13 = mapply(x3, x12)
    if x == 13:
        return x13
    O = fill(x1, x2, x13)
    return O

def solve_a740d043(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    O = replace(x3, ONE, ZERO)
    return O

def solve_6d75e8bb(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = replace(x3, ZERO, TWO)
    if x == 4:
        return x4
    x5 = asobject(x4)
    if x == 5:
        return x5
    x6 = corner(x2, R0)
    if x == 6:
        return x6
    x7 = shift(x5, x6)
    if x == 7:
        return x7
    O = paint(I, x7)
    return O

def solve_e21d9049(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = merge(x1)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = shape_f(x2)
    if x == 4:
        return x4
    x5 = lbind(multiply, x4)
    if x == 5:
        return x5
    x6 = lbind(mapply, neighbors)
    if x == 6:
        return x6
    x7 = power(x6, TWO)
    if x == 7:
        return x7
    x8 = neighbors(ORIGIN)
    if x == 8:
        return x8
    x9 = x7(x8)
    if x == 9:
        return x9
    x10 = apply(x5, x9)
    if x == 10:
        return x10
    x11 = mapply(x3, x10)
    if x == 11:
        return x11
    x12 = paint(I, x11)
    if x == 12:
        return x12
    x13 = asindices(I)
    if x == 13:
        return x13
    x14 = get_color_rank_t(I, L1)
    if x == 14:
        return x14
    x15 = f_ofcolor(I, x14)
    if x == 15:
        return x15
    x16 = lbind(hmatching, x15)
    if x == 16:
        return x16
    x17 = lbind(vmatching, x15)
    if x == 17:
        return x17
    x18 = fork(either, x16, x17)
    if x == 18:
        return x18
    x19 = compose(x18, initset)
    if x == 19:
        return x19
    x20 = sfilter_f(x13, x19)
    if x == 20:
        return x20
    x21 = difference(x13, x20)
    if x == 21:
        return x21
    O = cover(x12, x21)
    return O

def solve_fcb5c309(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_color_rank_t(I, L1)
    if x == 2:
        return x2
    x3 = colorfilter(x1, x2)
    if x == 3:
        return x3
    x4 = difference(x1, x3)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x4, size, F0)
    if x == 5:
        return x5
    x6 = subgrid(x5, I)
    if x == 6:
        return x6
    x7 = color(x5)
    if x == 7:
        return x7
    O = replace(x6, x7, x2)
    return O

def solve_eb281b96(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    x3 = width_t(I)
    if x == 3:
        return x3
    x4 = astuple(x2, x3)
    if x == 4:
        return x4
    x5 = crop(I, ORIGIN, x4)
    if x == 5:
        return x5
    x6 = mir_rot_t(x5, R0)
    if x == 6:
        return x6
    x7 = vconcat(I, x6)
    if x == 7:
        return x7
    x8 = double(x2)
    if x == 8:
        return x8
    x9 = astuple(x8, x3)
    if x == 9:
        return x9
    x10 = crop(x7, DOWN, x9)
    if x == 10:
        return x10
    O = vconcat(x7, x10)
    return O

def solve_b6afb2da(S, I, x=0):
    x1 = replace(I, FIVE, TWO)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = colorfilter(x2, FIVE)
    if x == 3:
        return x3
    x4 = mapply(box, x3)
    if x == 4:
        return x4
    x5 = fill(x1, FOUR, x4)
    if x == 5:
        return x5
    x6 = mapply(corners, x3)
    if x == 6:
        return x6
    O = fill(x5, ONE, x6)
    return O

def solve_74dd1130(S, I, x=0):
    O = mir_rot_t(I, R1)
    return O

def solve_a61ba2ce(S, I, x=0):
    x1 = rbind(subgrid, I)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = lbind(extract, x2)
    if x == 3:
        return x3
    x4 = lbind(index, I)
    if x == 4:
        return x4
    x5 = matcher(x4, ZERO)
    if x == 5:
        return x5
    x6 = lbind(compose, x5)
    if x == 6:
        return x6
    x7 = chain(x1, x3, x6)
    if x == 7:
        return x7
    x8 = rbind(corner, R3)
    if x == 8:
        return x8
    x9 = x7(x8)
    if x == 9:
        return x9
    x10 = rbind(corner, R2)
    if x == 10:
        return x10
    x11 = x7(x10)
    if x == 11:
        return x11
    x12 = hconcat(x9, x11)
    if x == 12:
        return x12
    x13 = rbind(corner, R1)
    if x == 13:
        return x13
    x14 = x7(x13)
    if x == 14:
        return x14
    x15 = rbind(corner, R0)
    if x == 15:
        return x15
    x16 = x7(x15)
    if x == 16:
        return x16
    x17 = hconcat(x14, x16)
    if x == 17:
        return x17
    O = vconcat(x12, x17)
    return O

def solve_ecdecbb3(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = compose(center, x1)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, L1)
    if x == 3:
        return x3
    x4 = fork(gravitate, x1, x3)
    if x == 4:
        return x4
    x5 = compose(crement, x4)
    if x == 5:
        return x5
    x6 = fork(add, x2, x5)
    if x == 6:
        return x6
    x7 = fork(connect, x2, x6)
    if x == 7:
        return x7
    x8 = o_g(I, R5)
    if x == 8:
        return x8
    x9 = colorfilter(x8, TWO)
    if x == 9:
        return x9
    x10 = colorfilter(x8, EIGHT)
    if x == 10:
        return x10
    x11 = product(x9, x10)
    if x == 11:
        return x11
    x12 = apply(x7, x11)
    if x == 12:
        return x12
    x13 = lbind(greater, EIGHT)
    if x == 13:
        return x13
    x14 = compose(x13, size)
    if x == 14:
        return x14
    x15 = mfilter_f(x12, x14)
    if x == 15:
        return x15
    x16 = fill(I, TWO, x15)
    if x == 16:
        return x16
    x17 = apply(x6, x11)
    if x == 17:
        return x17
    x18 = intersection(x15, x17)
    if x == 18:
        return x18
    x19 = mapply(neighbors, x18)
    if x == 19:
        return x19
    O = fill(x16, EIGHT, x19)
    return O

def solve_f5b8619d(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = mapply(vfrontier, x2)
    if x == 3:
        return x3
    x4 = underfill(I, EIGHT, x3)
    if x == 4:
        return x4
    x5 = hconcat(x4, x4)
    if x == 5:
        return x5
    O = vconcat(x5, x5)
    return O

def solve_a64e4611(S, I, x=0):
    x1 = asindices(I)
    if x == 1:
        return x1
    x2 = rbind(colorcount_f, THREE)
    if x == 2:
        return x2
    x3 = lbind(lbind, shift)
    if x == 3:
        return x3
    x4 = lbind(canvas, ZERO)
    if x == 4:
        return x4
    x5 = compose(asobject, x4)
    if x == 5:
        return x5
    x6 = rbind(get_arg_rank, F0)
    if x == 6:
        return x6
    x7 = fork(product, identity, identity)
    if x == 7:
        return x7
    x8 = rbind(get_nth_f, F0)
    if x == 8:
        return x8
    x9 = compose(x7, x8)
    if x == 9:
        return x9
    x10 = rbind(get_nth_f, L1)
    if x == 10:
        return x10
    x11 = fork(multiply, x8, x10)
    if x == 11:
        return x11
    x12 = rbind(fork, x11)
    if x == 12:
        return x12
    x13 = lbind(x12, multiply)
    if x == 13:
        return x13
    x14 = compose(positive, size)
    if x == 14:
        return x14
    x15 = lbind(chain, x14)
    if x == 15:
        return x15
    x16 = rbind(x15, x5)
    if x == 16:
        return x16
    x17 = lbind(lbind, occurrences)
    if x == 17:
        return x17
    x18 = chain(x13, x16, x17)
    if x == 18:
        return x18
    x19 = compose(x18, x10)
    if x == 19:
        return x19
    x20 = fork(x6, x9, x19)
    if x == 20:
        return x20
    x21 = chain(x3, x5, x20)
    if x == 21:
        return x21
    x22 = compose(x5, x20)
    if x == 22:
        return x22
    x23 = fork(occurrences, x10, x22)
    if x == 23:
        return x23
    x24 = fork(mapply, x21, x23)
    if x == 24:
        return x24
    x25 = multiply(TWO, SIX)
    if x == 25:
        return x25
    x26 = interval(THREE, x25, ONE)
    if x == 26:
        return x26
    x27 = astuple(x26, I)
    if x == 27:
        return x27
    x28 = x24(x27)
    if x == 28:
        return x28
    x29 = fill(I, THREE, x28)
    if x == 29:
        return x29
    x30 = interval(THREE, TEN, ONE)
    if x == 30:
        return x30
    x31 = astuple(x30, x29)
    if x == 31:
        return x31
    x32 = x24(x31)
    if x == 32:
        return x32
    x33 = fill(x29, THREE, x32)
    if x == 33:
        return x33
    x34 = astuple(x30, x33)
    if x == 34:
        return x34
    x35 = x24(x34)
    if x == 35:
        return x35
    x36 = fill(x33, THREE, x35)
    if x == 36:
        return x36
    x37 = rbind(toobject, x36)
    if x == 37:
        return x37
    x38 = chain(x2, x37, neighbors)
    if x == 38:
        return x38
    x39 = matcher(x38, EIGHT)
    if x == 39:
        return x39
    x40 = sfilter(x1, x39)
    if x == 40:
        return x40
    x41 = fill(I, THREE, x40)
    if x == 41:
        return x41
    x42 = f_ofcolor(x41, ZERO)
    if x == 42:
        return x42
    x43 = lbind(contained, THREE)
    if x == 43:
        return x43
    x44 = rbind(toobject, x41)
    if x == 44:
        return x44
    x45 = chain(x43, palette_f, x44)
    if x == 45:
        return x45
    x46 = compose(x45, dneighbors)
    if x == 46:
        return x46
    x47 = rbind(bordering, x41)
    if x == 47:
        return x47
    x48 = compose(x47, initset)
    if x == 48:
        return x48
    x49 = fork(both, x46, x48)
    if x == 49:
        return x49
    x50 = sfilter(x42, x49)
    if x == 50:
        return x50
    O = fill(x41, THREE, x50)
    return O

def solve_d10ecb37(S, I, x=0):
    O = crop(I, ORIGIN, TWO_BY_TWO)
    return O

def solve_dc1df850(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = colorfilter(x1, TWO)
    if x == 2:
        return x2
    x3 = mapply(outbox, x2)
    if x == 3:
        return x3
    O = fill(I, ONE, x3)
    return O

def solve_6c434453(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, EIGHT)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    x4 = cover(I, x3)
    if x == 4:
        return x4
    x5 = dneighbors(UNITY)
    if x == 5:
        return x5
    x6 = insert(UNITY, x5)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = rbind(corner, R0)
    if x == 8:
        return x8
    x9 = apply(x8, x2)
    if x == 9:
        return x9
    x10 = mapply(x7, x9)
    if x == 10:
        return x10
    O = fill(x4, TWO, x10)
    return O

def solve_ff805c23(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = mir_rot_t(I, R0)
    if x == 2:
        return x2
    x3 = subgrid(x1, x2)
    if x == 3:
        return x3
    x4 = palette_t(x3)
    if x == 4:
        return x4
    x5 = contained(ONE, x4)
    if x == 5:
        return x5
    x6 = mir_rot_t(I, R2)
    if x == 6:
        return x6
    x7 = subgrid(x1, x6)
    if x == 7:
        return x7
    O = branch(x5, x7, x3)
    return O

def solve_d07ae81c(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = get_nth_f(x2, F0)
    if x == 3:
        return x3
    x4 = center(x3)
    if x == 4:
        return x4
    x5 = neighbors(x4)
    if x == 5:
        return x5
    x6 = toobject(x5, I)
    if x == 6:
        return x6
    x7 = get_color_rank_f(x6, F0)
    if x == 7:
        return x7
    x8 = difference(x1, x2)
    if x == 8:
        return x8
    x9 = apply(color, x8)
    if x == 9:
        return x9
    x10 = get_nth_f(x9, F0)
    if x == 10:
        return x10
    x11 = equality(x7, x10)
    if x == 11:
        return x11
    x12 = color(x3)
    if x == 12:
        return x12
    x13 = apply(color, x2)
    if x == 13:
        return x13
    x14 = other_f(x13, x12)
    if x == 14:
        return x14
    x15 = branch(x11, x12, x14)
    if x == 15:
        return x15
    x16 = f_ofcolor(I, x10)
    if x == 16:
        return x16
    x17 = rbind(shoot, UNITY)
    if x == 17:
        return x17
    x18 = rbind(shoot, NEG_UNITY)
    if x == 18:
        return x18
    x19 = fork(combine, x17, x18)
    if x == 19:
        return x19
    x20 = rbind(shoot, DOWN_LEFT)
    if x == 20:
        return x20
    x21 = rbind(shoot, UP_RIGHT)
    if x == 21:
        return x21
    x22 = fork(combine, x20, x21)
    if x == 22:
        return x22
    x23 = fork(combine, x19, x22)
    if x == 23:
        return x23
    x24 = compose(x23, center)
    if x == 24:
        return x24
    x25 = mapply(x24, x2)
    if x == 25:
        return x25
    x26 = intersection(x16, x25)
    if x == 26:
        return x26
    x27 = fill(I, x15, x26)
    if x == 27:
        return x27
    x28 = branch(x11, x14, x12)
    if x == 28:
        return x28
    x29 = get_nth_f(x9, L1)
    if x == 29:
        return x29
    x30 = f_ofcolor(I, x29)
    if x == 30:
        return x30
    x31 = intersection(x30, x25)
    if x == 31:
        return x31
    O = fill(x27, x28, x31)
    return O

def solve_f35d900a(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = remove(ZERO, x1)
    if x == 2:
        return x2
    x3 = lbind(other, x2)
    if x == 3:
        return x3
    x4 = compose(x3, color)
    if x == 4:
        return x4
    x5 = fork(recolor_i, x4, outbox)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = mapply(x5, x6)
    if x == 7:
        return x7
    x8 = paint(I, x7)
    if x == 8:
        return x8
    x9 = mapply(toindices, x6)
    if x == 9:
        return x9
    x10 = box(x9)
    if x == 10:
        return x10
    x11 = difference(x10, x9)
    if x == 11:
        return x11
    x12 = rbind(get_arg_rank, L1)
    if x == 12:
        return x12
    x13 = lbind(x12, x9)
    if x == 13:
        return x13
    x14 = rbind(compose, initset)
    if x == 14:
        return x14
    x15 = lbind(rbind, manhattan)
    if x == 15:
        return x15
    x16 = chain(x14, x15, initset)
    if x == 16:
        return x16
    x17 = chain(initset, x13, x16)
    if x == 17:
        return x17
    x18 = fork(manhattan, initset, x17)
    if x == 18:
        return x18
    x19 = compose(even, x18)
    if x == 19:
        return x19
    x20 = sfilter_f(x11, x19)
    if x == 20:
        return x20
    O = fill(x8, FIVE, x20)
    return O

def solve_2dee498d(S, I, x=0):
    x1 = hsplit(I, THREE)
    if x == 1:
        return x1
    O = get_nth_t(x1, F0)
    return O

def solve_97999447(S, I, x=0):
    x1 = rbind(shoot, RIGHT)
    if x == 1:
        return x1
    x2 = compose(x1, center)
    if x == 2:
        return x2
    x3 = fork(recolor_i, color, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R5)
    if x == 4:
        return x4
    x5 = mapply(x3, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = apply(toindices, x4)
    if x == 7:
        return x7
    x8 = interval(ZERO, FIVE, ONE)
    if x == 8:
        return x8
    x9 = apply(double, x8)
    if x == 9:
        return x9
    x10 = apply(increment, x9)
    if x == 10:
        return x10
    x11 = apply(tojvec, x10)
    if x == 11:
        return x11
    x12 = prapply(shift, x7, x11)
    if x == 12:
        return x12
    x13 = merge_f(x12)
    if x == 13:
        return x13
    O = fill(x6, FIVE, x13)
    return O

def solve_d8c310e9(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = hperiod(x2)
    if x == 3:
        return x3
    x4 = tojvec(x3)
    if x == 4:
        return x4
    x5 = shift(x2, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = multiply(x3, THREE)
    if x == 7:
        return x7
    x8 = tojvec(x7)
    if x == 8:
        return x8
    x9 = shift(x2, x8)
    if x == 9:
        return x9
    O = paint(x6, x9)
    return O

def solve_4347f46a(S, I, x=0):
    x1 = fork(difference, toindices, box)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = mapply(x1, x2)
    if x == 3:
        return x3
    O = fill(I, ZERO, x3)
    return O

def solve_08ed6ac7(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = totuple(x1)
    if x == 2:
        return x2
    x3 = size_t(x2)
    if x == 3:
        return x3
    x4 = interval(x3, ZERO, NEG_ONE)
    if x == 4:
        return x4
    x5 = order(x1, height_f)
    if x == 5:
        return x5
    x6 = mpapply(recolor_o, x4, x5)
    if x == 6:
        return x6
    O = paint(I, x6)
    return O

def solve_a87f7484(S, I, x=0):
    x1 = portrait_t(I)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_t, R1)
    if x == 2:
        return x2
    x3 = branch(x1, x2, identity)
    if x == 3:
        return x3
    x4 = x3(I)
    if x == 4:
        return x4
    x5 = numcolors_t(I)
    if x == 5:
        return x5
    x6 = decrement(x5)
    if x == 6:
        return x6
    x7 = hsplit(x4, x6)
    if x == 7:
        return x7
    x8 = rbind(f_ofcolor, ZERO)
    if x == 8:
        return x8
    x9 = apply(x8, x7)
    if x == 9:
        return x9
    x10 = get_common_rank_t(x9, L1)
    if x == 10:
        return x10
    x11 = matcher(x8, x10)
    if x == 11:
        return x11
    x12 = extract(x7, x11)
    if x == 12:
        return x12
    O = x3(x12)
    return O

def solve_42a50994(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    O = cover(I, x3)
    return O

