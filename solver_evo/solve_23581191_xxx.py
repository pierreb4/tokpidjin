def solve_23581191_one(S, I):
    return fill(paint(I, mapply(fork(recolor_i, color, compose(fork(combine, vfrontier, hfrontier), center)), o_g(I, R7))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), fork(intersection, rbind(get_nth_f, F0), rbind(get_nth_f, L1))(apply(compose(fork(combine, vfrontier, hfrontier), center), o_g(I, R7))))


def solve_23581191(S, I, x=0):
    x1 = fork(combine, vfrontier, hfrontier)
    if x == 1:
        return x1
    x2 = compose(x1, center)
    if x == 2:
        return x2
    x3 = fork(recolor_i, color, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R7)
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
    x10 = rbind(get_nth_f, F0)
    if x == 10:
        return x10
    x11 = rbind(get_nth_f, L1)
    if x == 11:
        return x11
    x12 = fork(intersection, x10, x11)
    if x == 12:
        return x12
    x13 = apply(x2, x4)
    if x == 13:
        return x13
    x14 = x12(x13)
    if x == 14:
        return x14
    O = fill(x6, x9, x14)
    return O
