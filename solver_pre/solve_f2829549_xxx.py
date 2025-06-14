def solve_f2829549_one(S, I):
    return fill(canvas(ZERO, shape_t(lefthalf(I))), THREE, intersection(f_ofcolor(lefthalf(I), ZERO), f_ofcolor(righthalf(I), ZERO)))


def solve_f2829549(S, I, x=0):
    x1 = lefthalf(I)
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
    x5 = righthalf(I)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, ZERO)
    if x == 6:
        return x6
    x7 = intersection(x4, x6)
    if x == 7:
        return x7
    O = fill(x3, THREE, x7)
    return O
