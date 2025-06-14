def solve_017c7c7b_one(S, I):
    return replace(vconcat(I, branch(equality(tophalf(I), bottomhalf(I)), bottomhalf(I), crop(I, TWO_BY_ZERO, THREE_BY_THREE))), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


def solve_017c7c7b(S, I, x=0):
    x1 = tophalf(I)
    if x == 1:
        return x1
    x2 = bottomhalf(I)
    if x == 2:
        return x2
    x3 = equality(x1, x2)
    if x == 3:
        return x3
    x4 = crop(I, TWO_BY_ZERO, THREE_BY_THREE)
    if x == 4:
        return x4
    x5 = branch(x3, x2, x4)
    if x == 5:
        return x5
    x6 = vconcat(I, x5)
    if x == 6:
        return x6
    x7 = identity(p_g)
    if x == 7:
        return x7
    x8 = rbind(get_nth_t, F0)
    if x == 8:
        return x8
    x9 = c_iz_n(S, x7, x8)
    if x == 9:
        return x9
    x10 = c_zo_n(S, x7, x8)
    if x == 10:
        return x10
    O = replace(x6, x9, x10)
    return O
