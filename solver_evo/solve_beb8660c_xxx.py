def solve_beb8660c_one(S, I):
    return mir_rot_t(paint(canvas(BLACK, shape_t(I)), mpapply(shift, apply(normalize, order(o_g(I, R5), compose(invert, size))), apply(toivec, interval(ZERO, size(apply(normalize, order(o_g(I, R5), compose(invert, size)))), ONE)))), R5)


def solve_beb8660c(S, I):
    x1 = shape_t(I)
    x2 = canvas(BLACK, x1)
    x3 = o_g(I, R5)
    x4 = compose(invert, size)
    x5 = order(x3, x4)
    x6 = apply(normalize, x5)
    x7 = size(x6)
    x8 = interval(ZERO, x7, ONE)
    x9 = apply(toivec, x8)
    x10 = mpapply(shift, x6, x9)
    x11 = paint(x2, x10)
    O = mir_rot_t(x11, R5)
    return O
