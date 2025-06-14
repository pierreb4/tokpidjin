def solve_ac0a08a4_one(S, I):
    return upscale_t(I, decrement(numcolors_t(I)))


def solve_ac0a08a4(S, I, x=0):
    x1 = numcolors_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    O = upscale_t(I, x2)
    return O
