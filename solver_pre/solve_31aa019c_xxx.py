def solve_31aa019c_one(S, I):
    return fill(fill(canvas(ZERO, astuple(TEN, TEN)), get_color_rank_t(I, L1), initset(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0))), TWO, neighbors(get_nth_f(f_ofcolor(I, get_color_rank_t(I, L1)), F0)))


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
