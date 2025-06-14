def solve_25d8a9c8_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), toindices(mfilter_f(sizefilter(o_g(I, R4), THREE), hline_o))), BLACK, difference(asindices(I), toindices(mfilter_f(sizefilter(o_g(I, R4), THREE), hline_o))))


def solve_25d8a9c8(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F1)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R4)
    if x == 4:
        return x4
    x5 = sizefilter(x4, THREE)
    if x == 5:
        return x5
    x6 = mfilter_f(x5, hline_o)
    if x == 6:
        return x6
    x7 = toindices(x6)
    if x == 7:
        return x7
    x8 = fill(I, x3, x7)
    if x == 8:
        return x8
    x9 = asindices(I)
    if x == 9:
        return x9
    x10 = difference(x9, x7)
    if x == 10:
        return x10
    O = fill(x8, BLACK, x10)
    return O
