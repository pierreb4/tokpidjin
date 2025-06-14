def solve_0ca9ddb6_one(S, I):
    return fill(fill(I, SEVEN, mapply(dneighbors, f_ofcolor(I, ONE))), FOUR, mapply(ineighbors, f_ofcolor(I, TWO)))


def solve_0ca9ddb6(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = mapply(dneighbors, x1)
    if x == 2:
        return x2
    x3 = fill(I, SEVEN, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, TWO)
    if x == 4:
        return x4
    x5 = mapply(ineighbors, x4)
    if x == 5:
        return x5
    O = fill(x3, FOUR, x5)
    return O
