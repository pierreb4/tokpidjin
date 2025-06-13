def solve_5c2c9af4_one(S, I):
    return fill(I, get_color_rank_t(I, L1), shift(mapply(box, pair(apply(lbind(multiply, subtract(center(f_ofcolor(I, get_color_rank_t(I, L1))), corner(f_ofcolor(I, get_color_rank_t(I, L1)), R0))), interval(ZERO, NINE, ONE)), apply(lbind(multiply, subtract(center(f_ofcolor(I, get_color_rank_t(I, L1))), corner(f_ofcolor(I, get_color_rank_t(I, L1)), R0))), interval(ZERO, multiply(NEG_ONE, NINE), NEG_ONE)))), center(f_ofcolor(I, get_color_rank_t(I, L1)))))


def solve_5c2c9af4(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = f_ofcolor(I, x1)
    x3 = center(x2)
    x4 = corner(x2, R0)
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
