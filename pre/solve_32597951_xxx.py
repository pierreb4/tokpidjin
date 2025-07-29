def solve_32597951_one(S, I):
    return fill(I, THREE, delta(f_ofcolor(I, EIGHT)))


def solve_32597951(S, I):
    x1 = f_ofcolor(I, EIGHT)
    x2 = delta(x1)
    O = fill(I, THREE, x2)
    return O
