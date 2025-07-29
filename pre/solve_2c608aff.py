def solve_2c608aff_one(S, I):
    return underfill(I, get_color_rank_t(I, L1), mfilter_f(prapply(connect, toindices(get_arg_rank_f(o_g(I, R5), size, F0)), f_ofcolor(I, get_color_rank_t(I, L1))), fork(either, vline_i, hline_i)))


def solve_2c608aff(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = o_g(I, R5)
    x3 = get_arg_rank_f(x2, size, F0)
    x4 = toindices(x3)
    x5 = f_ofcolor(I, x1)
    x6 = prapply(connect, x4, x5)
    x7 = fork(either, vline_i, hline_i)
    x8 = mfilter_f(x6, x7)
    O = underfill(I, x1, x8)
    return O
