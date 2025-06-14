def solve_8be77c9e_one(S, I):
    return vconcat(I, mir_rot_t(I, R0))


def solve_8be77c9e(S, I, x=0):
    x1 = mir_rot_t(I, R0)
    if x == 1:
        return x1
    O = vconcat(I, x1)
    return O
