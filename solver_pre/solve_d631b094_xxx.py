def solve_d631b094_one(S, I):
    return canvas(other_f(palette_t(I), ZERO), astuple(ONE, size_f(f_ofcolor(I, other_f(palette_t(I), ZERO)))))


def solve_d631b094(S, I):
    x1 = palette_t(I)
    x2 = other_f(x1, ZERO)
    x3 = f_ofcolor(I, x2)
    x4 = size_f(x3)
    x5 = astuple(ONE, x4)
    O = canvas(x2, x5)
    return O
