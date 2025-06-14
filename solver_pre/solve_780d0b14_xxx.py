def solve_780d0b14_one(S, I):
    return mir_rot_t(sfilter(mir_rot_t(sfilter(paint(fill(I, ZERO, asindices(I)), pair(apply(color, totuple(sfilter(o_g(I, R7), compose(rbind(greater, TWO), size)))), apply(center, totuple(sfilter(o_g(I, R7), compose(rbind(greater, TWO), size)))))), chain(rbind(greater, ONE), size, compose(dedupe, totuple))), R4), chain(rbind(greater, ONE), size, compose(dedupe, totuple))), R6)


def solve_780d0b14(S, I, x=0):
    x1 = asindices(I)
    if x == 1:
        return x1
    x2 = fill(I, ZERO, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R7)
    if x == 3:
        return x3
    x4 = rbind(greater, TWO)
    if x == 4:
        return x4
    x5 = compose(x4, size)
    if x == 5:
        return x5
    x6 = sfilter(x3, x5)
    if x == 6:
        return x6
    x7 = totuple(x6)
    if x == 7:
        return x7
    x8 = apply(color, x7)
    if x == 8:
        return x8
    x9 = apply(center, x7)
    if x == 9:
        return x9
    x10 = pair(x8, x9)
    if x == 10:
        return x10
    x11 = paint(x2, x10)
    if x == 11:
        return x11
    x12 = rbind(greater, ONE)
    if x == 12:
        return x12
    x13 = compose(dedupe, totuple)
    if x == 13:
        return x13
    x14 = chain(x12, size, x13)
    if x == 14:
        return x14
    x15 = sfilter(x11, x14)
    if x == 15:
        return x15
    x16 = mir_rot_t(x15, R4)
    if x == 16:
        return x16
    x17 = sfilter(x16, x14)
    if x == 17:
        return x17
    O = mir_rot_t(x17, R6)
    return O
