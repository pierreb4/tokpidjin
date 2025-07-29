def solve_f2829549_one(S, I):
    return fill(canvas(ZERO, shape_t(lefthalf(I))), THREE, intersection(f_ofcolor(lefthalf(I), ZERO), f_ofcolor(righthalf(I), ZERO)))


def solve_f2829549(S, I):
    x1 = lefthalf(I)
    x2 = shape_t(x1)
    x3 = canvas(ZERO, x2)
    x4 = f_ofcolor(x1, ZERO)
    x5 = righthalf(I)
    x6 = f_ofcolor(x5, ZERO)
    x7 = intersection(x4, x6)
    O = fill(x3, THREE, x7)
    return O
