def solve_29c11459_one(S, I):
    return fill(paint(paint(I, mapply(fork(recolor_i, color, compose(hfrontier, center)), o_g(righthalf(I), R5))), merge_f(o_g(paint(lefthalf(I), mapply(fork(recolor_i, color, compose(hfrontier, center)), o_g(lefthalf(I), R5))), R5))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shift(apply(rbind(corner, R1), o_g(paint(lefthalf(I), mapply(fork(recolor_i, color, compose(hfrontier, center)), o_g(lefthalf(I), R5))), R5)), RIGHT))


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
    x14 = identity(p_g)
    if x == 14:
        return x14
    x15 = rbind(get_nth_t, F0)
    if x == 15:
        return x15
    x16 = c_zo_n(S, x14, x15)
    if x == 16:
        return x16
    x17 = rbind(corner, R1)
    if x == 17:
        return x17
    x18 = apply(x17, x11)
    if x == 18:
        return x18
    x19 = shift(x18, RIGHT)
    if x == 19:
        return x19
    O = fill(x13, x16, x19)
    return O
