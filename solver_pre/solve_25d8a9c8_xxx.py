def solve_25d8a9c8_one(S, I):
    return fill(fill(I, FIVE, toindices(mfilter_f(sizefilter(o_g(I, R4), THREE), hline_o))), ZERO, difference(asindices(I), toindices(mfilter_f(sizefilter(o_g(I, R4), THREE), hline_o))))


def solve_25d8a9c8(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = sizefilter(x1, THREE)
    if x == 2:
        return x2
    x3 = mfilter_f(x2, hline_o)
    if x == 3:
        return x3
    x4 = toindices(x3)
    if x == 4:
        return x4
    x5 = fill(I, FIVE, x4)
    if x == 5:
        return x5
    x6 = asindices(I)
    if x == 6:
        return x6
    x7 = difference(x6, x4)
    if x == 7:
        return x7
    O = fill(x5, ZERO, x7)
    return O
