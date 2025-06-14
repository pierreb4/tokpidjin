def solve_88a10436_one(S, I):
    return paint(I, shift(shift(normalize(get_nth_f(difference(o_g(I, R1), colorfilter(o_g(I, R1), FIVE)), F0)), center(get_nth_f(colorfilter(o_g(I, R1), FIVE), F0))), NEG_UNITY))


def solve_88a10436(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = colorfilter(x1, FIVE)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = get_nth_f(x3, F0)
    if x == 4:
        return x4
    x5 = normalize(x4)
    if x == 5:
        return x5
    x6 = get_nth_f(x2, F0)
    if x == 6:
        return x6
    x7 = center(x6)
    if x == 7:
        return x7
    x8 = shift(x5, x7)
    if x == 8:
        return x8
    x9 = shift(x8, NEG_UNITY)
    if x == 9:
        return x9
    O = paint(I, x9)
    return O
