def solve_6ecd11f4_one(S, I):
    return fill(subgrid(get_arg_rank_f(o_g(I, R3), size, L1), I), ZERO, f_ofcolor(downscale(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I), divide(width_t(subgrid(get_arg_rank_f(o_g(I, R3), size, F0), I)), width_t(subgrid(get_arg_rank_f(o_g(I, R3), size, L1), I)))), ZERO))


def solve_6ecd11f4(S, I):
    x1 = o_g(I, R3)
    x2 = get_arg_rank_f(x1, size, L1)
    x3 = subgrid(x2, I)
    x4 = get_arg_rank_f(x1, size, F0)
    x5 = subgrid(x4, I)
    x6 = width_t(x5)
    x7 = width_t(x3)
    x8 = divide(x6, x7)
    x9 = downscale(x5, x8)
    x10 = f_ofcolor(x9, ZERO)
    O = fill(x3, ZERO, x10)
    return O
