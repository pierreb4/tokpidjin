def solve_017c7c7b_one(S, I):
    return replace(vconcat(I, branch(equality(tophalf(I), bottomhalf(I)), bottomhalf(I), crop(I, TWO_BY_ZERO, THREE_BY_THREE))), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


def solve_017c7c7b(S, I):
    x1 = tophalf(I)
    x2 = bottomhalf(I)
    x3 = equality(x1, x2)
    x4 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    x5 = branch(x3, x2, x4)
    x6 = vconcat(I, x5)
    x7 = identity(p_g)
    x8 = rbind(get_nth_t, F0)
    x9 = c_iz_n(S, x7, x8)
    x10 = c_zo_n(S, x7, x8)
    O = replace(x6, x9, x10)
    return O
