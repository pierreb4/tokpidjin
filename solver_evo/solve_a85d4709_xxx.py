def solve_a85d4709_one(S, I):
    return fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)))), lbind(matcher, rbind(get_nth_f, L1)))(ZERO)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)))), lbind(matcher, rbind(get_nth_f, L1)))(TWO)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)))), lbind(matcher, rbind(get_nth_f, L1)))(ONE))


def solve_a85d4709(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = lbind(mapply, hfrontier)
    if x == 4:
        return x4
    x5 = rbind(get_nth_t, F1)
    if x == 5:
        return x5
    x6 = c_iz_n(S, x1, x5)
    if x == 6:
        return x6
    x7 = f_ofcolor(I, x6)
    if x == 7:
        return x7
    x8 = lbind(sfilter, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_f, L1)
    if x == 9:
        return x9
    x10 = lbind(matcher, x9)
    if x == 10:
        return x10
    x11 = chain(x4, x8, x10)
    if x == 11:
        return x11
    x12 = x11(ZERO)
    if x == 12:
        return x12
    x13 = fill(I, x3, x12)
    if x == 13:
        return x13
    x14 = rbind(get_nth_t, F2)
    if x == 14:
        return x14
    x15 = c_zo_n(S, x1, x14)
    if x == 15:
        return x15
    x16 = x11(TWO)
    if x == 16:
        return x16
    x17 = fill(x13, x15, x16)
    if x == 17:
        return x17
    x18 = c_zo_n(S, x1, x5)
    if x == 18:
        return x18
    x19 = x11(ONE)
    if x == 19:
        return x19
    O = fill(x17, x18, x19)
    return O
