def solve_31aa019c_one(S, I):
    return fill(fill(canvas(ZERO, astuple(TEN, TEN)), get_color_rank_t(I, L1), initset(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0))), TWO, neighbors(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0)))


def solve_31aa019c(S, I):
    x1 = astuple(TEN, TEN)
    x2 = canvas(ZERO, x1)
    x3 = get_color_rank_t(I, L1)
    x4 = f_ofcolor(I, x3)
    x5 = get_nth_f(x4, F0)
    x6 = initset(x5)
    x7 = fill(x2, x3, x6)
    x8 = neighbors(x5)
    O = fill(x7, TWO, x8)
    return O
