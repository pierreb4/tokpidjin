def solve_d2abd087_one(S, I):
    return fill(fill(I, TWO, mfilter_f(o_g(I, R5), matcher(size, SIX))), ONE, mfilter_f(o_g(I, R5), compose(flip, matcher(size, SIX))))


def solve_d2abd087(S, I):
    x1 = o_g(I, R5)
    x2 = matcher(size, SIX)
    x3 = mfilter_f(x1, x2)
    x4 = fill(I, TWO, x3)
    x5 = compose(flip, x2)
    x6 = mfilter_f(x1, x5)
    O = fill(x4, ONE, x6)
    return O
