def solve_b60334d2_one(S, I):
    return fill(fill(replace(I, FIVE, ZERO), ONE, mapply(dneighbors, f_ofcolor(I, FIVE))), FIVE, mapply(ineighbors, f_ofcolor(I, FIVE)))


def solve_b60334d2(S, I, x=0):
    x1 = replace(I, FIVE, ZERO)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, FIVE)
    if x == 2:
        return x2
    x3 = mapply(dneighbors, x2)
    if x == 3:
        return x3
    x4 = fill(x1, ONE, x3)
    if x == 4:
        return x4
    x5 = mapply(ineighbors, x2)
    if x == 5:
        return x5
    O = fill(x4, FIVE, x5)
    return O
