def solve_b6afb2da_one(S, I):
    return fill(fill(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), mapply(box, colorfilter(o_g(I, R4), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(corners, colorfilter(o_g(I, R4), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))


def solve_b6afb2da(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = rbind(get_nth_t, F1)
    x5 = c_zo_n(S, x1, x4)
    x6 = replace(I, x3, x5)
    x7 = rbind(get_nth_t, F2)
    x8 = c_zo_n(S, x1, x7)
    x9 = o_g(I, R4)
    x10 = colorfilter(x9, x3)
    x11 = mapply(box, x10)
    x12 = fill(x6, x8, x11)
    x13 = c_zo_n(S, x1, x2)
    x14 = mapply(corners, x10)
    O = fill(x12, x13, x14)
    return O
