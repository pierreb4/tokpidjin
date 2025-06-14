def solve_d687bc17_one(S, I):
    return paint(cover(I, merge_f(sizefilter(o_g(I, R5), ONE))), mapply(fork(shift, identity, fork(gravitate, identity, chain(rbind(get_nth_f, F0), lbind(colorfilter, difference(o_g(I, R5), sizefilter(o_g(I, R5), ONE))), color))), sfilter_f(sizefilter(o_g(I, R5), ONE), compose(rbind(contained, apply(color, difference(o_g(I, R5), sizefilter(o_g(I, R5), ONE)))), color))))


def solve_d687bc17(S, I, x=0):
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
    x5 = rbind(get_nth_f, F0)
    if x == 5:
        return x5
    x6 = difference(x1, x2)
    if x == 6:
        return x6
    x7 = lbind(colorfilter, x6)
    if x == 7:
        return x7
    x8 = chain(x5, x7, color)
    if x == 8:
        return x8
    x9 = fork(gravitate, identity, x8)
    if x == 9:
        return x9
    x10 = fork(shift, identity, x9)
    if x == 10:
        return x10
    x11 = apply(color, x6)
    if x == 11:
        return x11
    x12 = rbind(contained, x11)
    if x == 12:
        return x12
    x13 = compose(x12, color)
    if x == 13:
        return x13
    x14 = sfilter_f(x2, x13)
    if x == 14:
        return x14
    x15 = mapply(x10, x14)
    if x == 15:
        return x15
    O = paint(x4, x15)
    return O
