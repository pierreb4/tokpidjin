def solve_b6afb2da_one(S, I):
    return fill(fill(replace(I, FIVE, TWO), FOUR, mapply(box, colorfilter(o_g(I, R4), FIVE))), ONE, mapply(corners, colorfilter(o_g(I, R4), FIVE)))


def solve_b6afb2da(S, I):
    x1 = replace(I, FIVE, TWO)
    x2 = o_g(I, R4)
    x3 = colorfilter(x2, FIVE)
    x4 = mapply(box, x3)
    x5 = fill(x1, FOUR, x4)
    x6 = mapply(corners, x3)
    O = fill(x5, ONE, x6)
    return O
