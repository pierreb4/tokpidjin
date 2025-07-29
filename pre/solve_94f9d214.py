def solve_94f9d214_one(S, I):
    return fill(canvas(ZERO, astuple(FOUR, FOUR)), TWO, intersection(f_ofcolor(tophalf(I), ZERO), f_ofcolor(bottomhalf(I), ZERO)))


def solve_94f9d214(S, I):
    x1 = astuple(FOUR, FOUR)
    x2 = canvas(ZERO, x1)
    x3 = tophalf(I)
    x4 = f_ofcolor(x3, ZERO)
    x5 = bottomhalf(I)
    x6 = f_ofcolor(x5, ZERO)
    x7 = intersection(x4, x6)
    O = fill(x2, TWO, x7)
    return O
