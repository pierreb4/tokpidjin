def solve_d89b689b_one(S, I):
    return paint(cover(I, merge_f(sizefilter(o_g(I, R5), ONE))), mapply(fork(recolor_i, color, compose(lbind(rbind(get_arg_rank, L1), apply(initset, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), lbind(rbind, manhattan))), sizefilter(o_g(I, R5), ONE)))


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
    x6 = identity(p_g)
    if x == 6:
        return x6
    x7 = rbind(get_nth_t, F0)
    if x == 7:
        return x7
    x8 = c_iz_n(S, x6, x7)
    if x == 8:
        return x8
    x9 = f_ofcolor(I, x8)
    if x == 9:
        return x9
    x10 = apply(initset, x9)
    if x == 10:
        return x10
    x11 = lbind(x5, x10)
    if x == 11:
        return x11
    x12 = lbind(rbind, manhattan)
    if x == 12:
        return x12
    x13 = compose(x11, x12)
    if x == 13:
        return x13
    x14 = fork(recolor_i, color, x13)
    if x == 14:
        return x14
    x15 = mapply(x14, x2)
    if x == 15:
        return x15
    O = paint(x4, x15)
    return O
