def solve_f76d97a5_one(S, I):
    return replace(switch(I, get_nth_f(palette_t(I), F0), get_nth_f(palette_t(I), L1)), FIVE, ZERO)


def solve_f76d97a5(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = get_nth_f(x1, L1)
    if x == 3:
        return x3
    x4 = switch(I, x2, x3)
    if x == 4:
        return x4
    O = replace(x4, FIVE, ZERO)
    return O
