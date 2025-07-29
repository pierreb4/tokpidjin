def solve_4347f46a_one(S, I):
    return fill(I, ZERO, mapply(fork(difference, toindices, box), o_g(I, R5)))


def solve_4347f46a(S, I):
    x1 = fork(difference, toindices, box)
    x2 = o_g(I, R5)
    x3 = mapply(x1, x2)
    O = fill(I, ZERO, x3)
    return O
