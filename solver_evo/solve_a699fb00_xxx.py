def solve_a699fb00_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), intersection(shift(f_ofcolor(I, BLUE), RIGHT), shift(f_ofcolor(I, BLUE), LEFT)))


def solve_a699fb00(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = f_ofcolor(I, BLUE)
    x5 = shift(x4, RIGHT)
    x6 = shift(x4, LEFT)
    x7 = intersection(x5, x6)
    O = fill(I, x3, x7)
    return O
