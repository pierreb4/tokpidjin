def solve_23581191_one(S, I):
    return fill(paint(I, mapply(fork(recolor_i, color, compose(fork(combine, vfrontier, hfrontier), center)), o_g(I, R7))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), fork(intersection, rbind(get_nth_f, F0), rbind(get_nth_f, L1))(apply(compose(fork(combine, vfrontier, hfrontier), center), o_g(I, R7))))


def solve_23581191(S, I):
    x1 = fork(combine, vfrontier, hfrontier)
    x2 = compose(x1, center)
    x3 = fork(recolor_i, color, x2)
    x4 = o_g(I, R7)
    x5 = mapply(x3, x4)
    x6 = paint(I, x5)
    x7 = identity(p_g)
    x8 = rbind(get_nth_t, F0)
    x9 = c_zo_n(S, x7, x8)
    x10 = rbind(get_nth_f, F0)
    x11 = rbind(get_nth_f, L1)
    x12 = fork(intersection, x10, x11)
    x13 = apply(x2, x4)
    x14 = x12(x13)
    O = fill(x6, x9, x14)
    return O
