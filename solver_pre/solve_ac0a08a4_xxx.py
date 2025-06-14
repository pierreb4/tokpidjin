def solve_ac0a08a4_one(S, I):
    return upscale_t(I, subtract(NINE, colorcount_t(I, ZERO)))


def solve_ac0a08a4(S, I, x=0):
    x1 = colorcount_t(I, ZERO)
    if x == 1:
        return x1
    x2 = subtract(NINE, x1)
    if x == 2:
        return x2
    O = upscale_t(I, x2)
    return O
