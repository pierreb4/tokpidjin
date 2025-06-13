from dsl import *
from constants import *


def solve_794b24be(S, I):
    x1 = canvas(ZERO, THREE_BY_THREE)
    x2 = f_ofcolor(I, ONE)
    x3 = size_f(x2)
    x4 = equality(x3, FOUR)
    x5 = decrement(x3)
    x6 = tojvec(x5)
    x7 = connect(ORIGIN, x6)
    x8 = insert(UNITY, x7)
    x9 = branch(x4, x8, x7)
    O = fill(x1, TWO, x9)
    return O

def solve_7c008303(S, I):
    three = b_iz_n(S, p_g, R0)
    x1 = replace(I, three, ZERO)
    eight = b_iz_n(S, p_g, R1)
    x2 = replace(x1, eight, ZERO)
    x3 = compress(x2)
    x4 = upscale_t(x3, THREE)
    x5 = f_ofcolor(I, THREE)
    x6 = subgrid(x5, I)
    x7 = f_ofcolor(x6, ZERO)
    O = fill(x4, ZERO, x7)
    return O

def solve_56dc2b01(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = recolor_i(EIGHT, x1)
    x3 = objects(I, T, F, T)
    x4 = colorfilter(x3, THREE)
    x5 = first(x4)
    x6 = gravitate(x1, x5)
    x7 = sign(x6)
    x8 = gravitate(x5, x1)
    x9 = first(x8)
    x10 = equality(x9, ZERO)
    x11 = branch(x10, width_f, height_f)
    x12 = x11(x5)
    x13 = multiply(x7, x12)
    x14 = crement(x13)
    x15 = shift(x2, x14)
    x16 = paint(I, x15)
    O = move(x16, x5, x8)
    return O

def solve_3618c87e(S, I):
    x1 = objects(I, T, F, T)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    O = move(I, x3, TWO_BY_ZERO)
    return O

def solve_045e512c(S, I):
    x1 = objects(I, T, T, T)
    x2 = argmax_f(x1, size)
    x3 = lbind(shift, x2)
    x4 = lbind(mapply, x3)
    x5 = double(TEN)
    x6 = interval(FOUR, x5, FOUR)
    x7 = rbind(apply, x6)
    x8 = lbind(rbind, multiply)
    x9 = lbind(position, x2)
    x10 = chain(x7, x8, x9)
    x11 = compose(x4, x10)
    x12 = fork(recolor_o, color, x11)
    x13 = remove_f(x2, x1)
    x14 = mapply(x12, x13)
    O = paint(I, x14)
    return O

def solve_f8a8fe49(S, I):
    x1 = replace(I, FIVE, ZERO)
    x2 = compose(normalize, asobject)
    x3 = objects(I, T, F, T)
    x4 = colorfilter(x3, TWO)
    x5 = first(x4)
    x6 = portrait_f(x5)
    x7 = branch(x6, hsplit, vsplit)
    x8 = branch(x6, vmirror_t, hmirror_t)
    x9 = f_ofcolor(I, TWO)
    x10 = subgrid(x9, I)
    x11 = trim(x10)
    x12 = x8(x11)
    x13 = x7(x12, TWO)
    x14 = apply(x2, x13)
    x15 = last_t(x14)
    x16 = ulcorner(x9)
    x17 = increment(x16)
    x18 = shift(x15, x17)
    x19 = branch(x6, tojvec, toivec)
    x20 = compose(x19, increment)
    x21 = branch(x6, width_f, height_f)
    x22 = x21(x15)
    x23 = x20(x22)
    x24 = invert(x23)
    x25 = shift(x18, x24)
    x26 = paint(x1, x25)
    x27 = first(x14)
    x28 = shift(x27, x17)
    x29 = double(x22)
    x30 = x20(x29)
    x31 = shift(x28, x30)
    O = paint(x26, x31)
    return O

def solve_c9e6f938(S, I):
    x1 = vmirror_t(I)
    O = hconcat(I, x1)
    return O

def solve_8403a5d5(S, I):
    x1 = objects(I, T, F, T)
    x2 = first_f(x1)
    x3 = color(x2)
    x4 = asindices(I)
    x5 = leftmost(x2)
    x6 = interval(x5, TEN, TWO)
    x7 = rbind(contained, x6)
    x8 = compose(x7, last)
    x9 = sfilter(x4, x8)
    x10 = fill(I, x3, x9)
    x11 = increment(x5)
    x12 = interval(x11, TEN, FOUR)
    x13 = apply(tojvec, x12)
    x14 = fill(x10, FIVE, x13)
    x15 = lbind(astuple, NINE)
    x16 = add(x5, THREE)
    x17 = interval(x16, TEN, FOUR)
    x18 = apply(x15, x17)
    O = fill(x14, FIVE, x18)
    return O

def solve_952a094c(S, I):
    x1 = objects(I, T, F, T)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = lbind(argmax, x2)
    x6 = lbind(rbind, manhattan)
    x7 = chain(x5, x6, initset)
    x8 = compose(color, x7)
    x9 = fork(astuple, x8, identity)
    x10 = argmax_f(x1, size)
    x11 = outbox(x10)
    x12 = corners(x11)
    x13 = apply(x9, x12)
    O = paint(x4, x13)
    return O

def solve_36fdfd69(S, I):
    x1 = upscale_t(I, TWO)
    x2 = objects(x1, T, T, T)
    x3 = colorfilter(x2, TWO)
    x4 = product(x3, x3)
    x5 = lbind(greater, FIVE)
    x6 = fork(manhattan, first, last)
    x7 = compose(x5, x6)
    x8 = sfilter_f(x4, x7)
    x9 = apply(merge, x8)
    x10 = mapply(delta, x9)
    x11 = fill(x1, FOUR, x10)
    x12 = merge(x3)
    x13 = paint(x11, x12)
    O = downscale(x13, TWO)
    return O

def solve_543a7ed5(S, I):
    x1 = objects(I, T, F, T)
    x2 = colorfilter(x1, SIX)
    x3 = mapply(outbox, x2)
    x4 = fill(I, THREE, x3)
    x5 = mapply(delta, x2)
    O = fill(x4, FOUR, x5)
    return O

def solve_ba97ae07(S, I):
    x1 = objects(I, T, F, T)
    x2 = totuple(x1)
    x3 = apply(color, x2)
    x4 = mostcommon_t(x3)
    x5 = f_ofcolor(I, x4)
    x6 = backdrop(x5)
    O = fill(I, x4, x6)
    return O

def solve_94f9d214(S, I):
    x1 = astuple(FOUR, FOUR)
    x2 = canvas(ZERO, x1)
    x3 = tophalf(I)
    x4 = f_ofcolor(x3, ZERO)
    x5 = bottomhalf(I)
    x6 = f_ofcolor(x5, ZERO)
    x7 = intersection(x4, x6)
    O = fill(x2, TWO, x7)
    return O

def solve_22eb0ac0(S, I):
    x1 = fork(recolor_i, color, backdrop)
    x2 = fgpartition(I)
    x3 = apply(x1, x2)
    x4 = mfilter_f(x3, hline_o)
    O = paint(I, x4)
    return O

def solve_22168020(S, I):
    x1 = lbind(prapply, connect)
    x2 = lbind(f_ofcolor, I)
    x3 = fork(x1, x2, x2)
    x4 = compose(merge, x3)
    x5 = fork(recolor_i, identity, x4)
    x6 = palette_t(I)
    x7 = remove(ZERO, x6)
    x8 = mapply(x5, x7)
    O = paint(I, x8)
    return O

def solve_8e1813be(S, I):
    zero = b_iz_n(S, p_g, R0)
    five = b_iz_n(S, p_g, R1)
    x1 = replace(I, five, zero)
    x2 = objects(x1, T, T, T)
    x3 = first_f(x2)
    x4 = vline_o(x3)
    x5 = branch(x4, dmirror_t, identity)
    x6 = x5(x1)
    x7 = objects(x6, T, T, T)
    x8 = order(x7, uppermost)
    x9 = apply(color, x8)
    x10 = dedupe(x9)
    x11 = size_t(x10)
    x12 = rbind(repeat, x11)
    x13 = apply(x12, x10)
    O = x5(x13)
    return O

def solve_9565186b(S, I):
    x1 = shape_t(I)
    x2 = canvas(FIVE, x1)
    x3 = objects(I, T, F, F)
    x4 = argmax_f(x3, size)
    O = paint(x2, x4)
    return O

def solve_746b3537(S, I):
    x1 = chain(size, dedupe, first)
    x2 = x1(I)
    x3 = equality(x2, ONE)
    x4 = branch(x3, dmirror_t, identity)
    x5 = x4(I)
    x6 = objects(x5, T, F, F)
    x7 = order(x6, leftmost)
    x8 = apply(color, x7)
    x9 = repeat(x8, ONE)
    O = x4(x9)
    return O

def solve_60c09cac(S, I):
    O = upscale_t(I, TWO)
    return O

def solve_1e32b0e9(S, I):
    x1 = asobject(I)
    x2 = palette_f(x1)
    x3 = height_t(I)
    x4 = subtract(x3, TWO)
    x5 = divide(x4, THREE)
    x6 = astuple(x5, x5)
    x7 = crop(I, ORIGIN, x6)
    x8 = partition(x7)
    x9 = matcher(color, ZERO)
    x10 = compose(flip, x9)
    x11 = extract(x8, x10)
    x12 = palette_f(x11)
    x13 = difference(x2, x12)
    x14 = mostcolor_t(I)
    x15 = initset(x14)
    x16 = difference(x13, x15)
    x17 = first(x16)
    x18 = lbind(shift, x11)
    x19 = lbind(multiply, x5)
    x20 = interval(ZERO, THREE, ONE)
    x21 = product(x20, x20)
    x22 = totuple(x21)
    x23 = apply(first, x22)
    x24 = apply(x19, x23)
    x25 = papply(add, x24, x23)
    x26 = apply(last, x22)
    x27 = apply(x19, x26)
    x28 = papply(add, x27, x26)
    x29 = papply(astuple, x25, x28)
    x30 = mapply(x18, x29)
    O = underfill(I, x17, x30)
    return O

def solve_941d9a10(S, I):
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, ZERO)
    x3 = apply(toindices, x2)
    x4 = lbind(extract, x3)
    x5 = lbind(lbind, contained)
    x6 = compose(x4, x5)
    x7 = x6(ORIGIN)
    x8 = fill(I, ONE, x7)
    x9 = shape_t(I)
    x10 = decrement(x9)
    x11 = x6(x10)
    x12 = fill(x8, THREE, x11)
    x13 = astuple(FIVE, FIVE)
    x14 = x6(x13)
    O = fill(x12, TWO, x14)
    return O


def solve_a78176bb(S, I):
    x1 = palette_t(I)
    x2 = remove(ZERO, x1)
    x3 = other_f(x2, FIVE)
    x4 = rbind(shoot, UNITY)
    x5 = rbind(shoot, NEG_UNITY)
    x6 = fork(combine, x4, x5)
    x7 = rbind(add, UP_RIGHT)
    x8 = objects(I, T, F, T)
    x9 = colorfilter(x8, FIVE)
    x10 = lbind(index, I)
    x11 = compose(x10, urcorner)
    x12 = matcher(x11, FIVE)
    x13 = sfilter_f(x9, x12)
    x14 = apply(urcorner, x13)
    x15 = apply(x7, x14)
    x16 = mapply(x6, x15)
    x17 = rbind(add, DOWN_LEFT)
    x18 = difference(x9, x13)
    x19 = apply(llcorner, x18)
    x20 = apply(x17, x19)
    x21 = mapply(x6, x20)
    x22 = combine_f(x16, x21)
    x23 = fill(I, x3, x22)
    five = b_iz_n(S, p_g, R0)
    O = replace(x23, five, ZERO)
    return O

def solve_bbc9ae5d(S, I):
    x1 = width_t(I)
    x2 = halve(x1)
    x3 = vupscale(I, x2)
    x4 = palette_t(I)
    x5 = other_f(x4, ZERO)
    x6 = rbind(shoot, UNITY)
    x7 = f_ofcolor(x3, x5)
    x8 = mapply(x6, x7)
    O = fill(x3, x5, x8)
    return O

def solve_445eab21(S, I):
    x1 = objects(I, T, F, T)
    x2 = fork(multiply, height_f, width_f)
    x3 = argmax_f(x1, x2)
    x4 = color(x3)
    O = canvas(x4, TWO_BY_TWO)
    return O

def solve_d43fd935(S, I):
    x1 = f_ofcolor(I, THREE)
    x2 = rbind(gravitate, x1)
    x3 = fork(add, center, x2)
    x4 = fork(connect, center, x3)
    x5 = fork(recolor_i, color, x4)
    x6 = objects(I, T, F, T)
    x7 = sizefilter(x6, ONE)
    x8 = rbind(vmatching, x1)
    x9 = rbind(hmatching, x1)
    x10 = fork(either, x8, x9)
    x11 = sfilter_f(x7, x10)
    x12 = mapply(x5, x11)
    O = paint(I, x12)
    return O

def solve_be94b721(S, I):
    x1 = objects(I, T, T, T)
    x2 = argmax_f(x1, size)
    O = subgrid(x2, I)
    return O

def solve_cbded52d(S, I):
    x1 = compose(color, first)
    x2 = compose(center, first)
    x3 = compose(center, last)
    x4 = fork(connect, x2, x3)
    x5 = chain(initset, center, x4)
    x6 = fork(recolor_i, x1, x5)
    x7 = objects(I, T, F, T)
    x8 = sizefilter(x7, ONE)
    x9 = product(x8, x8)
    x10 = fork(vmatching, first, last)
    x11 = fork(hmatching, first, last)
    x12 = fork(either, x10, x11)
    x13 = sfilter_f(x9, x12)
    x14 = mapply(x6, x13)
    O = paint(I, x14)
    return O

def solve_72ca375d(S, I):
    x1 = rbind(subgrid, I)
    x2 = objects(I, T, T, T)
    x3 = totuple(x2)
    x4 = apply(x1, x3)
    x5 = apply(vmirror_t, x4)
    x6 = papply(equality, x4, x5)
    x7 = pair(x4, x6)
    x8 = extract(x7, last)
    O = first_t(x8)
    return O

def solve_dc433765(S, I):
    x1 = f_ofcolor(I, THREE)
    x2 = recolor_i(THREE, x1)
    x3 = f_ofcolor(I, FOUR)
    x4 = first_f(x3)
    x5 = first_f(x1)
    x6 = subtract(x4, x5)
    x7 = sign(x6)
    O = move(I, x2, x7)
    return O

def solve_db93a21d(S, I):
    x1 = rbind(shoot, DOWN)
    x2 = f_ofcolor(I, NINE)
    x3 = mapply(x1, x2)
    x4 = underfill(I, ONE, x3)
    x5 = objects(I, T, T, T)
    x6 = colorfilter(x5, NINE)
    x7 = mapply(outbox, x6)
    x8 = fill(x4, THREE, x7)
    x9 = power(outbox, TWO)
    x10 = rbind(greater, ONE)
    x11 = compose(halve, width_f)
    x12 = compose(x10, x11)
    x13 = sfilter_f(x6, x12)
    x14 = mapply(x9, x13)
    x15 = fill(x8, THREE, x14)
    x16 = power(outbox, THREE)
    x17 = matcher(x11, THREE)
    x18 = sfilter_f(x6, x17)
    x19 = mapply(x16, x18)
    O = fill(x15, THREE, x19)
    return O

def solve_bb43febb(S, I):
    x1 = compose(backdrop, inbox)
    x2 = objects(I, T, F, F)
    x3 = colorfilter(x2, FIVE)
    x4 = mapply(x1, x3)
    O = fill(I, TWO, x4)
    return O

