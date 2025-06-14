def solve_46f33fce_one(S, I):
    return upscale_t(mir_rot_t(downscale(mir_rot_t(I, R5), TWO), R5), FOUR)


def solve_46f33fce(S, I, x=0):
    x1 = mir_rot_t(I, R5)
    if x == 1:
        return x1
    x2 = downscale(x1, TWO)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R5)
    if x == 3:
        return x3
    O = upscale_t(x3, FOUR)
    return O
