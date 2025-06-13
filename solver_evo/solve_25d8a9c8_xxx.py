def solve_25d8a9c8_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), toindices(mfilter_f(sizefilter(o_g(I, R4), THREE), hline_o))), BLACK, difference(asindices(I), toindices(mfilter_f(sizefilter(o_g(I, R4), THREE), hline_o))))


def solve_25d8a9c8(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F1)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R4)
    x5 = sizefilter(x4, THREE)
    x6 = mfilter_f(x5, hline_o)
    x7 = toindices(x6)
    x8 = fill(I, x3, x7)
    x9 = asindices(I)
    x10 = difference(x9, x7)
    O = fill(x8, BLACK, x10)
    return O
