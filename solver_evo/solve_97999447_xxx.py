def solve_97999447_one(S, I):
    return fill(paint(I, mapply(fork(recolor_i, color, compose(rbind(shoot, RIGHT), center)), o_g(I, R5))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(prapply(shift, apply(toindices, o_g(I, R5)), apply(tojvec, apply(increment, apply(double, interval(ZERO, FIVE, ONE)))))))


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
    x7 = identity(p_g)
    if x == 7:
        return x7
    x8 = rbind(get_nth_t, F0)
    if x == 8:
        return x8
    x9 = c_zo_n(S, x7, x8)
    if x == 9:
        return x9
    x10 = apply(toindices, x4)
    if x == 10:
        return x10
    x11 = interval(ZERO, FIVE, ONE)
    if x == 11:
        return x11
    x12 = apply(double, x11)
    if x == 12:
        return x12
    x13 = apply(increment, x12)
    if x == 13:
        return x13
    x14 = apply(tojvec, x13)
    if x == 14:
        return x14
    x15 = prapply(shift, x10, x14)
    if x == 15:
        return x15
    x16 = merge_f(x15)
    if x == 16:
        return x16
    O = fill(x6, x9, x16)
    return O
