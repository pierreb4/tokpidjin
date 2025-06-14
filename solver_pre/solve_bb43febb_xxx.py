def solve_bb43febb_one(S, I):
    return fill(I, TWO, mapply(compose(backdrop, inbox), colorfilter(o_g(I, R4), FIVE)))


def solve_bb43febb(S, I, x=0):
    x1 = compose(backdrop, inbox)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = colorfilter(x2, FIVE)
    if x == 3:
        return x3
    x4 = mapply(x1, x3)
    if x == 4:
        return x4
    O = fill(I, TWO, x4)
    return O
