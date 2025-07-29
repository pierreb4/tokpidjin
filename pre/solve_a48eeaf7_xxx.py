def solve_a48eeaf7_one(S, I):
    return fill(cover(I, f_ofcolor(I, FIVE)), FIVE, mapply(compose(lbind(rbind(get_arg_rank, L1), apply(initset, outbox(f_ofcolor(I, TWO)))), compose(lbind(lbind, manhattan), initset)), f_ofcolor(I, FIVE)))


def solve_a48eeaf7(S, I):
    x1 = f_ofcolor(I, FIVE)
    x2 = cover(I, x1)
    x3 = rbind(get_arg_rank, L1)
    x4 = f_ofcolor(I, TWO)
    x5 = outbox(x4)
    x6 = apply(initset, x5)
    x7 = lbind(x3, x6)
    x8 = lbind(lbind, manhattan)
    x9 = compose(x8, initset)
    x10 = compose(x7, x9)
    x11 = mapply(x10, x1)
    O = fill(x2, FIVE, x11)
    return O
