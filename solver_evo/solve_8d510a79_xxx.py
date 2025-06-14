def solve_8d510a79_one(S, I):
    return fill(underfill(I, RED, mapply(fork(sfilter, fork(shoot, identity, compose(chain(toivec, decrement, double), compose(lbind(greater, col_row(f_ofcolor(I, GRAY), R1)), rbind(get_nth_f, F0)))), compose(lbind(matcher, compose(lbind(greater, col_row(f_ofcolor(I, GRAY), R1)), rbind(get_nth_f, F0))), compose(lbind(greater, col_row(f_ofcolor(I, GRAY), R1)), rbind(get_nth_f, F0)))), f_ofcolor(I, RED))), BLUE, mapply(fork(shoot, identity, chain(invert, chain(toivec, decrement, double), compose(lbind(greater, col_row(f_ofcolor(I, GRAY), R1)), rbind(get_nth_f, F0)))), f_ofcolor(I, BLUE)))


def solve_8d510a79(S, I, x=0):
    x1 = chain(toivec, decrement, double)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, GRAY)
    if x == 2:
        return x2
    x3 = col_row(x2, R1)
    if x == 3:
        return x3
    x4 = lbind(greater, x3)
    if x == 4:
        return x4
    x5 = rbind(get_nth_f, F0)
    if x == 5:
        return x5
    x6 = compose(x4, x5)
    if x == 6:
        return x6
    x7 = compose(x1, x6)
    if x == 7:
        return x7
    x8 = fork(shoot, identity, x7)
    if x == 8:
        return x8
    x9 = lbind(matcher, x6)
    if x == 9:
        return x9
    x10 = compose(x9, x6)
    if x == 10:
        return x10
    x11 = fork(sfilter, x8, x10)
    if x == 11:
        return x11
    x12 = f_ofcolor(I, RED)
    if x == 12:
        return x12
    x13 = mapply(x11, x12)
    if x == 13:
        return x13
    x14 = underfill(I, RED, x13)
    if x == 14:
        return x14
    x15 = chain(invert, x1, x6)
    if x == 15:
        return x15
    x16 = fork(shoot, identity, x15)
    if x == 16:
        return x16
    x17 = f_ofcolor(I, BLUE)
    if x == 17:
        return x17
    x18 = mapply(x16, x17)
    if x == 18:
        return x18
    O = fill(x14, BLUE, x18)
    return O
