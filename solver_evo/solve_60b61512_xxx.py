def solve_60b61512_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(delta, o_g(I, R7)))


def solve_60b61512(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R7)
    x5 = mapply(delta, x4)
    O = fill(I, x3, x5)
    return O
