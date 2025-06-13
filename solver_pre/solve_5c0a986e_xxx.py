def solve_5c0a986e_one(S, I):
    return fill(fill(I, TWO, shoot(corner(f_ofcolor(I, TWO), R3), UNITY)), ONE, shoot(corner(f_ofcolor(I, ONE), R0), NEG_UNITY))


def solve_5c0a986e(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = corner(x1, R3)
    x3 = shoot(x2, UNITY)
    x4 = fill(I, TWO, x3)
    x5 = f_ofcolor(I, ONE)
    x6 = corner(x5, R0)
    x7 = shoot(x6, NEG_UNITY)
    O = fill(x4, ONE, x7)
    return O
