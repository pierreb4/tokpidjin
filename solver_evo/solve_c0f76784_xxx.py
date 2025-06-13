def solve_c0f76784_one(S, I):
    return fill(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), merge_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), square_f))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), get_arg_rank_f(sfilter_f(colorfilter(o_g(I, R4), BLACK), square_f), size, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), merge_f(sizefilter(sfilter_f(colorfilter(o_g(I, R4), BLACK), square_f), ONE)))


def solve_c0f76784(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F1)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R4)
    x5 = colorfilter(x4, BLACK)
    x6 = sfilter_f(x5, square_f)
    x7 = merge_f(x6)
    x8 = fill(I, x3, x7)
    x9 = rbind(get_nth_t, F2)
    x10 = c_zo_n(S, x1, x9)
    x11 = get_arg_rank_f(x6, size, F0)
    x12 = fill(x8, x10, x11)
    x13 = rbind(get_nth_t, F0)
    x14 = c_zo_n(S, x1, x13)
    x15 = sizefilter(x6, ONE)
    x16 = merge_f(x15)
    O = fill(x12, x14, x16)
    return O