def solve_68b16354(S, I):
    O = hmirror_t(I)
    return O

def solve_af902bf9(S, I):
    x1 = f_ofcolor(I, FOUR)
    x2 = prapply(connect, x1, x1)
    x3 = fork(either, vline_i, hline_i)
    x4 = mfilter_f(x2, x3)
    x5 = underfill(I, NEG_ONE, x4)
    x6 = compose(backdrop, inbox)
    x7 = objects(x5, F, F, T)
    x8 = mapply(x6, x7)
    x9 = fill(x5, TWO, x8)
    O = replace(x9, NEG_ONE, ZERO)
    return O

def solve_8e5a5113(S, I):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    x2 = rot90(x1)
    x3 = rot180(x1)
    x4 = astuple(x2, x3)
    x5 = apply(asobject, x4)
    x6 = astuple(FOUR, EIGHT)
    x7 = apply(tojvec, x6)
    x8 = mpapply(shift, x5, x7)
    O = paint(I, x8)
    return O

def solve_8be77c9e(S, I):
    x1 = hmirror_t(I)
    O = vconcat(I, x1)
    return O

def solve_1b60fb0c(S, I):
    x1 = rot90(I)
    x2 = f_ofcolor(x1, ONE)
    x3 = lbind(shift, x2)
    x4 = neighbors(ORIGIN)
    x5 = mapply(neighbors, x4)
    x6 = apply(x3, x5)
    x7 = f_ofcolor(I, ONE)
    x8 = lbind(intersection, x7)
    x9 = compose(size, x8)
    x10 = argmax_f(x6, x9)
    O = underfill(I, TWO, x10)
    return O

def solve_6fa7a44f(S, I):
    x1 = hmirror_t(I)
    O = vconcat(I, x1)
    return O

def solve_7468f01a(S, I):
    x1 = objects(I, F, T, T)
    x2 = first_f(x1)
    x3 = subgrid(x2, I)
    O = vmirror_t(x3)
    return O

def solve_98cf29f8(S, I):
    x1 = fgpartition(I)
    x2 = fork(multiply, height_f, width_f)
    x3 = fork(equality, size, x2)
    x4 = extract(x1, x3)
    x5 = other_f(x1, x4)
    x6 = cover(I, x5)
    x7 = color(x5)
    x8 = rbind(greater, THREE)
    x9 = rbind(colorcount_f, x7)
    x10 = rbind(toobject, I)
    x11 = chain(x10, ineighbors, last)
    x12 = chain(x8, x9, x11)
    x13 = sfilter_f(x5, x12)
    x14 = outbox(x13)
    x15 = backdrop(x14)
    x16 = gravitate(x15, x4)
    x17 = shift(x15, x16)
    O = fill(x6, x7, x17)
    return O

def solve_de1cd16c(S, I):
    x1 = rbind(subgrid, I)
    x2 = objects(I, T, F, F)
    x3 = sizefilter(x2, ONE)
    x4 = difference(x2, x3)
    x5 = apply(x1, x4)
    x6 = leastcolor_t(I)
    x7 = rbind(colorcount_t, x6)
    x8 = argmax_f(x5, x7)
    x9 = mostcolor_t(x8)
    O = canvas(x9, UNITY)
    return O

def solve_46f33fce(S, I):
    x1 = rot180(I)
    x2 = downscale(x1, TWO)
    x3 = rot180(x2)
    O = upscale_t(x3, FOUR)
    return O

