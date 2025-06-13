def solve_a79310a0_one(S, I):
    return replace(move(I, get_nth_f(o_g(I, R5), F0), DOWN), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


def solve_a79310a0(S, I):
    x1 = o_g(I, R5)
    x2 = get_nth_f(x1, F0)
    x3 = move(I, x2, DOWN)
    x4 = identity(p_g)
    x5 = rbind(get_nth_t, F0)
    x6 = c_iz_n(S, x4, x5)
    x7 = c_zo_n(S, x4, x5)
    O = replace(x3, x6, x7)
    return O
