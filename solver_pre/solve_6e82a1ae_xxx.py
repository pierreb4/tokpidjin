def solve_6e82a1ae_one(S, I):
    return fill(fill(fill(I, THREE, compose(merge, lbind(sizefilter, o_g(I, R5)))(TWO)), TWO, compose(merge, lbind(sizefilter, o_g(I, R5)))(THREE)), ONE, compose(merge, lbind(sizefilter, o_g(I, R5)))(FOUR))


def solve_6e82a1ae(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = lbind(sizefilter, x1)
    if x == 2:
        return x2
    x3 = compose(merge, x2)
    if x == 3:
        return x3
    x4 = x3(TWO)
    if x == 4:
        return x4
    x5 = fill(I, THREE, x4)
    if x == 5:
        return x5
    x6 = x3(THREE)
    if x == 6:
        return x6
    x7 = fill(x5, TWO, x6)
    if x == 7:
        return x7
    x8 = x3(FOUR)
    if x == 8:
        return x8
    O = fill(x7, ONE, x8)
    return O
