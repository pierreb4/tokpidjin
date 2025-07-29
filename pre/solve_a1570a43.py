def solve_a1570a43_one(S, I):
    return move(I, recolor_i(TWO, f_ofcolor(I, TWO)), increment(subtract(corner(f_ofcolor(I, THREE), R0), corner(f_ofcolor(I, TWO), R0))))


def solve_a1570a43(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = recolor_i(TWO, x1)
    x3 = f_ofcolor(I, THREE)
    x4 = corner(x3, R0)
    x5 = corner(x1, R0)
    x6 = subtract(x4, x5)
    x7 = increment(x6)
    O = move(I, x2, x7)
    return O
