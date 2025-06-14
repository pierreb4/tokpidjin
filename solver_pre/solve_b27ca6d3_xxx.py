def solve_b27ca6d3_one(S, I):
    return fill(I, THREE, mapply(outbox, sizefilter(o_g(I, R5), TWO)))


def solve_b27ca6d3(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, TWO)
    if x == 2:
        return x2
    x3 = mapply(outbox, x2)
    if x == 3:
        return x3
    O = fill(I, THREE, x3)
    return O
