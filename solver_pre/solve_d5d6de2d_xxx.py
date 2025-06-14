def solve_d5d6de2d_one(S, I):
    return fill(replace(I, TWO, ZERO), THREE, mapply(compose(backdrop, inbox), difference(o_g(I, R5), sfilter_f(o_g(I, R5), square_f))))


def solve_d5d6de2d(S, I, x=0):
    x1 = replace(I, TWO, ZERO)
    if x == 1:
        return x1
    x2 = compose(backdrop, inbox)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = sfilter_f(x3, square_f)
    if x == 4:
        return x4
    x5 = difference(x3, x4)
    if x == 5:
        return x5
    x6 = mapply(x2, x5)
    if x == 6:
        return x6
    O = fill(x1, THREE, x6)
    return O
