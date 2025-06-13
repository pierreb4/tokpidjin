def solve_f76d97a5_one(S, I):
    return replace(switch(I, get_nth_f(palette_t(I), F0), get_nth_f(palette_t(I), L1)), FIVE, ZERO)


def solve_f76d97a5(S, I):
    x1 = palette_t(I)
    x2 = get_nth_f(x1, F0)
    x3 = get_nth_f(x1, L1)
    x4 = switch(I, x2, x3)
    O = replace(x4, FIVE, ZERO)
    return O
