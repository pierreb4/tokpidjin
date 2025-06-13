def solve_99b1bc43_one(S, I):
    return fill(canvas(ZERO, shape_t(tophalf(I))), THREE, difference(combine_f(f_ofcolor(tophalf(I), ZERO), f_ofcolor(bottomhalf(I), ZERO)), intersection(f_ofcolor(tophalf(I), ZERO), f_ofcolor(bottomhalf(I), ZERO))))


def solve_99b1bc43(S, I):
    x1 = tophalf(I)
    x2 = shape_t(x1)
    x3 = canvas(ZERO, x2)
    x4 = f_ofcolor(x1, ZERO)
    x5 = bottomhalf(I)
    x6 = f_ofcolor(x5, ZERO)
    x7 = combine_f(x4, x6)
    x8 = intersection(x4, x6)
    x9 = difference(x7, x8)
    O = fill(x3, THREE, x9)
    return O
