def solve_7447852a_one(S, I):
    return fill(I, FOUR, mapply(rbind(get_nth_f, F0), sfilter_t(pair(order(colorfilter(o_g(I, R4), ZERO), compose(rbind(get_nth_f, L1), center)), interval(ZERO, size_t(order(colorfilter(o_g(I, R4), ZERO), compose(rbind(get_nth_f, L1), center))), ONE)), compose(rbind(contained, interval(ZERO, size_t(order(colorfilter(o_g(I, R4), ZERO), compose(rbind(get_nth_f, L1), center))), THREE)), rbind(get_nth_f, L1)))))


def solve_7447852a(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = colorfilter(x2, ZERO)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, L1)
    if x == 4:
        return x4
    x5 = compose(x4, center)
    if x == 5:
        return x5
    x6 = order(x3, x5)
    if x == 6:
        return x6
    x7 = size_t(x6)
    if x == 7:
        return x7
    x8 = interval(ZERO, x7, ONE)
    if x == 8:
        return x8
    x9 = pair(x6, x8)
    if x == 9:
        return x9
    x10 = interval(ZERO, x7, THREE)
    if x == 10:
        return x10
    x11 = rbind(contained, x10)
    if x == 11:
        return x11
    x12 = compose(x11, x4)
    if x == 12:
        return x12
    x13 = sfilter_t(x9, x12)
    if x == 13:
        return x13
    x14 = mapply(x1, x13)
    if x == 14:
        return x14
    O = fill(I, FOUR, x14)
    return O
