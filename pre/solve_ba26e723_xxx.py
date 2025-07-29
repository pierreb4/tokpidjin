def solve_ba26e723_one(S, I):
    return fill(I, SIX, sfilter_f(f_ofcolor(I, FOUR), compose(fork(equality, identity, compose(rbind(multiply, THREE), rbind(divide, THREE))), rbind(get_nth_f, L1))))


def solve_ba26e723(S, I):
    x1 = f_ofcolor(I, FOUR)
    x2 = rbind(multiply, THREE)
    x3 = rbind(divide, THREE)
    x4 = compose(x2, x3)
    x5 = fork(equality, identity, x4)
    x6 = rbind(get_nth_f, L1)
    x7 = compose(x5, x6)
    x8 = sfilter_f(x1, x7)
    O = fill(I, SIX, x8)
    return O
