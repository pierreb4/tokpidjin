def solve_1c786137_one(S, I):
    return trim(subgrid(get_arg_rank_f(o_g(I, R4), height_f, F0), I))


def solve_1c786137(S, I):
    x1 = o_g(I, R4)
    x2 = get_arg_rank_f(x1, height_f, F0)
    x3 = subgrid(x2, I)
    O = trim(x3)
    return O
