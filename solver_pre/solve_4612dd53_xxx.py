def solve_4612dd53_one(S, I):
    return underfill(I, TWO, shift(f_ofcolor(fill(subgrid(f_ofcolor(I, ONE), fill(I, TWO, box(f_ofcolor(I, ONE)))), TWO, branch(greater(size_f(mapply(vfrontier, f_ofcolor(subgrid(f_ofcolor(I, ONE), fill(I, TWO, box(f_ofcolor(I, ONE)))), ONE))), size_f(mapply(hfrontier, f_ofcolor(subgrid(f_ofcolor(I, ONE), fill(I, TWO, box(f_ofcolor(I, ONE)))), ONE)))), mapply(hfrontier, f_ofcolor(subgrid(f_ofcolor(I, ONE), fill(I, TWO, box(f_ofcolor(I, ONE)))), ONE)), mapply(vfrontier, f_ofcolor(subgrid(f_ofcolor(I, ONE), fill(I, TWO, box(f_ofcolor(I, ONE)))), ONE)))), TWO), corner(f_ofcolor(I, ONE), R0)))


def solve_4612dd53(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = box(x1)
    if x == 2:
        return x2
    x3 = fill(I, TWO, x2)
    if x == 3:
        return x3
    x4 = subgrid(x1, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(x4, ONE)
    if x == 5:
        return x5
    x6 = mapply(vfrontier, x5)
    if x == 6:
        return x6
    x7 = size_f(x6)
    if x == 7:
        return x7
    x8 = mapply(hfrontier, x5)
    if x == 8:
        return x8
    x9 = size_f(x8)
    if x == 9:
        return x9
    x10 = greater(x7, x9)
    if x == 10:
        return x10
    x11 = branch(x10, x8, x6)
    if x == 11:
        return x11
    x12 = fill(x4, TWO, x11)
    if x == 12:
        return x12
    x13 = f_ofcolor(x12, TWO)
    if x == 13:
        return x13
    x14 = corner(x1, R0)
    if x == 14:
        return x14
    x15 = shift(x13, x14)
    if x == 15:
        return x15
    O = underfill(I, TWO, x15)
    return O
