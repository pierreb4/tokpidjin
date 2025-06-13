def solve_780d0b14_one(S, I):
    return mir_rot_t(sfilter(mir_rot_t(sfilter(paint(fill(I, ZERO, asindices(I)), pair(apply(color, totuple(sfilter(o_g(I, R7), compose(rbind(greater, TWO), size)))), apply(center, totuple(sfilter(o_g(I, R7), compose(rbind(greater, TWO), size)))))), chain(rbind(greater, ONE), size, compose(dedupe, totuple))), R4), chain(rbind(greater, ONE), size, compose(dedupe, totuple))), R6)


def solve_780d0b14(S, I):
    x1 = asindices(I)
    x2 = fill(I, ZERO, x1)
    x3 = o_g(I, R7)
    x4 = rbind(greater, TWO)
    x5 = compose(x4, size)
    x6 = sfilter(x3, x5)
    x7 = totuple(x6)
    x8 = apply(color, x7)
    x9 = apply(center, x7)
    x10 = pair(x8, x9)
    x11 = paint(x2, x10)
    x12 = rbind(greater, ONE)
    x13 = compose(dedupe, totuple)
    x14 = chain(x12, size, x13)
    x15 = sfilter(x11, x14)
    x16 = mir_rot_t(x15, R4)
    x17 = sfilter(x16, x14)
    O = mir_rot_t(x17, R6)
    return O
