def solve_08ed6ac7_one(S, I):
    return paint(I, mpapply(recolor_o, interval(size_t(totuple(o_g(I, R5))), ZERO, NEG_ONE), order(o_g(I, R5), height_f)))


def solve_08ed6ac7(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = totuple(x1)
    if x == 2:
        return x2
    x3 = size_t(x2)
    if x == 3:
        return x3
    x4 = interval(x3, ZERO, NEG_ONE)
    if x == 4:
        return x4
    x5 = order(x1, height_f)
    if x == 5:
        return x5
    x6 = mpapply(recolor_o, x4, x5)
    if x == 6:
        return x6
    O = paint(I, x6)
    return O
