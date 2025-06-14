def solve_94f9d214_one(S, I):
    return fill(canvas(ZERO, astuple(FOUR, FOUR)), TWO, intersection(f_ofcolor(tophalf(I), ZERO), f_ofcolor(bottomhalf(I), ZERO)))


def solve_94f9d214(S, I, x=0):
    x1 = astuple(FOUR, FOUR)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
    if x == 2:
        return x2
    x3 = tophalf(I)
    if x == 3:
        return x3
    x4 = f_ofcolor(x3, ZERO)
    if x == 4:
        return x4
    x5 = bottomhalf(I)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, ZERO)
    if x == 6:
        return x6
    x7 = intersection(x4, x6)
    if x == 7:
        return x7
    O = fill(x2, TWO, x7)
    return O
