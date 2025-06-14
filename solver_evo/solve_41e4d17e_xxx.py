def solve_41e4d17e_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(compose(fork(combine, vfrontier, hfrontier), center), o_g(I, R5)))


def solve_41e4d17e(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = fork(combine, vfrontier, hfrontier)
    if x == 4:
        return x4
    x5 = compose(x4, center)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = mapply(x5, x6)
    if x == 7:
        return x7
    O = underfill(I, x3, x7)
    return O
