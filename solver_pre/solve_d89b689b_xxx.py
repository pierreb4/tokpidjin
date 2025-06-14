def solve_d89b689b_one(S, I):
    return paint(cover(I, merge_f(sizefilter(o_g(I, R5), ONE))), mapply(fork(recolor_i, color, compose(lbind(rbind(get_arg_rank, L1), apply(initset, f_ofcolor(I, EIGHT))), lbind(rbind, manhattan))), sizefilter(o_g(I, R5), ONE)))


def solve_d89b689b(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    x4 = cover(I, x3)
    if x == 4:
        return x4
    x5 = rbind(get_arg_rank, L1)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, EIGHT)
    if x == 6:
        return x6
    x7 = apply(initset, x6)
    if x == 7:
        return x7
    x8 = lbind(x5, x7)
    if x == 8:
        return x8
    x9 = lbind(rbind, manhattan)
    if x == 9:
        return x9
    x10 = compose(x8, x9)
    if x == 10:
        return x10
    x11 = fork(recolor_i, color, x10)
    if x == 11:
        return x11
    x12 = mapply(x11, x2)
    if x == 12:
        return x12
    O = paint(x4, x12)
    return O
