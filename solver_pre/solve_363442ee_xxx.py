def solve_363442ee_one(S, I):
    return paint(I, mapply(compose(lbind(shift, asobject(crop(I, ORIGIN, THREE_BY_THREE))), decrement), f_ofcolor(I, ONE)))


def solve_363442ee(S, I, x=0):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = asobject(x1)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = compose(x3, decrement)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, ONE)
    if x == 5:
        return x5
    x6 = mapply(x4, x5)
    if x == 6:
        return x6
    O = paint(I, x6)
    return O
