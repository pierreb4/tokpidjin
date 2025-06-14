def solve_a1570a43_one(S, I):
    return move(I, recolor_i(TWO, f_ofcolor(I, TWO)), increment(subtract(corner(f_ofcolor(I, THREE), R0), corner(f_ofcolor(I, TWO), R0))))


def solve_a1570a43(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = recolor_i(TWO, x1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, THREE)
    if x == 3:
        return x3
    x4 = corner(x3, R0)
    if x == 4:
        return x4
    x5 = corner(x1, R0)
    if x == 5:
        return x5
    x6 = subtract(x4, x5)
    if x == 6:
        return x6
    x7 = increment(x6)
    if x == 7:
        return x7
    O = move(I, x2, x7)
    return O
