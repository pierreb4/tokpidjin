def solve_b60334d2_one(S, I):
    return fill(fill(replace(I, FIVE, ZERO), ONE, mapply(dneighbors, f_ofcolor(I, FIVE))), FIVE, mapply(ineighbors, f_ofcolor(I, FIVE)))


def solve_b60334d2(S, I):
    x1 = replace(I, FIVE, ZERO)
    x2 = f_ofcolor(I, FIVE)
    x3 = mapply(dneighbors, x2)
    x4 = fill(x1, ONE, x3)
    x5 = mapply(ineighbors, x2)
    O = fill(x4, FIVE, x5)
    return O
