def solve_d5d6de2d_one(S, I):
    return fill(replace(I, TWO, ZERO), THREE, mapply(compose(backdrop, inbox), difference(o_g(I, R5), sfilter_f(o_g(I, R5), square_f))))


def solve_d5d6de2d(S, I):
    x1 = replace(I, TWO, ZERO)
    x2 = compose(backdrop, inbox)
    x3 = o_g(I, R5)
    x4 = sfilter_f(x3, square_f)
    x5 = difference(x3, x4)
    x6 = mapply(x2, x5)
    O = fill(x1, THREE, x6)
    return O
