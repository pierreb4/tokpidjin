def solve_d364b489_one(S, I):
    return fill(fill(fill(fill(I, EIGHT, shift(f_ofcolor(I, ONE), DOWN)), TWO, shift(f_ofcolor(I, ONE), UP)), SIX, shift(f_ofcolor(I, ONE), RIGHT)), SEVEN, shift(f_ofcolor(I, ONE), LEFT))


def solve_d364b489(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = shift(x1, DOWN)
    if x == 2:
        return x2
    x3 = fill(I, EIGHT, x2)
    if x == 3:
        return x3
    x4 = shift(x1, UP)
    if x == 4:
        return x4
    x5 = fill(x3, TWO, x4)
    if x == 5:
        return x5
    x6 = shift(x1, RIGHT)
    if x == 6:
        return x6
    x7 = fill(x5, SIX, x6)
    if x == 7:
        return x7
    x8 = shift(x1, LEFT)
    if x == 8:
        return x8
    O = fill(x7, SEVEN, x8)
    return O
