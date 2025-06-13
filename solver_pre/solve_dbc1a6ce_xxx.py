def solve_dbc1a6ce_one(S, I):
    return underfill(I, EIGHT, mfilter_f(apply(fork(connect, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), product(f_ofcolor(I, ONE), f_ofcolor(I, ONE))), fork(either, vline_i, hline_i)))


def solve_dbc1a6ce(S, I):
    x1 = rbind(get_nth_f, F0)
    x2 = rbind(get_nth_f, L1)
    x3 = fork(connect, x1, x2)
    x4 = f_ofcolor(I, ONE)
    x5 = product(x4, x4)
    x6 = apply(x3, x5)
    x7 = fork(either, vline_i, hline_i)
    x8 = mfilter_f(x6, x7)
    O = underfill(I, EIGHT, x8)
    return O
