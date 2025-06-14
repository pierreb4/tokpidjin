def solve_fafffa47_one(S, I):
    return fill(canvas(ZERO, shape_t(bottomhalf(I))), TWO, intersection(f_ofcolor(tophalf(I), ZERO), f_ofcolor(bottomhalf(I), ZERO)))


def solve_fafffa47(S, I, x=0):
    x1 = bottomhalf(I)
    if x == 1:
        return x1
    x2 = shape_t(x1)
    if x == 2:
        return x2
    x3 = canvas(ZERO, x2)
    if x == 3:
        return x3
    x4 = tophalf(I)
    if x == 4:
        return x4
    x5 = f_ofcolor(x4, ZERO)
    if x == 5:
        return x5
    x6 = f_ofcolor(x1, ZERO)
    if x == 6:
        return x6
    x7 = intersection(x5, x6)
    if x == 7:
        return x7
    O = fill(x3, TWO, x7)
    return O
