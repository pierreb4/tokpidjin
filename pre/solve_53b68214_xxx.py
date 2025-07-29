def solve_53b68214_one(S, I):
    return paint(paint(canvas(ZERO, astuple(width_t(I), width_t(I))), get_nth_f(o_g(I, R7), F0)), branch(portrait_f(get_nth_f(o_g(I, R7), F0)), mapply(lbind(shift, get_nth_f(o_g(I, R7), F0)), apply(lbind(multiply, toivec(vperiod(get_nth_f(o_g(I, R7), F0)))), interval(ZERO, NINE, ONE))), shift(get_nth_f(o_g(I, R7), F0), decrement(add(DOWN, shape_f(get_nth_f(o_g(I, R7), F0)))))))


def solve_53b68214(S, I):
    x1 = width_t(I)
    x2 = astuple(x1, x1)
    x3 = canvas(ZERO, x2)
    x4 = o_g(I, R7)
    x5 = get_nth_f(x4, F0)
    x6 = paint(x3, x5)
    x7 = portrait_f(x5)
    x8 = lbind(shift, x5)
    x9 = vperiod(x5)
    x10 = toivec(x9)
    x11 = lbind(multiply, x10)
    x12 = interval(ZERO, NINE, ONE)
    x13 = apply(x11, x12)
    x14 = mapply(x8, x13)
    x15 = shape_f(x5)
    x16 = add(DOWN, x15)
    x17 = decrement(x16)
    x18 = shift(x5, x17)
    x19 = branch(x7, x14, x18)
    O = paint(x6, x19)
    return O
