def solve_a68b268e_one(S, I):
    return fill(fill(fill(righthalf(bottomhalf(I)), CYAN, f_ofcolor(lefthalf(bottomhalf(I)), CYAN)), YELLOW, f_ofcolor(righthalf(tophalf(I)), YELLOW)), ORANGE, f_ofcolor(lefthalf(tophalf(I)), ORANGE))


def solve_a68b268e(S, I):
    x1 = bottomhalf(I)
    x2 = righthalf(x1)
    x3 = lefthalf(x1)
    x4 = f_ofcolor(x3, CYAN)
    x5 = fill(x2, CYAN, x4)
    x6 = tophalf(I)
    x7 = righthalf(x6)
    x8 = f_ofcolor(x7, YELLOW)
    x9 = fill(x5, YELLOW, x8)
    x10 = lefthalf(x6)
    x11 = f_ofcolor(x10, ORANGE)
    O = fill(x9, ORANGE, x11)
    return O
