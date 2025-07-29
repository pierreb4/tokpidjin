def solve_0520fde7_one(S, I):
    return replace(cellwise(lefthalf(mir_rot_t(I, R2)), mir_rot_t(righthalf(mir_rot_t(I, R2)), R2), ZERO), ONE, TWO)


def solve_0520fde7(S, I):
    x1 = mir_rot_t(I, R2)
    x2 = lefthalf(x1)
    x3 = righthalf(x1)
    x4 = mir_rot_t(x3, R2)
    x5 = cellwise(x2, x4, ZERO)
    O = replace(x5, ONE, TWO)
    return O
