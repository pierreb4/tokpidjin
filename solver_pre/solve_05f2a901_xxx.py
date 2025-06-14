def solve_05f2a901_one(S, I):
    return move(I, get_nth_f(colorfilter(o_g(I, R5), TWO), F0), gravitate(get_nth_f(colorfilter(o_g(I, R5), TWO), F0), get_nth_f(colorfilter(o_g(I, R5), EIGHT), F0)))


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
