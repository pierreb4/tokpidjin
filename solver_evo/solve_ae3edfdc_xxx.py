def solve_ae3edfdc_one(S, I):
    return paint(paint(replace(replace(I, GREEN, BLACK), ORANGE, BLACK), mapply(fork(shift, identity, chain(lbind(rbind, gravitate), rbind(get_nth_f, F0), lbind(colorfilter, o_g(I, R5)))(TWO)), lbind(colorfilter, o_g(I, R5))(THREE))), mapply(fork(shift, identity, chain(lbind(rbind, gravitate), rbind(get_nth_f, F0), lbind(colorfilter, o_g(I, R5)))(ONE)), lbind(colorfilter, o_g(I, R5))(SEVEN)))


def solve_ae3edfdc(S, I, x=0):
    x1 = replace(I, GREEN, BLACK)
    if x == 1:
        return x1
    x2 = replace(x1, ORANGE, BLACK)
    if x == 2:
        return x2
    x3 = lbind(rbind, gravitate)
    if x == 3:
        return x3
    x4 = rbind(get_nth_f, F0)
    if x == 4:
        return x4
    x5 = o_g(I, R5)
    if x == 5:
        return x5
    x6 = lbind(colorfilter, x5)
    if x == 6:
        return x6
    x7 = chain(x3, x4, x6)
    if x == 7:
        return x7
    x8 = x7(TWO)
    if x == 8:
        return x8
    x9 = fork(shift, identity, x8)
    if x == 9:
        return x9
    x10 = x6(THREE)
    if x == 10:
        return x10
    x11 = mapply(x9, x10)
    if x == 11:
        return x11
    x12 = paint(x2, x11)
    if x == 12:
        return x12
    x13 = x7(ONE)
    if x == 13:
        return x13
    x14 = fork(shift, identity, x13)
    if x == 14:
        return x14
    x15 = x6(SEVEN)
    if x == 15:
        return x15
    x16 = mapply(x14, x15)
    if x == 16:
        return x16
    O = paint(x12, x16)
    return O
