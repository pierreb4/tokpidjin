def solve_d89b689b_one(S, I):
    return paint(cover(I, merge_f(sizefilter(o_g(I, R5), ONE))), mapply(fork(recolor_i, color, compose(lbind(rbind(get_arg_rank, L1), apply(initset, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), lbind(rbind, manhattan))), sizefilter(o_g(I, R5), ONE)))


def solve_d89b689b(S, I):
    x1 = o_g(I, R5)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = rbind(get_arg_rank, L1)
    x6 = identity(p_g)
    x7 = rbind(get_nth_t, F0)
    x8 = c_iz_n(S, x6, x7)
    x9 = f_ofcolor(I, x8)
    x10 = apply(initset, x9)
    x11 = lbind(x5, x10)
    x12 = lbind(rbind, manhattan)
    x13 = compose(x11, x12)
    x14 = fork(recolor_i, color, x13)
    x15 = mapply(x14, x2)
    O = paint(x4, x15)
    return O
