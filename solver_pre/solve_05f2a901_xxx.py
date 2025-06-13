def solve_05f2a901_one(S, I):
    return move(I, get_nth_f(colorfilter(o_g(I, R5), TWO), F0), gravitate(get_nth_f(colorfilter(o_g(I, R5), TWO), F0), get_nth_f(colorfilter(o_g(I, R5), EIGHT), F0)))


def solve_05f2a901(S, I):
    x1 = o_g(I, R5)
    x2 = colorfilter(x1, TWO)
    x3 = get_nth_f(x2, F0)
    x4 = colorfilter(x1, EIGHT)
    x5 = get_nth_f(x4, F0)
    x6 = gravitate(x3, x5)
    O = move(I, x3, x6)
    return O
