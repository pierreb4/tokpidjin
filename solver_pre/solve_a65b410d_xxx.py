def solve_a65b410d_one(S, I):
    return underfill(underfill(underfill(underfill(I, THREE, shoot(corner(f_ofcolor(I, TWO), R1), UP_RIGHT)), ONE, shoot(corner(f_ofcolor(I, TWO), R1), DOWN_LEFT)), ONE, mapply(rbind(shoot, LEFT), shoot(corner(f_ofcolor(I, TWO), R1), DOWN_LEFT))), THREE, mapply(rbind(shoot, LEFT), shoot(corner(f_ofcolor(I, TWO), R1), UP_RIGHT)))


def solve_a65b410d(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = corner(x1, R1)
    x3 = shoot(x2, UP_RIGHT)
    x4 = underfill(I, THREE, x3)
    x5 = shoot(x2, DOWN_LEFT)
    x6 = underfill(x4, ONE, x5)
    x7 = rbind(shoot, LEFT)
    x8 = mapply(x7, x5)
    x9 = underfill(x6, ONE, x8)
    x10 = mapply(x7, x3)
    O = underfill(x9, THREE, x10)
    return O
