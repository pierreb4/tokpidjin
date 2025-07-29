def solve_caa06a1f_one(S, I):
    return paint(I, mapply(lbind(shift, shift(get_nth_f(o_g(paint(canvas(index(I, decrement(shape_t(I))), double(shape_t(I))), asobject(I)), R1), F0), LEFT)), apply(lbind(multiply, astuple(vperiod(shift(get_nth_f(o_g(paint(canvas(index(I, decrement(shape_t(I))), double(shape_t(I))), asobject(I)), R1), F0), LEFT)), hperiod(shift(get_nth_f(o_g(paint(canvas(index(I, decrement(shape_t(I))), double(shape_t(I))), asobject(I)), R1), F0), LEFT)))), power(lbind(mapply, neighbors), TWO)(neighbors(ORIGIN)))))


def solve_caa06a1f(S, I):
    x1 = shape_t(I)
    x2 = decrement(x1)
    x3 = index(I, x2)
    x4 = double(x1)
    x5 = canvas(x3, x4)
    x6 = asobject(I)
    x7 = paint(x5, x6)
    x8 = o_g(x7, R1)
    x9 = get_nth_f(x8, F0)
    x10 = shift(x9, LEFT)
    x11 = lbind(shift, x10)
    x12 = vperiod(x10)
    x13 = hperiod(x10)
    x14 = astuple(x12, x13)
    x15 = lbind(multiply, x14)
    x16 = lbind(mapply, neighbors)
    x17 = power(x16, TWO)
    x18 = neighbors(ORIGIN)
    x19 = x17(x18)
    x20 = apply(x15, x19)
    x21 = mapply(x11, x20)
    O = paint(I, x21)
    return O
