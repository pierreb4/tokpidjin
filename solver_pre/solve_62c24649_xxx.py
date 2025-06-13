def solve_62c24649_one(S, I):
    return vconcat(hconcat(I, mir_rot_t(I, R2)), mir_rot_t(hconcat(I, mir_rot_t(I, R2)), R0))


def solve_62c24649(S, I):
    x1 = mir_rot_t(I, R2)
    x2 = hconcat(I, x1)
    x3 = mir_rot_t(x2, R0)
    O = vconcat(x2, x3)
    return O
