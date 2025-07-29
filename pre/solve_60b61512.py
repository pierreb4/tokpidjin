def solve_60b61512_one(S, I):
    return fill(I, SEVEN, mapply(delta, o_g(I, R7)))


def solve_60b61512(S, I):
    x1 = o_g(I, R7)
    x2 = mapply(delta, x1)
    O = fill(I, SEVEN, x2)
    return O
