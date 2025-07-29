def solve_8d510a79_one(S, I):
    return fill(underfill(I, TWO, mapply(fork(sfilter, fork(shoot, identity, compose(chain(toivec, decrement, double), compose(lbind(greater, col_row(f_ofcolor(I, FIVE), R1)), rbind(get_nth_f, F0)))), compose(lbind(matcher, compose(lbind(greater, col_row(f_ofcolor(I, FIVE), R1)), rbind(get_nth_f, F0))), compose(lbind(greater, col_row(f_ofcolor(I, FIVE), R1)), rbind(get_nth_f, F0)))), f_ofcolor(I, TWO))), ONE, mapply(fork(shoot, identity, chain(invert, chain(toivec, decrement, double), compose(lbind(greater, col_row(f_ofcolor(I, FIVE), R1)), rbind(get_nth_f, F0)))), f_ofcolor(I, ONE)))


def solve_8d510a79(S, I):
    x1 = chain(toivec, decrement, double)
    x2 = f_ofcolor(I, FIVE)
    x3 = col_row(x2, R1)
    x4 = lbind(greater, x3)
    x5 = rbind(get_nth_f, F0)
    x6 = compose(x4, x5)
    x7 = compose(x1, x6)
    x8 = fork(shoot, identity, x7)
    x9 = lbind(matcher, x6)
    x10 = compose(x9, x6)
    x11 = fork(sfilter, x8, x10)
    x12 = f_ofcolor(I, TWO)
    x13 = mapply(x11, x12)
    x14 = underfill(I, TWO, x13)
    x15 = chain(invert, x1, x6)
    x16 = fork(shoot, identity, x15)
    x17 = f_ofcolor(I, ONE)
    x18 = mapply(x16, x17)
    O = fill(x14, ONE, x18)
    return O
