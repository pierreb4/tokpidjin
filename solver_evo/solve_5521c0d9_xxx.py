def solve_5521c0d9_one(S, I):
    return paint(cover(I, merge_f(o_g(I, R5))), mapply(fork(shift, identity, chain(toivec, invert, height_f)), o_g(I, R5)))


def solve_5521c0d9(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = cover(I, x2)
    if x == 3:
        return x3
    x4 = chain(toivec, invert, height_f)
    if x == 4:
        return x4
    x5 = fork(shift, identity, x4)
    if x == 5:
        return x5
    x6 = mapply(x5, x1)
    if x == 6:
        return x6
    O = paint(x3, x6)
    return O
