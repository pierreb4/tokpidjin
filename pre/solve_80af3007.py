def solve_80af3007_one(S, I):
    return downscale(cellwise(upscale_t(subgrid(get_nth_f(o_g(I, R7), F0), I), THREE), vconcat(vconcat(hconcat(hconcat(subgrid(get_nth_f(o_g(I, R7), F0), I), subgrid(get_nth_f(o_g(I, R7), F0), I)), subgrid(get_nth_f(o_g(I, R7), F0), I)), hconcat(hconcat(subgrid(get_nth_f(o_g(I, R7), F0), I), subgrid(get_nth_f(o_g(I, R7), F0), I)), subgrid(get_nth_f(o_g(I, R7), F0), I))), hconcat(hconcat(subgrid(get_nth_f(o_g(I, R7), F0), I), subgrid(get_nth_f(o_g(I, R7), F0), I)), subgrid(get_nth_f(o_g(I, R7), F0), I))), ZERO), THREE)


def solve_80af3007(S, I):
    x1 = o_g(I, R7)
    x2 = get_nth_f(x1, F0)
    x3 = subgrid(x2, I)
    x4 = upscale_t(x3, THREE)
    x5 = hconcat(x3, x3)
    x6 = hconcat(x5, x3)
    x7 = vconcat(x6, x6)
    x8 = vconcat(x7, x6)
    x9 = cellwise(x4, x8, ZERO)
    O = downscale(x9, THREE)
    return O
