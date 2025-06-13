def solve_dae9d2b5_one(S, I):
    return fill(lefthalf(I), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), combine_f(f_ofcolor(lefthalf(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F1))), f_ofcolor(righthalf(I), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)))))


def solve_dae9d2b5(S, I):
    x1 = lefthalf(I)
    x2 = identity(p_g)
    x3 = rbind(get_nth_t, F0)
    x4 = c_zo_n(S, x2, x3)
    x5 = rbind(get_nth_t, F1)
    x6 = c_iz_n(S, x2, x5)
    x7 = f_ofcolor(x1, x6)
    x8 = righthalf(I)
    x9 = c_iz_n(S, x2, x3)
    x10 = f_ofcolor(x8, x9)
    x11 = combine_f(x7, x10)
    O = fill(x1, x4, x11)
    return O
