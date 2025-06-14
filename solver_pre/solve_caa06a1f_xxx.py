def solve_caa06a1f_one(S, I):
    return paint(I, mapply(lbind(shift, shift(get_nth_f(o_g(paint(canvas(index(I, decrement(shape_t(I))), double(shape_t(I))), asobject(I)), R1), F0), LEFT)), apply(lbind(multiply, astuple(vperiod(shift(get_nth_f(o_g(paint(canvas(index(I, decrement(shape_t(I))), double(shape_t(I))), asobject(I)), R1), F0), LEFT)), hperiod(shift(get_nth_f(o_g(paint(canvas(index(I, decrement(shape_t(I))), double(shape_t(I))), asobject(I)), R1), F0), LEFT)))), power(lbind(mapply, neighbors), TWO)(neighbors(ORIGIN)))))


def solve_caa06a1f(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    x3 = index(I, x2)
    if x == 3:
        return x3
    x4 = double(x1)
    if x == 4:
        return x4
    x5 = canvas(x3, x4)
    if x == 5:
        return x5
    x6 = asobject(I)
    if x == 6:
        return x6
    x7 = paint(x5, x6)
    if x == 7:
        return x7
    x8 = o_g(x7, R1)
    if x == 8:
        return x8
    x9 = get_nth_f(x8, F0)
    if x == 9:
        return x9
    x10 = shift(x9, LEFT)
    if x == 10:
        return x10
    x11 = lbind(shift, x10)
    if x == 11:
        return x11
    x12 = vperiod(x10)
    if x == 12:
        return x12
    x13 = hperiod(x10)
    if x == 13:
        return x13
    x14 = astuple(x12, x13)
    if x == 14:
        return x14
    x15 = lbind(multiply, x14)
    if x == 15:
        return x15
    x16 = lbind(mapply, neighbors)
    if x == 16:
        return x16
    x17 = power(x16, TWO)
    if x == 17:
        return x17
    x18 = neighbors(ORIGIN)
    if x == 18:
        return x18
    x19 = x17(x18)
    if x == 19:
        return x19
    x20 = apply(x15, x19)
    if x == 20:
        return x20
    x21 = mapply(x11, x20)
    if x == 21:
        return x21
    O = paint(I, x21)
    return O
