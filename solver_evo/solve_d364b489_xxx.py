def solve_d364b489_one(S, I):
    return fill(fill(fill(fill(I, CYAN, shift(f_ofcolor(I, BLUE), DOWN)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shift(f_ofcolor(I, BLUE), UP)), MAGENTA, shift(f_ofcolor(I, BLUE), RIGHT)), ORANGE, shift(f_ofcolor(I, BLUE), LEFT))


def solve_d364b489(S, I, x=0):
    x1 = f_ofcolor(I, BLUE)
    if x == 1:
        return x1
    x2 = shift(x1, DOWN)
    if x == 2:
        return x2
    x3 = fill(I, CYAN, x2)
    if x == 3:
        return x3
    x4 = identity(p_g)
    if x == 4:
        return x4
    x5 = rbind(get_nth_t, F0)
    if x == 5:
        return x5
    x6 = c_zo_n(S, x4, x5)
    if x == 6:
        return x6
    x7 = shift(x1, UP)
    if x == 7:
        return x7
    x8 = fill(x3, x6, x7)
    if x == 8:
        return x8
    x9 = shift(x1, RIGHT)
    if x == 9:
        return x9
    x10 = fill(x8, MAGENTA, x9)
    if x == 10:
        return x10
    x11 = shift(x1, LEFT)
    if x == 11:
        return x11
    O = fill(x10, ORANGE, x11)
    return O
