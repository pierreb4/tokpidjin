def solve_ddf7fa4f_one(S, I):
    return paint(I, mapply(fork(recolor_o, compose(color, rbind(get_nth_f, F0)), rbind(get_nth_f, L1)), sfilter_f(product(sizefilter(o_g(I, R5), ONE), colorfilter(o_g(I, R5), GRAY)), fork(vmatching, rbind(get_nth_f, F0), rbind(get_nth_f, L1)))))


def solve_ddf7fa4f(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = compose(color, x1)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, L1)
    if x == 3:
        return x3
    x4 = fork(recolor_o, x2, x3)
    if x == 4:
        return x4
    x5 = o_g(I, R5)
    if x == 5:
        return x5
    x6 = sizefilter(x5, ONE)
    if x == 6:
        return x6
    x7 = colorfilter(x5, GRAY)
    if x == 7:
        return x7
    x8 = product(x6, x7)
    if x == 8:
        return x8
    x9 = fork(vmatching, x1, x3)
    if x == 9:
        return x9
    x10 = sfilter_f(x8, x9)
    if x == 10:
        return x10
    x11 = mapply(x4, x10)
    if x == 11:
        return x11
    O = paint(I, x11)
    return O
