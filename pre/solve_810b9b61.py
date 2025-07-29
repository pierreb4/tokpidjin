def solve_810b9b61_one(S, I):
    return fill(I, THREE, mfilter_f(difference(apply(toindices, o_g(I, R7)), sfilter_f(apply(toindices, o_g(I, R7)), fork(either, vline_i, hline_i))), fork(equality, identity, box)))


def solve_810b9b61(S, I):
    x1 = o_g(I, R7)
    x2 = apply(toindices, x1)
    x3 = fork(either, vline_i, hline_i)
    x4 = sfilter_f(x2, x3)
    x5 = difference(x2, x4)
    x6 = fork(equality, identity, box)
    x7 = mfilter_f(x5, x6)
    O = fill(I, THREE, x7)
    return O
