def solve_97999447_one(S, I):
    return fill(paint(I, mapply(fork(recolor_i, color, compose(rbind(shoot, RIGHT), center)), o_g(I, R5))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(prapply(shift, apply(toindices, o_g(I, R5)), apply(tojvec, apply(increment, apply(double, interval(ZERO, FIVE, ONE)))))))


def solve_97999447(S, I):
    x1 = rbind(shoot, RIGHT)
    x2 = compose(x1, center)
    x3 = fork(recolor_i, color, x2)
    x4 = o_g(I, R5)
    x5 = mapply(x3, x4)
    x6 = paint(I, x5)
    x7 = identity(p_g)
    x8 = rbind(get_nth_t, F0)
    x9 = c_zo_n(S, x7, x8)
    x10 = apply(toindices, x4)
    x11 = interval(ZERO, FIVE, ONE)
    x12 = apply(double, x11)
    x13 = apply(increment, x12)
    x14 = apply(tojvec, x13)
    x15 = prapply(shift, x10, x14)
    x16 = merge_f(x15)
    O = fill(x6, x9, x16)
    return O
