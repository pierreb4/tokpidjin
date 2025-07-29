def solve_bdad9b1f_one(S, I):
    return fill(fill(fill(I, TWO, hfrontier(center(f_ofcolor(I, TWO)))), EIGHT, vfrontier(center(f_ofcolor(I, EIGHT)))), FOUR, intersection(hfrontier(center(f_ofcolor(I, TWO))), vfrontier(center(f_ofcolor(I, EIGHT)))))


def solve_bdad9b1f(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = center(x1)
    x3 = hfrontier(x2)
    x4 = fill(I, TWO, x3)
    x5 = f_ofcolor(I, EIGHT)
    x6 = center(x5)
    x7 = vfrontier(x6)
    x8 = fill(x4, EIGHT, x7)
    x9 = intersection(x3, x7)
    O = fill(x8, FOUR, x9)
    return O
