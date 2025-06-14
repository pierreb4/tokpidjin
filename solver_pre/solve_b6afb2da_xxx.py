def solve_b6afb2da_one(S, I):
    return fill(fill(replace(I, FIVE, TWO), FOUR, mapply(box, colorfilter(o_g(I, R4), FIVE))), ONE, mapply(corners, colorfilter(o_g(I, R4), FIVE)))


def solve_b6afb2da(S, I, x=0):
    x1 = replace(I, FIVE, TWO)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = colorfilter(x2, FIVE)
    if x == 3:
        return x3
    x4 = mapply(box, x3)
    if x == 4:
        return x4
    x5 = fill(x1, FOUR, x4)
    if x == 5:
        return x5
    x6 = mapply(corners, x3)
    if x == 6:
        return x6
    O = fill(x5, ONE, x6)
    return O
