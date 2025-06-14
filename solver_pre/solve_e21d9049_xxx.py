def solve_e21d9049_one(S, I):
    return cover(paint(I, mapply(lbind(shift, merge(o_g(I, R5))), apply(lbind(multiply, shape_f(merge(o_g(I, R5)))), power(lbind(mapply, neighbors), TWO)(neighbors(ORIGIN))))), difference(asindices(I), sfilter_f(asindices(I), compose(fork(either, lbind(hmatching, f_ofcolor(I, get_color_rank_t(I, L1))), lbind(vmatching, f_ofcolor(I, get_color_rank_t(I, L1)))), initset))))


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
