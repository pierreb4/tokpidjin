def solve_85c4e7cd_one(S, I):
    return paint(I, mpapply(recolor_o, apply(color, order(o_g(I, R4), compose(invert, size))), order(o_g(I, R4), size)))


def solve_85c4e7cd(S, I):
    x1 = o_g(I, R4)
    x2 = compose(invert, size)
    x3 = order(x1, x2)
    x4 = apply(color, x3)
    x5 = order(x1, size)
    x6 = mpapply(recolor_o, x4, x5)
    O = paint(I, x6)
    return O
