def solve_23b5c85d_one(S, I):
    return subgrid(get_arg_rank_f(o_g(I, R7), size, L1), I)


def solve_23b5c85d(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O
