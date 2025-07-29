def solve_913fb3ed_one(S, I):
    return fill(fill(fill(I, SIX, mapply(neighbors, f_ofcolor(I, THREE))), FOUR, mapply(neighbors, f_ofcolor(I, EIGHT))), ONE, mapply(neighbors, f_ofcolor(I, TWO)))


def solve_913fb3ed(S, I):
    x1 = f_ofcolor(I, THREE)
    x2 = mapply(neighbors, x1)
    x3 = fill(I, SIX, x2)
    x4 = f_ofcolor(I, EIGHT)
    x5 = mapply(neighbors, x4)
    x6 = fill(x3, FOUR, x5)
    x7 = f_ofcolor(I, TWO)
    x8 = mapply(neighbors, x7)
    O = fill(x6, ONE, x8)
    return O
