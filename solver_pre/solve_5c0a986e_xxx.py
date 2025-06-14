def solve_5c0a986e_one(S, I):
    return fill(fill(I, TWO, shoot(corner(f_ofcolor(I, TWO), R3), UNITY)), ONE, shoot(corner(f_ofcolor(I, ONE), R0), NEG_UNITY))


def solve_5c0a986e(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = corner(x1, R3)
    if x == 2:
        return x2
    x3 = shoot(x2, UNITY)
    if x == 3:
        return x3
    x4 = fill(I, TWO, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, ONE)
    if x == 5:
        return x5
    x6 = corner(x5, R0)
    if x == 6:
        return x6
    x7 = shoot(x6, NEG_UNITY)
    if x == 7:
        return x7
    O = fill(x4, ONE, x7)
    return O
