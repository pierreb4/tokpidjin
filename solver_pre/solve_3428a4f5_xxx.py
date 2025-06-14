def solve_3428a4f5_one(S, I):
    return fill(canvas(ZERO, astuple(SIX, FIVE)), THREE, difference(combine_f(f_ofcolor(tophalf(I), TWO), f_ofcolor(bottomhalf(I), TWO)), intersection(f_ofcolor(tophalf(I), TWO), f_ofcolor(bottomhalf(I), TWO))))


def solve_3428a4f5(S, I, x=0):
    x1 = astuple(SIX, FIVE)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = tophalf(I)
    if x == 3:
        return x3
    x4 = f_ofcolor(x3, TWO)
    if x == 4:
        return x4
    x5 = bottomhalf(I)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, TWO)
    if x == 6:
        return x6
    x7 = combine_f(x4, x6)
    if x == 7:
        return x7
    x8 = intersection(x4, x6)
    if x == 8:
        return x8
    x9 = difference(x7, x8)
    if x == 9:
        return x9
    O = fill(x2, THREE, x9)
    return O
