def solve_27f8ce4f_one(S, I):
    return fill(vconcat(vconcat(hconcat(hconcat(I, I), I), hconcat(hconcat(I, I), I)), hconcat(hconcat(I, I), I)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), difference(asindices(upscale_t(I, THREE)), f_ofcolor(upscale_t(I, THREE), get_color_rank_t(I, F0))))


def solve_27f8ce4f(S, I):
    x1 = hconcat(I, I)
    x2 = hconcat(x1, I)
    x3 = vconcat(x2, x2)
    x4 = vconcat(x3, x2)
    x5 = identity(p_g)
    x6 = rbind(get_nth_t, F0)
    x7 = c_zo_n(S, x5, x6)
    x8 = upscale_t(I, THREE)
    x9 = asindices(x8)
    x10 = get_color_rank_t(I, F0)
    x11 = f_ofcolor(x8, x10)
    x12 = difference(x9, x11)
    O = fill(x4, x7, x12)
    return O
