def solve_d631b094_one(S, I):
    return canvas(other_f(palette_t(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))), astuple(ONE, size_f(f_ofcolor(I, other_f(palette_t(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))))


def solve_d631b094(S, I, x=0):
    x1 = palette_t(I)
    if x == 1:
        return x1
    x2 = identity(p_g)
    if x == 2:
        return x2
    x3 = rbind(get_nth_t, F0)
    if x == 3:
        return x3
    x4 = c_iz_n(S, x2, x3)
    if x == 4:
        return x4
    x5 = other_f(x1, x4)
    if x == 5:
        return x5
    x6 = f_ofcolor(I, x5)
    if x == 6:
        return x6
    x7 = size_f(x6)
    if x == 7:
        return x7
    x8 = astuple(ONE, x7)
    if x == 8:
        return x8
    O = canvas(x5, x8)
    return O
