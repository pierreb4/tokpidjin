def solve_97999447_one(S, I):
    return fill(paint(I, mapply(fork(recolor_i, color, compose(rbind(shoot, RIGHT), center)), o_g(I, R5))), FIVE, merge_f(prapply(shift, apply(toindices, o_g(I, R5)), apply(tojvec, apply(increment, apply(double, interval(ZERO, FIVE, ONE)))))))


def solve_97999447(S, I):
    x1 = rbind(shoot, RIGHT)
    x2 = compose(x1, center)
    x3 = fork(recolor_i, color, x2)
    x4 = o_g(I, R5)
    x5 = mapply(x3, x4)
    x6 = paint(I, x5)
    x7 = apply(toindices, x4)
    x8 = interval(ZERO, FIVE, ONE)
    x9 = apply(double, x8)
    x10 = apply(increment, x9)
    x11 = apply(tojvec, x10)
    x12 = prapply(shift, x7, x11)
    x13 = merge_f(x12)
    O = fill(x6, FIVE, x13)
    return O
