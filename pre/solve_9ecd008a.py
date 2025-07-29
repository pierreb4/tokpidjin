def solve_9ecd008a_one(S, I):
    return subgrid(f_ofcolor(I, ZERO), mir_rot_t(I, R2))


def solve_9ecd008a(S, I):
    x1 = f_ofcolor(I, ZERO)
    x2 = mir_rot_t(I, R2)
    O = subgrid(x1, x2)
    return O
