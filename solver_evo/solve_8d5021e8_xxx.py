def solve_8d5021e8_one(S, I):
    return mir_rot_t(vconcat(vconcat(hconcat(mir_rot_t(I, R2), I), mir_rot_t(hconcat(mir_rot_t(I, R2), I), R0)), hconcat(mir_rot_t(I, R2), I)), R0)


def solve_8d5021e8(S, I):
    x1 = mir_rot_t(I, R2)
    x2 = hconcat(x1, I)
    x3 = mir_rot_t(x2, R0)
    x4 = vconcat(x2, x3)
    x5 = vconcat(x4, x2)
    O = mir_rot_t(x5, R0)
    return O
