def solve_5c0a986e_one(S, I):
    return fill(fill(I, RED, shoot(corner(f_ofcolor(I, RED), R3), UNITY)), BLUE, shoot(corner(f_ofcolor(I, BLUE), R0), NEG_UNITY))


def solve_5c0a986e(S, I):
    x1 = f_ofcolor(I, RED)
    x2 = corner(x1, R3)
    x3 = shoot(x2, UNITY)
    x4 = fill(I, RED, x3)
    x5 = f_ofcolor(I, BLUE)
    x6 = corner(x5, R0)
    x7 = shoot(x6, NEG_UNITY)
    O = fill(x4, BLUE, x7)
    return O
