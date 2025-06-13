def solve_a740d043_one(S, I):
    return replace(subgrid(merge_f(o_g(I, R7)), I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


def solve_a740d043(S, I):
    x1 = o_g(I, R7)
    x2 = merge_f(x1)
    x3 = subgrid(x2, I)
    x4 = identity(p_g)
    x5 = rbind(get_nth_t, F0)
    x6 = c_iz_n(S, x4, x5)
    x7 = c_zo_n(S, x4, x5)
    O = replace(x3, x6, x7)
    return O