def solve_178fcbfb(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = mapply(vfrontier, x1)
    x3 = fill(I, TWO, x2)
    x4 = compose(hfrontier, center)
    x5 = fork(recolor_i, color, x4)
    x6 = objects(I, T, F, T)
    x7 = colorfilter(x6, TWO)
    x8 = difference(x6, x7)
    x9 = mapply(x5, x8)
    O = paint(x3, x9)
    return O

def solve_5521c0d9(S, I):
    x1 = objects(I, T, F, T)
    x2 = merge_f(x1)
    x3 = cover(I, x2)
    x4 = chain(toivec, invert, height_f)
    x5 = fork(shift, identity, x4)
    x6 = mapply(x5, x1)
    O = paint(x3, x6)
    return O

def solve_6cf79266(S, I):
    x1 = astuple(ZERO, ORIGIN)
    x2 = initset(x1)
    x3 = upscale_f(x2, THREE)
    x4 = toindices(x3)
    x5 = lbind(shift, x4)
    x6 = f_ofcolor(I, ZERO)
    x7 = rbind(difference, x6)
    x8 = chain(size, x7, x5)
    x9 = matcher(x8, ZERO)
    x10 = lbind(add, NEG_UNITY)
    x11 = chain(flip, x9, x10)
    x12 = fork(both, x9, x11)
    x13 = sfilter_f(x6, x12)
    x14 = mapply(x5, x13)
    O = fill(I, ONE, x14)
    return O

def solve_bd4472b8(S, I):
    x1 = width_t(I)
    x2 = astuple(TWO, x1)
    x3 = crop(I, ORIGIN, x2)
    x4 = tophalf(x3)
    x5 = dmirror_t(x4)
    x6 = hupscale(x5, x1)
    x7 = repeat(x6, TWO)
    x8 = merge_t(x7)
    O = vconcat(x3, x8)
    return O

def solve_aabf363d(S, I):
    x1 = leastcolor_t(I)
    x2 = replace(I, x1, ZERO)
    x3 = leastcolor_t(x2)
    O = replace(x2, x3, x1)
    return O

def solve_f8ff0b80(S, I):
    x1 = rbind(canvas, UNITY)
    x2 = objects(I, T, T, T)
    x3 = order(x2, size)
    x4 = apply(color, x3)
    x5 = apply(x1, x4)
    x6 = merge_t(x5)
    O = hmirror_t(x6)
    return O

def solve_dbc1a6ce(S, I):
    x1 = fork(connect, first, last)
    x2 = f_ofcolor(I, ONE)
    x3 = product(x2, x2)
    x4 = apply(x1, x3)
    x5 = fork(either, vline_i, hline_i)
    x6 = mfilter_f(x4, x5)
    O = underfill(I, EIGHT, x6)
    return O

def solve_6f8cd79b(S, I):
    x1 = asindices(I)
    x2 = apply(initset, x1)
    x3 = rbind(bordering, I)
    x4 = mfilter_f(x2, x3)
    O = fill(I, EIGHT, x4)
    return O

def solve_5c0a986e(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = lrcorner(x1)
    x3 = shoot(x2, UNITY)
    x4 = fill(I, TWO, x3)
    x5 = f_ofcolor(I, ONE)
    x6 = ulcorner(x5)
    x7 = shoot(x6, NEG_UNITY)
    O = fill(x4, ONE, x7)
    return O

def solve_d9fac9be(S, I):
    x1 = palette_t(I)
    x2 = remove(ZERO, x1)
    x3 = objects(I, T, F, T)
    x4 = argmax_f(x3, size)
    x5 = color(x4)
    x6 = other_f(x2, x5)
    O = canvas(x6, UNITY)
    return O

def solve_72322fa7(S, I):
    x1 = lbind(lbind, shift)
    x2 = compose(x1, normalize)
    x3 = lbind(occurrences, I)
    x4 = lbind(matcher, first)
    x5 = compose(x4, mostcolor_f)
    x6 = fork(sfilter, identity, x5)
    x7 = compose(x3, x6)
    x8 = fork(mapply, x2, x7)
    x9 = objects(I, F, T, T)
    x10 = matcher(numcolors_f, ONE)
    x11 = sfilter_f(x9, x10)
    x12 = difference(x9, x11)
    x13 = mapply(x8, x12)
    x14 = paint(I, x13)
    x15 = lbind(rbind, add)
    x16 = fork(difference, identity, x6)
    x17 = compose(ulcorner, x16)
    x18 = fork(subtract, ulcorner, x17)
    x19 = compose(x15, x18)
    x20 = compose(x3, x16)
    x21 = fork(apply, x19, x20)
    x22 = fork(mapply, x2, x21)
    x23 = mapply(x22, x12)
    O = paint(x14, x23)
    return O

def solve_23b5c85d(S, I):
    x1 = partition(I)
    x2 = argmin_f(x1, size)
    O = subgrid(x2, I)
    return O

def solve_6e02f1e3(S, I):
    x1 = canvas(ZERO, THREE_BY_THREE)
    x2 = numcolors_t(I)
    x3 = equality(x2, THREE)
    x4 = branch(x3, TWO_BY_ZERO, ORIGIN)
    x5 = equality(x2, TWO)
    x6 = branch(x5, TWO_BY_TWO, ZERO_BY_TWO)
    x7 = connect(x4, x6)
    O = fill(x1, FIVE, x7)
    return O

def solve_56ff96f3(S, I):
    x1 = fork(recolor_i, color, backdrop)
    x2 = fgpartition(I)
    x3 = mapply(x1, x2)
    O = paint(I, x3)
    return O

def solve_44d8ac46(S, I):
    x1 = objects(I, T, F, T)
    x2 = apply(delta, x1)
    x3 = mfilter_f(x2, square_f)
    O = fill(I, TWO, x3)
    return O

def solve_67a3c6ac(S, I):
    O = vmirror_t(I)
    return O

def solve_ea786f4a(S, I):
    x1 = shoot(ORIGIN, UNITY)
    x2 = width_t(I)
    x3 = decrement(x2)
    x4 = tojvec(x3)
    x5 = shoot(x4, DOWN_LEFT)
    x6 = combine(x1, x5)
    O = fill(I, ZERO, x6)
    return O

def solve_1f85a75f(S, I):
    x1 = partition(I)
    x2 = argmin_f(x1, size)
    O = subgrid(x2, I)
    return O

def solve_780d0b14(S, I):
    x1 = asindices(I)
    x2 = fill(I, ZERO, x1)
    x3 = objects(I, T, T, T)
    x4 = rbind(greater, TWO)
    x5 = compose(x4, size)
    x6 = sfilter(x3, x5)
    x7 = totuple(x6)
    x8 = apply(color, x7)
    x9 = apply(center, x7)
    x10 = pair(x8, x9)
    x11 = paint(x2, x10)
    x12 = rbind(greater, ONE)
    x13 = compose(dedupe, totuple)
    x14 = chain(x12, size, x13)
    x15 = sfilter(x11, x14)
    x16 = rot90(x15)
    x17 = sfilter(x16, x14)
    O = rot270(x17)
    return O

def solve_4290ef0e(S, I):
    x1 = mostcolor_t(I)
    x2 = fgpartition(I)
    x3 = apply(size, x2)
    x4 = contained(ONE, x3)
    x5 = size_f(x2)
    x6 = increment(x5)
    x7 = branch(x4, x5, x6)
    x8 = double(x7)
    x9 = decrement(x8)
    x10 = astuple(x9, x9)
    x11 = canvas(x1, x10)
    x12 = rbind(argmin, centerofmass)
    x13 = compose(initset, vmirror_f)
    x14 = fork(insert, dmirror_f, x13)
    x15 = fork(insert, cmirror_f, x14)
    x16 = fork(insert, hmirror_f, x15)
    x17 = compose(x12, x16)
    x18 = rbind(branch, NEG_TWO)
    x19 = fork(x18, positive, decrement)
    x20 = lbind(remove, ZERO)
    x21 = lbind(prapply, manhattan)
    x22 = fork(x21, identity, identity)
    x23 = compose(x20, x22)
    x24 = chain(x19, minimum, x23)
    x25 = rbind(valmax, width_f)
    x26 = compose(double, x25)
    x27 = fork(add, x24, x26)
    x28 = objects(I, T, F, T)
    x29 = lbind(colorfilter, x28)
    x30 = compose(x29, color)
    x31 = compose(x27, x30)
    x32 = compose(invert, x31)
    x33 = order(x2, x32)
    x34 = apply(x17, x33)
    x35 = apply(normalize, x34)
    x36 = interval(ZERO, x7, ONE)
    x37 = pair(x36, x36)
    x38 = mpapply(shift, x35, x37)
    x39 = paint(x11, x38)
    x40 = rot90(x39)
    x41 = paint(x40, x38)
    x42 = rot90(x41)
    x43 = paint(x42, x38)
    x44 = rot90(x43)
    O = paint(x44, x38)
    return O

def solve_776ffc46(S, I):
    x1 = objects(I, T, F, T)
    x2 = colorfilter(x1, FIVE)
    x3 = fork(equality, toindices, box)
    x4 = extract(x2, x3)
    x5 = inbox(x4)
    x6 = subgrid(x5, I)
    x7 = asobject(x6)
    x8 = matcher(first, ZERO)
    x9 = compose(flip, x8)
    x10 = sfilter_f(x7, x9)
    x11 = normalize(x10)
    x12 = color(x11)
    x13 = compose(toindices, normalize)
    x14 = toindices(x11)
    x15 = matcher(x13, x14)
    x16 = mfilter_f(x1, x15)
    O = fill(I, x12, x16)
    return O

def solve_cce03e0d(S, I):
    x1 = hconcat(I, I)
    x2 = hconcat(x1, I)
    x3 = vconcat(x2, x2)
    x4 = vconcat(x3, x2)
    x5 = upscale_t(I, THREE)
    x6 = f_ofcolor(x5, ZERO)
    x7 = f_ofcolor(x5, ONE)
    x8 = combine_f(x6, x7)
    O = fill(x4, ZERO, x8)
    return O

def solve_49d1d64f(S, I):
    x1 = shape_t(I)
    x2 = add(x1, TWO)
    x3 = canvas(ZERO, x2)
    x4 = asobject(I)
    x5 = shift(x4, UNITY)
    x6 = paint(x3, x5)
    x7 = lbind(argmin, x5)
    x8 = rbind(compose, initset)
    x9 = lbind(lbind, manhattan)
    x10 = chain(x8, x9, initset)
    x11 = chain(first, x7, x10)
    x12 = fork(astuple, x11, identity)
    x13 = fork(difference, box, corners)
    x14 = asindices(x3)
    x15 = x13(x14)
    x16 = apply(x12, x15)
    O = paint(x6, x16)
    return O

def solve_a2fd1cf0(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = uppermost(x1)
    x3 = f_ofcolor(I, THREE)
    x4 = uppermost(x3)
    x5 = astuple(x2, x4)
    x6 = minimum(x5)
    x7 = leftmost(x3)
    x8 = astuple(x6, x7)
    x9 = maximum(x5)
    x10 = astuple(x9, x7)
    x11 = connect(x8, x10)
    x12 = leftmost(x1)
    x13 = astuple(x12, x7)
    x14 = minimum(x13)
    x15 = astuple(x2, x14)
    x16 = maximum(x13)
    x17 = astuple(x2, x16)
    x18 = connect(x15, x17)
    x19 = combine_f(x11, x18)
    O = underfill(I, EIGHT, x19)
    return O

def solve_5168d44c(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = recolor_i(TWO, x1)
    x3 = f_ofcolor(I, THREE)
    x4 = height_f(x3)
    x5 = equality(x4, ONE)
    x6 = branch(x5, ZERO_BY_TWO, TWO_BY_ZERO)
    O = move(I, x2, x6)
    return O

def solve_25d8a9c8(S, I):
    x1 = objects(I, T, F, F)
    x2 = sizefilter(x1, THREE)
    x3 = mfilter_f(x2, hline_o)
    x4 = toindices(x3)
    x5 = fill(I, FIVE, x4)
    x6 = asindices(I)
    x7 = difference(x6, x4)
    O = fill(x5, ZERO, x7)
    return O

def solve_ae4f1146(S, I):
    x1 = objects(I, F, F, T)
    x2 = rbind(colorcount_f, ONE)
    x3 = argmax_f(x1, x2)
    O = subgrid(x3, I)
    return O

def solve_90f3ed37(S, I):
    x1 = interval(TWO, NEG_ONE, NEG_ONE)
    x2 = apply(tojvec, x1)
    x3 = rbind(apply, x2)
    x4 = lbind(lbind, shift)
    x5 = objects(I, T, T, T)
    x6 = order(x5, uppermost)
    x7 = first_t(x6)
    x8 = normalize(x7)
    x9 = lbind(shift, x8)
    x10 = compose(x9, ulcorner)
    x11 = chain(x3, x4, x10)
    x12 = lbind(compose, size)
    x13 = lbind(lbind, intersection)
    x14 = compose(x12, x13)
    x15 = fork(argmax, x11, x14)
    x16 = remove_f(x7, x6)
    x17 = mapply(x15, x16)
    O = underfill(I, ONE, x17)
    return O

def solve_1f642eb9(S, I):
    x1 = objects(I, T, F, T)
    x2 = sizefilter(x1, ONE)
    x3 = difference(x1, x2)
    x4 = first_f(x3)
    x5 = rbind(gravitate, x4)
    x6 = compose(crement, x5)
    x7 = fork(shift, identity, x6)
    x8 = mapply(x7, x2)
    O = paint(I, x8)
    return O

def solve_fcc82909(S, I):
    x1 = rbind(add, DOWN)
    x2 = compose(x1, llcorner)
    x3 = compose(toivec, numcolors_f)
    x4 = fork(add, lrcorner, x3)
    x5 = fork(astuple, x2, x4)
    x6 = compose(box, x5)
    x7 = objects(I, F, T, T)
    x8 = mapply(x6, x7)
    O = fill(I, THREE, x8)
    return O

def solve_1a07d186(S, I):
    x1 = objects(I, T, F, T)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = difference(x1, x2)
    x6 = lbind(colorfilter, x5)
    x7 = chain(first, x6, color)
    x8 = fork(gravitate, identity, x7)
    x9 = fork(shift, identity, x8)
    x10 = apply(color, x5)
    x11 = rbind(contained, x10)
    x12 = compose(x11, color)
    x13 = sfilter_f(x2, x12)
    x14 = mapply(x9, x13)
    O = paint(x4, x14)
    return O

def solve_1190e5a7(S, I):
    x1 = mostcolor_t(I)
    x2 = frontiers(I)
    x3 = sfilter_f(x2, vline_o)
    x4 = difference(x2, x3)
    x5 = astuple(x4, x3)
    x6 = apply(size, x5)
    x7 = increment(x6)
    O = canvas(x1, x7)
    return O

def solve_9ddd00f0(S, I):
    x1 = lbind(apply, maximum)
    x2 = replace(I, FOUR, ZERO)
    x3 = dmirror_t(x2)
    x4 = papply(pair, x2, x3)
    x5 = apply(x1, x4)
    x6 = cmirror_t(x5)
    x7 = papply(pair, x5, x6)
    x8 = apply(x1, x7)
    O = cmirror_t(x8)
    return O

def solve_d13f3404(S, I):
    x1 = astuple(SIX, SIX)
    x2 = canvas(ZERO, x1)
    x3 = rbind(shoot, UNITY)
    x4 = compose(x3, center)
    x5 = fork(recolor_i, color, x4)
    x6 = objects(I, T, F, T)
    x7 = mapply(x5, x6)
    O = paint(x2, x7)
    return O

def solve_253bf280(S, I):
    x1 = f_ofcolor(I, EIGHT)
    x2 = prapply(connect, x1, x1)
    x3 = rbind(greater, ONE)
    x4 = compose(x3, size)
    x5 = sfilter_f(x2, x4)
    x6 = fork(either, vline_i, hline_i)
    x7 = mfilter_f(x5, x6)
    x8 = fill(I, THREE, x7)
    O = fill(x8, EIGHT, x1)
    return O

def solve_a61f2674(S, I):
    x1 = replace(I, FIVE, ZERO)
    x2 = objects(I, T, F, T)
    x3 = argmax_f(x2, size)
    x4 = recolor_o(ONE, x3)
    x5 = argmin_f(x2, size)
    x6 = recolor_o(TWO, x5)
    x7 = combine_f(x4, x6)
    O = paint(x1, x7)
    return O

def solve_ec883f72(S, I):
    x1 = palette_t(I)
    x2 = remove(ZERO, x1)
    x3 = objects(I, T, T, T)
    x4 = fork(multiply, height_f, width_f)
    x5 = argmax_f(x3, x4)
    x6 = color(x5)
    x7 = other_f(x2, x6)
    x8 = lrcorner(x5)
    x9 = shoot(x8, UNITY)
    x10 = llcorner(x5)
    x11 = shoot(x10, DOWN_LEFT)
    x12 = combine(x9, x11)
    x13 = urcorner(x5)
    x14 = shoot(x13, UP_RIGHT)
    x15 = ulcorner(x5)
    x16 = shoot(x15, NEG_UNITY)
    x17 = combine(x14, x16)
    x18 = combine(x12, x17)
    O = underfill(I, x7, x18)
    return O

def solve_0b148d64(S, I):
    x1 = partition(I)
    x2 = argmin_f(x1, size)
    O = subgrid(x2, I)
    return O

def solve_25d487eb(S, I):
    x1 = leastcolor_t(I)
    x2 = f_ofcolor(I, x1)
    x3 = center(x2)
    x4 = objects(I, T, F, T)
    x5 = merge_f(x4)
    x6 = center(x5)
    x7 = subtract(x6, x3)
    x8 = shoot(x3, x7)
    O = underfill(I, x1, x8)
    return O

def solve_77fdfe62(S, I):
    x1 = replace(I, EIGHT, ZERO)
    x2 = replace(x1, ONE, ZERO)
    x3 = compress(x2)
    x4 = f_ofcolor(I, EIGHT)
    x5 = subgrid(x4, I)
    x6 = width_t(x5)
    x7 = halve(x6)
    x8 = upscale_t(x3, x7)
    x9 = f_ofcolor(x5, ZERO)
    O = fill(x8, ZERO, x9)
    return O

def solve_91413438(S, I):
    x1 = colorcount_t(I, ZERO)
    x2 = multiply(x1, THREE)
    x3 = multiply(x2, x1)
    x4 = subtract(x3, THREE)
    x5 = astuple(THREE, x4)
    x6 = canvas(ZERO, x5)
    x7 = hconcat(I, x6)
    x8 = objects(x7, T, T, T)
    x9 = first_f(x8)
    x10 = lbind(shift, x9)
    x11 = compose(x10, tojvec)
    x12 = rbind(multiply, THREE)
    x13 = subtract(NINE, x1)
    x14 = interval(ZERO, x13, ONE)
    x15 = apply(x12, x14)
    x16 = mapply(x11, x15)
    x17 = paint(x7, x16)
    x18 = hsplit(x17, x1)
    O = merge_t(x18)
    return O

def solve_d4f3cd78(S, I):
    x1 = f_ofcolor(I, FIVE)
    x2 = delta(x1)
    x3 = fill(I, EIGHT, x2)
    x4 = box(x1)
    x5 = difference(x4, x1)
    x6 = first_f(x5)
    x7 = position(x4, x5)
    x8 = shoot(x6, x7)
    O = fill(x3, EIGHT, x8)
    return O

def solve_d687bc17(S, I):
    x1 = objects(I, T, F, T)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = difference(x1, x2)
    x6 = lbind(colorfilter, x5)
    x7 = chain(first, x6, color)
    x8 = fork(gravitate, identity, x7)
    x9 = fork(shift, identity, x8)
    x10 = apply(color, x5)
    x11 = rbind(contained, x10)
    x12 = compose(x11, color)
    x13 = sfilter_f(x2, x12)
    x14 = mapply(x9, x13)
    O = paint(x4, x14)
    return O

def solve_ea32f347(S, I):
    x1 = replace(I, FIVE, FOUR)
    x2 = objects(I, T, F, T)
    x3 = argmax_f(x2, size)
    x4 = fill(x1, ONE, x3)
    x5 = argmin_f(x2, size)
    O = fill(x4, TWO, x5)
    return O

def solve_3de23699(S, I):
    x1 = fgpartition(I)
    x2 = sizefilter(x1, FOUR)
    x3 = first_f(x2)
    x4 = subgrid(x3, I)
    x5 = trim(x4)
    x6 = difference(x1, x2)
    x7 = first_f(x6)
    x8 = color(x7)
    x9 = color(x3)
    O = replace(x5, x8, x9)
    return O

def solve_36d67576(S, I):
    x1 = lbind(lbind, shift)
    x2 = compose(x1, normalize)
    x3 = lbind(rbind, subtract)
    x4 = compose(x3, ulcorner)
    x5 = astuple(TWO, FOUR)
    x6 = rbind(contained, x5)
    x7 = compose(x6, first)
    x8 = rbind(sfilter, x7)
    x9 = chain(x4, x8, normalize)
    x10 = lbind(occurrences, I)
    x11 = chain(x10, x8, normalize)
    x12 = fork(apply, x9, x11)
    x13 = fork(mapply, x2, x12)
    x14 = astuple(cmirror_f, dmirror_f)
    x15 = astuple(hmirror_f, vmirror_f)
    x16 = combine(x14, x15)
    x17 = fork(compose, first, last)
    x18 = product(x16, x16)
    x19 = apply(x17, x18)
    x20 = totuple(x19)
    x21 = combine(x16, x20)
    x22 = objects(I, F, F, T)
    x23 = argmax_f(x22, numcolors_f)
    x24 = rapply_t(x21, x23)
    x25 = mapply(x13, x24)
    O = paint(I, x25)
    return O

def solve_3906de3d(S, I):
    x1 = rbind(order, identity)
    x2 = rot270(I)
    x3 = switch(x2, ONE, TWO)
    x4 = apply(x1, x3)
    x5 = switch(x4, ONE, TWO)
    O = cmirror_t(x5)
    return O

def solve_cd3c21df(S, I):
    x1 = vmirror_t(I)
    x2 = fgpartition(x1)
    x3 = order(x2, size)
    x4 = last_t(x3)
    x5 = remove_f(x4, x3)
    x6 = compose(toindices, normalize)
    x7 = x6(x4)
    x8 = rbind(intersection, x7)
    x9 = rbind(upscale_f, TWO)
    x10 = chain(toindices, x9, normalize)
    x11 = chain(size, x8, x10)
    x12 = argmax_t(x5, x11)
    x13 = subgrid(x12, x1)
    O = vmirror_t(x13)
    return O

def solve_73182012(S, I):
    x1 = objects(I, F, T, T)
    x2 = first_f(x1)
    x3 = subgrid(x2, I)
    x4 = lefthalf(x3)
    O = tophalf(x4)
    return O

def solve_b775ac94(S, I):
    x1 = lbind(index, I)
    x2 = lbind(compose, toindices)
    x3 = rbind(compose, first)
    x4 = lbind(rbind, equality)
    x5 = chain(x3, x4, mostcolor_f)
    x6 = fork(sfilter, identity, x5)
    x7 = rbind(compose, initset)
    x8 = lbind(rbind, adjacent)
    x9 = fork(difference, identity, x6)
    x10 = chain(x7, x8, x9)
    x11 = fork(extract, x6, x10)
    x12 = fork(insert, x11, x9)
    x13 = lbind(recolor_i, ZERO)
    x14 = chain(x13, delta, x12)
    x15 = fork(combine, x12, x14)
    x16 = x2(x15)
    x17 = lbind(compose, x6)
    x18 = fork(position, x6, x9)
    x19 = chain(toivec, first, x18)
    x20 = fork(multiply, shape_f, x19)
    x21 = fork(shift, hmirror_f, x20)
    x22 = x17(x21)
    x23 = compose(crement, invert)
    x24 = lbind(compose, x23)
    x25 = x24(x19)
    x26 = fork(shift, x22, x25)
    x27 = x2(x26)
    x28 = fork(intersection, x16, x27)
    x29 = chain(x1, first, x28)
    x30 = fork(recolor_o, x29, x26)
    x31 = objects(I, F, T, T)
    x32 = mapply(x30, x31)
    x33 = paint(I, x32)
    x34 = chain(tojvec, last, x18)
    x35 = fork(multiply, shape_f, x34)
    x36 = fork(shift, vmirror_f, x35)
    x37 = x17(x36)
    x38 = x24(x34)
    x39 = fork(shift, x37, x38)
    x40 = x2(x39)
    x41 = fork(intersection, x16, x40)
    x42 = chain(x1, first, x41)
    x43 = fork(recolor_o, x42, x39)
    x44 = mapply(x43, x31)
    x45 = paint(x33, x44)
    x46 = compose(hmirror_f, vmirror_f)
    x47 = fork(multiply, shape_f, x18)
    x48 = fork(shift, x46, x47)
    x49 = x17(x48)
    x50 = x24(x18)
    x51 = fork(shift, x49, x50)
    x52 = x2(x51)
    x53 = fork(intersection, x16, x52)
    x54 = chain(x1, first, x53)
    x55 = fork(recolor_o, x54, x51)
    x56 = mapply(x55, x31)
    O = paint(x45, x56)
    return O

def solve_3eda0437(S, I):
    x1 = lbind(lbind, shift)
    x2 = lbind(occurrences, I)
    x3 = fork(apply, x1, x2)
    x4 = lbind(canvas, ZERO)
    x5 = chain(x3, asobject, x4)
    x6 = interval(TWO, TEN, ONE)
    x7 = prapply(astuple, x6, x6)
    x8 = mapply(x5, x7)
    x9 = argmax_f(x8, size)
    O = fill(I, SIX, x9)
    return O

def solve_f8c80d96(S, I):
    x1 = leastcolor_t(I)
    x2 = objects(I, T, F, F)
    x3 = argmin_f(x2, width_f)
    x4 = size_f(x3)
    x5 = equality(x4, ONE)
    x6 = branch(x5, identity, outbox)
    x7 = chain(outbox, outbox, x6)
    x8 = colorfilter(x2, x1)
    x9 = argmax_f(x8, size)
    x10 = x7(x9)
    x11 = fill(I, x1, x10)
    x12 = power(x7, TWO)
    x13 = x12(x9)
    x14 = fill(x11, x1, x13)
    x15 = power(x7, THREE)
    x16 = x15(x9)
    x17 = fill(x14, x1, x16)
    O = replace(x17, ZERO, FIVE)
    return O

def solve_28bf18c6(S, I):
    x1 = objects(I, T, T, T)
    x2 = first_f(x1)
    x3 = subgrid(x2, I)
    O = hconcat(x3, x3)
    return O

def solve_d90796e8(S, I):
    x1 = objects(I, F, F, T)
    x2 = sizefilter(x1, TWO)
    x3 = lbind(contained, TWO)
    x4 = compose(x3, palette_f)
    x5 = mfilter_f(x2, x4)
    x6 = cover(I, x5)
    x7 = matcher(first, THREE)
    x8 = sfilter_f(x5, x7)
    O = fill(x6, EIGHT, x8)
    return O

def solve_1bfc4729(S, I):
    x1 = tophalf(I)
    x2 = leastcolor_t(x1)
    x3 = hfrontier(TWO_BY_ZERO)
    x4 = asindices(I)
    x5 = box(x4)
    x6 = combine(x3, x5)
    x7 = fill(x1, x2, x6)
    x8 = hmirror_t(x7)
    x9 = bottomhalf(I)
    x10 = leastcolor_t(x9)
    x11 = replace(x8, x2, x10)
    O = vconcat(x7, x11)
    return O

def solve_6e19193c(S, I):
    x1 = leastcolor_t(I)
    x2 = compose(first, delta)
    x3 = rbind(colorcount_f, x1)
    x4 = matcher(x3, TWO)
    x5 = rbind(toobject, I)
    x6 = chain(x4, x5, dneighbors)
    x7 = rbind(sfilter, x6)
    x8 = chain(first, x7, toindices)
    x9 = fork(subtract, x2, x8)
    x10 = fork(shoot, x2, x9)
    x11 = objects(I, T, F, T)
    x12 = mapply(x10, x11)
    x13 = fill(I, x1, x12)
    x14 = mapply(delta, x11)
    O = fill(x13, ZERO, x14)
    return O

def solve_e73095fd(S, I):
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, ZERO)
    x3 = fork(equality, toindices, backdrop)
    x4 = sfilter_f(x2, x3)
    x5 = matcher(size, ZERO)
    x6 = f_ofcolor(I, FIVE)
    x7 = rbind(intersection, x6)
    x8 = lbind(mapply, dneighbors)
    x9 = chain(x8, corners, outbox)
    x10 = fork(difference, x9, outbox)
    x11 = chain(x5, x7, x10)
    x12 = mfilter_f(x4, x11)
    O = fill(I, FOUR, x12)
    return O

def solve_9172f3a0(S, I):
    O = upscale_t(I, THREE)
    return O

def solve_90c28cc7(S, I):
    x1 = objects(I, F, F, T)
    x2 = first_f(x1)
    x3 = subgrid(x2, I)
    x4 = dedupe(x3)
    x5 = rot90(x4)
    x6 = dedupe(x5)
    O = rot270(x6)
    return O

def solve_88a62173(S, I):
    x1 = lefthalf(I)
    x2 = tophalf(x1)
    x3 = righthalf(I)
    x4 = tophalf(x3)
    x5 = astuple(x2, x4)
    x6 = bottomhalf(x1)
    x7 = bottomhalf(x3)
    x8 = astuple(x6, x7)
    x9 = combine_t(x5, x8)
    O = leastcommon_t(x9)
    return O

def solve_2dc579da(S, I):
    x1 = rbind(hsplit, TWO)
    x2 = vsplit(I, TWO)
    x3 = mapply(x1, x2)
    O = argmax_t(x3, numcolors_t)
    return O

def solve_aedd82e4(S, I):
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, TWO)
    x3 = sizefilter(x2, ONE)
    x4 = merge_f(x3)
    O = fill(I, ONE, x4)
    return O

def solve_8f2ea7aa(S, I):
    x1 = objects(I, T, F, T)
    x2 = merge_f(x1)
    x3 = subgrid(x2, I)
    x4 = upscale_t(x3, THREE)
    x5 = hconcat(x3, x3)
    x6 = hconcat(x5, x3)
    x7 = vconcat(x6, x6)
    x8 = vconcat(x7, x6)
    O = cellwise(x4, x8, ZERO)
    return O

def solve_ddf7fa4f(S, I):
    x1 = compose(color, first)
    x2 = fork(recolor_o, x1, last)
    x3 = objects(I, T, F, T)
    x4 = sizefilter(x3, ONE)
    x5 = colorfilter(x3, FIVE)
    x6 = product(x4, x5)
    x7 = fork(vmatching, first, last)
    x8 = sfilter_f(x6, x7)
    x9 = mapply(x2, x8)
    O = paint(I, x9)
    return O

def solve_28e73c20(S, I):
    x1 = canvas(THREE, UNITY)
    x2 = lbind(hupscale, x1)
    x3 = compose(x2, height_t)
    x4 = rbind(hconcat, x1)
    x5 = canvas(ZERO, UNITY)
    x6 = lbind(hupscale, x5)
    x7 = chain(x6, decrement, height_t)
    x8 = compose(x4, x7)
    x9 = fork(vconcat, x8, rot90)
    x10 = fork(vconcat, x3, x9)
    x11 = width_t(I)
    x12 = subtract(x11, FOUR)
    x13 = power(x10, x12)
    x14 = even(x11)
    x15 = upscale_t(x1, FOUR)
    x16 = astuple(TWO, TWO)
    x17 = astuple(ONE, TWO)
    x18 = initset(DOWN)
    x19 = insert(UNITY, x18)
    x20 = insert(x17, x19)
    x21 = insert(x16, x20)
    x22 = fill(x15, ZERO, x21)
    x23 = vupscale(x1, FIVE)
    x24 = hupscale(x23, THREE)
    x25 = astuple(THREE, ONE)
    x26 = astuple(TWO, ONE)
    x27 = insert(x26, x19)
    x28 = insert(x25, x27)
    x29 = fill(x24, ZERO, x28)
    x30 = branch(x14, x22, x29)
    O = x13(x30)
    return O

def solve_d406998b(S, I):
    x1 = vmirror_t(I)
    x2 = f_ofcolor(x1, FIVE)
    x3 = compose(even, last)
    x4 = sfilter_f(x2, x3)
    x5 = fill(x1, THREE, x4)
    O = vmirror_t(x5)
    return O

def solve_95990924(S, I):
    x1 = objects(I, T, F, T)
    x2 = apply(outbox, x1)
    x3 = apply(ulcorner, x2)
    x4 = fill(I, ONE, x3)
    x5 = apply(urcorner, x2)
    x6 = fill(x4, TWO, x5)
    x7 = apply(llcorner, x2)
    x8 = fill(x6, THREE, x7)
    x9 = apply(lrcorner, x2)
    O = fill(x8, FOUR, x9)
    return O

def solve_dae9d2b5(S, I):
    x1 = lefthalf(I)
    x2 = f_ofcolor(x1, FOUR)
    x3 = righthalf(I)
    x4 = f_ofcolor(x3, THREE)
    x5 = combine_f(x2, x4)
    O = fill(x1, SIX, x5)
    return O

def solve_868de0fa(S, I):
    x1 = objects(I, T, F, F)
    x2 = sfilter_f(x1, square_f)
    x3 = compose(even, height_f)
    x4 = sfilter_f(x2, x3)
    x5 = merge_f(x4)
    x6 = fill(I, TWO, x5)
    x7 = difference(x2, x4)
    x8 = merge_f(x7)
    O = fill(x6, SEVEN, x8)
    return O

def solve_c8cbb738(S, I):
    x1 = mostcolor_t(I)
    x2 = fgpartition(I)
    x3 = valmax_f(x2, shape_f)
    x4 = canvas(x1, x3)
    x5 = lbind(subtract, x3)
    x6 = chain(halve, x5, shape_f)
    x7 = fork(shift, identity, x6)
    x8 = apply(normalize, x2)
    x9 = mapply(x7, x8)
    O = paint(x4, x9)
    return O

def solve_d2abd087(S, I):
    x1 = objects(I, T, F, T)
    x2 = matcher(size, SIX)
    x3 = mfilter_f(x1, x2)
    x4 = fill(I, TWO, x3)
    x5 = compose(flip, x2)
    x6 = mfilter_f(x1, x5)
    O = fill(x4, ONE, x6)
    return O

def solve_5614dbcf(S, I):
    x1 = replace(I, FIVE, ZERO)
    O = downscale(x1, THREE)
    return O

def solve_27a28665(S, I):
    x1 = objects(I, T, F, F)
    x2 = valmax_f(x1, size)
    x3 = equality(x2, FIVE)
    x4 = equality(x2, FOUR)
    x5 = equality(x2, ONE)
    x6 = branch(x5, TWO, ONE)
    x7 = branch(x4, THREE, x6)
    x8 = branch(x3, SIX, x7)
    O = canvas(x8, UNITY)
    return O

def solve_1caeab9d(S, I):
    x1 = objects(I, T, T, T)
    x2 = merge_f(x1)
    x3 = cover(I, x2)
    x4 = f_ofcolor(I, ONE)
    x5 = lowermost(x4)
    x6 = lbind(subtract, x5)
    x7 = chain(toivec, x6, lowermost)
    x8 = fork(shift, identity, x7)
    x9 = mapply(x8, x1)
    O = paint(x3, x9)
    return O

def solve_06df4c85(S, I):
    x1 = compose(last, first)
    x2 = power(last, TWO)
    x3 = fork(connect, x1, x2)
    x4 = fork(recolor_i, color, x3)
    x5 = partition(I)
    x6 = argmax_f(x5, size)
    x7 = colorfilter(x5, ZERO)
    x8 = difference(x5, x7)
    x9 = remove_f(x6, x8)
    x10 = merge_f(x9)
    x11 = product(x10, x10)
    x12 = power(first, TWO)
    x13 = compose(first, last)
    x14 = fork(equality, x12, x13)
    x15 = sfilter_f(x11, x14)
    x16 = apply(x4, x15)
    x17 = fork(either, vline_o, hline_o)
    x18 = mfilter_f(x16, x17)
    x19 = paint(I, x18)
    x20 = mostcolor_t(I)
    x21 = f_ofcolor(I, x20)
    O = fill(x19, x20, x21)
    return O

def solve_0962bcdd(S, I):
    x1 = leastcolor_t(I)
    x2 = replace(I, ZERO, x1)
    x3 = leastcolor_t(x2)
    x4 = f_ofcolor(I, x3)
    x5 = mapply(dneighbors, x4)
    x6 = fill(I, x3, x5)
    x7 = fork(connect, ulcorner, lrcorner)
    x8 = fork(connect, llcorner, urcorner)
    x9 = fork(combine, x7, x8)
    x10 = objects(x6, F, T, T)
    x11 = mapply(x9, x10)
    O = fill(x6, x1, x11)
    return O

def solve_f2829549(S, I):
    x1 = lefthalf(I)
    x2 = shape_t(x1)
    x3 = canvas(ZERO, x2)
    x4 = f_ofcolor(x1, ZERO)
    x5 = righthalf(I)
    x6 = f_ofcolor(x5, ZERO)
    x7 = intersection(x4, x6)
    O = fill(x3, THREE, x7)
    return O

def solve_f25fbde4(S, I):
    x1 = objects(I, T, T, T)
    x2 = first_f(x1)
    x3 = subgrid(x2, I)
    O = upscale_t(x3, TWO)
    return O

def solve_3f7978a0(S, I):
    x1 = fgpartition(I)
    x2 = matcher(color, FIVE)
    x3 = extract(x1, x2)
    x4 = ulcorner(x3)
    x5 = subtract(x4, DOWN)
    x6 = shape_f(x3)
    x7 = add(x6, TWO_BY_ZERO)
    O = crop(I, x5, x7)
    return O

def solve_137eaa0f(S, I):
    x1 = canvas(ZERO, THREE_BY_THREE)
    x2 = matcher(first, FIVE)
    x3 = rbind(sfilter, x2)
    x4 = chain(invert, center, x3)
    x5 = fork(shift, identity, x4)
    x6 = objects(I, F, T, T)
    x7 = mapply(x5, x6)
    x8 = shift(x7, UNITY)
    O = paint(x1, x8)
    return O

def solve_321b1fc6(S, I):
    x1 = objects(I, F, F, T)
    x2 = colorfilter(x1, EIGHT)
    x3 = difference(x1, x2)
    x4 = first_f(x3)
    x5 = cover(I, x4)
    x6 = normalize(x4)
    x7 = lbind(shift, x6)
    x8 = apply(ulcorner, x2)
    x9 = mapply(x7, x8)
    O = paint(x5, x9)
    return O

def solve_c0f76784(S, I):
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, ZERO)
    x3 = sfilter_f(x2, square_f)
    x4 = merge_f(x3)
    x5 = fill(I, SEVEN, x4)
    x6 = argmax_f(x3, size)
    x7 = fill(x5, EIGHT, x6)
    x8 = sizefilter(x3, ONE)
    x9 = merge_f(x8)
    O = fill(x7, SIX, x9)
    return O

def solve_b60334d2(S, I):
    x1 = replace(I, FIVE, ZERO)
    x2 = f_ofcolor(I, FIVE)
    x3 = mapply(dneighbors, x2)
    x4 = fill(x1, ONE, x3)
    x5 = mapply(ineighbors, x2)
    O = fill(x4, FIVE, x5)
    return O

def solve_67385a82(S, I):
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, THREE)
    x3 = sizefilter(x2, ONE)
    x4 = difference(x2, x3)
    x5 = merge_f(x4)
    O = fill(I, EIGHT, x5)
    return O

