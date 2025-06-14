def solve_6e82a1ae_one(S, I):
    return fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), compose(merge, lbind(sizefilter, o_g(I, R5)))(TWO)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), compose(merge, lbind(sizefilter, o_g(I, R5)))(THREE)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), compose(merge, lbind(sizefilter, o_g(I, R5)))(FOUR))


def solve_6e82a1ae(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F2)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R5)
    if x == 4:
        return x4
    x5 = lbind(sizefilter, x4)
    if x == 5:
        return x5
    x6 = compose(merge, x5)
    if x == 6:
        return x6
    x7 = x6(TWO)
    if x == 7:
        return x7
    x8 = fill(I, x3, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_t, F1)
    if x == 9:
        return x9
    x10 = c_zo_n(S, x1, x9)
    if x == 10:
        return x10
    x11 = x6(THREE)
    if x == 11:
        return x11
    x12 = fill(x8, x10, x11)
    if x == 12:
        return x12
    x13 = rbind(get_nth_t, F0)
    if x == 13:
        return x13
    x14 = c_zo_n(S, x1, x13)
    if x == 14:
        return x14
    x15 = x6(FOUR)
    if x == 15:
        return x15
    O = fill(x12, x14, x15)
    return O
