def solve_a699fb00_one(S, I):
    return fill(I, TWO, intersection(shift(f_ofcolor(I, ONE), RIGHT), shift(f_ofcolor(I, ONE), LEFT)))


def solve_a699fb00(S, I):
    x1 = f_ofcolor(I, ONE)
    x2 = shift(x1, RIGHT)
    x3 = shift(x1, LEFT)
    x4 = intersection(x2, x3)
    O = fill(I, TWO, x4)
    return O
