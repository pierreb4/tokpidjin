def solve_29c11459_one(S, I):
    return fill(paint(paint(I, mapply(fork(recolor_i, color, compose(hfrontier, center)), o_g(righthalf(I), R5))), merge_f(o_g(paint(lefthalf(I), mapply(fork(recolor_i, color, compose(hfrontier, center)), o_g(lefthalf(I), R5))), R5))), FIVE, shift(apply(rbind(corner, R1), o_g(paint(lefthalf(I), mapply(fork(recolor_i, color, compose(hfrontier, center)), o_g(lefthalf(I), R5))), R5)), RIGHT))


def solve_29c11459(S, I, x=0):
    x1 = compose(hfrontier, center)
    if x == 1:
        return x1
    x2 = fork(recolor_i, color, x1)
    if x == 2:
        return x2
    x3 = righthalf(I)
    if x == 3:
        return x3
    x4 = o_g(x3, R5)
    if x == 4:
        return x4
    x5 = mapply(x2, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = lefthalf(I)
    if x == 7:
        return x7
    x8 = o_g(x7, R5)
    if x == 8:
        return x8
    x9 = mapply(x2, x8)
    if x == 9:
        return x9
    x10 = paint(x7, x9)
    if x == 10:
        return x10
    x11 = o_g(x10, R5)
    if x == 11:
        return x11
    x12 = merge_f(x11)
    if x == 12:
        return x12
    x13 = paint(x6, x12)
    if x == 13:
        return x13
    x14 = rbind(corner, R1)
    if x == 14:
        return x14
    x15 = apply(x14, x11)
    if x == 15:
        return x15
    x16 = shift(x15, RIGHT)
    if x == 16:
        return x16
    O = fill(x13, FIVE, x16)
    return O
