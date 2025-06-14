def solve_5ad4f10b_one(S, I):
    return downscale(replace(replace(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), get_color_rank_t(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), L1), ZERO), color(get_arg_rank_f(o_g(I, R7), size, F0)), get_color_rank_t(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), L1)), divide(height_t(replace(replace(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), get_color_rank_t(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), L1), ZERO), color(get_arg_rank_f(o_g(I, R7), size, F0)), get_color_rank_t(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), L1))), THREE))


def solve_5ad4f10b(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = get_color_rank_t(x3, L1)
    if x == 4:
        return x4
    x5 = replace(x3, x4, ZERO)
    if x == 5:
        return x5
    x6 = color(x2)
    if x == 6:
        return x6
    x7 = replace(x5, x6, x4)
    if x == 7:
        return x7
    x8 = height_t(x7)
    if x == 8:
        return x8
    x9 = divide(x8, THREE)
    if x == 9:
        return x9
    O = downscale(x7, x9)
    return O
