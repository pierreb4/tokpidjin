def solve_beb8660c_one(S, I):
    return mir_rot_t(paint(canvas(BLACK, shape_t(I)), mpapply(shift, apply(normalize, order(o_g(I, R5), compose(invert, size))), apply(toivec, interval(ZERO, size(apply(normalize, order(o_g(I, R5), compose(invert, size)))), ONE)))), R5)


def solve_beb8660c(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = canvas(BLACK, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = compose(invert, size)
    if x == 4:
        return x4
    x5 = order(x3, x4)
    if x == 5:
        return x5
    x6 = apply(normalize, x5)
    if x == 6:
        return x6
    x7 = size(x6)
    if x == 7:
        return x7
    x8 = interval(ZERO, x7, ONE)
    if x == 8:
        return x8
    x9 = apply(toivec, x8)
    if x == 9:
        return x9
    x10 = mpapply(shift, x6, x9)
    if x == 10:
        return x10
    x11 = paint(x2, x10)
    if x == 11:
        return x11
    O = mir_rot_t(x11, R5)
    return O
