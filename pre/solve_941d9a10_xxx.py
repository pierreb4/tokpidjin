def solve_941d9a10_one(S, I):
    return fill(fill(fill(I, ONE, compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(lbind, contained))(ORIGIN)), THREE, compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(lbind, contained))(decrement(shape_t(I)))), TWO, compose(lbind(extract, apply(toindices, colorfilter(o_g(I, R4), ZERO))), lbind(lbind, contained))(astuple(FIVE, FIVE)))


def solve_941d9a10(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, ZERO)
    x3 = apply(toindices, x2)
    x4 = lbind(extract, x3)
    x5 = lbind(lbind, contained)
    x6 = compose(x4, x5)
    x7 = x6(ORIGIN)
    x8 = fill(I, ONE, x7)
    x9 = shape_t(I)
    x10 = decrement(x9)
    x11 = x6(x10)
    x12 = fill(x8, THREE, x11)
    x13 = astuple(FIVE, FIVE)
    x14 = x6(x13)
    O = fill(x12, TWO, x14)
    return O
