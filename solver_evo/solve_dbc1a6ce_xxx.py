def solve_dbc1a6ce_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(apply(fork(connect, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), product(f_ofcolor(I, BLUE), f_ofcolor(I, BLUE))), fork(either, vline_i, hline_i)))


def solve_dbc1a6ce(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = rbind(get_nth_f, F0)
    x5 = rbind(get_nth_f, L1)
    x6 = fork(connect, x4, x5)
    x7 = f_ofcolor(I, BLUE)
    x8 = product(x7, x7)
    x9 = apply(x6, x8)
    x10 = fork(either, vline_i, hline_i)
    x11 = mfilter_f(x9, x10)
    O = underfill(I, x3, x11)
    return O
