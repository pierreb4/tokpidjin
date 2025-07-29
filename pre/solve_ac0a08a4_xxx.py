def solve_ac0a08a4_one(S, I):
    return upscale_t(I, subtract(NINE, colorcount_t(I, ZERO)))


def solve_ac0a08a4(S, I):
    x1 = colorcount_t(I, ZERO)
    x2 = subtract(NINE, x1)
    O = upscale_t(I, x2)
    return O
