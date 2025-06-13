def solve_c1d99e64_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(frontiers(I)))


def solve_c1d99e64(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = frontiers(I)
    x5 = merge_f(x4)
    O = fill(I, x3, x5)
    return O
