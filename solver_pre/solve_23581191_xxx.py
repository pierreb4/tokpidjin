def solve_23581191_one(S, I):
    return fill(paint(I, mapply(fork(recolor_i, color, compose(fork(combine, vfrontier, hfrontier), center)), o_g(I, R7))), TWO, fork(intersection, rbind(get_nth_f, F0), rbind(get_nth_f, L1))(apply(compose(fork(combine, vfrontier, hfrontier), center), o_g(I, R7))))


def solve_23581191(S, I):
    x1 = fork(combine, vfrontier, hfrontier)
    x2 = compose(x1, center)
    x3 = fork(recolor_i, color, x2)
    x4 = o_g(I, R7)
    x5 = mapply(x3, x4)
    x6 = paint(I, x5)
    x7 = rbind(get_nth_f, F0)
    x8 = rbind(get_nth_f, L1)
    x9 = fork(intersection, x7, x8)
    x10 = apply(x2, x4)
    x11 = x9(x10)
    O = fill(x6, TWO, x11)
    return O
