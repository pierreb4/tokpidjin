def solve_a68b268e_one(S, I):
    return fill(fill(fill(righthalf(bottomhalf(I)), CYAN, f_ofcolor(lefthalf(bottomhalf(I)), CYAN)), YELLOW, f_ofcolor(righthalf(tophalf(I)), YELLOW)), ORANGE, f_ofcolor(lefthalf(tophalf(I)), ORANGE))


def solve_a68b268e(S, I, x=0):
    x1 = bottomhalf(I)
    if x == 1:
        return x1
    x2 = righthalf(x1)
    if x == 2:
        return x2
    x3 = lefthalf(x1)
    if x == 3:
        return x3
    x4 = f_ofcolor(x3, CYAN)
    if x == 4:
        return x4
    x5 = fill(x2, CYAN, x4)
    if x == 5:
        return x5
    x6 = tophalf(I)
    if x == 6:
        return x6
    x7 = righthalf(x6)
    if x == 7:
        return x7
    x8 = f_ofcolor(x7, YELLOW)
    if x == 8:
        return x8
    x9 = fill(x5, YELLOW, x8)
    if x == 9:
        return x9
    x10 = lefthalf(x6)
    if x == 10:
        return x10
    x11 = f_ofcolor(x10, ORANGE)
    if x == 11:
        return x11
    O = fill(x9, ORANGE, x11)
    return O
