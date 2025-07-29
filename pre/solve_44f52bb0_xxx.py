def solve_44f52bb0_one(S, I):
    return canvas(branch(equality(mir_rot_t(I, R2), I), ONE, SEVEN), UNITY)


def solve_44f52bb0(S, I):
    x1 = mir_rot_t(I, R2)
    x2 = equality(x1, I)
    x3 = branch(x2, ONE, SEVEN)
    O = canvas(x3, UNITY)
    return O
