def solve_83302e8f_one(S, I):
    return paint(paint(I, recolor_o(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(sfilter_f(colorfilter(o_g(I, R4), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), square_f)))), recolor_o(c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), merge_f(difference(colorfilter(o_g(I, R4), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), sfilter_f(colorfilter(o_g(I, R4), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), square_f)))))


def solve_83302e8f(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R4)
    if x == 4:
        return x4
    x5 = c_iz_n(S, x1, x2)
    if x == 5:
        return x5
    x6 = colorfilter(x4, x5)
    if x == 6:
        return x6
    x7 = sfilter_f(x6, square_f)
    if x == 7:
        return x7
    x8 = merge_f(x7)
    if x == 8:
        return x8
    x9 = recolor_o(x3, x8)
    if x == 9:
        return x9
    x10 = paint(I, x9)
    if x == 10:
        return x10
    x11 = rbind(get_nth_t, F1)
    if x == 11:
        return x11
    x12 = c_zo_n(S, x1, x11)
    if x == 12:
        return x12
    x13 = difference(x6, x7)
    if x == 13:
        return x13
    x14 = merge_f(x13)
    if x == 14:
        return x14
    x15 = recolor_o(x12, x14)
    if x == 15:
        return x15
    O = paint(x10, x15)
    return O
