def solve_868de0fa_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(sfilter_f(sfilter_f(o_g(I, R4), square_f), compose(even, height_f)))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), recolor_o(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(difference(sfilter_f(o_g(I, R4), square_f), sfilter_f(sfilter_f(o_g(I, R4), square_f), compose(even, height_f))))))


def solve_868de0fa(S, I, x=0):
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
    x5 = sfilter_f(x4, square_f)
    if x == 5:
        return x5
    x6 = compose(even, height_f)
    if x == 6:
        return x6
    x7 = sfilter_f(x5, x6)
    if x == 7:
        return x7
    x8 = merge_f(x7)
    if x == 8:
        return x8
    x9 = fill(I, x3, x8)
    if x == 9:
        return x9
    x10 = rbind(get_nth_t, F1)
    if x == 10:
        return x10
    x11 = c_zo_n(S, x1, x10)
    if x == 11:
        return x11
    x12 = difference(x5, x7)
    if x == 12:
        return x12
    x13 = merge_f(x12)
    if x == 13:
        return x13
    x14 = recolor_o(x3, x13)
    if x == 14:
        return x14
    O = fill(x9, x11, x14)
    return O
