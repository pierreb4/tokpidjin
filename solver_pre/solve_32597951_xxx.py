def solve_32597951_one(S, I):
    return fill(I, THREE, delta(f_ofcolor(I, EIGHT)))


def solve_32597951(S, I, x=0):
    x1 = f_ofcolor(I, EIGHT)
    if x == 1:
        return x1
    x2 = delta(x1)
    if x == 2:
        return x2
    O = fill(I, THREE, x2)
    return O
