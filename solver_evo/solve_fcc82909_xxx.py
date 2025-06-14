def solve_fcc82909_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(compose(box, fork(astuple, compose(rbind(add, DOWN), rbind(corner, R2)), fork(add, rbind(corner, R3), compose(toivec, numcolors_f)))), o_g(I, R3)))


def solve_fcc82909(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(add, DOWN)
    if x == 4:
        return x4
    x5 = rbind(corner, R2)
    if x == 5:
        return x5
    x6 = compose(x4, x5)
    if x == 6:
        return x6
    x7 = rbind(corner, R3)
    if x == 7:
        return x7
    x8 = compose(toivec, numcolors_f)
    if x == 8:
        return x8
    x9 = fork(add, x7, x8)
    if x == 9:
        return x9
    x10 = fork(astuple, x6, x9)
    if x == 10:
        return x10
    x11 = compose(box, x10)
    if x == 11:
        return x11
    x12 = o_g(I, R3)
    if x == 12:
        return x12
    x13 = mapply(x11, x12)
    if x == 13:
        return x13
    O = fill(I, x3, x13)
    return O
