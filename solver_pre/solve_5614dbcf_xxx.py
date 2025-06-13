def solve_5614dbcf_one(S, I):
    return downscale(replace(I, FIVE, ZERO), THREE)


def solve_5614dbcf(S, I):
    x1 = replace(I, FIVE, ZERO)
    O = downscale(x1, THREE)
    return O