def solve_3befdf3e(S, I):
    x1 = leastcolor_t(I)
    x2 = palette_t(I)
    x3 = remove(ZERO, x2)
    x4 = other_f(x3, x1)
    x5 = switch(I, x1, x4)
    x6 = lbind(power, outbox)
    x7 = compose(width_f, inbox)
    x8 = compose(x6, x7)
    x9 = initset(x8)
    x10 = lbind(rapply, x9)
    x11 = chain(initset, first, x10)
    x12 = fork(rapply, x11, identity)
    x13 = compose(first, x12)
    x14 = compose(backdrop, x13)
    x15 = objects(I, F, F, T)
    x16 = mapply(x14, x15)
    x17 = underfill(x5, x4, x16)
    x18 = lbind(chain, backdrop)
    x19 = lbind(x18, inbox)
    x20 = compose(x19, x8)
    x21 = lbind(apply, initset)
    x22 = chain(x21, corners, x14)
    x23 = fork(mapply, x20, x22)
    x24 = fork(intersection, x14, x23)
    x25 = mapply(x24, x15)
    O = fill(x17, ZERO, x25)
    return O

def solve_239be575(S, I):
    x1 = objects(I, F, T, T)
    x2 = lbind(contained, TWO)
    x3 = compose(x2, palette_f)
    x4 = sfilter_f(x1, x3)
    x5 = size_f(x4)
    x6 = greater(x5, ONE)
    x7 = branch(x6, ZERO, EIGHT)
    O = canvas(x7, UNITY)
    return O

def solve_ae3edfdc(S, I):
    x1 = replace(I, THREE, ZERO)
    x2 = replace(x1, SEVEN, ZERO)
    x3 = lbind(rbind, gravitate)
    x4 = objects(I, T, F, T)
    x5 = lbind(colorfilter, x4)
    x6 = chain(x3, first, x5)
    x7 = x6(TWO)
    x8 = fork(shift, identity, x7)
    x9 = x5(THREE)
    x10 = mapply(x8, x9)
    x11 = paint(x2, x10)
    x12 = x6(ONE)
    x13 = fork(shift, identity, x12)
    x14 = x5(SEVEN)
    x15 = mapply(x13, x14)
    O = paint(x11, x15)
    return O

def solve_0520fde7(S, I):
    x1 = vmirror_t(I)
    x2 = lefthalf(x1)
    x3 = righthalf(x1)
    x4 = vmirror_t(x3)
    x5 = cellwise(x2, x4, ZERO)
    O = replace(x5, ONE, TWO)
    return O

def solve_44f52bb0(S, I):
    x1 = vmirror_t(I)
    x2 = equality(x1, I)
    x3 = branch(x2, ONE, SEVEN)
    O = canvas(x3, UNITY)
    return O

def solve_1e0a9b12(S, I):
    x1 = rbind(order, identity)
    x2 = rot270(I)
    x3 = apply(x1, x2)
    O = rot90(x3)
    return O

def solve_7e0986d6(S, I):
    x1 = leastcolor_t(I)
    x2 = replace(I, x1, ZERO)
    x3 = leastcolor_t(x2)
    x4 = f_ofcolor(I, x1)
    x5 = rbind(colorcount_f, x3)
    x6 = chain(positive, decrement, x5)
    x7 = rbind(toobject, x2)
    x8 = chain(x6, x7, dneighbors)
    x9 = sfilter_f(x4, x8)
    O = fill(x2, x3, x9)
    return O

def solve_85c4e7cd(S, I):
    x1 = objects(I, T, F, F)
    x2 = compose(invert, size)
    x3 = order(x1, x2)
    x4 = apply(color, x3)
    x5 = order(x1, size)
    x6 = mpapply(recolor_o, x4, x5)
    O = paint(I, x6)
    return O

