def solve_1caeab9d_one(S, I):
    return paint(cover(I, merge_f(o_g(I, R7))), mapply(fork(shift, identity, chain(toivec, lbind(subtract, col_row(f_ofcolor(I, ONE), R0)), rbind(col_row, R0))), o_g(I, R7)))


def solve_1caeab9d(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = cover(I, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, ONE)
    if x == 4:
        return x4
    x5 = col_row(x4, R0)
    if x == 5:
        return x5
    x6 = lbind(subtract, x5)
    if x == 6:
        return x6
    x7 = rbind(col_row, R0)
    if x == 7:
        return x7
    x8 = chain(toivec, x6, x7)
    if x == 8:
        return x8
    x9 = fork(shift, identity, x8)
    if x == 9:
        return x9
    x10 = mapply(x9, x1)
    if x == 10:
        return x10
    O = paint(x3, x10)
    return O
