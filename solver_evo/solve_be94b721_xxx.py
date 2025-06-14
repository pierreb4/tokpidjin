def solve_be94b721_one(S, I):
    return subgrid(get_arg_rank_f(o_g(I, R5), size, F0), I)


def solve_be94b721(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O
