def solve_1f642eb9_one(S, I):
    return paint(I, mapply(fork(shift, identity, compose(crement, rbind(gravitate, get_nth_f(difference(o_g(I, R5), sizefilter(o_g(I, R5), ONE)), F0)))), sizefilter(o_g(I, R5), ONE)))


def solve_1f642eb9(S, I):
    x1 = o_g(I, R5)
    x2 = sizefilter(x1, ONE)
    x3 = difference(x1, x2)
    x4 = get_nth_f(x3, F0)
    x5 = rbind(gravitate, x4)
    x6 = compose(crement, x5)
    x7 = fork(shift, identity, x6)
    x8 = mapply(x7, x2)
    O = paint(I, x8)
    return O
