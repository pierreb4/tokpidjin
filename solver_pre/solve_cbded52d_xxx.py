def solve_cbded52d_one(S, I):
    return paint(I, mapply(fork(recolor_i, compose(color, rbind(get_nth_f, F0)), chain(initset, center, fork(connect, compose(center, rbind(get_nth_f, F0)), compose(center, rbind(get_nth_f, L1))))), sfilter_f(product(sizefilter(o_g(I, R5), ONE), sizefilter(o_g(I, R5), ONE)), fork(either, fork(vmatching, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), fork(hmatching, rbind(get_nth_f, F0), rbind(get_nth_f, L1))))))


def solve_cbded52d(S, I):
    x1 = rbind(get_nth_f, F0)
    x2 = compose(color, x1)
    x3 = compose(center, x1)
    x4 = rbind(get_nth_f, L1)
    x5 = compose(center, x4)
    x6 = fork(connect, x3, x5)
    x7 = chain(initset, center, x6)
    x8 = fork(recolor_i, x2, x7)
    x9 = o_g(I, R5)
    x10 = sizefilter(x9, ONE)
    x11 = product(x10, x10)
    x12 = fork(vmatching, x1, x4)
    x13 = fork(hmatching, x1, x4)
    x14 = fork(either, x12, x13)
    x15 = sfilter_f(x11, x14)
    x16 = mapply(x8, x15)
    O = paint(I, x16)
    return O
