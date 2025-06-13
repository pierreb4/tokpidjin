def solve_a85d4709_one(S, I):
    return fill(fill(fill(I, TWO, chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, FIVE)), lbind(matcher, rbind(get_nth_f, L1)))(ZERO)), THREE, chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, FIVE)), lbind(matcher, rbind(get_nth_f, L1)))(TWO)), FOUR, chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, FIVE)), lbind(matcher, rbind(get_nth_f, L1)))(ONE))


def solve_a85d4709(S, I):
    x1 = lbind(mapply, hfrontier)
    x2 = f_ofcolor(I, FIVE)
    x3 = lbind(sfilter, x2)
    x4 = rbind(get_nth_f, L1)
    x5 = lbind(matcher, x4)
    x6 = chain(x1, x3, x5)
    x7 = x6(ZERO)
    x8 = fill(I, TWO, x7)
    x9 = x6(TWO)
    x10 = fill(x8, THREE, x9)
    x11 = x6(ONE)
    O = fill(x10, FOUR, x11)
    return O
