def solve_c9f8e694_one(S, I):
    return fill(hupscale(crop(I, ORIGIN, astuple(height_t(I), ONE)), width_t(I)), ZERO, f_ofcolor(I, ZERO))


def solve_c9f8e694(S, I):
    x1 = height_t(I)
    x2 = astuple(x1, ONE)
    x3 = crop(I, ORIGIN, x2)
    x4 = width_t(I)
    x5 = hupscale(x3, x4)
    x6 = f_ofcolor(I, ZERO)
    O = fill(x5, ZERO, x6)
    return O
