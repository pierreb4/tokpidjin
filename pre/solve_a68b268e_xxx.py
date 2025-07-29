def solve_a68b268e_one(S, I):
    return fill(fill(fill(righthalf(bottomhalf(I)), EIGHT, f_ofcolor(lefthalf(bottomhalf(I)), EIGHT)), FOUR, f_ofcolor(righthalf(tophalf(I)), FOUR)), SEVEN, f_ofcolor(lefthalf(tophalf(I)), SEVEN))


def solve_a68b268e(S, I):
    x1 = bottomhalf(I)
    x2 = righthalf(x1)
    x3 = lefthalf(x1)
    x4 = f_ofcolor(x3, EIGHT)
    x5 = fill(x2, EIGHT, x4)
    x6 = tophalf(I)
    x7 = righthalf(x6)
    x8 = f_ofcolor(x7, FOUR)
    x9 = fill(x5, FOUR, x8)
    x10 = lefthalf(x6)
    x11 = f_ofcolor(x10, SEVEN)
    O = fill(x9, SEVEN, x11)
    return O
