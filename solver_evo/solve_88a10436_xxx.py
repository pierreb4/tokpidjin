def solve_88a10436_one(S, I):
    return paint(I, shift(shift(normalize(get_nth_f(difference(o_g(I, R1), colorfilter(o_g(I, R1), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), F0)), center(get_nth_f(colorfilter(o_g(I, R1), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), F0))), NEG_UNITY))


def solve_88a10436(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = identity(p_g)
    if x == 2:
        return x2
    x3 = rbind(get_nth_t, F0)
    if x == 3:
        return x3
    x4 = c_iz_n(S, x2, x3)
    if x == 4:
        return x4
    x5 = colorfilter(x1, x4)
    if x == 5:
        return x5
    x6 = difference(x1, x5)
    if x == 6:
        return x6
    x7 = get_nth_f(x6, F0)
    if x == 7:
        return x7
    x8 = normalize(x7)
    if x == 8:
        return x8
    x9 = get_nth_f(x5, F0)
    if x == 9:
        return x9
    x10 = center(x9)
    if x == 10:
        return x10
    x11 = shift(x8, x10)
    if x == 11:
        return x11
    x12 = shift(x11, NEG_UNITY)
    if x == 12:
        return x12
    O = paint(I, x12)
    return O
