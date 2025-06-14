def solve_7447852a_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(rbind(get_nth_f, F0), sfilter_t(pair(order(colorfilter(o_g(I, R4), BLACK), compose(rbind(get_nth_f, L1), center)), interval(ZERO, size_t(order(colorfilter(o_g(I, R4), BLACK), compose(rbind(get_nth_f, L1), center))), ONE)), compose(rbind(contained, interval(ZERO, size_t(order(colorfilter(o_g(I, R4), BLACK), compose(rbind(get_nth_f, L1), center))), THREE)), rbind(get_nth_f, L1)))))


def solve_7447852a(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, F0)
    if x == 4:
        return x4
    x5 = o_g(I, R4)
    if x == 5:
        return x5
    x6 = colorfilter(x5, BLACK)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, L1)
    if x == 7:
        return x7
    x8 = compose(x7, center)
    if x == 8:
        return x8
    x9 = order(x6, x8)
    if x == 9:
        return x9
    x10 = size_t(x9)
    if x == 10:
        return x10
    x11 = interval(ZERO, x10, ONE)
    if x == 11:
        return x11
    x12 = pair(x9, x11)
    if x == 12:
        return x12
    x13 = interval(ZERO, x10, THREE)
    if x == 13:
        return x13
    x14 = rbind(contained, x13)
    if x == 14:
        return x14
    x15 = compose(x14, x7)
    if x == 15:
        return x15
    x16 = sfilter_t(x12, x15)
    if x == 16:
        return x16
    x17 = mapply(x4, x16)
    if x == 17:
        return x17
    O = fill(I, x3, x17)
    return O
