def solve_c0f76784_one(S, I):
    return fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), merge_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), square_f))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), get_arg_rank_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), square_f), size, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(sizefilter(sfilter_f(colorfilter(o_g(I, R4), BLACK), square_f), ONE)))


def solve_c0f76784(S, I, x=0):
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
    x5 = colorfilter(x4, BLACK)
    if x == 5:
        return x5
    x6 = sfilter_f(x5, square_f)
    if x == 6:
        return x6
    x7 = merge_f(x6)
    if x == 7:
        return x7
    x8 = fill(I, x3, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_t, F2)
    if x == 9:
        return x9
    x10 = c_zo_n(S, x1, x9)
    if x == 10:
        return x10
    x11 = get_arg_rank_f(x6, size, F0)
    if x == 11:
        return x11
    x12 = fill(x8, x10, x11)
    if x == 12:
        return x12
    x13 = rbind(get_nth_t, F0)
    if x == 13:
        return x13
    x14 = c_zo_n(S, x1, x13)
    if x == 14:
        return x14
    x15 = sizefilter(x6, ONE)
    if x == 15:
        return x15
    x16 = merge_f(x15)
    if x == 16:
        return x16
    O = fill(x12, x14, x16)
    return O
