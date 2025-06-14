def solve_1c786137_one(S, I):
    return trim(subgrid(get_arg_rank_f(o_g(I, R4), height_f, F0), I))


def solve_1c786137(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, height_f, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    O = trim(x3)
    return O
