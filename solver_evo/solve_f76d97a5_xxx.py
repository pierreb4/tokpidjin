def solve_f76d97a5_one(S, I):
    return replace(switch(I, get_nth_f(palette_t(I), F0), get_nth_f(palette_t(I), L1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


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
    x5 = identity(p_g)
    if x == 5:
        return x5
    x6 = rbind(get_nth_t, F0)
    if x == 6:
        return x6
    x7 = c_iz_n(S, x5, x6)
    if x == 7:
        return x7
    x8 = c_zo_n(S, x5, x6)
    if x == 8:
        return x8
    O = replace(x4, x7, x8)
    return O
