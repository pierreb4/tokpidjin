def solve_b94a9452_one(S, I):
    return switch(subgrid(get_nth_f(o_g(I, R1), F0), I), get_color_rank_t(subgrid(get_nth_f(o_g(I, R1), F0), I), L1), get_color_rank_t(subgrid(get_nth_f(o_g(I, R1), F0), I), F0))


def solve_b94a9452(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = get_color_rank_t(x3, L1)
    if x == 4:
        return x4
    x5 = get_color_rank_t(x3, F0)
    if x == 5:
        return x5
    O = switch(x3, x4, x5)
    return O
