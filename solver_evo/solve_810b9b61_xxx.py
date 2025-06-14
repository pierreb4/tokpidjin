def solve_810b9b61_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(difference(apply(toindices, o_g(I, R7)), sfilter_f(apply(toindices, o_g(I, R7)), fork(either, vline_i, hline_i))), fork(equality, identity, box)))


def solve_810b9b61(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R7)
    if x == 4:
        return x4
    x5 = apply(toindices, x4)
    if x == 5:
        return x5
    x6 = fork(either, vline_i, hline_i)
    if x == 6:
        return x6
    x7 = sfilter_f(x5, x6)
    if x == 7:
        return x7
    x8 = difference(x5, x7)
    if x == 8:
        return x8
    x9 = fork(equality, identity, box)
    if x == 9:
        return x9
    x10 = mfilter_f(x8, x9)
    if x == 10:
        return x10
    O = fill(I, x3, x10)
    return O
