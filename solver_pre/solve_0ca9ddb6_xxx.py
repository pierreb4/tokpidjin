def solve_0ca9ddb6_one(S, I):
    return fill(fill(I, SEVEN, mapply(dneighbors, f_ofcolor(I, ONE))), FOUR, mapply(ineighbors, f_ofcolor(I, TWO)))


def solve_0ca9ddb6(S, I):
    x1 = f_ofcolor(I, ONE)
    x2 = mapply(dneighbors, x1)
    x3 = fill(I, SEVEN, x2)
    x4 = f_ofcolor(I, TWO)
    x5 = mapply(ineighbors, x4)
    O = fill(x3, FOUR, x5)
    return O
