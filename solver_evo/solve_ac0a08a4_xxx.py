def solve_ac0a08a4_one(S, I):
    return upscale_t(I, decrement(numcolors_t(I)))


def solve_ac0a08a4(S, I):
    x1 = numcolors_t(I)
    x2 = decrement(x1)
    O = upscale_t(I, x2)
    return O
