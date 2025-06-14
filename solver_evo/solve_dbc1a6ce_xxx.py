def solve_dbc1a6ce_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(apply(fork(connect, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), product(f_ofcolor(I, BLUE), f_ofcolor(I, BLUE))), fork(either, vline_i, hline_i)))


def solve_dbc1a6ce(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, F0)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, L1)
    if x == 5:
        return x5
    x6 = fork(connect, x4, x5)
    if x == 6:
        return x6
    x7 = f_ofcolor(I, BLUE)
    if x == 7:
        return x7
    x8 = product(x7, x7)
    if x == 8:
        return x8
    x9 = apply(x6, x8)
    if x == 9:
        return x9
    x10 = fork(either, vline_i, hline_i)
    if x == 10:
        return x10
    x11 = mfilter_f(x9, x10)
    if x == 11:
        return x11
    O = underfill(I, x3, x11)
    return O
