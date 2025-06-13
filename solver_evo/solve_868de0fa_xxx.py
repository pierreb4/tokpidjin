def solve_868de0fa_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(sfilter_f(sfilter_f(o_g(I, R4), square_f), compose(even, height_f)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), recolor_o(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(difference(sfilter_f(o_g(I, R4), square_f), sfilter_f(sfilter_f(o_g(I, R4), square_f), compose(even, height_f))))))


def solve_868de0fa(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R4)
    x5 = sfilter_f(x4, square_f)
    x6 = compose(even, height_f)
    x7 = sfilter_f(x5, x6)
    x8 = merge_f(x7)
    x9 = fill(I, x3, x8)
    x10 = rbind(get_nth_t, F1)
    x11 = c_zo_n(S, x1, x10)
    x12 = difference(x5, x7)
    x13 = merge_f(x12)
    x14 = recolor_o(x3, x13)
    O = fill(x9, x11, x14)
    return O
