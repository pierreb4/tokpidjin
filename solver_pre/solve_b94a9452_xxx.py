def solve_b94a9452_one(S, I):
    return switch(subgrid(get_nth_f(o_g(I, R1), F0), I), get_color_rank_t(subgrid(get_nth_f(o_g(I, R1), F0), I), L1), get_color_rank_t(subgrid(get_nth_f(o_g(I, R1), F0), I), F0))


def solve_b94a9452(S, I):
    x1 = o_g(I, R1)
    x2 = get_nth_f(x1, F0)
    x3 = subgrid(x2, I)
    x4 = get_color_rank_t(x3, L1)
    x5 = get_color_rank_t(x3, F0)
    O = switch(x3, x4, x5)
    return O
