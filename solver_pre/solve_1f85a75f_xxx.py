def solve_1f85a75f_one(S, I):
    return subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I)


def solve_1f85a75f(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O
