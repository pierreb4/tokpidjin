def solve_810b9b61_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(difference(apply(toindices, o_g(I, R7)), sfilter_f(apply(toindices, o_g(I, R7)), fork(either, vline_i, hline_i))), fork(equality, identity, box)))


def solve_810b9b61(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R7)
    x5 = apply(toindices, x4)
    x6 = fork(either, vline_i, hline_i)
    x7 = sfilter_f(x5, x6)
    x8 = difference(x5, x7)
    x9 = fork(equality, identity, box)
    x10 = mfilter_f(x8, x9)
    O = fill(I, x3, x10)
    return O
