def solve_d4f3cd78_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), delta(f_ofcolor(I, GRAY))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shoot(get_nth_f(difference(box(f_ofcolor(I, GRAY)), f_ofcolor(I, GRAY)), F0), position(box(f_ofcolor(I, GRAY)), difference(box(f_ofcolor(I, GRAY)), f_ofcolor(I, GRAY)))))


def solve_d4f3cd78(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, GRAY)
    if x == 4:
        return x4
    x5 = delta(x4)
    if x == 5:
        return x5
    x6 = fill(I, x3, x5)
    if x == 6:
        return x6
    x7 = box(x4)
    if x == 7:
        return x7
    x8 = difference(x7, x4)
    if x == 8:
        return x8
    x9 = get_nth_f(x8, F0)
    if x == 9:
        return x9
    x10 = position(x7, x8)
    if x == 10:
        return x10
    x11 = shoot(x9, x10)
    if x == 11:
        return x11
    O = fill(x6, x3, x11)
    return O
