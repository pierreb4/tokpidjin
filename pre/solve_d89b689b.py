def solve_d89b689b_one(S, I):
    return paint(cover(I, merge_f(sizefilter(o_g(I, R5), ONE))), mapply(fork(recolor_i, color, compose(lbind(rbind(get_arg_rank, L1), apply(initset, f_ofcolor(I, EIGHT))), lbind(rbind, manhattan))), sizefilter(o_g(I, R5), ONE)))


def solve_d89b689b(S, I):
    x1 = o_g(I, R5)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = rbind(get_arg_rank, L1)
    x6 = f_ofcolor(I, EIGHT)
    x7 = apply(initset, x6)
    x8 = lbind(x5, x7)
    x9 = lbind(rbind, manhattan)
    x10 = compose(x8, x9)
    x11 = fork(recolor_i, color, x10)
    x12 = mapply(x11, x2)
    O = paint(x4, x12)
    return O
