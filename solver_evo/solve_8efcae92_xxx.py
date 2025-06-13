def solve_8efcae92_one(S, I):
    return subgrid(get_arg_rank_f(colorfilter(o_g(I, R4), BLUE), compose(size, delta), F0), I)


def solve_8efcae92(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, BLUE)
    x3 = compose(size, delta)
    x4 = get_arg_rank_f(x2, x3, F0)
    O = subgrid(x4, I)
    return O
