def solve_bdad9b1f_one(S, I):
    return fill(fill(fill(I, TWO, hfrontier(center(f_ofcolor(I, TWO)))), EIGHT, vfrontier(center(f_ofcolor(I, EIGHT)))), FOUR, intersection(hfrontier(center(f_ofcolor(I, TWO))), vfrontier(center(f_ofcolor(I, EIGHT)))))


def solve_bdad9b1f(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = center(x1)
    if x == 2:
        return x2
    x3 = hfrontier(x2)
    if x == 3:
        return x3
    x4 = fill(I, TWO, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, EIGHT)
    if x == 5:
        return x5
    x6 = center(x5)
    if x == 6:
        return x6
    x7 = vfrontier(x6)
    if x == 7:
        return x7
    x8 = fill(x4, EIGHT, x7)
    if x == 8:
        return x8
    x9 = intersection(x3, x7)
    if x == 9:
        return x9
    O = fill(x8, FOUR, x9)
    return O
