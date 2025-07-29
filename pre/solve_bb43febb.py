def solve_bb43febb_one(S, I):
    return fill(I, TWO, mapply(compose(backdrop, inbox), colorfilter(o_g(I, R4), FIVE)))


def solve_bb43febb(S, I):
    x1 = compose(backdrop, inbox)
    x2 = o_g(I, R4)
    x3 = colorfilter(x2, FIVE)
    x4 = mapply(x1, x3)
    O = fill(I, TWO, x4)
    return O
