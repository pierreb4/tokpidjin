def solve_dae9d2b5_one(S, I):
    return fill(lefthalf(I), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), combine_f(f_ofcolor(lefthalf(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F1))), f_ofcolor(righthalf(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))


def solve_dae9d2b5(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = identity(p_g)
    if x == 2:
        return x2
    x3 = rbind(get_nth_t, F0)
    if x == 3:
        return x3
    x4 = c_zo_n(S, x2, x3)
    if x == 4:
        return x4
    x5 = rbind(get_nth_t, F1)
    if x == 5:
        return x5
    x6 = c_iz_n(S, x2, x5)
    if x == 6:
        return x6
    x7 = f_ofcolor(x1, x6)
    if x == 7:
        return x7
    x8 = righthalf(I)
    if x == 8:
        return x8
    x9 = c_iz_n(S, x2, x3)
    if x == 9:
        return x9
    x10 = f_ofcolor(x8, x9)
    if x == 10:
        return x10
    x11 = combine_f(x7, x10)
    if x == 11:
        return x11
    O = fill(x1, x4, x11)
    return O
