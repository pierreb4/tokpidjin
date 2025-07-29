def solve_321b1fc6_one(S, I):
    return paint(cover(I, get_nth_f(difference(o_g(I, R1), colorfilter(o_g(I, R1), EIGHT)), F0)), mapply(lbind(shift, normalize(get_nth_f(difference(o_g(I, R1), colorfilter(o_g(I, R1), EIGHT)), F0))), apply(rbind(corner, R0), colorfilter(o_g(I, R1), EIGHT))))


def solve_321b1fc6(S, I):
    x1 = o_g(I, R1)
    x2 = colorfilter(x1, EIGHT)
    x3 = difference(x1, x2)
    x4 = get_nth_f(x3, F0)
    x5 = cover(I, x4)
    x6 = normalize(x4)
    x7 = lbind(shift, x6)
    x8 = rbind(corner, R0)
    x9 = apply(x8, x2)
    x10 = mapply(x7, x9)
    O = paint(x5, x10)
    return O
