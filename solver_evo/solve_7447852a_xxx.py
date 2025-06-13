def solve_7447852a_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(rbind(get_nth_f, F0), sfilter_t(pair(order(colorfilter(o_g(I, R4), BLACK), compose(rbind(get_nth_f, L1), center)), interval(ZERO, size_t(order(colorfilter(o_g(I, R4), BLACK), compose(rbind(get_nth_f, L1), center))), ONE)), compose(rbind(contained, interval(ZERO, size_t(order(colorfilter(o_g(I, R4), BLACK), compose(rbind(get_nth_f, L1), center))), THREE)), rbind(get_nth_f, L1)))))


def solve_7447852a(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = rbind(get_nth_f, F0)
    x5 = o_g(I, R4)
    x6 = colorfilter(x5, BLACK)
    x7 = rbind(get_nth_f, L1)
    x8 = compose(x7, center)
    x9 = order(x6, x8)
    x10 = size_t(x9)
    x11 = interval(ZERO, x10, ONE)
    x12 = pair(x9, x11)
    x13 = interval(ZERO, x10, THREE)
    x14 = rbind(contained, x13)
    x15 = compose(x14, x7)
    x16 = sfilter_t(x12, x15)
    x17 = mapply(x4, x16)
    O = fill(I, x3, x17)
    return O
