def solve_88a10436_one(S, I):
    return paint(I, shift(shift(normalize(get_nth_f(difference(o_g(I, R1), colorfilter(o_g(I, R1), FIVE)), F0)), center(get_nth_f(colorfilter(o_g(I, R1), FIVE), F0))), NEG_UNITY))


def solve_88a10436(S, I):
    x1 = o_g(I, R1)
    x2 = colorfilter(x1, FIVE)
    x3 = difference(x1, x2)
    x4 = get_nth_f(x3, F0)
    x5 = normalize(x4)
    x6 = get_nth_f(x2, F0)
    x7 = center(x6)
    x8 = shift(x5, x7)
    x9 = shift(x8, NEG_UNITY)
    O = paint(I, x9)
    return O
