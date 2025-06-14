def solve_a9f96cdd_one(S, I):
    return fill(fill(fill(fill(replace(I, TWO, ZERO), THREE, shift(f_ofcolor(I, TWO), NEG_UNITY)), SIX, shift(f_ofcolor(I, TWO), UP_RIGHT)), EIGHT, shift(f_ofcolor(I, TWO), DOWN_LEFT)), SEVEN, shift(f_ofcolor(I, TWO), UNITY))


def solve_a9f96cdd(S, I, x=0):
    x1 = replace(I, TWO, ZERO)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, TWO)
    if x == 2:
        return x2
    x3 = shift(x2, NEG_UNITY)
    if x == 3:
        return x3
    x4 = fill(x1, THREE, x3)
    if x == 4:
        return x4
    x5 = shift(x2, UP_RIGHT)
    if x == 5:
        return x5
    x6 = fill(x4, SIX, x5)
    if x == 6:
        return x6
    x7 = shift(x2, DOWN_LEFT)
    if x == 7:
        return x7
    x8 = fill(x6, EIGHT, x7)
    if x == 8:
        return x8
    x9 = shift(x2, UNITY)
    if x == 9:
        return x9
    O = fill(x8, SEVEN, x9)
    return O
