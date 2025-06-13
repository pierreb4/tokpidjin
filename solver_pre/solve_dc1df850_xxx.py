def solve_dc1df850_one(S, I):
    return fill(I, ONE, mapply(outbox, colorfilter(o_g(I, R5), TWO)))


def solve_dc1df850(S, I):
    x1 = o_g(I, R5)
    x2 = colorfilter(x1, TWO)
    x3 = mapply(outbox, x2)
    O = fill(I, ONE, x3)
    return O
