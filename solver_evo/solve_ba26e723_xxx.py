def solve_ba26e723_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), sfilter_f(f_ofcolor(I, YELLOW), compose(fork(equality, identity, compose(rbind(multiply, GREEN), rbind(divide, GREEN))), rbind(get_nth_f, L1))))


def solve_ba26e723(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, YELLOW)
    if x == 4:
        return x4
    x5 = rbind(multiply, GREEN)
    if x == 5:
        return x5
    x6 = rbind(divide, GREEN)
    if x == 6:
        return x6
    x7 = compose(x5, x6)
    if x == 7:
        return x7
    x8 = fork(equality, identity, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_f, L1)
    if x == 9:
        return x9
    x10 = compose(x8, x9)
    if x == 10:
        return x10
    x11 = sfilter_f(x4, x10)
    if x == 11:
        return x11
    O = fill(I, x3, x11)
    return O
