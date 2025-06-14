def solve_b6afb2da_one(S, I):
    return fill(fill(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), mapply(box, colorfilter(o_g(I, R4), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(corners, colorfilter(o_g(I, R4), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))


def solve_b6afb2da(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(get_nth_t, F1)
    if x == 4:
        return x4
    x5 = c_zo_n(S, x1, x4)
    if x == 5:
        return x5
    x6 = replace(I, x3, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_t, F2)
    if x == 7:
        return x7
    x8 = c_zo_n(S, x1, x7)
    if x == 8:
        return x8
    x9 = o_g(I, R4)
    if x == 9:
        return x9
    x10 = colorfilter(x9, x3)
    if x == 10:
        return x10
    x11 = mapply(box, x10)
    if x == 11:
        return x11
    x12 = fill(x6, x8, x11)
    if x == 12:
        return x12
    x13 = c_zo_n(S, x1, x2)
    if x == 13:
        return x13
    x14 = mapply(corners, x10)
    if x == 14:
        return x14
    O = fill(x12, x13, x14)
    return O
