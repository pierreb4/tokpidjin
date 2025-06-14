def solve_c9f8e694_one(S, I):
    return fill(hupscale(crop(I, ORIGIN, astuple(height_t(I), ONE)), width_t(I)), BLACK, f_ofcolor(I, BLACK))


def solve_c9f8e694(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = astuple(x1, ONE)
    if x == 2:
        return x2
    x3 = crop(I, ORIGIN, x2)
    if x == 3:
        return x3
    x4 = width_t(I)
    if x == 4:
        return x4
    x5 = hupscale(x3, x4)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, BLACK)
    if x == 6:
        return x6
    O = fill(x5, BLACK, x6)
    return O
