def solve_ba26e723_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), sfilter_f(f_ofcolor(I, YELLOW), compose(fork(equality, identity, compose(rbind(multiply, GREEN), rbind(divide, GREEN))), rbind(get_nth_f, L1))))


def solve_ba26e723(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = f_ofcolor(I, YELLOW)
    x5 = rbind(multiply, GREEN)
    x6 = rbind(divide, GREEN)
    x7 = compose(x5, x6)
    x8 = fork(equality, identity, x7)
    x9 = rbind(get_nth_f, L1)
    x10 = compose(x8, x9)
    x11 = sfilter_f(x4, x10)
    O = fill(I, x3, x11)
    return O
