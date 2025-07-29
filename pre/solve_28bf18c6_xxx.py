def solve_28bf18c6_one(S, I):
    return hconcat(subgrid(get_nth_f(o_g(I, R7), F0), I), subgrid(get_nth_f(o_g(I, R7), F0), I))


def solve_28bf18c6(S, I):
    x1 = o_g(I, R7)
    x2 = get_nth_f(x1, F0)
    x3 = subgrid(x2, I)
    O = hconcat(x3, x3)
    return O