def solve_4938f0c2(S, I):
    x1 = objects(I, T, T, T)
    x2 = size_f(x1)
    x3 = greater(x2, FOUR)
    x4 = f_ofcolor(I, TWO)
    x5 = vmirror_f(x4)
    x6 = width_f(x4)
    x7 = tojvec(x6)
    x8 = add(x7, ZERO_BY_TWO)
    x9 = shift(x5, x8)
    x10 = fill(I, TWO, x9)
    x11 = f_ofcolor(x10, TWO)
    x12 = hmirror_f(x11)
    x13 = height_f(x4)
    x14 = toivec(x13)
    x15 = add(x14, TWO_BY_ZERO)
    x16 = shift(x12, x15)
    x17 = fill(x10, TWO, x16)
    O = branch(x3, I, x17)
    return O

def solve_4be741c5(S, I):
    x1 = portrait_t(I)
    x2 = branch(x1, dmirror_t, identity)
    x3 = x2(I)
    x4 = branch(x1, height_t, width_t)
    x5 = x4(I)
    x6 = astuple(ONE, x5)
    x7 = crop(x3, ORIGIN, x6)
    x8 = apply(dedupe, x7)
    O = x2(x8)
    return O

def solve_d631b094(S, I):
    x1 = palette_t(I)
    x2 = other_f(x1, ZERO)
    x3 = f_ofcolor(I, x2)
    x4 = size_f(x3)
    x5 = astuple(ONE, x4)
    O = canvas(x2, x5)
    return O

def solve_c3e719e8(S, I):
    x1 = hconcat(I, I)
    x2 = hconcat(x1, I)
    x3 = vconcat(x2, x2)
    x4 = vconcat(x3, x2)
    x5 = upscale_t(I, THREE)
    x6 = asindices(x5)
    x7 = mostcolor_t(I)
    x8 = f_ofcolor(x5, x7)
    x9 = difference(x6, x8)
    O = fill(x4, ZERO, x9)
    return O

def solve_a3325580(S, I):
    x1 = objects(I, T, F, T)
    x2 = valmax_f(x1, size)
    x3 = astuple(ONE, x2)
    x4 = rbind(canvas, x3)
    x5 = sizefilter(x1, x2)
    x6 = order(x5, leftmost)
    x7 = apply(color, x6)
    x8 = apply(x4, x7)
    x9 = merge_t(x8)
    O = dmirror_t(x9)
    return O

def solve_e9614598(S, I):
    x1 = fork(add, first, last)
    x2 = f_ofcolor(I, ONE)
    x3 = x1(x2)
    x4 = halve(x3)
    x5 = dneighbors(x4)
    x6 = insert(x4, x5)
    O = fill(I, THREE, x6)
    return O

def solve_ed36ccf7(S, I):
    O = rot270(I)
    return O

def solve_f25ffba3(S, I):
    x1 = bottomhalf(I)
    x2 = hmirror_t(x1)
    O = vconcat(x2, x1)
    return O

def solve_caa06a1f(S, I):
    x1 = shape_t(I)
    x2 = decrement(x1)
    x3 = index(I, x2)
    x4 = double(x1)
    x5 = canvas(x3, x4)
    x6 = asobject(I)
    x7 = paint(x5, x6)
    x8 = objects(x7, F, F, T)
    x9 = first_f(x8)
    x10 = shift(x9, LEFT)
    x11 = lbind(shift, x10)
    x12 = vperiod(x10)
    x13 = hperiod(x10)
    x14 = astuple(x12, x13)
    x15 = lbind(multiply, x14)
    x16 = lbind(mapply, neighbors)
    x17 = power(x16, TWO)
    x18 = neighbors(ORIGIN)
    x19 = x17(x18)
    x20 = apply(x15, x19)
    x21 = mapply(x11, x20)
    O = paint(I, x21)
    return O

def solve_1b2d62fb(S, I):
    x1 = lefthalf(I)
    x2 = replace(x1, NINE, ZERO)
    x3 = f_ofcolor(x1, ZERO)
    x4 = righthalf(I)
    x5 = f_ofcolor(x4, ZERO)
    x6 = intersection(x3, x5)
    O = fill(x2, EIGHT, x6)
    return O

def solve_6150a2bd(S, I):
    O = rot180(I)
    return O

def solve_3428a4f5(S, I):
    x1 = astuple(SIX, FIVE)
    x2 = canvas(ZERO, x1)
    x3 = tophalf(I)
    x4 = f_ofcolor(x3, TWO)
    x5 = bottomhalf(I)
    x6 = f_ofcolor(x5, TWO)
    x7 = combine_f(x4, x6)
    x8 = intersection(x4, x6)
    x9 = difference(x7, x8)
    O = fill(x2, THREE, x9)
    return O

def solve_ce9e57f2(S, I):
    x1 = fork(connect, ulcorner, centerofmass)
    x2 = objects(I, T, F, T)
    x3 = mapply(x1, x2)
    x4 = fill(I, EIGHT, x3)
    O = switch(x4, EIGHT, TWO)
    return O

def solve_025d127b(S, I):
    x1 = objects(I, T, F, T)
    x2 = merge_f(x1)
    x3 = rbind(argmax, rightmost)
    x4 = lbind(colorfilter, x1)
    x5 = compose(x3, x4)
    x6 = apply(color, x1)
    x7 = mapply(x5, x6)
    x8 = difference(x2, x7)
    O = move(I, x8, RIGHT)
    return O

def solve_47c1f68c(S, I):
    x1 = vmirror_t(I)
    x2 = leastcolor_t(I)
    x3 = cellwise(I, x1, x2)
    x4 = hmirror_t(x3)
    x5 = cellwise(x3, x4, x2)
    x6 = compress(x5)
    x7 = objects(I, T, T, T)
    x8 = merge_f(x7)
    x9 = mostcolor_f(x8)
    O = replace(x6, x2, x9)
    return O

def solve_c9f8e694(S, I):
    x1 = height_t(I)
    x2 = astuple(x1, ONE)
    x3 = crop(I, ORIGIN, x2)
    x4 = width_t(I)
    x5 = hupscale(x3, x4)
    x6 = f_ofcolor(I, ZERO)
    O = fill(x5, ZERO, x6)
    return O

def solve_6cdd2623(S, I):
    x1 = fgpartition(I)
    x2 = merge_f(x1)
    x3 = cover(I, x2)
    x4 = leastcolor_t(I)
    x5 = f_ofcolor(I, x4)
    x6 = prapply(connect, x5, x5)
    x7 = fork(either, hline_i, vline_i)
    x8 = box(x2)
    x9 = rbind(difference, x8)
    x10 = chain(positive, size, x9)
    x11 = fork(both, x7, x10)
    x12 = mfilter_f(x6, x11)
    O = fill(x3, x4, x12)
    return O

def solve_3af2c5a8(S, I):
    x1 = vmirror_t(I)
    x2 = hconcat(I, x1)
    x3 = hmirror_t(x2)
    O = vconcat(x2, x3)
    return O

def solve_5c2c9af4(S, I):
    x1 = leastcolor_t(I)
    x2 = f_ofcolor(I, x1)
    x3 = center(x2)
    x4 = ulcorner(x2)
    x5 = subtract(x3, x4)
    x6 = lbind(multiply, x5)
    x7 = interval(ZERO, NINE, ONE)
    x8 = apply(x6, x7)
    x9 = multiply(NEG_ONE, NINE)
    x10 = interval(ZERO, x9, NEG_ONE)
    x11 = apply(x6, x10)
    x12 = pair(x8, x11)
    x13 = mapply(box, x12)
    x14 = shift(x13, x3)
    O = fill(I, x1, x14)
    return O

def solve_b190f7f5(S, I):
    x1 = portrait_t(I)
    x2 = branch(x1, vsplit, hsplit)
    x3 = x2(I, TWO)
    x4 = argmax_t(x3, numcolors_t)
    x5 = width_t(x4)
    x6 = upscale_t(x4, x5)
    x7 = rbind(repeat, x5)
    x8 = chain(dmirror_t, merge, x7)
    x9 = argmin_t(x3, numcolors_t)
    x10 = x8(x9)
    x11 = x8(x10)
    x12 = f_ofcolor(x11, ZERO)
    O = fill(x6, ZERO, x12)
    return O

def solve_d4469b4b(S, I):
    x1 = canvas(ZERO, THREE_BY_THREE)
    x2 = fork(combine, vfrontier, hfrontier)
    x3 = palette_t(I)
    x4 = other_f(x3, ZERO)
    x5 = equality(x4, TWO)
    x6 = equality(x4, ONE)
    x7 = branch(x6, UNITY, TWO_BY_TWO)
    x8 = branch(x5, RIGHT, x7)
    x9 = x2(x8)
    O = fill(x1, FIVE, x9)
    return O

def solve_913fb3ed(S, I):
    x1 = f_ofcolor(I, THREE)
    x2 = mapply(neighbors, x1)
    x3 = fill(I, SIX, x2)
    x4 = f_ofcolor(I, EIGHT)
    x5 = mapply(neighbors, x4)
    x6 = fill(x3, FOUR, x5)
    x7 = f_ofcolor(I, TWO)
    x8 = mapply(neighbors, x7)
    O = fill(x6, ONE, x8)
    return O

def solve_d89b689b(S, I):
    x1 = objects(I, T, F, T)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = f_ofcolor(I, EIGHT)
    x6 = apply(initset, x5)
    x7 = lbind(argmin, x6)
    x8 = lbind(rbind, manhattan)
    x9 = compose(x7, x8)
    x10 = fork(recolor_i, color, x9)
    x11 = mapply(x10, x2)
    O = paint(x4, x11)
    return O

def solve_d56f2372(S, I):
    x1 = rbind(subgrid, I)
    x2 = objects(I, T, T, T)
    x3 = totuple(x2)
    x4 = apply(x1, x3)
    x5 = apply(vmirror_t, x4)
    x6 = papply(equality, x4, x5)
    x7 = pair(x4, x6)
    x8 = extract(x7, last)
    O = first_t(x8)
    return O

def solve_673ef223(S, I):
    x1 = replace(I, EIGHT, FOUR)
    x2 = objects(I, T, F, T)
    x3 = argmin_f(x2, uppermost)
    x4 = leftmost(x3)
    x5 = equality(x4, ZERO)
    x6 = branch(x5, LEFT, RIGHT)
    x7 = rbind(shoot, x6)
    x8 = f_ofcolor(I, EIGHT)
    x9 = mapply(x7, x8)
    x10 = underfill(x1, EIGHT, x9)
    x11 = fork(subtract, maximum, minimum)
    x12 = colorfilter(x2, TWO)
    x13 = apply(uppermost, x12)
    x14 = x11(x13)
    x15 = toivec(x14)
    x16 = shift(x8, x15)
    x17 = mapply(hfrontier, x16)
    O = underfill(x10, EIGHT, x17)
    return O

def solve_10fcaaa3(S, I):
    x1 = hconcat(I, I)
    x2 = vconcat(x1, x1)
    x3 = leastcolor_t(I)
    x4 = f_ofcolor(x2, x3)
    x5 = mapply(ineighbors, x4)
    O = underfill(x2, EIGHT, x5)
    return O

def solve_d6ad076f(S, I):
    x1 = objects(I, T, F, T)
    x2 = argmin_f(x1, size)
    x3 = argmax_f(x1, size)
    x4 = vmatching(x2, x3)
    x5 = branch(x4, DOWN, RIGHT)
    x6 = branch(x4, uppermost, leftmost)
    x7 = valmax_f(x1, x6)
    x8 = x6(x2)
    x9 = equality(x7, x8)
    x10 = branch(x9, NEG_ONE, ONE)
    x11 = multiply(x5, x10)
    x12 = rbind(shoot, x11)
    x13 = inbox(x2)
    x14 = mapply(x12, x13)
    x15 = underfill(I, EIGHT, x14)
    x16 = objects(x15, T, F, T)
    x17 = colorfilter(x16, EIGHT)
    x18 = rbind(bordering, I)
    x19 = mfilter_f(x17, x18)
    O = cover(x15, x19)
    return O

def solve_5117e062(S, I):
    x1 = objects(I, F, T, T)
    x2 = matcher(numcolors_f, TWO)
    x3 = extract(x1, x2)
    x4 = subgrid(x3, I)
    x5 = mostcolor_f(x3)
    O = replace(x4, EIGHT, x5)
    return O

def solve_8d5021e8(S, I):
    x1 = vmirror_t(I)
    x2 = hconcat(x1, I)
    x3 = hmirror_t(x2)
    x4 = vconcat(x2, x3)
    x5 = vconcat(x4, x2)
    O = hmirror_t(x5)
    return O

def solve_41e4d17e(S, I):
    x1 = fork(combine, vfrontier, hfrontier)
    x2 = compose(x1, center)
    x3 = objects(I, T, F, T)
    x4 = mapply(x2, x3)
    O = underfill(I, SIX, x4)
    return O

def solve_6aa20dc0(S, I):
    x1 = lbind(lbind, shift)
    x2 = lbind(occurrences, I)
    x3 = lbind(matcher, first)
    x4 = compose(x3, mostcolor_f)
    x5 = fork(sfilter, identity, x4)
    x6 = fork(difference, identity, x5)
    x7 = compose(x2, x6)
    x8 = fork(mapply, x1, x7)
    x9 = fork(compose, first, last)
    x10 = initset(identity)
    x11 = insert(vmirror_f, x10)
    x12 = insert(hmirror_f, x11)
    x13 = insert(cmirror_f, x12)
    x14 = insert(dmirror_f, x13)
    x15 = lbind(rbind, upscale_f)
    x16 = interval(ONE, FOUR, ONE)
    x17 = apply(x15, x16)
    x18 = product(x14, x17)
    x19 = apply(x9, x18)
    x20 = objects(I, F, T, T)
    x21 = argmax_f(x20, numcolors_f)
    x22 = normalize(x21)
    x23 = rapply_f(x19, x22)
    x24 = mapply(x8, x23)
    O = paint(I, x24)
    return O

def solve_39a8645d(S, I):
    x1 = objects(I, T, T, T)
    x2 = argmin_f(x1, size)
    O = subgrid(x2, I)
    return O

def solve_8d510a79(S, I):
    x1 = chain(toivec, decrement, double)
    x2 = f_ofcolor(I, FIVE)
    x3 = uppermost(x2)
    x4 = lbind(greater, x3)
    x5 = compose(x4, first)
    x6 = compose(x1, x5)
    x7 = fork(shoot, identity, x6)
    x8 = lbind(matcher, x5)
    x9 = compose(x8, x5)
    x10 = fork(sfilter, x7, x9)
    x11 = f_ofcolor(I, TWO)
    x12 = mapply(x10, x11)
    x13 = underfill(I, TWO, x12)
    x14 = chain(invert, x1, x5)
    x15 = fork(shoot, identity, x14)
    x16 = f_ofcolor(I, ONE)
    x17 = mapply(x15, x16)
    O = fill(x13, ONE, x17)
    return O

