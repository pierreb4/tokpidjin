def solve_08ed6ac7_one(S, I):
    return paint(I, mpapply(recolor_o, interval(size_t(totuple(o_g(I, R5))), ZERO, NEG_ONE), order(o_g(I, R5), height_f)))


def solve_08ed6ac7(S, I):
    x1 = o_g(I, R5)
    x2 = totuple(x1)
    x3 = size_t(x2)
    x4 = interval(x3, ZERO, NEG_ONE)
    x5 = order(x1, height_f)
    x6 = mpapply(recolor_o, x4, x5)
    O = paint(I, x6)
    return O
