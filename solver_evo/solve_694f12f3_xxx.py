def solve_694f12f3_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), compose(backdrop, inbox)(get_arg_rank_f(colorfilter(o_g(I, R4), YELLOW), size, L1))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), compose(backdrop, inbox)(get_arg_rank_f(colorfilter(o_g(I, R4), YELLOW), size, F0)))


def solve_694f12f3(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = compose(backdrop, inbox)
    x5 = o_g(I, R4)
    x6 = colorfilter(x5, YELLOW)
    x7 = get_arg_rank_f(x6, size, L1)
    x8 = x4(x7)
    x9 = fill(I, x3, x8)
    x10 = rbind(get_nth_t, F1)
    x11 = c_zo_n(S, x1, x10)
    x12 = get_arg_rank_f(x6, size, F0)
    x13 = x4(x12)
    O = fill(x9, x11, x13)
    return O
