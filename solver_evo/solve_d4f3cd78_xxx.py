def solve_d4f3cd78_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), delta(f_ofcolor(I, GRAY))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shoot(get_nth_f(difference(box(f_ofcolor(I, GRAY)), f_ofcolor(I, GRAY)), F0), position(box(f_ofcolor(I, GRAY)), difference(box(f_ofcolor(I, GRAY)), f_ofcolor(I, GRAY)))))


def solve_d4f3cd78(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = f_ofcolor(I, GRAY)
    x5 = delta(x4)
    x6 = fill(I, x3, x5)
    x7 = box(x4)
    x8 = difference(x7, x4)
    x9 = get_nth_f(x8, F0)
    x10 = position(x7, x8)
    x11 = shoot(x9, x10)
    O = fill(x6, x3, x11)
    return O
