def solve_a48eeaf7_one(S, I):
    return fill(cover(I, f_ofcolor(I, FIVE)), FIVE, mapply(compose(lbind(rbind(get_arg_rank, L1), apply(initset, outbox(f_ofcolor(I, TWO)))), compose(lbind(lbind, manhattan), initset)), f_ofcolor(I, FIVE)))


def solve_a48eeaf7(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = cover(I, x1)
    if x == 2:
        return x2
    x3 = rbind(get_arg_rank, L1)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, TWO)
    if x == 4:
        return x4
    x5 = outbox(x4)
    if x == 5:
        return x5
    x6 = apply(initset, x5)
    if x == 6:
        return x6
    x7 = lbind(x3, x6)
    if x == 7:
        return x7
    x8 = lbind(lbind, manhattan)
    if x == 8:
        return x8
    x9 = compose(x8, initset)
    if x == 9:
        return x9
    x10 = compose(x7, x9)
    if x == 10:
        return x10
    x11 = mapply(x10, x1)
    if x == 11:
        return x11
    O = fill(x2, FIVE, x11)
    return O
