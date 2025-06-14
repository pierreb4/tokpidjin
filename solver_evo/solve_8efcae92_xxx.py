def solve_8efcae92_one(S, I):
    return subgrid(get_arg_rank_f(colorfilter(o_g(I, R4), BLUE), compose(size, delta), F0), I)


def solve_8efcae92(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, BLUE)
    if x == 2:
        return x2
    x3 = compose(size, delta)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x2, x3, F0)
    if x == 4:
        return x4
    O = subgrid(x4, I)
    return O
