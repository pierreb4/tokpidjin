def solve_44f52bb0_one(S, I):
    return canvas(branch(equality(mir_rot_t(I, R2), I), ONE, SEVEN), UNITY)


def solve_44f52bb0(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = equality(x1, I)
    if x == 2:
        return x2
    x3 = branch(x2, ONE, SEVEN)
    if x == 3:
        return x3
    O = canvas(x3, UNITY)
    return O
