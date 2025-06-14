def solve_54d9e175_one(S, I):
    return replace(replace(replace(replace(paint(I, mapply(fork(recolor_i, color, compose(neighbors, center)), sizefilter(o_g(I, R5), ONE))), c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2))), c_iz_n(S, identity(p_g), rbind(get_nth_t, F4)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F3))), c_iz_n(S, identity(p_g), rbind(get_nth_t, F2)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0))), c_iz_n(S, identity(p_g), rbind(get_nth_t, F3)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)))


def solve_54d9e175(S, I, x=0):
    x1 = compose(neighbors, center)
    if x == 1:
        return x1
    x2 = fork(recolor_i, color, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = sizefilter(x3, ONE)
    if x == 4:
        return x4
    x5 = mapply(x2, x4)
    if x == 5:
        return x5
    x6 = paint(I, x5)
    if x == 6:
        return x6
    x7 = identity(p_g)
    if x == 7:
        return x7
    x8 = rbind(get_nth_t, F1)
    if x == 8:
        return x8
    x9 = c_iz_n(S, x7, x8)
    if x == 9:
        return x9
    x10 = rbind(get_nth_t, F2)
    if x == 10:
        return x10
    x11 = c_zo_n(S, x7, x10)
    if x == 11:
        return x11
    x12 = replace(x6, x9, x11)
    if x == 12:
        return x12
    x13 = rbind(get_nth_t, F4)
    if x == 13:
        return x13
    x14 = c_iz_n(S, x7, x13)
    if x == 14:
        return x14
    x15 = rbind(get_nth_t, F3)
    if x == 15:
        return x15
    x16 = c_zo_n(S, x7, x15)
    if x == 16:
        return x16
    x17 = replace(x12, x14, x16)
    if x == 17:
        return x17
    x18 = c_iz_n(S, x7, x10)
    if x == 18:
        return x18
    x19 = rbind(get_nth_t, F0)
    if x == 19:
        return x19
    x20 = c_zo_n(S, x7, x19)
    if x == 20:
        return x20
    x21 = replace(x17, x18, x20)
    if x == 21:
        return x21
    x22 = c_iz_n(S, x7, x15)
    if x == 22:
        return x22
    x23 = c_zo_n(S, x7, x8)
    if x == 23:
        return x23
    O = replace(x21, x22, x23)
    return O
