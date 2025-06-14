def solve_6e02f1e3_one(S, I):
    return fill(canvas(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), THREE_BY_THREE), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), connect(branch(equality(numcolors_t(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), TWO_BY_ZERO, ORIGIN), branch(equality(numcolors_t(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F1))), TWO_BY_TWO, ZERO_BY_TWO)))


def solve_6e02f1e3(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = canvas(x3, THREE_BY_THREE)
    if x == 4:
        return x4
    x5 = rbind(get_nth_t, F1)
    if x == 5:
        return x5
    x6 = c_zo_n(S, x1, x5)
    if x == 6:
        return x6
    x7 = numcolors_t(I)
    if x == 7:
        return x7
    x8 = c_iz_n(S, x1, x2)
    if x == 8:
        return x8
    x9 = equality(x7, x8)
    if x == 9:
        return x9
    x10 = branch(x9, TWO_BY_ZERO, ORIGIN)
    if x == 10:
        return x10
    x11 = c_iz_n(S, x1, x5)
    if x == 11:
        return x11
    x12 = equality(x7, x11)
    if x == 12:
        return x12
    x13 = branch(x12, TWO_BY_TWO, ZERO_BY_TWO)
    if x == 13:
        return x13
    x14 = connect(x10, x13)
    if x == 14:
        return x14
    O = fill(x4, x6, x14)
    return O
