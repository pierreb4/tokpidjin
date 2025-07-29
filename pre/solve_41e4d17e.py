def solve_41e4d17e_one(S, I):
    return underfill(I, SIX, mapply(compose(fork(combine, vfrontier, hfrontier), center), o_g(I, R5)))


def solve_41e4d17e(S, I):
    x1 = fork(combine, vfrontier, hfrontier)
    x2 = compose(x1, center)
    x3 = o_g(I, R5)
    x4 = mapply(x2, x3)
    O = underfill(I, SIX, x4)
    return O
