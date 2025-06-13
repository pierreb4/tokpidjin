def solve_41e4d17e_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(compose(fork(combine, vfrontier, hfrontier), center), o_g(I, R5)))


def solve_41e4d17e(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = fork(combine, vfrontier, hfrontier)
    x5 = compose(x4, center)
    x6 = o_g(I, R5)
    x7 = mapply(x5, x6)
    O = underfill(I, x3, x7)
    return O
