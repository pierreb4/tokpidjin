def solve_b27ca6d3_one(S, I):
    return fill(I, THREE, mapply(outbox, sizefilter(o_g(I, R5), TWO)))


def solve_b27ca6d3(S, I):
    x1 = o_g(I, R5)
    x2 = sizefilter(x1, TWO)
    x3 = mapply(outbox, x2)
    O = fill(I, THREE, x3)
    return O
