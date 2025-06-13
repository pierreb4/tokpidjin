def solve_a85d4709_one(S, I):
    return fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)))), lbind(matcher, rbind(get_nth_f, L1)))(ZERO)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)))), lbind(matcher, rbind(get_nth_f, L1)))(TWO)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1)))), lbind(matcher, rbind(get_nth_f, L1)))(ONE))


def solve_a85d4709(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = lbind(mapply, hfrontier)
    x5 = rbind(get_nth_t, F1)
    x6 = c_iz_n(S, x1, x5)
    x7 = f_ofcolor(I, x6)
    x8 = lbind(sfilter, x7)
    x9 = rbind(get_nth_f, L1)
    x10 = lbind(matcher, x9)
    x11 = chain(x4, x8, x10)
    x12 = x11(ZERO)
    x13 = fill(I, x3, x12)
    x14 = rbind(get_nth_t, F2)
    x15 = c_zo_n(S, x1, x14)
    x16 = x11(TWO)
    x17 = fill(x13, x15, x16)
    x18 = c_zo_n(S, x1, x5)
    x19 = x11(ONE)
    O = fill(x17, x18, x19)
    return O
