def solve_543a7ed5_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(outbox, colorfilter(o_g(I, R5), MAGENTA))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), mapply(delta, colorfilter(o_g(I, R5), MAGENTA)))


def solve_543a7ed5(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R5)
    x5 = colorfilter(x4, MAGENTA)
    x6 = mapply(outbox, x5)
    x7 = fill(I, x3, x6)
    x8 = rbind(get_nth_t, F1)
    x9 = c_zo_n(S, x1, x8)
    x10 = mapply(delta, x5)
    O = fill(x7, x9, x10)
    return O
