def solve_2c608aff_one(S, I):
    return underfill(I, get_color_rank_t(I, L1), mfilter_f(prapply(connect, toindices(get_arg_rank_f(o_g(I, R5), size, F0)), f_ofcolor(I, get_color_rank_t(I, L1))), fork(either, vline_i, hline_i)))


def solve_2c608aff(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x2, size, F0)
    if x == 3:
        return x3
    x4 = toindices(x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, x1)
    if x == 5:
        return x5
    x6 = prapply(connect, x4, x5)
    if x == 6:
        return x6
    x7 = fork(either, vline_i, hline_i)
    if x == 7:
        return x7
    x8 = mfilter_f(x6, x7)
    if x == 8:
        return x8
    O = underfill(I, x1, x8)
    return O
