def solve_46442a0e_one(S, I):
    return vconcat(hconcat(I, mir_rot_t(I, R4)), hconcat(mir_rot_t(I, R6), mir_rot_t(I, R5)))


def solve_46442a0e(S, I):
    x1 = mir_rot_t(I, R4)
    x2 = hconcat(I, x1)
    x3 = mir_rot_t(I, R6)
    x4 = mir_rot_t(I, R5)
    x5 = hconcat(x3, x4)
    O = vconcat(x2, x5)
    return O
