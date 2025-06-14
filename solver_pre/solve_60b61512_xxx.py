def solve_60b61512_one(S, I):
    return fill(I, SEVEN, mapply(delta, o_g(I, R7)))


def solve_60b61512(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = mapply(delta, x1)
    if x == 2:
        return x2
    O = fill(I, SEVEN, x2)
    return O
