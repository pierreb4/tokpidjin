def solve_fcc82909_one(S, I):
    return fill(I, THREE, mapply(compose(box, fork(astuple, compose(rbind(add, DOWN), rbind(corner, R2)), fork(add, rbind(corner, R3), compose(toivec, numcolors_f)))), o_g(I, R3)))


def solve_fcc82909(S, I, x=0):
    x1 = rbind(add, DOWN)
    if x == 1:
        return x1
    x2 = rbind(corner, R2)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = rbind(corner, R3)
    if x == 4:
        return x4
    x5 = compose(toivec, numcolors_f)
    if x == 5:
        return x5
    x6 = fork(add, x4, x5)
    if x == 6:
        return x6
    x7 = fork(astuple, x3, x6)
    if x == 7:
        return x7
    x8 = compose(box, x7)
    if x == 8:
        return x8
    x9 = o_g(I, R3)
    if x == 9:
        return x9
    x10 = mapply(x8, x9)
    if x == 10:
        return x10
    O = fill(I, THREE, x10)
    return O
