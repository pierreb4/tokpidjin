def solve_4258a5f9_one(S, I):
    return fill(I, ONE, mapply(neighbors, f_ofcolor(I, FIVE)))


def solve_4258a5f9(S, I):
    x1 = f_ofcolor(I, FIVE)
    x2 = mapply(neighbors, x1)
    O = fill(I, ONE, x2)
    return O
