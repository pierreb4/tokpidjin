def solve_29c11459_one(S, I):
    return fill(paint(paint(I, mapply(fork(recolor_i, color, compose(hfrontier, center)), o_g(righthalf(I), R5))), merge_f(o_g(paint(lefthalf(I), mapply(fork(recolor_i, color, compose(hfrontier, center)), o_g(lefthalf(I), R5))), R5))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shift(apply(rbind(corner, R1), o_g(paint(lefthalf(I), mapply(fork(recolor_i, color, compose(hfrontier, center)), o_g(lefthalf(I), R5))), R5)), RIGHT))


def solve_29c11459(S, I):
    x1 = compose(hfrontier, center)
    x2 = fork(recolor_i, color, x1)
    x3 = righthalf(I)
    x4 = o_g(x3, R5)
    x5 = mapply(x2, x4)
    x6 = paint(I, x5)
    x7 = lefthalf(I)
    x8 = o_g(x7, R5)
    x9 = mapply(x2, x8)
    x10 = paint(x7, x9)
    x11 = o_g(x10, R5)
    x12 = merge_f(x11)
    x13 = paint(x6, x12)
    x14 = identity(p_g)
    x15 = rbind(get_nth_t, F0)
    x16 = c_zo_n(S, x14, x15)
    x17 = rbind(corner, R1)
    x18 = apply(x17, x11)
    x19 = shift(x18, RIGHT)
    O = fill(x13, x16, x19)
    return O
