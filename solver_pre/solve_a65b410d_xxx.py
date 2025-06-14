def solve_a65b410d_one(S, I):
    return underfill(underfill(underfill(underfill(I, THREE, shoot(corner(f_ofcolor(I, TWO), R1), UP_RIGHT)), ONE, shoot(corner(f_ofcolor(I, TWO), R1), DOWN_LEFT)), ONE, mapply(rbind(shoot, LEFT), shoot(corner(f_ofcolor(I, TWO), R1), DOWN_LEFT))), THREE, mapply(rbind(shoot, LEFT), shoot(corner(f_ofcolor(I, TWO), R1), UP_RIGHT)))


def solve_a65b410d(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = corner(x1, R1)
    if x == 2:
        return x2
    x3 = shoot(x2, UP_RIGHT)
    if x == 3:
        return x3
    x4 = underfill(I, THREE, x3)
    if x == 4:
        return x4
    x5 = shoot(x2, DOWN_LEFT)
    if x == 5:
        return x5
    x6 = underfill(x4, ONE, x5)
    if x == 6:
        return x6
    x7 = rbind(shoot, LEFT)
    if x == 7:
        return x7
    x8 = mapply(x7, x5)
    if x == 8:
        return x8
    x9 = underfill(x6, ONE, x8)
    if x == 9:
        return x9
    x10 = mapply(x7, x3)
    if x == 10:
        return x10
    O = underfill(x9, THREE, x10)
    return O
