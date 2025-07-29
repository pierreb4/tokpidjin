def solve_5521c0d9_one(S, I):
    return paint(cover(I, merge_f(o_g(I, R5))), mapply(fork(shift, identity, chain(toivec, invert, height_f)), o_g(I, R5)))


def solve_5521c0d9(S, I):
    x1 = o_g(I, R5)
    x2 = merge_f(x1)
    x3 = cover(I, x2)
    x4 = chain(toivec, invert, height_f)
    x5 = fork(shift, identity, x4)
    x6 = mapply(x5, x1)
    O = paint(x3, x6)
    return O
