def solve_cbded52d_one(S, I):
    return paint(I, mapply(fork(recolor_i, compose(color, rbind(get_nth_f, F0)), chain(initset, center, fork(connect, compose(center, rbind(get_nth_f, F0)), compose(center, rbind(get_nth_f, L1))))), sfilter_f(product(sizefilter(o_g(I, R5), ONE), sizefilter(o_g(I, R5), ONE)), fork(either, fork(vmatching, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), fork(hmatching, rbind(get_nth_f, F0), rbind(get_nth_f, L1))))))


def solve_cbded52d(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = compose(color, x1)
    if x == 2:
        return x2
    x3 = compose(center, x1)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, L1)
    if x == 4:
        return x4
    x5 = compose(center, x4)
    if x == 5:
        return x5
    x6 = fork(connect, x3, x5)
    if x == 6:
        return x6
    x7 = chain(initset, center, x6)
    if x == 7:
        return x7
    x8 = fork(recolor_i, x2, x7)
    if x == 8:
        return x8
    x9 = o_g(I, R5)
    if x == 9:
        return x9
    x10 = sizefilter(x9, ONE)
    if x == 10:
        return x10
    x11 = product(x10, x10)
    if x == 11:
        return x11
    x12 = fork(vmatching, x1, x4)
    if x == 12:
        return x12
    x13 = fork(hmatching, x1, x4)
    if x == 13:
        return x13
    x14 = fork(either, x12, x13)
    if x == 14:
        return x14
    x15 = sfilter_f(x11, x14)
    if x == 15:
        return x15
    x16 = mapply(x8, x15)
    if x == 16:
        return x16
    O = paint(I, x16)
    return O
