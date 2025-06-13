def solve_d687bc17_one(S, I):
    return paint(cover(I, merge_f(sizefilter(o_g(I, R5), ONE))), mapply(fork(shift, identity, fork(gravitate, identity, chain(rbind(get_nth_f, F0), lbind(colorfilter, difference(o_g(I, R5), sizefilter(o_g(I, R5), ONE))), color))), sfilter_f(sizefilter(o_g(I, R5), ONE), compose(rbind(contained, apply(color, difference(o_g(I, R5), sizefilter(o_g(I, R5), ONE)))), color))))


def solve_d687bc17(S, I):
    x1 = o_g(I, R5)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    x4 = cover(I, x3)
    x5 = rbind(get_nth_f, F0)
    x6 = difference(x1, x2)
    x7 = lbind(colorfilter, x6)
    x8 = chain(x5, x7, color)
    x9 = fork(gravitate, identity, x8)
    x10 = fork(shift, identity, x9)
    x11 = apply(color, x6)
    x12 = rbind(contained, x11)
    x13 = compose(x12, color)
    x14 = sfilter_f(x2, x13)
    x15 = mapply(x10, x14)
    O = paint(x4, x15)
    return O
