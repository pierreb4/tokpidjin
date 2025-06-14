def solve_77fdfe62_one(S, I):
    return fill(upscale_t(compress(replace(replace(I, EIGHT, ZERO), ONE, ZERO)), halve(width_t(subgrid(f_ofcolor(I, EIGHT), I)))), ZERO, f_ofcolor(subgrid(f_ofcolor(I, EIGHT), I), ZERO))


def solve_77fdfe62(S, I, x=0):
    x1 = replace(I, EIGHT, ZERO)
    if x == 1:
        return x1
    x2 = replace(x1, ONE, ZERO)
    if x == 2:
        return x2
    x3 = compress(x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = subgrid(x4, I)
    if x == 5:
        return x5
    x6 = width_t(x5)
    if x == 6:
        return x6
    x7 = halve(x6)
    if x == 7:
        return x7
    x8 = upscale_t(x3, x7)
    if x == 8:
        return x8
    x9 = f_ofcolor(x5, ZERO)
    if x == 9:
        return x9
    O = fill(x8, ZERO, x9)
    return O
