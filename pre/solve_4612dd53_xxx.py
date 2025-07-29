def solve_4612dd53_one(S, I):
    return underfill(I, TWO, shift(f_ofcolor(fill(subgrid(f_ofcolor(I, ONE), fill(I, TWO, box(f_ofcolor(I, ONE)))), TWO, branch(greater(size_f(mapply(vfrontier, f_ofcolor(subgrid(f_ofcolor(I, ONE), fill(I, TWO, box(f_ofcolor(I, ONE)))), ONE))), size_f(mapply(hfrontier, f_ofcolor(subgrid(f_ofcolor(I, ONE), fill(I, TWO, box(f_ofcolor(I, ONE)))), ONE)))), mapply(hfrontier, f_ofcolor(subgrid(f_ofcolor(I, ONE), fill(I, TWO, box(f_ofcolor(I, ONE)))), ONE)), mapply(vfrontier, f_ofcolor(subgrid(f_ofcolor(I, ONE), fill(I, TWO, box(f_ofcolor(I, ONE)))), ONE)))), TWO), corner(f_ofcolor(I, ONE), R0)))


def solve_4612dd53(S, I):
    x1 = f_ofcolor(I, ONE)
    x2 = box(x1)
    x3 = fill(I, TWO, x2)
    x4 = subgrid(x1, x3)
    x5 = f_ofcolor(x4, ONE)
    x6 = mapply(vfrontier, x5)
    x7 = size_f(x6)
    x8 = mapply(hfrontier, x5)
    x9 = size_f(x8)
    x10 = greater(x7, x9)
    x11 = branch(x10, x8, x6)
    x12 = fill(x4, TWO, x11)
    x13 = f_ofcolor(x12, TWO)
    x14 = corner(x1, R0)
    x15 = shift(x13, x14)
    O = underfill(I, TWO, x15)
    return O
