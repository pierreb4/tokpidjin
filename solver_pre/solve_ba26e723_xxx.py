def solve_ba26e723_one(S, I):
    return fill(I, SIX, sfilter_f(f_ofcolor(I, FOUR), compose(fork(equality, identity, compose(rbind(multiply, THREE), rbind(divide, THREE))), rbind(get_nth_f, L1))))


def solve_ba26e723(S, I, x=0):
    x1 = f_ofcolor(I, FOUR)
    if x == 1:
        return x1
    x2 = rbind(multiply, THREE)
    if x == 2:
        return x2
    x3 = rbind(divide, THREE)
    if x == 3:
        return x3
    x4 = compose(x2, x3)
    if x == 4:
        return x4
    x5 = fork(equality, identity, x4)
    if x == 5:
        return x5
    x6 = rbind(get_nth_f, L1)
    if x == 6:
        return x6
    x7 = compose(x5, x6)
    if x == 7:
        return x7
    x8 = sfilter_f(x1, x7)
    if x == 8:
        return x8
    O = fill(I, SIX, x8)
    return O
