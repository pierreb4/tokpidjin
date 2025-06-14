def solve_543a7ed5_one(S, I):
    return fill(fill(I, THREE, mapply(outbox, colorfilter(o_g(I, R5), SIX))), FOUR, mapply(delta, colorfilter(o_g(I, R5), SIX)))


def solve_543a7ed5(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = colorfilter(x1, SIX)
    if x == 2:
        return x2
    x3 = mapply(outbox, x2)
    if x == 3:
        return x3
    x4 = fill(I, THREE, x3)
    if x == 4:
        return x4
    x5 = mapply(delta, x2)
    if x == 5:
        return x5
    O = fill(x4, FOUR, x5)
    return O
