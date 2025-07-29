def solve_6e82a1ae_one(S, I):
    return fill(fill(fill(I, THREE, compose(merge, lbind(sizefilter, o_g(I, R5)))(TWO)), TWO, compose(merge, lbind(sizefilter, o_g(I, R5)))(THREE)), ONE, compose(merge, lbind(sizefilter, o_g(I, R5)))(FOUR))


def solve_6e82a1ae(S, I):
    x1 = o_g(I, R5)
    x2 = lbind(sizefilter, x1)
    x3 = compose(merge, x2)
    x4 = x3(TWO)
    x5 = fill(I, THREE, x4)
    x6 = x3(THREE)
    x7 = fill(x5, TWO, x6)
    x8 = x3(FOUR)
    O = fill(x7, ONE, x8)
    return O
