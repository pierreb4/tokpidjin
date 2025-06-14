def solve_41e4d17e_one(S, I):
    return underfill(I, SIX, mapply(compose(fork(combine, vfrontier, hfrontier), center), o_g(I, R5)))


def solve_41e4d17e(S, I, x=0):
    x1 = fork(combine, vfrontier, hfrontier)
    if x == 1:
        return x1
    x2 = compose(x1, center)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = mapply(x2, x3)
    if x == 4:
        return x4
    O = underfill(I, SIX, x4)
    return O
