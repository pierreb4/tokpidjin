def solve_5ad4f10b_one(S, I):
    return downscale(replace(replace(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), get_color_rank_t(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), L1), BLACK), color(get_arg_rank_f(o_g(I, R7), size, F0)), get_color_rank_t(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), L1)), divide(height_t(replace(replace(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), get_color_rank_t(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), L1), BLACK), color(get_arg_rank_f(o_g(I, R7), size, F0)), get_color_rank_t(subgrid(get_arg_rank_f(o_g(I, R7), size, F0), I), L1))), THREE))


def solve_5ad4f10b(S, I):
    x1 = o_g(I, R7)
    x2 = get_arg_rank_f(x1, size, F0)
    x3 = subgrid(x2, I)
    x4 = get_color_rank_t(x3, L1)
    x5 = replace(x3, x4, BLACK)
    x6 = color(x2)
    x7 = replace(x5, x6, x4)
    x8 = height_t(x7)
    x9 = divide(x8, THREE)
    O = downscale(x7, x9)
    return O
