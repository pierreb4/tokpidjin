def solve_7447852a_one(S, I):
    return fill(I, FOUR, mapply(rbind(get_nth_f, F0), sfilter_t(pair(order(colorfilter(o_g(I, R4), ZERO), compose(rbind(get_nth_f, L1), center)), interval(ZERO, size_t(order(colorfilter(o_g(I, R4), ZERO), compose(rbind(get_nth_f, L1), center))), ONE)), compose(rbind(contained, interval(ZERO, size_t(order(colorfilter(o_g(I, R4), ZERO), compose(rbind(get_nth_f, L1), center))), THREE)), rbind(get_nth_f, L1)))))


def solve_7447852a(S, I):
    x1 = rbind(get_nth_f, F0)
    x2 = o_g(I, R4)
    x3 = colorfilter(x2, ZERO)
    x4 = rbind(get_nth_f, L1)
    x5 = compose(x4, center)
    x6 = order(x3, x5)
    x7 = size_t(x6)
    x8 = interval(ZERO, x7, ONE)
    x9 = pair(x6, x8)
    x10 = interval(ZERO, x7, THREE)
    x11 = rbind(contained, x10)
    x12 = compose(x11, x4)
    x13 = sfilter_t(x9, x12)
    x14 = mapply(x1, x13)
    O = fill(I, FOUR, x14)
    return O
