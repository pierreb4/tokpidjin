def solve_83302e8f_one(S, I):
    return paint(paint(I, recolor_o(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(sfilter_f(colorfilter(o_g(I, R4), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), square_f)))), recolor_o(c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), merge_f(difference(colorfilter(o_g(I, R4), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), sfilter_f(colorfilter(o_g(I, R4), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), square_f)))))


def solve_83302e8f(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R4)
    x5 = c_iz_n(S, x1, x2)
    x6 = colorfilter(x4, x5)
    x7 = sfilter_f(x6, square_f)
    x8 = merge_f(x7)
    x9 = recolor_o(x3, x8)
    x10 = paint(I, x9)
    x11 = rbind(get_nth_t, F1)
    x12 = c_zo_n(S, x1, x11)
    x13 = difference(x6, x7)
    x14 = merge_f(x13)
    x15 = recolor_o(x12, x14)
    O = paint(x10, x15)
    return O
