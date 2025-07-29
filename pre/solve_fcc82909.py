def solve_fcc82909_one(S, I):
    return fill(I, THREE, mapply(compose(box, fork(astuple, compose(rbind(add, DOWN), rbind(corner, R2)), fork(add, rbind(corner, R3), compose(toivec, numcolors_f)))), o_g(I, R3)))


def solve_fcc82909(S, I):
    x1 = rbind(add, DOWN)
    x2 = rbind(corner, R2)
    x3 = compose(x1, x2)
    x4 = rbind(corner, R3)
    x5 = compose(toivec, numcolors_f)
    x6 = fork(add, x4, x5)
    x7 = fork(astuple, x3, x6)
    x8 = compose(box, x7)
    x9 = o_g(I, R3)
    x10 = mapply(x8, x9)
    O = fill(I, THREE, x10)
    return O
