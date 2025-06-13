def solve_a1570a43_one(S, I):
    return move(I, recolor_i(RED, f_ofcolor(I, RED)), increment(subtract(corner(f_ofcolor(I, GREEN), R0), corner(f_ofcolor(I, RED), R0))))


def solve_a1570a43(S, I):
    x1 = f_ofcolor(I, RED)
    x2 = recolor_i(RED, x1)
    x3 = f_ofcolor(I, GREEN)
    x4 = corner(x3, R0)
    x5 = corner(x1, R0)
    x6 = subtract(x4, x5)
    x7 = increment(x6)
    O = move(I, x2, x7)
    return O
