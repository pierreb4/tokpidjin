def solve_8d5021e8_one(S, I):
    return mir_rot_t(vconcat(vconcat(hconcat(mir_rot_t(I, R2), I), mir_rot_t(hconcat(mir_rot_t(I, R2), I), R0)), hconcat(mir_rot_t(I, R2), I)), R0)


def solve_8d5021e8(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = hconcat(x1, I)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R0)
    if x == 3:
        return x3
    x4 = vconcat(x2, x3)
    if x == 4:
        return x4
    x5 = vconcat(x4, x2)
    if x == 5:
        return x5
    O = mir_rot_t(x5, R0)
    return O
