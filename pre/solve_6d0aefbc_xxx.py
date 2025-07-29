def solve_6d0aefbc_one(S, I):
    return hconcat(I, mir_rot_t(I, R2))


def solve_6d0aefbc(S, I):
    x1 = mir_rot_t(I, R2)
    O = hconcat(I, x1)
    return O
