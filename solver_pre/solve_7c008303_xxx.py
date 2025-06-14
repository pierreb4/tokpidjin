def solve_7c008303_one(S, I):
    return fill(upscale_t(compress(replace(replace(I, THREE, ZERO), EIGHT, ZERO)), THREE), ZERO, f_ofcolor(subgrid(f_ofcolor(I, THREE), I), ZERO))


def solve_7c008303(S, I, x=0):
    x1 = replace(I, THREE, ZERO)
    if x == 1:
        return x1
    x2 = replace(x1, EIGHT, ZERO)
    if x == 2:
        return x2
    x3 = compress(x2)
    if x == 3:
        return x3
    x4 = upscale_t(x3, THREE)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, THREE)
    if x == 5:
        return x5
    x6 = subgrid(x5, I)
    if x == 6:
        return x6
    x7 = f_ofcolor(x6, ZERO)
    if x == 7:
        return x7
    O = fill(x4, ZERO, x7)
    return O
