def solve_3aa6fb7a_one(S, I):
    return underfill(I, ONE, mapply(corners, o_g(I, R5)))


def solve_3aa6fb7a(S, I):
    x1 = o_g(I, R5)
    x2 = mapply(corners, x1)
    O = underfill(I, ONE, x2)
    return O
