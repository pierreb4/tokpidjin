def solve_a699fb00_one(S, I):
    return fill(I, TWO, intersection(shift(f_ofcolor(I, ONE), RIGHT), shift(f_ofcolor(I, ONE), LEFT)))


def solve_a699fb00(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = shift(x1, RIGHT)
    if x == 2:
        return x2
    x3 = shift(x1, LEFT)
    if x == 3:
        return x3
    x4 = intersection(x2, x3)
    if x == 4:
        return x4
    O = fill(I, TWO, x4)
    return O
