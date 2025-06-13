def solve_1caeab9d_one(S, I):
    return paint(cover(I, merge_f(o_g(I, R7))), mapply(fork(shift, identity, chain(toivec, lbind(subtract, col_row(f_ofcolor(I, ONE), R0)), rbind(col_row, R0))), o_g(I, R7)))


def solve_1caeab9d(S, I):
    x1 = o_g(I, R7)
    x2 = merge_f(x1)
    x3 = cover(I, x2)
    x4 = f_ofcolor(I, ONE)
    x5 = col_row(x4, R0)
    x6 = lbind(subtract, x5)
    x7 = rbind(col_row, R0)
    x8 = chain(toivec, x6, x7)
    x9 = fork(shift, identity, x8)
    x10 = mapply(x9, x1)
    O = paint(x3, x10)
    return O
