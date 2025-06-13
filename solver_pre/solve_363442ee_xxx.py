def solve_363442ee_one(S, I):
    return paint(I, mapply(compose(lbind(shift, asobject(crop(I, ORIGIN, THREE_BY_THREE))), decrement), f_ofcolor(I, ONE)))


def solve_363442ee(S, I):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    x2 = asobject(x1)
    x3 = lbind(shift, x2)
    x4 = compose(x3, decrement)
    x5 = f_ofcolor(I, ONE)
    x6 = mapply(x4, x5)
    O = paint(I, x6)
    return O
