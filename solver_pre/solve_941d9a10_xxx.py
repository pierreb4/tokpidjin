def solve_941d9a10_one(S, I):
    return fill(fill(fill(I, ONE, compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(lbind, contained))(ORIGIN)), THREE, compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(lbind, contained))(decrement(shape_t(I)))), TWO, compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(lbind, contained))(astuple(FIVE, FIVE)))


def solve_941d9a10(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = apply(toindices, x2)
    if x == 3:
        return x3
    x4 = lbind(extract, x3)
    if x == 4:
        return x4
    x5 = lbind(lbind, contained)
    if x == 5:
        return x5
    x6 = compose(x4, x5)
    if x == 6:
        return x6
    x7 = x6(ORIGIN)
    if x == 7:
        return x7
    x8 = fill(I, ONE, x7)
    if x == 8:
        return x8
    x9 = shape_t(I)
    if x == 9:
        return x9
    x10 = decrement(x9)
    if x == 10:
        return x10
    x11 = x6(x10)
    if x == 11:
        return x11
    x12 = fill(x8, THREE, x11)
    if x == 12:
        return x12
    x13 = astuple(FIVE, FIVE)
    if x == 13:
        return x13
    x14 = x6(x13)
    if x == 14:
        return x14
    O = fill(x12, TWO, x14)
    return O
