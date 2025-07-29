def solve_b91ae062_one(S, I):
    return upscale_t(I, decrement(numcolors_t(I)))


def solve_b91ae062(S, I):
    x1 = numcolors_t(I)
    x2 = decrement(x1)
    O = upscale_t(I, x2)
    return O
