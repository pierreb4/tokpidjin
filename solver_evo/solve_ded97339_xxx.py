def solve_ded97339_one(S, I):
    return underfill(I, CYAN, mfilter_f(apply(fork(connect, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), product(f_ofcolor(I, CYAN), f_ofcolor(I, CYAN))), fork(either, vline_i, hline_i)))


def solve_ded97339(S, I):
    x1 = rbind(get_nth_f, F0)
    x2 = rbind(get_nth_f, L1)
    x3 = fork(connect, x1, x2)
    x4 = f_ofcolor(I, CYAN)
    x5 = product(x4, x4)
    x6 = apply(x3, x5)
    x7 = fork(either, vline_i, hline_i)
    x8 = mfilter_f(x6, x7)
    O = underfill(I, CYAN, x8)
    return O