def solve_234bbc79(S, I):
    x1 = compose(first, last)
    x2 = lbind(add, RIGHT)
    x3 = compose(last, last)
    x4 = lbind(matcher, x3)
    x5 = compose(x4, rightmost)
    x6 = fork(sfilter, identity, x5)
    x7 = compose(dneighbors, last)
    x8 = rbind(chain, x7)
    x9 = lbind(x8, size)
    x10 = lbind(rbind, intersection)
    x11 = chain(x9, x10, toindices)
    x12 = fork(argmin, x6, x11)
    x13 = compose(last, x12)
    x14 = compose(x13, first)
    x15 = compose(x4, leftmost)
    x16 = fork(sfilter, identity, x15)
    x17 = fork(argmin, x16, x11)
    x18 = compose(last, x17)
    x19 = chain(x18, first, last)
    x20 = fork(subtract, x14, x19)
    x21 = compose(x2, x20)
    x22 = fork(shift, x1, x21)
    x23 = fork(combine, first, x22)
    x24 = fork(remove, x1, last)
    x25 = fork(astuple, x23, x24)
    x26 = objects(I, F, F, T)
    x27 = size_f(x26)
    x28 = power(x25, x27)
    x29 = astuple(ZERO, DOWN_LEFT)
    x30 = initset(x29)
    x31 = rbind(other, FIVE)
    x32 = compose(x31, palette_f)
    x33 = fork(recolor_o, x32, identity)
    x34 = apply(x33, x26)
    x35 = order(x34, leftmost)
    x36 = astuple(x30, x35)
    x37 = x28(x36)
    x38 = first(x37)
    x39 = width_f(x38)
    x40 = decrement(x39)
    x41 = astuple(THREE, x40)
    x42 = canvas(ZERO, x41)
    O = paint(x42, x38)
    return O

def solve_b230c067(S, I):
    x1 = replace(I, EIGHT, ONE)
    x2 = objects(I, T, T, T)
    x3 = totuple(x2)
    x4 = apply(normalize, x3)
    x5 = leastcommon_t(x4)
    x6 = matcher(normalize, x5)
    x7 = extract(x2, x6)
    O = fill(x1, TWO, x7)
    return O

def solve_ce602527(S, I):
    x1 = vmirror_t(I)
    x2 = fgpartition(x1)
    x3 = order(x2, size)
    x4 = last_t(x3)
    x5 = remove_f(x4, x3)
    x6 = compose(toindices, normalize)
    x7 = x6(x4)
    x8 = rbind(intersection, x7)
    x9 = rbind(upscale_f, TWO)
    x10 = chain(toindices, x9, normalize)
    x11 = chain(size, x8, x10)
    x12 = argmax_t(x5, x11)
    x13 = subgrid(x12, x1)
    O = vmirror_t(x13)
    return O

def solve_aba27056(S, I):
    x1 = objects(I, T, F, T)
    x2 = mapply(toindices, x1)
    x3 = delta(x2)
    x4 = fill(I, FOUR, x3)
    x5 = box(x2)
    x6 = difference(x5, x2)
    x7 = lbind(shift, x6)
    x8 = position(x3, x6)
    x9 = lbind(multiply, x8)
    x10 = interval(ZERO, NINE, ONE)
    x11 = apply(x9, x10)
    x12 = mapply(x7, x11)
    x13 = fill(x4, FOUR, x12)
    x14 = fork(subtract, last, first)
    x15 = fork(shoot, first, x14)
    x16 = corners(x6)
    x17 = f_ofcolor(x13, ZERO)
    x18 = rbind(colorcount_f, ZERO)
    x19 = rbind(toobject, x13)
    x20 = chain(x18, x19, dneighbors)
    x21 = matcher(x20, TWO)
    x22 = sfilter_f(x17, x21)
    x23 = rbind(adjacent, x2)
    x24 = rbind(adjacent, x12)
    x25 = fork(both, x23, x24)
    x26 = compose(x25, initset)
    x27 = sfilter_f(x22, x26)
    x28 = product(x16, x27)
    x29 = mapply(x15, x28)
    O = fill(x13, FOUR, x29)
    return O

def solve_d22278a0(S, I):
    x1 = asindices(I)
    x2 = lbind(sfilter, x1)
    x3 = fork(multiply, sign, identity)
    x4 = lbind(apply, x3)
    x5 = chain(even, maximum, x4)
    x6 = compose(center, last)
    x7 = fork(subtract, first, x6)
    x8 = compose(x5, x7)
    x9 = lbind(compose, x8)
    x10 = lbind(rbind, astuple)
    x11 = chain(x2, x9, x10)
    x12 = objects(I, T, F, T)
    x13 = lbind(argmin, x12)
    x14 = fork(add, first, last)
    x15 = chain(x14, x4, x7)
    x16 = lbind(compose, x15)
    x17 = lbind(lbind, astuple)
    x18 = compose(x16, x17)
    x19 = compose(x13, x18)
    x20 = rbind(compose, x19)
    x21 = lbind(rbind, equality)
    x22 = chain(x2, x20, x21)
    x23 = fork(intersection, x11, x22)
    x24 = lbind(fork, greater)
    x25 = rbind(compose, x18)
    x26 = lbind(lbind, valmin)
    x27 = rbind(remove, x12)
    x28 = chain(x25, x26, x27)
    x29 = compose(x16, x10)
    x30 = fork(x24, x28, x29)
    x31 = compose(x2, x30)
    x32 = fork(intersection, x23, x31)
    x33 = fork(recolor_i, color, x32)
    x34 = mapply(x33, x12)
    O = paint(I, x34)
    return O

def solve_e6721834(S, I):
    x1 = portrait_t(I)
    x2 = branch(x1, vsplit, hsplit)
    x3 = x2(I, TWO)
    x4 = order(x3, numcolors_t)
    x5 = first(x4)
    x6 = lbind(occurrences, x5)
    x7 = last_t(x4)
    x8 = objects(x7, F, F, T)
    x9 = merge_f(x8)
    x10 = mostcolor_f(x9)
    x11 = matcher(first, x10)
    x12 = compose(flip, x11)
    x13 = rbind(sfilter, x12)
    x14 = chain(first, x6, x13)
    x15 = compose(ulcorner, x13)
    x16 = fork(subtract, x14, x15)
    x17 = fork(shift, identity, x16)
    x18 = compose(x6, x13)
    x19 = chain(positive, size, x18)
    x20 = sfilter_f(x8, x19)
    x21 = apply(x17, x20)
    x22 = compose(decrement, width_f)
    x23 = chain(positive, decrement, x22)
    x24 = mfilter_f(x21, x23)
    O = paint(x5, x24)
    return O

def solve_6855a6e4(S, I):
    x1 = fgpartition(I)
    x2 = colorfilter(x1, TWO)
    x3 = first(x2)
    x4 = portrait_f(x3)
    x5 = rot90(I)
    x6 = branch(x4, I, x5)
    x7 = objects(x6, T, F, T)
    x8 = colorfilter(x7, FIVE)
    x9 = merge_f(x8)
    x10 = cover(x6, x9)
    x11 = compose(first, center)
    x12 = apply(center, x8)
    x13 = valmin_f(x12, first)
    x14 = matcher(x11, x13)
    x15 = extract(x8, x14)
    x16 = subgrid(x15, x6)
    x17 = hmirror_t(x16)
    x18 = f_ofcolor(x17, FIVE)
    x19 = recolor_i(FIVE, x18)
    x20 = ulcorner(x15)
    x21 = height_f(x19)
    x22 = add(THREE, x21)
    x23 = toivec(x22)
    x24 = add(x20, x23)
    x25 = shift(x19, x24)
    x26 = paint(x10, x25)
    x27 = compose(flip, x14)
    x28 = extract(x8, x27)
    x29 = subgrid(x28, x6)
    x30 = hmirror_t(x29)
    x31 = f_ofcolor(x30, FIVE)
    x32 = recolor_i(FIVE, x31)
    x33 = ulcorner(x28)
    x34 = height_f(x32)
    x35 = add(THREE, x34)
    x36 = toivec(x35)
    x37 = subtract(x33, x36)
    x38 = shift(x32, x37)
    x39 = paint(x26, x38)
    x40 = rot270(x39)
    O = branch(x4, x39, x40)
    return O

def solve_00d62c1b(S, I):
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, ZERO)
    x3 = rbind(bordering, I)
    x4 = compose(flip, x3)
    x5 = mfilter_f(x2, x4)
    O = fill(I, FOUR, x5)
    return O

def solve_b9b7f026(S, I):
    x1 = objects(I, T, F, F)
    x2 = argmin_f(x1, size)
    x3 = remove_f(x2, x1)
    x4 = rbind(adjacent, x2)
    x5 = extract(x3, x4)
    x6 = color(x5)
    O = canvas(x6, UNITY)
    return O

def solve_e8593010(S, I):
    x1 = objects(I, T, F, T)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    x4 = fill(I, THREE, x3)
    x5 = sizefilter(x1, TWO)
    x6 = merge_f(x5)
    x7 = fill(x4, TWO, x6)
    O = replace(x7, ZERO, ONE)
    return O

def solve_d017b73f(S, I):
    x1 = compose(first, last)
    x2 = lbind(add, RIGHT)
    x3 = compose(last, last)
    x4 = lbind(matcher, x3)
    x5 = compose(x4, rightmost)
    x6 = fork(sfilter, identity, x5)
    x7 = compose(dneighbors, last)
    x8 = rbind(chain, x7)
    x9 = lbind(x8, size)
    x10 = lbind(rbind, intersection)
    x11 = chain(x9, x10, toindices)
    x12 = fork(argmin, x6, x11)
    x13 = compose(last, x12)
    x14 = compose(x13, first)
    x15 = compose(x4, leftmost)
    x16 = fork(sfilter, identity, x15)
    x17 = fork(argmin, x16, x11)
    x18 = compose(last, x17)
    x19 = chain(x18, first, last)
    x20 = fork(subtract, x14, x19)
    x21 = compose(x2, x20)
    x22 = fork(shift, x1, x21)
    x23 = fork(combine, first, x22)
    x24 = fork(remove, x1, last)
    x25 = fork(astuple, x23, x24)
    x26 = objects(I, F, F, T)
    x27 = size_f(x26)
    x28 = power(x25, x27)
    x29 = astuple(ZERO, DOWN_LEFT)
    x30 = initset(x29)
    x31 = rbind(other, FIVE)
    x32 = compose(x31, palette_f)
    x33 = fork(recolor_o, x32, identity)
    x34 = apply(x33, x26)
    x35 = order(x34, leftmost)
    x36 = astuple(x30, x35)
    x37 = x28(x36)
    x38 = first(x37)
    x39 = width_f(x38)
    x40 = decrement(x39)
    x41 = astuple(THREE, x40)
    x42 = canvas(ZERO, x41)
    O = paint(x42, x38)
    return O

def solve_0e206a2e(S, I):
    x1 = lbind(lbind, shift)
    x2 = compose(x1, normalize)
    x3 = lbind(rbind, subtract)
    x4 = compose(x3, ulcorner)
    x5 = palette_t(I)
    x6 = remove(ZERO, x5)
    x7 = lbind(colorcount_t, I)
    x8 = argmax_f(x6, x7)
    x9 = remove(x8, x6)
    x10 = rbind(contained, x9)
    x11 = compose(x10, first)
    x12 = rbind(sfilter, x11)
    x13 = chain(x4, x12, normalize)
    x14 = lbind(occurrences, I)
    x15 = chain(x14, x12, normalize)
    x16 = fork(apply, x13, x15)
    x17 = fork(mapply, x2, x16)
    x18 = astuple(cmirror_f, dmirror_f)
    x19 = astuple(hmirror_f, vmirror_f)
    x20 = combine(x18, x19)
    x21 = fork(compose, first, last)
    x22 = product(x20, x20)
    x23 = apply(x21, x22)
    x24 = totuple(x23)
    x25 = combine(x20, x24)
    x26 = lbind(rapply, x25)
    x27 = objects(I, F, F, T)
    x28 = rbind(greater, ONE)
    x29 = compose(x28, numcolors_f)
    x30 = sfilter(x27, x29)
    x31 = mapply(x26, x30)
    x32 = mapply(x17, x31)
    x33 = paint(I, x32)
    x34 = merge_f(x30)
    O = cover(x33, x34)
    return O

def solve_1f876c06(S, I):
    x1 = compose(last, first)
    x2 = power(last, TWO)
    x3 = fork(connect, x1, x2)
    x4 = fork(recolor_i, color, x3)
    x5 = fgpartition(I)
    x6 = mapply(x4, x5)
    O = paint(I, x6)
    return O

def solve_4c5c2cf0(S, I):
    x1 = objects(I, F, T, T)
    x2 = first_f(x1)
    x3 = subgrid(x2, I)
    x4 = hmirror_t(x3)
    x5 = objects(x4, F, T, T)
    x6 = first_f(x5)
    x7 = objects(I, T, T, T)
    x8 = fork(equality, identity, rot90)
    x9 = rbind(subgrid, I)
    x10 = compose(x8, x9)
    x11 = extract(x7, x10)
    x12 = center(x11)
    x13 = objects(x4, T, T, T)
    x14 = rbind(subgrid, x4)
    x15 = compose(x8, x14)
    x16 = extract(x13, x15)
    x17 = center(x16)
    x18 = subtract(x12, x17)
    x19 = shift(x6, x18)
    x20 = paint(I, x19)
    x21 = objects(x20, F, T, T)
    x22 = first_f(x21)
    x23 = subgrid(x22, x20)
    x24 = vmirror_t(x23)
    x25 = objects(x24, F, T, T)
    x26 = first_f(x25)
    x27 = objects(x24, T, T, T)
    x28 = color(x11)
    x29 = matcher(color, x28)
    x30 = extract(x27, x29)
    x31 = center(x30)
    x32 = subtract(x12, x31)
    x33 = shift(x26, x32)
    O = paint(x20, x33)
    return O

def solve_d5d6de2d(S, I):
    x1 = replace(I, TWO, ZERO)
    x2 = compose(backdrop, inbox)
    x3 = objects(I, T, F, T)
    x4 = sfilter_f(x3, square_f)
    x5 = difference(x3, x4)
    x6 = mapply(x2, x5)
    O = fill(x1, THREE, x6)
    return O

def solve_46442a0e(S, I):
    x1 = rot90(I)
    x2 = hconcat(I, x1)
    x3 = rot270(I)
    x4 = rot180(I)
    x5 = hconcat(x3, x4)
    O = vconcat(x2, x5)
    return O

def solve_29c11459(S, I):
    x1 = compose(hfrontier, center)
    x2 = fork(recolor_i, color, x1)
    x3 = righthalf(I)
    x4 = objects(x3, T, F, T)
    x5 = mapply(x2, x4)
    x6 = paint(I, x5)
    x7 = lefthalf(I)
    x8 = objects(x7, T, F, T)
    x9 = mapply(x2, x8)
    x10 = paint(x7, x9)
    x11 = objects(x10, T, F, T)
    x12 = merge_f(x11)
    x13 = paint(x6, x12)
    x14 = apply(urcorner, x11)
    x15 = shift(x14, RIGHT)
    O = fill(x13, FIVE, x15)
    return O

def solve_508bd3b6(S, I):
    x1 = objects(I, T, T, T)
    x2 = argmin_f(x1, size)
    x3 = ulcorner(x2)
    x4 = index(I, x3)
    x5 = equality(x4, EIGHT)
    x6 = urcorner(x2)
    x7 = branch(x5, x3, x6)
    x8 = branch(x5, UNITY, DOWN_LEFT)
    x9 = width_t(I)
    x10 = multiply(x8, x9)
    x11 = double(x10)
    x12 = add(x7, x11)
    x13 = subtract(x7, x11)
    x14 = connect(x12, x13)
    x15 = fill(I, THREE, x14)
    x16 = argmax_f(x1, size)
    x17 = paint(x15, x16)
    x18 = objects(x17, T, F, T)
    x19 = rbind(adjacent, x16)
    x20 = extract(x18, x19)
    x21 = first_f(x20)
    x22 = last_t(x21)
    x23 = flip(x5)
    x24 = branch(x23, UNITY, DOWN_LEFT)
    x25 = multiply(x24, x9)
    x26 = double(x25)
    x27 = add(x22, x26)
    x28 = subtract(x22, x26)
    x29 = connect(x27, x28)
    x30 = fill(x17, THREE, x29)
    x31 = paint(x30, x2)
    O = paint(x31, x16)
    return O

