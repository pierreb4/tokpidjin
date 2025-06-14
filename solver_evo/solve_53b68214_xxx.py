def solve_53b68214_one(S, I):
    return paint(paint(canvas(BLACK, astuple(width_t(I), width_t(I))), get_nth_f(o_g(I, R7), F0)), branch(portrait_f(get_nth_f(o_g(I, R7), F0)), mapply(lbind(shift, get_nth_f(o_g(I, R7), F0)), apply(lbind(multiply, toivec(vperiod(get_nth_f(o_g(I, R7), F0)))), interval(ZERO, NINE, ONE))), shift(get_nth_f(o_g(I, R7), F0), decrement(add(DOWN, shape_f(get_nth_f(o_g(I, R7), F0)))))))


def solve_53b68214(S, I, x=0):
    x1 = width_t(I)
    if x == 1:
        return x1
    x2 = astuple(x1, x1)
    if x == 2:
        return x2
    x3 = canvas(BLACK, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R7)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = paint(x3, x5)
    if x == 6:
        return x6
    x7 = portrait_f(x5)
    if x == 7:
        return x7
    x8 = lbind(shift, x5)
    if x == 8:
        return x8
    x9 = vperiod(x5)
    if x == 9:
        return x9
    x10 = toivec(x9)
    if x == 10:
        return x10
    x11 = lbind(multiply, x10)
    if x == 11:
        return x11
    x12 = interval(ZERO, NINE, ONE)
    if x == 12:
        return x12
    x13 = apply(x11, x12)
    if x == 13:
        return x13
    x14 = mapply(x8, x13)
    if x == 14:
        return x14
    x15 = shape_f(x5)
    if x == 15:
        return x15
    x16 = add(DOWN, x15)
    if x == 16:
        return x16
    x17 = decrement(x16)
    if x == 17:
        return x17
    x18 = shift(x5, x17)
    if x == 18:
        return x18
    x19 = branch(x7, x14, x18)
    if x == 19:
        return x19
    O = paint(x6, x19)
    return O
