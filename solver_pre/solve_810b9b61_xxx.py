def solve_810b9b61_one(S, I):
    return fill(I, THREE, mfilter_f(difference(apply(toindices, o_g(I, R7)), sfilter_f(apply(toindices, o_g(I, R7)), fork(either, vline_i, hline_i))), fork(equality, identity, box)))


def solve_810b9b61(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = apply(toindices, x1)
    if x == 2:
        return x2
    x3 = fork(either, vline_i, hline_i)
    if x == 3:
        return x3
    x4 = sfilter_f(x2, x3)
    if x == 4:
        return x4
    x5 = difference(x2, x4)
    if x == 5:
        return x5
    x6 = fork(equality, identity, box)
    if x == 6:
        return x6
    x7 = mfilter_f(x5, x6)
    if x == 7:
        return x7
    O = fill(I, THREE, x7)
    return O
