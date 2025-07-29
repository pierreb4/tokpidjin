def solve_d364b489_one(S, I):
    return fill(fill(fill(fill(I, EIGHT, shift(f_ofcolor(I, ONE), DOWN)), TWO, shift(f_ofcolor(I, ONE), UP)), SIX, shift(f_ofcolor(I, ONE), RIGHT)), SEVEN, shift(f_ofcolor(I, ONE), LEFT))


def solve_d364b489(S, I):
    x1 = f_ofcolor(I, ONE)
    x2 = shift(x1, DOWN)
    x3 = fill(I, EIGHT, x2)
    x4 = shift(x1, UP)
    x5 = fill(x3, TWO, x4)
    x6 = shift(x1, RIGHT)
    x7 = fill(x5, SIX, x6)
    x8 = shift(x1, LEFT)
    O = fill(x7, SEVEN, x8)
    return O
