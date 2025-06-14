def solve_6a1e5592_one(S, I):
    return fill(cover(I, merge_f(colorfilter(o_g(I, R5), FIVE))), ONE, mapply(chain(rbind(rbind(get_arg_rank, F0), fork(subtract, fork(subtract, fork(subtract, fork(add, chain(rbind(multiply, TEN), size, rbind(intersection, asindices(crop(I, ORIGIN, astuple(FIVE, width_t(I)))))), compose(invert, chain(rbind(multiply, TEN), size, rbind(intersection, f_ofcolor(crop(I, ORIGIN, astuple(FIVE, width_t(I))), TWO))))), chain(size, rbind(intersection, f_ofcolor(crop(I, ORIGIN, astuple(FIVE, width_t(I))), ZERO)), outbox)), compose(rbind(multiply, FIVE), rbind(col_row, R1))), chain(size, rbind(intersection, f_ofcolor(crop(I, ORIGIN, astuple(FIVE, width_t(I))), ZERO)), delta))), rbind(apply, asindices(crop(I, ORIGIN, astuple(FIVE, width_t(I))))), lbind(lbind, shift)), apply(compose(toindices, normalize), colorfilter(o_g(I, R5), FIVE))))


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
