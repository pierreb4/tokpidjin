def solve_c9e6f938_one(S, I):
    return hconcat(I, mir_rot_t(I, R2))


def solve_c9e6f938(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    O = hconcat(I, x1)
    return O
