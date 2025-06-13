def solve_cce03e0d_one(S, I):
    return fill(vconcat(vconcat(hconcat(hconcat(I, I), I), hconcat(hconcat(I, I), I)), hconcat(hconcat(I, I), I)), BLACK, combine_f(f_ofcolor(upscale_t(I, THREE), BLACK), f_ofcolor(upscale_t(I, THREE), BLUE)))


def solve_cce03e0d(S, I):
    x1 = hconcat(I, I)
    x2 = hconcat(x1, I)
    x3 = vconcat(x2, x2)
    x4 = vconcat(x3, x2)
    x5 = upscale_t(I, THREE)
    x6 = f_ofcolor(x5, BLACK)
    x7 = f_ofcolor(x5, BLUE)
    x8 = combine_f(x6, x7)
    O = fill(x4, BLACK, x8)
    return O
