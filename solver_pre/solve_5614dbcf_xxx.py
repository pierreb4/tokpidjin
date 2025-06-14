def solve_5614dbcf_one(S, I):
    return downscale(replace(I, FIVE, ZERO), THREE)


def solve_5614dbcf(S, I, x=0):
    x1 = replace(I, FIVE, ZERO)
    if x == 1:
        return x1
    O = downscale(x1, THREE)
    return O
