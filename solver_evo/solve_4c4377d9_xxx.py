def solve_4c4377d9_one(S, I):
    return vconcat(mir_rot_t(I, R0), I)


def solve_4c4377d9(S, I, x=0):
    x1 = mir_rot_t(I, R0)
    if x == 1:
        return x1
    O = vconcat(x1, I)
    return O
