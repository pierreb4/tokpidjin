def solve_ae3edfdc_one(S, I):
    return paint(paint(replace(replace(I, GREEN, BLACK), ORANGE, BLACK), mapply(fork(shift, identity, chain(lbind(rbind, gravitate), rbind(get_nth_f, F0), lbind(colorfilter, o_g(I, R5)))(TWO)), lbind(colorfilter, o_g(I, R5))(THREE))), mapply(fork(shift, identity, chain(lbind(rbind, gravitate), rbind(get_nth_f, F0), lbind(colorfilter, o_g(I, R5)))(ONE)), lbind(colorfilter, o_g(I, R5))(SEVEN)))


def solve_ae3edfdc(S, I):
    x1 = replace(I, GREEN, BLACK)
    x2 = replace(x1, ORANGE, BLACK)
    x3 = lbind(rbind, gravitate)
    x4 = rbind(get_nth_f, F0)
    x5 = o_g(I, R5)
    x6 = lbind(colorfilter, x5)
    x7 = chain(x3, x4, x6)
    x8 = x7(TWO)
    x9 = fork(shift, identity, x8)
    x10 = x6(THREE)
    x11 = mapply(x9, x10)
    x12 = paint(x2, x11)
    x13 = x7(ONE)
    x14 = fork(shift, identity, x13)
    x15 = x6(SEVEN)
    x16 = mapply(x14, x15)
    O = paint(x12, x16)
    return O
