def solve_4258a5f9_one(S, I):
    return fill(I, ONE, mapply(neighbors, f_ofcolor(I, FIVE)))


def solve_4258a5f9(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = mapply(neighbors, x1)
    if x == 2:
        return x2
    O = fill(I, ONE, x2)
    return O
