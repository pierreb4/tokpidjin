def solve_1b2d62fb_one(S, I):
    return fill(replace(lefthalf(I), NINE, ZERO), EIGHT, intersection(f_ofcolor(lefthalf(I), ZERO), f_ofcolor(righthalf(I), ZERO)))


def solve_1b2d62fb(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = replace(x1, NINE, ZERO)
    if x == 2:
        return x2
    x3 = f_ofcolor(x1, ZERO)
    if x == 3:
        return x3
    x4 = righthalf(I)
    if x == 4:
        return x4
    x5 = f_ofcolor(x4, ZERO)
    if x == 5:
        return x5
    x6 = intersection(x3, x5)
    if x == 6:
        return x6
    O = fill(x2, EIGHT, x6)
    return O
