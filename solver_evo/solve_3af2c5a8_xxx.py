def solve_3af2c5a8_one(S, I):
    return vconcat(hconcat(I, mir_rot_t(I, R2)), mir_rot_t(hconcat(I, mir_rot_t(I, R2)), R0))


def solve_3af2c5a8(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = hconcat(I, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R0)
    if x == 3:
        return x3
    O = vconcat(x2, x3)
    return O
