def solve_c3e719e8_one(S, I):
    return fill(vconcat(vconcat(hconcat(hconcat(I, I), I), hconcat(hconcat(I, I), I)), hconcat(hconcat(I, I), I)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), difference(asindices(upscale_t(I, THREE)), f_ofcolor(upscale_t(I, THREE), get_color_rank_t(I, F0))))


def solve_c3e719e8(S, I, x=0):
    x1 = hconcat(I, I)
    if x == 1:
        return x1
    x2 = hconcat(x1, I)
    if x == 2:
        return x2
    x3 = vconcat(x2, x2)
    if x == 3:
        return x3
    x4 = vconcat(x3, x2)
    if x == 4:
        return x4
    x5 = identity(p_g)
    if x == 5:
        return x5
    x6 = rbind(get_nth_t, F0)
    if x == 6:
        return x6
    x7 = c_zo_n(S, x5, x6)
    if x == 7:
        return x7
    x8 = upscale_t(I, THREE)
    if x == 8:
        return x8
    x9 = asindices(x8)
    if x == 9:
        return x9
    x10 = get_color_rank_t(I, F0)
    if x == 10:
        return x10
    x11 = f_ofcolor(x8, x10)
    if x == 11:
        return x11
    x12 = difference(x9, x11)
    if x == 12:
        return x12
    O = fill(x4, x7, x12)
    return O
