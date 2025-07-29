def solve_fafffa47_one(S, I):
    return fill(canvas(ZERO, shape_t(bottomhalf(I))), TWO, intersection(f_ofcolor(tophalf(I), ZERO), f_ofcolor(bottomhalf(I), ZERO)))


def solve_fafffa47(S, I):
    x1 = bottomhalf(I)
    x2 = shape_t(x1)
    x3 = canvas(ZERO, x2)
    x4 = tophalf(I)
    x5 = f_ofcolor(x4, ZERO)
    x6 = f_ofcolor(x1, ZERO)
    x7 = intersection(x5, x6)
    O = fill(x3, TWO, x7)
    return O
