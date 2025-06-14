def solve_913fb3ed_one(S, I):
    return fill(fill(fill(I, SIX, mapply(neighbors, f_ofcolor(I, THREE))), FOUR, mapply(neighbors, f_ofcolor(I, EIGHT))), ONE, mapply(neighbors, f_ofcolor(I, TWO)))


def solve_913fb3ed(S, I, x=0):
    x1 = f_ofcolor(I, THREE)
    if x == 1:
        return x1
    x2 = mapply(neighbors, x1)
    if x == 2:
        return x2
    x3 = fill(I, SIX, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = mapply(neighbors, x4)
    if x == 5:
        return x5
    x6 = fill(x3, FOUR, x5)
    if x == 6:
        return x6
    x7 = f_ofcolor(I, TWO)
    if x == 7:
        return x7
    x8 = mapply(neighbors, x7)
    if x == 8:
        return x8
    O = fill(x6, ONE, x8)
    return O
