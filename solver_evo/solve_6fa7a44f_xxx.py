def solve_6fa7a44f_one(S, I):
    return vconcat(I, mir_rot_t(I, R0))


def solve_6fa7a44f(S, I):
    x1 = mir_rot_t(I, R0)
    O = vconcat(I, x1)
    return O
