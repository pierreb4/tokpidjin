def solve_6ecd11f4_one(S, I):
    return fill(subgrid(get_arg_rank_f(o_g(I, R3), size, L1), I), BLACK, f_ofcolor(downscale(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I), divide(width_t(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I)), width_t(subgrid(get_arg_rank_f(o_g(I, R3), size, L1), I)))), BLACK))


def solve_6ecd11f4(S, I, x=0):
    x1 = o_g(I, R3)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, L1)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x1, size, F0)
    if x == 4:
        return x4
    x5 = subgrid(x4, I)
    if x == 5:
        return x5
    x6 = width_t(x5)
    if x == 6:
        return x6
    x7 = width_t(x3)
    if x == 7:
        return x7
    x8 = divide(x6, x7)
    if x == 8:
        return x8
    x9 = downscale(x5, x8)
    if x == 9:
        return x9
    x10 = f_ofcolor(x9, BLACK)
    if x == 10:
        return x10
    O = fill(x3, BLACK, x10)
    return O
