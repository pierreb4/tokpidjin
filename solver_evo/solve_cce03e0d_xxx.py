def solve_cce03e0d_one(S, I):
    return fill(vconcat(vconcat(hconcat(hconcat(I, I), I), hconcat(hconcat(I, I), I)), hconcat(hconcat(I, I), I)), BLACK, combine_f(f_ofcolor(upscale_t(I, THREE), BLACK), f_ofcolor(upscale_t(I, THREE), BLUE)))


def solve_cce03e0d(S, I, x=0):
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
    x6 = f_ofcolor(x5, BLACK)
    if x == 6:
        return x6
    x7 = f_ofcolor(x5, BLUE)
    if x == 7:
        return x7
    x8 = combine_f(x6, x7)
    if x == 8:
        return x8
    O = fill(x4, BLACK, x8)
    return O
