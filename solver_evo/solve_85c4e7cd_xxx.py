def solve_85c4e7cd_one(S, I):
    return paint(I, mpapply(recolor_o, apply(color, order(o_g(I, R4), compose(invert, size))), order(o_g(I, R4), size)))


def solve_85c4e7cd(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = compose(invert, size)
    if x == 2:
        return x2
    x3 = order(x1, x2)
    if x == 3:
        return x3
    x4 = apply(color, x3)
    if x == 4:
        return x4
    x5 = order(x1, size)
    if x == 5:
        return x5
    x6 = mpapply(recolor_o, x4, x5)
    if x == 6:
        return x6
    O = paint(I, x6)
    return O
