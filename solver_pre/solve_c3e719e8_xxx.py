def solve_c3e719e8_one(S, I):
    return fill(vconcat(vconcat(hconcat(hconcat(I, I), I), hconcat(hconcat(I, I), I)), hconcat(hconcat(I, I), I)), ZERO, difference(asindices(upscale_t(I, THREE)), f_ofcolor(upscale_t(I, THREE), get_color_rank_t(I, F0))))


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
    x5 = upscale_t(I, THREE)
    if x == 5:
        return x5
    x6 = asindices(x5)
    if x == 6:
        return x6
    x7 = get_color_rank_t(I, F0)
    if x == 7:
        return x7
    x8 = f_ofcolor(x5, x7)
    if x == 8:
        return x8
    x9 = difference(x6, x8)
    if x == 9:
        return x9
    O = fill(x4, ZERO, x9)
    return O
