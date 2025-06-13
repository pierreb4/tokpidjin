def solve_88a10436_one(S, I):
    return paint(I, shift(shift(normalize(get_nth_f(difference(o_g(I, R1), colorfilter(o_g(I, R1), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), F0)), center(get_nth_f(colorfilter(o_g(I, R1), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), F0))), NEG_UNITY))


def solve_88a10436(S, I):
    x1 = o_g(I, R1)
    x2 = identity(p_g)
    x3 = rbind(get_nth_t, F0)
    x4 = c_iz_n(S, x2, x3)
    x5 = colorfilter(x1, x4)
    x6 = difference(x1, x5)
    x7 = get_nth_f(x6, F0)
    x8 = normalize(x7)
    x9 = get_nth_f(x5, F0)
    x10 = center(x9)
    x11 = shift(x8, x10)
    x12 = shift(x11, NEG_UNITY)
    O = paint(I, x12)
    return O
