def solve_1f0c79e5_one(S, I):
    return paint(I, mapply(lbind(shift, recolor_i(get_color_rank_t(replace(I, TWO, ZERO), L1), combine_f(f_ofcolor(I, TWO), f_ofcolor(replace(I, TWO, ZERO), get_color_rank_t(replace(I, TWO, ZERO), L1))))), prapply(multiply, apply(compose(decrement, double), shift(f_ofcolor(I, TWO), invert(corner(combine_f(f_ofcolor(I, TWO), f_ofcolor(replace(I, TWO, ZERO), get_color_rank_t(replace(I, TWO, ZERO), L1))), R0)))), interval(ZERO, NINE, ONE))))


def solve_1f0c79e5(S, I):
    x1 = replace(I, TWO, ZERO)
    x2 = get_color_rank_t(x1, L1)
    x3 = f_ofcolor(I, TWO)
    x4 = f_ofcolor(x1, x2)
    x5 = combine_f(x3, x4)
    x6 = recolor_i(x2, x5)
    x7 = lbind(shift, x6)
    x8 = compose(decrement, double)
    x9 = corner(x5, R0)
    x10 = invert(x9)
    x11 = shift(x3, x10)
    x12 = apply(x8, x11)
    x13 = interval(ZERO, NINE, ONE)
    x14 = prapply(multiply, x12, x13)
    x15 = mapply(x7, x14)
    O = paint(I, x15)
    return O
