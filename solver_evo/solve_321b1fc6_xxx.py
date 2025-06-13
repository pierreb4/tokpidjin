def solve_321b1fc6_one(S, I):
    return paint(cover(I, get_nth_f(difference(o_g(I, R1), colorfilter(o_g(I, R1), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), F0)), mapply(lbind(shift, normalize(get_nth_f(difference(o_g(I, R1), colorfilter(o_g(I, R1), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))), F0))), apply(rbind(corner, R0), colorfilter(o_g(I, R1), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))))


def solve_321b1fc6(S, I):
    x1 = o_g(I, R1)
    x2 = identity(p_g)
    x3 = rbind(get_nth_t, F0)
    x4 = c_iz_n(S, x2, x3)
    x5 = colorfilter(x1, x4)
    x6 = difference(x1, x5)
    x7 = get_nth_f(x6, F0)
    x8 = cover(I, x7)
    x9 = normalize(x7)
    x10 = lbind(shift, x9)
    x11 = rbind(corner, R0)
    x12 = apply(x11, x5)
    x13 = mapply(x10, x12)
    O = paint(x8, x13)
    return O
