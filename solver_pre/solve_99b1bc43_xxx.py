def solve_99b1bc43_one(S, I):
    return fill(canvas(ZERO, shape_t(tophalf(I))), THREE, difference(combine_f(f_ofcolor(tophalf(I), ZERO), f_ofcolor(bottomhalf(I), ZERO)), intersection(f_ofcolor(tophalf(I), ZERO), f_ofcolor(bottomhalf(I), ZERO))))


def solve_99b1bc43(S, I, x=0):
    x1 = tophalf(I)
    if x == 1:
        return x1
    x2 = shape_t(x1)
    if x == 2:
        return x2
    x3 = canvas(ZERO, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(x1, ZERO)
    if x == 4:
        return x4
    x5 = bottomhalf(I)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, ZERO)
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
    O = fill(x3, THREE, x9)
    return O
