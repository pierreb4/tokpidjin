def solve_543a7ed5_one(S, I):
    return fill(fill(I, THREE, mapply(outbox, colorfilter(o_g(I, R5), SIX))), FOUR, mapply(delta, colorfilter(o_g(I, R5), SIX)))


def solve_543a7ed5(S, I):
    x1 = o_g(I, R5)
    x2 = colorfilter(x1, SIX)
    x3 = mapply(outbox, x2)
    x4 = fill(I, THREE, x3)
    x5 = mapply(delta, x2)
    O = fill(x4, FOUR, x5)
    return O
