def solve_46f33fce_one(S, I):
    return upscale_t(mir_rot_t(downscale(mir_rot_t(I, R5), TWO), R5), FOUR)


def solve_46f33fce(S, I):
    x1 = mir_rot_t(I, R5)
    x2 = downscale(x1, TWO)
    x3 = mir_rot_t(x2, R5)
    O = upscale_t(x3, FOUR)
    return O
