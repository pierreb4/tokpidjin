def solve_9ecd008a_one(S, I):
    return subgrid(f_ofcolor(I, ZERO), mir_rot_t(I, R2))


def solve_9ecd008a(S, I, x=0):
    x1 = f_ofcolor(I, ZERO)
    if x == 1:
        return x1
    x2 = mir_rot_t(I, R2)
    if x == 2:
        return x2
    O = subgrid(x1, x2)
    return O
