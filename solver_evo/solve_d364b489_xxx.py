def solve_d364b489_one(S, I):
    return fill(fill(fill(fill(I, CYAN, shift(f_ofcolor(I, BLUE), DOWN)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shift(f_ofcolor(I, BLUE), UP)), MAGENTA, shift(f_ofcolor(I, BLUE), RIGHT)), ORANGE, shift(f_ofcolor(I, BLUE), LEFT))


def solve_d364b489(S, I):
    x1 = f_ofcolor(I, BLUE)
    x2 = shift(x1, DOWN)
    x3 = fill(I, CYAN, x2)
    x4 = identity(p_g)
    x5 = rbind(get_nth_t, F0)
    x6 = c_zo_n(S, x4, x5)
    x7 = shift(x1, UP)
    x8 = fill(x3, x6, x7)
    x9 = shift(x1, RIGHT)
    x10 = fill(x8, MAGENTA, x9)
    x11 = shift(x1, LEFT)
    O = fill(x10, ORANGE, x11)
    return O
