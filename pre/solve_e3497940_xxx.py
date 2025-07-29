def solve_e3497940_one(S, I):
    return paint(lefthalf(I), merge_f(o_g(mir_rot_t(righthalf(I), R2), R5)))


def solve_e3497940(S, I):
    x1 = lefthalf(I)
    x2 = righthalf(I)
    x3 = mir_rot_t(x2, R2)
    x4 = o_g(x3, R5)
    x5 = merge_f(x4)
    O = paint(x1, x5)
    return O
