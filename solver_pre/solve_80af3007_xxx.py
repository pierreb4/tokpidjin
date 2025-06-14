def solve_80af3007_one(S, I):
    return downscale(cellwise(upscale_t(subgrid(get_nth_f(o_g(I, R7), F0), I), THREE), vconcat(vconcat(hconcat(hconcat(subgrid(get_nth_f(o_g(I, R7), F0), I), subgrid(get_nth_f(o_g(I, R7), F0), I)), subgrid(get_nth_f(o_g(I, R7), F0), I)), hconcat(hconcat(subgrid(get_nth_f(o_g(I, R7), F0), I), subgrid(get_nth_f(o_g(I, R7), F0), I)), subgrid(get_nth_f(o_g(I, R7), F0), I))), hconcat(hconcat(subgrid(get_nth_f(o_g(I, R7), F0), I), subgrid(get_nth_f(o_g(I, R7), F0), I)), subgrid(get_nth_f(o_g(I, R7), F0), I))), ZERO), THREE)


def solve_80af3007(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = upscale_t(x3, THREE)
    if x == 4:
        return x4
    x5 = hconcat(x3, x3)
    if x == 5:
        return x5
    x6 = hconcat(x5, x3)
    if x == 6:
        return x6
    x7 = vconcat(x6, x6)
    if x == 7:
        return x7
    x8 = vconcat(x7, x6)
    if x == 8:
        return x8
    x9 = cellwise(x4, x8, ZERO)
    if x == 9:
        return x9
    O = downscale(x9, THREE)
    return O
