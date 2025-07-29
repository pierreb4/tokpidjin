def solve_ff805c23_one(S, I):
    return branch(contained(ONE, palette_t(subgrid(f_ofcolor(I, ONE), mir_rot_t(I, R0)))), subgrid(f_ofcolor(I, ONE), mir_rot_t(I, R2)), subgrid(f_ofcolor(I, ONE), mir_rot_t(I, R0)))


def solve_ff805c23(S, I):
    x1 = f_ofcolor(I, ONE)
    x2 = mir_rot_t(I, R0)
    x3 = subgrid(x1, x2)
    x4 = palette_t(x3)
    x5 = contained(ONE, x4)
    x6 = mir_rot_t(I, R2)
    x7 = subgrid(x1, x6)
    O = branch(x5, x7, x3)
    return O
