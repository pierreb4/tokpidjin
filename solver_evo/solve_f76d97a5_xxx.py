def solve_f76d97a5_one(S, I):
    return replace(switch(I, get_nth_f(palette_t(I), F0), get_nth_f(palette_t(I), L1)), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


def solve_f76d97a5(S, I):
    x1 = palette_t(I)
    x2 = get_nth_f(x1, F0)
    x3 = get_nth_f(x1, L1)
    x4 = switch(I, x2, x3)
    x5 = identity(p_g)
    x6 = rbind(get_nth_t, F0)
    x7 = c_iz_n(S, x5, x6)
    x8 = c_zo_n(S, x5, x6)
    O = replace(x4, x7, x8)
    return O
