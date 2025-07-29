def solve_e21d9049_one(S, I):
    return cover(paint(I, mapply(lbind(shift, merge(o_g(I, R5))), apply(lbind(multiply, shape_f(merge(o_g(I, R5)))), power(lbind(mapply, neighbors), TWO)(neighbors(ORIGIN))))), difference(asindices(I), sfilter_f(asindices(I), compose(fork(either, lbind(hmatching, f_ofcolor(I, get_color_rank_t(I, L1))), lbind(vmatching, f_ofcolor(I, get_color_rank_t(I, L1)))), initset))))


def solve_e21d9049(S, I):
    x1 = o_g(I, R5)
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
    x14 = get_color_rank_t(I, L1)
    x15 = f_ofcolor(I, x14)
    x16 = lbind(hmatching, x15)
    x17 = lbind(vmatching, x15)
    x18 = fork(either, x16, x17)
    x19 = compose(x18, initset)
    x20 = sfilter_f(x13, x19)
    x21 = difference(x13, x20)
    O = cover(x12, x21)
    return O
