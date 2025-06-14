def solve_d2abd087_one(S, I):
    return fill(fill(I, TWO, mfilter_f(o_g(I, R5), matcher(size, SIX))), ONE, mfilter_f(o_g(I, R5), compose(flip, matcher(size, SIX))))


def solve_d2abd087(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = matcher(size, SIX)
    if x == 2:
        return x2
    x3 = mfilter_f(x1, x2)
    if x == 3:
        return x3
    x4 = fill(I, TWO, x3)
    if x == 4:
        return x4
    x5 = compose(flip, x2)
    if x == 5:
        return x5
    x6 = mfilter_f(x1, x5)
    if x == 6:
        return x6
    O = fill(x4, ONE, x6)
    return O
