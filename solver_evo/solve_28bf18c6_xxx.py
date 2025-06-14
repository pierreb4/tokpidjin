def solve_28bf18c6_one(S, I):
    return hconcat(subgrid(get_nth_f(o_g(I, R7), F0), I), subgrid(get_nth_f(o_g(I, R7), F0), I))


def solve_28bf18c6(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    O = hconcat(x3, x3)
    return O
