def solve_25d8a9c8_one(S, I):
    return fill(fill(I, FIVE, toindices(mfilter_f(sizefilter(o_g(I, R4), THREE), hline_o))), ZERO, difference(asindices(I), toindices(mfilter_f(sizefilter(o_g(I, R4), THREE), hline_o))))


def solve_25d8a9c8(S, I):
    x1 = o_g(I, R4)
    x2 = sizefilter(x1, THREE)
    x3 = mfilter_f(x2, hline_o)
    x4 = toindices(x3)
    x5 = fill(I, FIVE, x4)
    x6 = asindices(I)
    x7 = difference(x6, x4)
    O = fill(x5, ZERO, x7)
    return O
