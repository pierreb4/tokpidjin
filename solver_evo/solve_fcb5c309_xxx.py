def solve_fcb5c309_one(S, I):
    return replace(subgrid(get_arg_rank_f(difference(o_g(I, R5), colorfilter(o_g(I, R5), get_color_rank_t(I, L1))), size, F0), I), color(get_arg_rank_f(difference(o_g(I, R5), colorfilter(o_g(I, R5), get_color_rank_t(I, L1))), size, F0)), get_color_rank_t(I, L1))


def solve_fcb5c309(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_color_rank_t(I, L1)
    if x == 2:
        return x2
    x3 = colorfilter(x1, x2)
    if x == 3:
        return x3
    x4 = difference(x1, x3)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x4, size, F0)
    if x == 5:
        return x5
    x6 = subgrid(x5, I)
    if x == 6:
        return x6
    x7 = color(x5)
    if x == 7:
        return x7
    O = replace(x6, x7, x2)
    return O
