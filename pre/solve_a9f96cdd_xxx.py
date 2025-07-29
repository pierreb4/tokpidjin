def solve_a9f96cdd_one(S, I):
    return fill(fill(fill(fill(replace(I, TWO, ZERO), THREE, shift(f_ofcolor(I, TWO), NEG_UNITY)), SIX, shift(f_ofcolor(I, TWO), UP_RIGHT)), EIGHT, shift(f_ofcolor(I, TWO), DOWN_LEFT)), SEVEN, shift(f_ofcolor(I, TWO), UNITY))


def solve_a9f96cdd(S, I):
    x1 = replace(I, TWO, ZERO)
    x2 = f_ofcolor(I, TWO)
    x3 = shift(x2, NEG_UNITY)
    x4 = fill(x1, THREE, x3)
    x5 = shift(x2, UP_RIGHT)
    x6 = fill(x4, SIX, x5)
    x7 = shift(x2, DOWN_LEFT)
    x8 = fill(x6, EIGHT, x7)
    x9 = shift(x2, UNITY)
    O = fill(x8, SEVEN, x9)
    return O
