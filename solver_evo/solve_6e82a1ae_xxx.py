def solve_6e82a1ae_one(S, I):
    return fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), compose(merge, lbind(sizefilter, o_g(I, R5)))(TWO)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), compose(merge, lbind(sizefilter, o_g(I, R5)))(THREE)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), compose(merge, lbind(sizefilter, o_g(I, R5)))(FOUR))


def solve_6e82a1ae(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F2)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R5)
    x5 = lbind(sizefilter, x4)
    x6 = compose(merge, x5)
    x7 = x6(TWO)
    x8 = fill(I, x3, x7)
    x9 = rbind(get_nth_t, F1)
    x10 = c_zo_n(S, x1, x9)
    x11 = x6(THREE)
    x12 = fill(x8, x10, x11)
    x13 = rbind(get_nth_t, F0)
    x14 = c_zo_n(S, x1, x13)
    x15 = x6(FOUR)
    O = fill(x12, x14, x15)
    return O
