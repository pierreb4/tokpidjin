def solve_1b2d62fb_one(S, I):
    return fill(replace(lefthalf(I), NINE, ZERO), EIGHT, intersection(f_ofcolor(lefthalf(I), ZERO), f_ofcolor(righthalf(I), ZERO)))


def solve_1b2d62fb(S, I):
    x1 = lefthalf(I)
    x2 = replace(x1, NINE, ZERO)
    x3 = f_ofcolor(x1, ZERO)
    x4 = righthalf(I)
    x5 = f_ofcolor(x4, ZERO)
    x6 = intersection(x3, x5)
    O = fill(x2, EIGHT, x6)
    return O
