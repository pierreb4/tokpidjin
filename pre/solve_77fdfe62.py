def solve_77fdfe62_one(S, I):
    return fill(upscale_t(compress(replace(replace(I, EIGHT, ZERO), ONE, ZERO)), halve(width_t(subgrid(f_ofcolor(I, EIGHT), I)))), ZERO, f_ofcolor(subgrid(f_ofcolor(I, EIGHT), I), ZERO))


def solve_77fdfe62(S, I):
    x1 = replace(I, EIGHT, ZERO)
    x2 = replace(x1, ONE, ZERO)
    x3 = compress(x2)
    x4 = f_ofcolor(I, EIGHT)
    x5 = subgrid(x4, I)
    x6 = width_t(x5)
    x7 = halve(x6)
    x8 = upscale_t(x3, x7)
    x9 = f_ofcolor(x5, ZERO)
    O = fill(x8, ZERO, x9)
    return O
