def solve_97999447_one(S, I):
    return fill(paint(I, mapply(fork(recolor_i, color, compose(rbind(shoot, RIGHT), center)), o_g(I, R5))), FIVE, merge_f(prapply(shift, apply(toindices, o_g(I, R5)), apply(tojvec, apply(increment, apply(double, interval(ZERO, FIVE, ONE)))))))


def solve_97999447(S, I, x=0):
    x1 = rbind(shoot, RIGHT)
    if x == 1:
        return x1
    x2 = compose(x1, center)
    if x == 2:
        return x2
    x3 = fork(recolor_i, color, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R5)
    if x == 4:
        return x4
    x5 = mapply(x3, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = apply(toindices, x4)
    if x == 7:
        return x7
    x8 = interval(ZERO, FIVE, ONE)
    if x == 8:
        return x8
    x9 = apply(double, x8)
    if x == 9:
        return x9
    x10 = apply(increment, x9)
    if x == 10:
        return x10
    x11 = apply(tojvec, x10)
    if x == 11:
        return x11
    x12 = prapply(shift, x7, x11)
    if x == 12:
        return x12
    x13 = merge_f(x12)
    if x == 13:
        return x13
    O = fill(x6, FIVE, x13)
    return O
