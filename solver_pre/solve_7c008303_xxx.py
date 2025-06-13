def solve_7c008303_one(S, I):
    return fill(upscale_t(compress(replace(replace(I, THREE, ZERO), EIGHT, ZERO)), THREE), ZERO, f_ofcolor(subgrid(f_ofcolor(I, THREE), I), ZERO))


def solve_7c008303(S, I):
    x1 = replace(I, THREE, ZERO)
    x2 = replace(x1, EIGHT, ZERO)
    x3 = compress(x2)
    x4 = upscale_t(x3, THREE)
    x5 = f_ofcolor(I, THREE)
    x6 = subgrid(x5, I)
    x7 = f_ofcolor(x6, ZERO)
    O = fill(x4, ZERO, x7)
    return O
