def solve_7fe24cdd_one(S, I):
    return vconcat(hconcat(I, mir_rot_t(I, R4)), hconcat(mir_rot_t(I, R6), mir_rot_t(I, R5)))


def solve_7fe24cdd(S, I, x=0):
    x1 = mir_rot_t(I, R4)
    if x == 1:
        return x1
    x2 = hconcat(I, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(I, R6)
    if x == 3:
        return x3
    x4 = mir_rot_t(I, R5)
    if x == 4:
        return x4
    x5 = hconcat(x3, x4)
    if x == 5:
        return x5
    O = vconcat(x2, x5)
    return O
