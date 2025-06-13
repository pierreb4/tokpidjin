def solve_c9f8e694_one(S, I):
    return fill(hupscale(crop(I, ORIGIN, astuple(height_t(I), ONE)), width_t(I)), BLACK, f_ofcolor(I, BLACK))


def solve_c9f8e694(S, I):
    x1 = height_t(I)
    x2 = astuple(x1, ONE)
    x3 = crop(I, ORIGIN, x2)
    x4 = width_t(I)
    x5 = hupscale(x3, x4)
    x6 = f_ofcolor(I, BLACK)
    O = fill(x5, BLACK, x6)
    return O
