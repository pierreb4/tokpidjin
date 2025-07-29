def solve_ce4f8723_one(S, I):
    return fill(canvas(THREE, astuple(FOUR, FOUR)), ZERO, intersection(f_ofcolor(tophalf(I), ZERO), f_ofcolor(bottomhalf(I), ZERO)))


def solve_ce4f8723(S, I):
    x1 = astuple(FOUR, FOUR)
    x2 = canvas(THREE, x1)
    x3 = tophalf(I)
    x4 = f_ofcolor(x3, ZERO)
    x5 = bottomhalf(I)
    x6 = f_ofcolor(x5, ZERO)
    x7 = intersection(x4, x6)
    O = fill(x2, ZERO, x7)
    return O
