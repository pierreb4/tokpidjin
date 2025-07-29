def solve_fcb5c309_one(S, I):
    return replace(subgrid(get_arg_rank_f(difference(o_g(I, R5), colorfilter(o_g(I, R5), get_color_rank_t(I, L1))), size, F0), I), color(get_arg_rank_f(difference(o_g(I, R5), colorfilter(o_g(I, R5), get_color_rank_t(I, L1))), size, F0)), get_color_rank_t(I, L1))


def solve_fcb5c309(S, I):
    x1 = o_g(I, R5)
    x2 = get_color_rank_t(I, L1)
    x3 = colorfilter(x1, x2)
    x4 = difference(x1, x3)
    x5 = get_arg_rank_f(x4, size, F0)
    x6 = subgrid(x5, I)
    x7 = color(x5)
    O = replace(x6, x7, x2)
    return O
