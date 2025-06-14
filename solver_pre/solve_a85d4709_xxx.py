def solve_a85d4709_one(S, I):
    return fill(fill(fill(I, TWO, chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, FIVE)), lbind(matcher, rbind(get_nth_f, L1)))(ZERO)), THREE, chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, FIVE)), lbind(matcher, rbind(get_nth_f, L1)))(TWO)), FOUR, chain(lbind(mapply, hfrontier), lbind(sfilter, f_ofcolor(I, FIVE)), lbind(matcher, rbind(get_nth_f, L1)))(ONE))


def solve_a85d4709(S, I, x=0):
    x1 = lbind(mapply, hfrontier)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, FIVE)
    if x == 2:
        return x2
    x3 = lbind(sfilter, x2)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, L1)
    if x == 4:
        return x4
    x5 = lbind(matcher, x4)
    if x == 5:
        return x5
    x6 = chain(x1, x3, x5)
    if x == 6:
        return x6
    x7 = x6(ZERO)
    if x == 7:
        return x7
    x8 = fill(I, TWO, x7)
    if x == 8:
        return x8
    x9 = x6(TWO)
    if x == 9:
        return x9
    x10 = fill(x8, THREE, x9)
    if x == 10:
        return x10
    x11 = x6(ONE)
    if x == 11:
        return x11
    O = fill(x10, FOUR, x11)
    return O
