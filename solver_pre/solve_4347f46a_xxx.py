def solve_4347f46a_one(S, I):
    return fill(I, ZERO, mapply(fork(difference, toindices, box), o_g(I, R5)))


def solve_4347f46a(S, I, x=0):
    x1 = fork(difference, toindices, box)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = mapply(x1, x2)
    if x == 3:
        return x3
    O = fill(I, ZERO, x3)
    return O
