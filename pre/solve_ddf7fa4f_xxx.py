def solve_ddf7fa4f_one(S, I):
    return paint(I, mapply(fork(recolor_o, compose(color, rbind(get_nth_f, F0)), rbind(get_nth_f, L1)), sfilter_f(product(sizefilter(o_g(I, R5), ONE), colorfilter(o_g(I, R5), FIVE)), fork(vmatching, rbind(get_nth_f, F0), rbind(get_nth_f, L1)))))


def solve_ddf7fa4f(S, I):
    x1 = rbind(get_nth_f, F0)
    x2 = compose(color, x1)
    x3 = rbind(get_nth_f, L1)
    x4 = fork(recolor_o, x2, x3)
    x5 = o_g(I, R5)
    x6 = sizefilter(x5, ONE)
    x7 = colorfilter(x5, FIVE)
    x8 = product(x6, x7)
    x9 = fork(vmatching, x1, x3)
    x10 = sfilter_f(x8, x9)
    x11 = mapply(x4, x10)
    O = paint(I, x11)
    return O
