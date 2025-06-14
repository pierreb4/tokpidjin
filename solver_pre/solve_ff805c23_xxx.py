def solve_ff805c23_one(S, I):
    return branch(contained(ONE, palette_t(subgrid(f_ofcolor(I, ONE), mir_rot_t(I, R0)))), subgrid(f_ofcolor(I, ONE), mir_rot_t(I, R2)), subgrid(f_ofcolor(I, ONE), mir_rot_t(I, R0)))


def solve_ff805c23(S, I, x=0):
    x1 = f_ofcolor(I, ONE)
    if x == 1:
        return x1
    x2 = mir_rot_t(I, R0)
    if x == 2:
        return x2
    x3 = subgrid(x1, x2)
    if x == 3:
        return x3
    x4 = palette_t(x3)
    if x == 4:
        return x4
    x5 = contained(ONE, x4)
    if x == 5:
        return x5
    x6 = mir_rot_t(I, R2)
    if x == 6:
        return x6
    x7 = subgrid(x1, x6)
    if x == 7:
        return x7
    O = branch(x5, x7, x3)
    return O
