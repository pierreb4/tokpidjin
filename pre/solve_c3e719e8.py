def solve_c3e719e8_one(S, I):
    return fill(vconcat(vconcat(hconcat(hconcat(I, I), I), hconcat(hconcat(I, I), I)), hconcat(hconcat(I, I), I)), ZERO, difference(asindices(upscale_t(I, THREE)), f_ofcolor(upscale_t(I, THREE), get_color_rank_t(I, F0))))


def solve_c3e719e8(S, I):
    x1 = hconcat(I, I)
    x2 = hconcat(x1, I)
    x3 = vconcat(x2, x2)
    x4 = vconcat(x3, x2)
    x5 = upscale_t(I, THREE)
    x6 = asindices(x5)
    x7 = get_color_rank_t(I, F0)
    x8 = f_ofcolor(x5, x7)
    x9 = difference(x6, x8)
    O = fill(x4, ZERO, x9)
    return O
