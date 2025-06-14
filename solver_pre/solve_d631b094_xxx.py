def solve_d631b094_one(S, I):
    return canvas(other_f(palette_t(I), ZERO), astuple(ONE, size_f(f_ofcolor(I, other_f(palette_t(I), ZERO)))))


def solve_d631b094(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = other_f(x1, ZERO)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, x2)
    if x == 3:
        return x3
    x4 = size_f(x3)
    if x == 4:
        return x4
    x5 = astuple(ONE, x4)
    if x == 5:
        return x5
    O = canvas(x2, x5)
    return O
