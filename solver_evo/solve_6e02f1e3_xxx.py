def solve_6e02f1e3_one(S, I):
    return fill(canvas(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), THREE_BY_THREE), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), connect(branch(equality(numcolors_t(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), TWO_BY_ZERO, ORIGIN), branch(equality(numcolors_t(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F1))), TWO_BY_TWO, ZERO_BY_TWO)))


def solve_6e02f1e3(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = canvas(x3, THREE_BY_THREE)
    x5 = rbind(get_nth_t, F1)
    x6 = c_zo_n(S, x1, x5)
    x7 = numcolors_t(I)
    x8 = c_iz_n(S, x1, x2)
    x9 = equality(x7, x8)
    x10 = branch(x9, TWO_BY_ZERO, ORIGIN)
    x11 = c_iz_n(S, x1, x5)
    x12 = equality(x7, x11)
    x13 = branch(x12, TWO_BY_TWO, ZERO_BY_TWO)
    x14 = connect(x10, x13)
    O = fill(x4, x6, x14)
    return O