def solve_4093f84a(S, I):
    x1 = f_ofcolor(I, FIVE)
    x2 = portrait_f(x1)
    x3 = branch(x2, identity, dmirror_t)
    x4 = rbind(order, identity)
    x5 = leastcolor_t(I)
    x6 = replace(I, x5, FIVE)
    x7 = x3(x6)
    x8 = lefthalf(x7)
    x9 = apply(x4, x8)
    x10 = rbind(order, invert)
    x11 = righthalf(x7)
    x12 = apply(x10, x11)
    x13 = hconcat(x9, x12)
    O = x3(x13)
    return O

def solve_29623171(S, I):
    x1 = leastcolor_t(I)
    x2 = rbind(interval, ONE)
    x3 = rbind(add, THREE)
    x4 = fork(x2, identity, x3)
    x5 = compose(x4, first)
    x6 = compose(x4, last)
    x7 = fork(product, x5, x6)
    x8 = interval(ZERO, NINE, FOUR)
    x9 = product(x8, x8)
    x10 = apply(x7, x9)
    x11 = rbind(colorcount_f, x1)
    x12 = rbind(toobject, I)
    x13 = compose(x11, x12)
    x14 = valmax_f(x10, x13)
    x15 = matcher(x13, x14)
    x16 = mfilter_f(x10, x15)
    x17 = fill(I, x1, x16)
    x18 = compose(flip, x15)
    x19 = mfilter_f(x10, x18)
    O = fill(x17, ZERO, x19)
    return O

def solve_e26a3af2(S, I):
    x1 = compose(size, dedupe)
    x2 = rot90(I)
    x3 = apply(mostcommon, x2)
    x4 = x1(x3)
    x5 = apply(mostcommon, I)
    x6 = x1(x5)
    x7 = greater(x4, x6)
    x8 = branch(x7, vupscale, hupscale)
    x9 = repeat(x3, ONE)
    x10 = repeat(x5, ONE)
    x11 = rot90(x10)
    x12 = branch(x7, x9, x11)
    x13 = branch(x7, height_t, width_t)
    x14 = x13(I)
    O = x8(x12, x14)
    return O

def solve_2281f1f4(S, I):
    x1 = f_ofcolor(I, FIVE)
    x2 = urcorner(x1)
    x3 = power(first, TWO)
    x4 = power(last, TWO)
    x5 = fork(astuple, x3, x4)
    x6 = product(x1, x1)
    x7 = apply(x5, x6)
    x8 = remove_t(x2, x7)
    O = underfill(I, TWO, x8)
    return O

def solve_007bbfb7(S, I):
    x1 = hupscale(I, THREE)
    x2 = vupscale(x1, THREE)
    x3 = hconcat(I, I)
    x4 = hconcat(x3, I)
    x5 = vconcat(x4, x4)
    x6 = vconcat(x5, x4)
    O = cellwise(x2, x6, ZERO)
    return O

def solve_760b3cac(S, I):
    x1 = f_ofcolor(I, EIGHT)
    x2 = vmirror_f(x1)
    x3 = f_ofcolor(I, FOUR)
    x4 = ulcorner(x3)
    x5 = index(I, x4)
    x6 = equality(x5, FOUR)
    x7 = branch(x6, NEG_ONE, ONE)
    x8 = multiply(x7, THREE)
    x9 = tojvec(x8)
    x10 = shift(x2, x9)
    O = fill(I, EIGHT, x10)
    return O

def solve_a699fb00(S, I):
    x1 = f_ofcolor(I, ONE)
    x2 = shift(x1, RIGHT)
    x3 = shift(x1, LEFT)
    x4 = intersection(x2, x3)
    O = fill(I, TWO, x4)
    return O

def solve_890034e9(S, I):
    x1 = leastcolor_t(I)
    x2 = f_ofcolor(I, x1)
    x3 = normalize(x2)
    x4 = shift(x3, NEG_UNITY)
    x5 = lbind(shift, x4)
    x6 = inbox(x2)
    x7 = recolor_i(ZERO, x6)
    x8 = occurrences(I, x7)
    x9 = mapply(x5, x8)
    O = fill(I, x1, x9)
    return O

def solve_ce4f8723(S, I):
    x1 = astuple(FOUR, FOUR)
    x2 = canvas(THREE, x1)
    x3 = tophalf(I)
    x4 = f_ofcolor(x3, ZERO)
    x5 = bottomhalf(I)
    x6 = f_ofcolor(x5, ZERO)
    x7 = intersection(x4, x6)
    O = fill(x2, ZERO, x7)
    return O

def solve_3bdb4ada(S, I):
    x1 = compose(last, first)
    x2 = power(last, TWO)
    x3 = fork(subtract, x1, x2)
    x4 = compose(even, x3)
    x5 = lbind(compose, x4)
    x6 = lbind(rbind, astuple)
    x7 = compose(x5, x6)
    x8 = fork(sfilter, first, x7)
    x9 = compose(increment, ulcorner)
    x10 = objects(I, T, F, T)
    x11 = totuple(x10)
    x12 = apply(x9, x11)
    x13 = compose(decrement, lrcorner)
    x14 = apply(x13, x11)
    x15 = papply(connect, x12, x14)
    x16 = apply(last, x12)
    x17 = pair(x15, x16)
    x18 = mapply(x8, x17)
    O = fill(I, ZERO, x18)
    return O

def solve_2c608aff(S, I):
    x1 = leastcolor_t(I)
    x2 = objects(I, T, F, T)
    x3 = argmax_f(x2, size)
    x4 = toindices(x3)
    x5 = f_ofcolor(I, x1)
    x6 = prapply(connect, x4, x5)
    x7 = fork(either, vline_i, hline_i)
    x8 = mfilter_f(x6, x7)
    O = underfill(I, x1, x8)
    return O

def solve_a79310a0(S, I):
    x1 = objects(I, T, F, T)
    x2 = first_f(x1)
    x3 = move(I, x2, DOWN)
    O = replace(x3, EIGHT, TWO)
    return O

def solve_f76d97a5(S, I):
    x1 = palette_t(I)
    x2 = first_f(x1)
    x3 = last_f(x1)
    x4 = switch(I, x2, x3)
    O = replace(x4, FIVE, ZERO)
    return O

def solve_963e52fc(S, I):
    x1 = asobject(I)
    x2 = ulcorner(x1)
    x3 = height_f(x1)
    x4 = hperiod(x1)
    x5 = astuple(x3, x4)
    x6 = crop(I, x2, x5)
    x7 = rot90(x6)
    x8 = width_t(I)
    x9 = double(x8)
    x10 = divide(x9, x4)
    x11 = increment(x10)
    x12 = repeat(x7, x11)
    x13 = merge_t(x12)
    x14 = rot270(x13)
    x15 = astuple(x3, x9)
    O = crop(x14, ORIGIN, x15)
    return O

def solve_c7d4e6ad(S, I):
    x1 = height_t(I)
    x2 = astuple(x1, ONE)
    x3 = crop(I, ORIGIN, x2)
    x4 = width_t(I)
    x5 = hupscale(x3, x4)
    x6 = f_ofcolor(I, ZERO)
    O = fill(x5, ZERO, x6)
    return O

def solve_4c4377d9(S, I):
    x1 = hmirror_t(I)
    O = vconcat(x1, I)
    return O

