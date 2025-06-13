def solve_d2abd087_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), mfilter_f(o_g(I, R5), matcher(size, MAGENTA))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(o_g(I, R5), compose(flip, matcher(size, MAGENTA))))


def solve_d2abd087(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F1)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R5)
    x5 = matcher(size, MAGENTA)
    x6 = mfilter_f(x4, x5)
    x7 = fill(I, x3, x6)
    x8 = rbind(get_nth_t, F0)
    x9 = c_zo_n(S, x1, x8)
    x10 = compose(flip, x5)
    x11 = mfilter_f(x4, x10)
    O = fill(x7, x9, x11)
    return O
