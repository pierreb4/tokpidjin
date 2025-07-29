def solve_3428a4f5_one(S, I):
    return fill(canvas(ZERO, astuple(SIX, FIVE)), THREE, difference(combine_f(f_ofcolor(tophalf(I), TWO), f_ofcolor(bottomhalf(I), TWO)), intersection(f_ofcolor(tophalf(I), TWO), f_ofcolor(bottomhalf(I), TWO))))


def solve_3428a4f5(S, I):
    x1 = astuple(SIX, FIVE)
    x2 = canvas(ZERO, x1)
    x3 = tophalf(I)
    x4 = f_ofcolor(x3, TWO)
    x5 = bottomhalf(I)
    x6 = f_ofcolor(x5, TWO)
    x7 = combine_f(x4, x6)
    x8 = intersection(x4, x6)
    x9 = difference(x7, x8)
    O = fill(x2, THREE, x9)
    return O