def solve_d4a91cb9(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = first(x1)
    x3 = first(x2)
    x4 = f_ofcolor(I, EIGHT)
    x5 = first(x4)
    x6 = last_t(x5)
    x7 = astuple(x3, x6)
    x8 = connect(x7, x5)
    x9 = connect(x7, x2)
    x10 = combine_f(x8, x9)
    O = underfill(I, FOUR, x10)
    return O

def solve_05f2a901(S, I):
    x1 = objects(I, T, F, T)
    x2 = colorfilter(x1, TWO)
    x3 = first_f(x2)
    x4 = colorfilter(x1, EIGHT)
    x5 = first_f(x4)
    x6 = gravitate(x3, x5)
    O = move(I, x3, x6)
    return O

def solve_3bd67248(S, I):
    x1 = height_t(I)
    x2 = decrement(x1)
    x3 = decrement(x2)
    x4 = astuple(x3, ONE)
    x5 = shoot(x4, UP_RIGHT)
    x6 = fill(I, TWO, x5)
    x7 = astuple(x2, ONE)
    x8 = shoot(x7, RIGHT)
    O = fill(x6, FOUR, x8)
    return O

def solve_d511f180(S, I):
    O = switch(I, FIVE, EIGHT)
    return O

def solve_e8dc4411(S, I):
    x1 = leastcolor_t(I)
    x2 = f_ofcolor(I, ZERO)
    x3 = lbind(shift, x2)
    x4 = fork(connect, ulcorner, lrcorner)
    x5 = x4(x2)
    x6 = intersection(x2, x5)
    x7 = equality(x5, x6)
    x8 = fork(subtract, identity, crement)
    x9 = fork(add, identity, x8)
    x10 = branch(x7, identity, x9)
    x11 = shape_f(x2)
    x12 = f_ofcolor(I, x1)
    x13 = position(x2, x12)
    x14 = multiply(x11, x13)
    x15 = apply(x10, x14)
    x16 = lbind(multiply, x15)
    x17 = interval(ONE, FIVE, ONE)
    x18 = apply(x16, x17)
    x19 = mapply(x3, x18)
    O = fill(I, x1, x19)
    return O

def solve_beb8660c(S, I):
    x1 = shape_t(I)
    x2 = canvas(ZERO, x1)
    x3 = objects(I, T, F, T)
    x4 = compose(invert, size)
    x5 = order(x3, x4)
    x6 = apply(normalize, x5)
    x7 = size(x6)
    x8 = interval(ZERO, x7, ONE)
    x9 = apply(toivec, x8)
    x10 = mpapply(shift, x6, x9)
    x11 = paint(x2, x10)
    O = rot180(x11)
    return O

def solve_75b8110e(S, I):
    x1 = lefthalf(I)
    x2 = tophalf(x1)
    x3 = rbind(f_ofcolor, ZERO)
    x4 = fork(difference, asindices, x3)
    x5 = fork(toobject, x4, identity)
    x6 = righthalf(I)
    x7 = bottomhalf(x6)
    x8 = x5(x7)
    x9 = paint(x2, x8)
    x10 = bottomhalf(x1)
    x11 = x5(x10)
    x12 = paint(x9, x11)
    x13 = tophalf(x6)
    x14 = x5(x13)
    O = paint(x12, x14)
    return O

def solve_7fe24cdd(S, I):
    x1 = rot90(I)
    x2 = hconcat(I, x1)
    x3 = rot270(I)
    x4 = rot180(I)
    x5 = hconcat(x3, x4)
    O = vconcat(x2, x5)
    return O

def solve_469497ad(S, I):
    x1 = numcolors_t(I)
    x2 = decrement(x1)
    x3 = upscale_t(I, x2)
    x4 = objects(x3, F, F, T)
    x5 = argmin_f(x4, size)
    x6 = ulcorner(x5)
    x7 = shoot(x6, NEG_UNITY)
    x8 = shoot(x6, UNITY)
    x9 = combine(x7, x8)
    x10 = llcorner(x5)
    x11 = shoot(x10, DOWN_LEFT)
    x12 = shoot(x10, UP_RIGHT)
    x13 = combine(x11, x12)
    x14 = combine(x9, x13)
    x15 = underfill(x3, TWO, x14)
    x16 = objects(x15, T, F, T)
    x17 = argmax_f(x16, lrcorner)
    O = paint(x15, x17)
    return O

def solve_c1d99e64(S, I):
    x1 = frontiers(I)
    x2 = merge_f(x1)
    O = fill(I, TWO, x2)
    return O

def solve_810b9b61(S, I):
    x1 = objects(I, T, T, T)
    x2 = apply(toindices, x1)
    x3 = fork(either, vline_i, hline_i)
    x4 = sfilter_f(x2, x3)
    x5 = difference(x2, x4)
    x6 = fork(equality, identity, box)
    x7 = mfilter_f(x5, x6)
    O = fill(I, THREE, x7)
    return O

def solve_11852cab(S, I):
    x1 = objects(I, T, T, T)
    x2 = merge_f(x1)
    x3 = hmirror_f(x2)
    x4 = paint(I, x3)
    x5 = vmirror_f(x2)
    x6 = paint(x4, x5)
    x7 = dmirror_f(x2)
    x8 = paint(x6, x7)
    x9 = cmirror_f(x2)
    O = paint(x8, x9)
    return O

def solve_0ca9ddb6(S, I):
    x1 = f_ofcolor(I, ONE)
    x2 = mapply(dneighbors, x1)
    x3 = fill(I, SEVEN, x2)
    x4 = f_ofcolor(I, TWO)
    x5 = mapply(ineighbors, x4)
    O = fill(x3, FOUR, x5)
    return O

def solve_363442ee(S, I):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    x2 = asobject(x1)
    x3 = lbind(shift, x2)
    x4 = compose(x3, decrement)
    x5 = f_ofcolor(I, ONE)
    x6 = mapply(x4, x5)
    O = paint(I, x6)
    return O

def solve_fafffa47(S, I):
    x1 = bottomhalf(I)
    x2 = shape_t(x1)
    x3 = canvas(ZERO, x2)
    x4 = tophalf(I)
    x5 = f_ofcolor(x4, ZERO)
    x6 = f_ofcolor(x1, ZERO)
    x7 = intersection(x5, x6)
    O = fill(x3, TWO, x7)
    return O

def solve_7b6016b9(S, I):
    x1 = objects(I, T, F, F)
    x2 = rbind(bordering, I)
    x3 = compose(flip, x2)
    x4 = mfilter_f(x1, x3)
    x5 = fill(I, TWO, x4)
    O = replace(x5, ZERO, THREE)
    return O

def solve_09629e4f(S, I):
    x1 = objects(I, F, T, T)
    x2 = argmin(x1, numcolors_f)
    x3 = normalize(x2)
    x4 = upscale_f(x3, FOUR)
    x5 = paint(I, x4)
    x6 = f_ofcolor(I, FIVE)
    O = fill(x5, FIVE, x6)
    return O

def solve_c59eb873(S, I):
    O = upscale_t(I, TWO)
    return O

def solve_e179c5f4(S, I):
    x1 = f_ofcolor(I, ONE)
    x2 = first(x1)
    x3 = shoot(x2, UP_RIGHT)
    x4 = fill(I, ONE, x3)
    x5 = f_ofcolor(x4, ONE)
    x6 = urcorner(x5)
    x7 = shoot(x6, NEG_UNITY)
    x8 = fill(x4, ONE, x7)
    x9 = f_ofcolor(x8, ONE)
    x10 = ulcorner(x9)
    x11 = subgrid(x9, x8)
    x12 = height_t(x11)
    x13 = decrement(x12)
    x14 = width_t(x11)
    x15 = astuple(x13, x14)
    x16 = crop(x8, x10, x15)
    x17 = repeat(x16, NINE)
    x18 = merge(x17)
    x19 = height_t(I)
    x20 = astuple(x19, x14)
    x21 = crop(x18, ORIGIN, x20)
    x22 = hmirror_t(x21)
    O = replace(x22, ZERO, EIGHT)
    return O

def solve_6b9890af(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = subgrid(x1, I)
    x3 = objects(I, T, T, T)
    x4 = argmin_f(x3, size)
    x5 = width_t(x2)
    x6 = divide(x5, THREE)
    x7 = upscale_f(x4, x6)
    x8 = normalize(x7)
    x9 = shift(x8, UNITY)
    O = paint(x2, x9)
    return O

def solve_f15e1fac(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = portrait_f(x1)
    x3 = branch(x2, identity, dmirror_t)
    x4 = leftmost(x1)
    x5 = equality(x4, ZERO)
    x6 = branch(x5, identity, vmirror_t)
    x7 = x3(I)
    x8 = x6(x7)
    x9 = f_ofcolor(x8, EIGHT)
    x10 = uppermost(x9)
    x11 = equality(x10, ZERO)
    x12 = branch(x11, identity, hmirror_t)
    x13 = chain(x3, x6, x12)
    x14 = x12(x8)
    x15 = rbind(shoot, DOWN)
    x16 = f_ofcolor(x14, EIGHT)
    x17 = mapply(x15, x16)
    x18 = lbind(sfilter, x17)
    x19 = compose(first, last)
    x20 = chain(decrement, first, first)
    x21 = fork(greater, x19, x20)
    x22 = chain(increment, last, first)
    x23 = fork(greater, x22, x19)
    x24 = fork(both, x21, x23)
    x25 = lbind(compose, x24)
    x26 = lbind(lbind, astuple)
    x27 = chain(x18, x25, x26)
    x28 = f_ofcolor(x14, TWO)
    x29 = apply(first, x28)
    x30 = insert(ZERO, x29)
    x31 = order(x30, identity)
    x32 = height_t(x14)
    x33 = insert(x32, x29)
    x34 = apply(decrement, x33)
    x35 = order(x34, identity)
    x36 = pair(x31, x35)
    x37 = apply(x27, x36)
    x38 = size_f(x28)
    x39 = increment(x38)
    x40 = interval(ZERO, x39, ONE)
    x41 = apply(tojvec, x40)
    x42 = papply(shift, x37, x41)
    x43 = merge(x42)
    x44 = fill(x14, EIGHT, x43)
    O = x13(x44)
    return O

def solve_6455b5f5(S, I):
    x1 = objects(I, T, F, F)
    x2 = argmax_f(x1, size)
    x3 = recolor_o(ONE, x2)
    x4 = paint(I, x3)
    x5 = colorfilter(x1, ZERO)
    x6 = valmin_f(x1, size)
    x7 = sizefilter(x5, x6)
    x8 = merge_f(x7)
    O = fill(x4, EIGHT, x8)
    return O

def solve_a1570a43(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = recolor_i(TWO, x1)
    x3 = f_ofcolor(I, THREE)
    x4 = ulcorner(x3)
    x5 = ulcorner(x1)
    x6 = subtract(x4, x5)
    x7 = increment(x6)
    O = move(I, x2, x7)
    return O

def solve_48d8fb45(S, I):
    x1 = objects(I, T, T, T)
    x2 = matcher(size, ONE)
    x3 = extract(x1, x2)
    x4 = lbind(adjacent, x3)
    x5 = extract(x1, x4)
    O = subgrid(x5, I)
    return O

def solve_a5f85a15(S, I):
    x1 = interval(ONE, NINE, ONE)
    x2 = apply(double, x1)
    x3 = apply(decrement, x2)
    x4 = papply(astuple, x3, x3)
    x5 = lbind(shift, x4)
    x6 = objects(I, T, T, T)
    x7 = apply(ulcorner, x6)
    x8 = mapply(x5, x7)
    O = fill(I, FOUR, x8)
    return O

def solve_e50d258f(S, I):
    x1 = width_t(I)
    x2 = astuple(NINE, x1)
    x3 = canvas(ZERO, x2)
    x4 = vconcat(I, x3)
    x5 = objects(x4, F, F, T)
    x6 = rbind(colorcount_f, TWO)
    x7 = argmax_f(x5, x6)
    O = subgrid(x7, I)
    return O

def solve_9dfd6313(S, I):
    O = dmirror_t(I)
    return O

def solve_bdad9b1f(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = center(x1)
    x3 = hfrontier(x2)
    x4 = fill(I, TWO, x3)
    x5 = f_ofcolor(I, EIGHT)
    x6 = center(x5)
    x7 = vfrontier(x6)
    x8 = fill(x4, EIGHT, x7)
    x9 = intersection(x3, x7)
    O = fill(x8, FOUR, x9)
    return O

def solve_9edfc990(S, I):
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, ZERO)
    x3 = f_ofcolor(I, ONE)
    x4 = rbind(adjacent, x3)
    x5 = mfilter_f(x2, x4)
    x6 = recolor_o(ONE, x5)
    O = paint(I, x6)
    return O

def solve_9af7a82c(S, I):
    x1 = rbind(astuple, ONE)
    x2 = compose(x1, size)
    x3 = fork(canvas, color, x2)
    x4 = lbind(canvas, ZERO)
    x5 = objects(I, T, F, F)
    x6 = valmax_f(x5, size)
    x7 = lbind(subtract, x6)
    x8 = chain(x1, x7, size)
    x9 = compose(x4, x8)
    x10 = fork(vconcat, x3, x9)
    x11 = compose(cmirror_t, x10)
    x12 = order(x5, size)
    x13 = apply(x11, x12)
    x14 = merge_t(x13)
    O = cmirror_t(x14)
    return O

def solve_1f0c79e5(S, I):
    x1 = replace(I, TWO, ZERO)
    x2 = leastcolor_t(x1)
    x3 = f_ofcolor(I, TWO)
    x4 = f_ofcolor(x1, x2)
    x5 = combine_f(x3, x4)
    x6 = recolor_i(x2, x5)
    x7 = lbind(shift, x6)
    x8 = compose(decrement, double)
    x9 = ulcorner(x5)
    x10 = invert(x9)
    x11 = shift(x3, x10)
    x12 = apply(x8, x11)
    x13 = interval(ZERO, NINE, ONE)
    x14 = prapply(multiply, x12, x13)
    x15 = mapply(x7, x14)
    O = paint(I, x15)
    return O

def solve_a68b268e(S, I):
    x1 = bottomhalf(I)
    x2 = righthalf(x1)
    x3 = lefthalf(x1)
    x4 = f_ofcolor(x3, EIGHT)
    x5 = fill(x2, EIGHT, x4)
    x6 = tophalf(I)
    x7 = righthalf(x6)
    x8 = f_ofcolor(x7, FOUR)
    x9 = fill(x5, FOUR, x8)
    x10 = lefthalf(x6)
    x11 = f_ofcolor(x10, SEVEN)
    O = fill(x9, SEVEN, x11)
    return O

def solve_496994bd(S, I):
    x1 = height_t(I)
    x2 = halve(x1)
    x3 = width_t(I)
    x4 = astuple(x2, x3)
    x5 = crop(I, ORIGIN, x4)
    x6 = hmirror_t(x5)
    O = vconcat(x5, x6)
    return O

def solve_d037b0a7(S, I):
    x1 = rbind(shoot, DOWN)
    x2 = compose(x1, center)
    x3 = fork(recolor_i, color, x2)
    x4 = objects(I, T, F, T)
    x5 = mapply(x3, x4)
    O = paint(I, x5)
    return O

def solve_a5313dff(S, I):
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, ZERO)
    x3 = rbind(bordering, I)
    x4 = compose(flip, x3)
    x5 = mfilter_f(x2, x4)
    O = fill(I, ONE, x5)
    return O

def solve_e76a88a6(S, I):
    x1 = objects(I, F, F, T)
    x2 = argmax_f(x1, numcolors_f)
    x3 = normalize(x2)
    x4 = lbind(shift, x3)
    x5 = remove_f(x2, x1)
    x6 = apply(ulcorner, x5)
    x7 = mapply(x4, x6)
    O = paint(I, x7)
    return O

def solve_539a4f51(S, I):
    x1 = index(I, ORIGIN)
    x2 = multiply(UNITY, TEN)
    x3 = canvas(x1, x2)
    x4 = colorcount_t(I, ZERO)
    x5 = positive(x4)
    x6 = shape_t(I)
    x7 = decrement(x6)
    x8 = branch(x5, x7, x6)
    x9 = crop(I, ORIGIN, x8)
    x10 = width_t(x9)
    x11 = astuple(ONE, x10)
    x12 = crop(x9, ORIGIN, x11)
    x13 = vupscale(x12, x10)
    x14 = hconcat(x9, x13)
    x15 = dmirror_t(x13)
    x16 = hconcat(x15, x9)
    x17 = vconcat(x14, x16)
    x18 = asobject(x17)
    O = paint(x3, x18)
    return O

def solve_928ad970(S, I):
    x1 = f_ofcolor(I, FIVE)
    x2 = subgrid(x1, I)
    x3 = trim(x2)
    x4 = leastcolor_t(x3)
    x5 = inbox(x1)
    O = fill(I, x4, x5)
    return O

def solve_a740d043(S, I):
    x1 = objects(I, T, T, T)
    x2 = merge_f(x1)
    x3 = subgrid(x2, I)
    O = replace(x3, ONE, ZERO)
    return O

def solve_6d75e8bb(S, I):
    x1 = objects(I, T, F, T)
    x2 = first_f(x1)
    x3 = subgrid(x2, I)
    x4 = replace(x3, ZERO, TWO)
    x5 = asobject(x4)
    x6 = ulcorner(x2)
    x7 = shift(x5, x6)
    O = paint(I, x7)
    return O

def solve_e21d9049(S, I):
    x1 = objects(I, T, F, T)
    x2 = merge(x1)
    x3 = lbind(shift, x2)
    x4 = shape_f(x2)
    x5 = lbind(multiply, x4)
    x6 = lbind(mapply, neighbors)
    x7 = power(x6, TWO)
    x8 = neighbors(ORIGIN)
    x9 = x7(x8)
    x10 = apply(x5, x9)
    x11 = mapply(x3, x10)
    x12 = paint(I, x11)
    x13 = asindices(I)
    x14 = leastcolor_t(I)
    x15 = f_ofcolor(I, x14)
    x16 = lbind(hmatching, x15)
    x17 = lbind(vmatching, x15)
    x18 = fork(either, x16, x17)
    x19 = compose(x18, initset)
    x20 = sfilter_f(x13, x19)
    x21 = difference(x13, x20)
    O = cover(x12, x21)
    return O

def solve_fcb5c309(S, I):
    x1 = objects(I, T, F, T)
    x2 = leastcolor_t(I)
    x3 = colorfilter(x1, x2)
    x4 = difference(x1, x3)
    x5 = argmax_f(x4, size)
    x6 = subgrid(x5, I)
    x7 = color(x5)
    O = replace(x6, x7, x2)
    return O

def solve_eb281b96(S, I):
    x1 = height_t(I)
    x2 = decrement(x1)
    x3 = width_t(I)
    x4 = astuple(x2, x3)
    x5 = crop(I, ORIGIN, x4)
    x6 = hmirror_t(x5)
    x7 = vconcat(I, x6)
    x8 = double(x2)
    x9 = astuple(x8, x3)
    x10 = crop(x7, DOWN, x9)
    O = vconcat(x7, x10)
    return O

def solve_b6afb2da(S, I):
    x1 = replace(I, FIVE, TWO)
    x2 = objects(I, T, F, F)
    x3 = colorfilter(x2, FIVE)
    x4 = mapply(box, x3)
    x5 = fill(x1, FOUR, x4)
    x6 = mapply(corners, x3)
    O = fill(x5, ONE, x6)
    return O

def solve_74dd1130(S, I):
    O = dmirror_t(I)
    return O

def solve_a61ba2ce(S, I):
    x1 = rbind(subgrid, I)
    x2 = objects(I, T, F, T)
    x3 = lbind(extract, x2)
    x4 = lbind(index, I)
    x5 = matcher(x4, ZERO)
    x6 = lbind(compose, x5)
    x7 = chain(x1, x3, x6)
    x8 = x7(lrcorner)
    x9 = x7(llcorner)
    x10 = hconcat(x8, x9)
    x11 = x7(urcorner)
    x12 = x7(ulcorner)
    x13 = hconcat(x11, x12)
    O = vconcat(x10, x13)
    return O

def solve_ecdecbb3(S, I):
    x1 = compose(center, first)
    x2 = fork(gravitate, first, last)
    x3 = compose(crement, x2)
    x4 = fork(add, x1, x3)
    x5 = fork(connect, x1, x4)
    x6 = objects(I, T, F, T)
    x7 = colorfilter(x6, TWO)
    x8 = colorfilter(x6, EIGHT)
    x9 = product(x7, x8)
    x10 = apply(x5, x9)
    x11 = lbind(greater, EIGHT)
    x12 = compose(x11, size)
    x13 = mfilter_f(x10, x12)
    x14 = fill(I, TWO, x13)
    x15 = apply(x4, x9)
    x16 = intersection(x13, x15)
    x17 = mapply(neighbors, x16)
    O = fill(x14, EIGHT, x17)
    return O

def solve_6c434453(S, I):
    x1 = objects(I, T, F, T)
    x2 = sizefilter(x1, EIGHT)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = dneighbors(UNITY)
    x6 = insert(UNITY, x5)
    x7 = lbind(shift, x6)
    x8 = apply(ulcorner, x2)
    x9 = mapply(x7, x8)
    O = fill(x4, TWO, x9)
    return O

def solve_ff805c23(S, I):
    x1 = f_ofcolor(I, ONE)
    x2 = hmirror_t(I)
    x3 = subgrid(x1, x2)
    x4 = palette_t(x3)
    x5 = contained(ONE, x4)
    x6 = vmirror_t(I)
    x7 = subgrid(x1, x6)
    O = branch(x5, x7, x3)
    return O

def solve_f35d900a(S, I):
    x1 = palette_t(I)
    x2 = remove(ZERO, x1)
    x3 = lbind(other, x2)
    x4 = compose(x3, color)
    x5 = fork(recolor_i, x4, outbox)
    x6 = objects(I, T, F, T)
    x7 = mapply(x5, x6)
    x8 = paint(I, x7)
    x9 = mapply(toindices, x6)
    x10 = box(x9)
    x11 = difference(x10, x9)
    x12 = lbind(argmin, x9)
    x13 = rbind(compose, initset)
    x14 = lbind(rbind, manhattan)
    x15 = chain(x13, x14, initset)
    x16 = chain(initset, x12, x15)
    x17 = fork(manhattan, initset, x16)
    x18 = compose(even, x17)
    x19 = sfilter_f(x11, x18)
    O = fill(x8, FIVE, x19)
    return O

def solve_2dee498d(S, I):
    x1 = hsplit(I, THREE)
    O = first_t(x1)
    return O

def solve_d8c310e9(S, I):
    x1 = objects(I, F, F, T)
    x2 = first_f(x1)
    x3 = hperiod(x2)
    x4 = tojvec(x3)
    x5 = shift(x2, x4)
    x6 = paint(I, x5)
    x7 = multiply(x3, THREE)
    x8 = tojvec(x7)
    x9 = shift(x2, x8)
    O = paint(x6, x9)
    return O

def solve_08ed6ac7(S, I):
    x1 = objects(I, T, F, T)
    x2 = totuple(x1)
    x3 = size_t(x2)
    x4 = interval(x3, ZERO, NEG_ONE)
    x5 = order(x1, height_f)
    x6 = mpapply(recolor_o, x4, x5)
    O = paint(I, x6)
    return O

def solve_a87f7484(S, I):
    x1 = portrait_t(I)
    x2 = branch(x1, dmirror_t, identity)
    x3 = x2(I)
    x4 = numcolors_t(I)
    x5 = decrement(x4)
    x6 = hsplit(x3, x5)
    x7 = rbind(f_ofcolor, ZERO)
    x8 = apply(x7, x6)
    x9 = leastcommon_t(x8)
    x10 = matcher(x7, x9)
    x11 = extract(x6, x10)
    O = x2(x11)
    return O

