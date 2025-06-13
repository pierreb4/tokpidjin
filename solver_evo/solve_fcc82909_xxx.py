def solve_fcc82909_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(compose(box, fork(astuple, compose(rbind(add, DOWN), rbind(corner, R2)), fork(add, rbind(corner, R3), compose(toivec, numcolors_f)))), o_g(I, R3)))


def solve_fcc82909(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = rbind(add, DOWN)
    x5 = rbind(corner, R2)
    x6 = compose(x4, x5)
    x7 = rbind(corner, R3)
    x8 = compose(toivec, numcolors_f)
    x9 = fork(add, x7, x8)
    x10 = fork(astuple, x6, x9)
    x11 = compose(box, x10)
    x12 = o_g(I, R3)
    x13 = mapply(x11, x12)
    O = fill(I, x3, x13)
    return O
