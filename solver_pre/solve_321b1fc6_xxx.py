def solve_321b1fc6_one(S, I):
    return paint(cover(I, get_nth_f(difference(o_g(I, R1), colorfilter(o_g(I, R1), EIGHT)), F0)), mapply(lbind(shift, normalize(get_nth_f(difference(o_g(I, R1), colorfilter(o_g(I, R1), EIGHT)), F0))), apply(rbind(corner, R0), colorfilter(o_g(I, R1), EIGHT))))


def solve_321b1fc6(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = colorfilter(x1, EIGHT)
    if x == 2:
        return x2
    x3 = difference(x1, x2)
    if x == 3:
        return x3
    x4 = get_nth_f(x3, F0)
    if x == 4:
        return x4
    x5 = cover(I, x4)
    if x == 5:
        return x5
    x6 = normalize(x4)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = rbind(corner, R0)
    if x == 8:
        return x8
    x9 = apply(x8, x2)
    if x == 9:
        return x9
    x10 = mapply(x7, x9)
    if x == 10:
        return x10
    O = paint(x5, x10)
    return O
