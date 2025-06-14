def solve_1cf80156_one(S, I):
    return subgrid(get_nth_f(o_g(I, R7), F0), I)


def solve_1cf80156(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O
