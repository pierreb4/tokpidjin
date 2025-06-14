def solve_e3497940_one(S, I):
    return paint(lefthalf(I), merge_f(o_g(mir_rot_t(righthalf(I), R2), R5)))


def solve_e3497940(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = righthalf(I)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R2)
    if x == 3:
        return x3
    x4 = o_g(x3, R5)
    if x == 4:
        return x4
    x5 = merge_f(x4)
    if x == 5:
        return x5
    O = paint(x1, x5)
    return O
