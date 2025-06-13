def solve_d4a91cb9_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), combine_f(connect(astuple(get_nth_f(get_nth_f(f_ofcolor(I, RED), F0), F0), get_nth_t(get_nth_f(f_ofcolor(I, CYAN), F0), L1)), get_nth_f(f_ofcolor(I, CYAN), F0)), connect(astuple(get_nth_f(get_nth_f(f_ofcolor(I, RED), F0), F0), get_nth_t(get_nth_f(f_ofcolor(I, CYAN), F0), L1)), get_nth_f(f_ofcolor(I, RED), F0))))


def solve_d4a91cb9(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = f_ofcolor(I, RED)
    x5 = get_nth_f(x4, F0)
    x6 = get_nth_f(x5, F0)
    x7 = f_ofcolor(I, CYAN)
    x8 = get_nth_f(x7, F0)
    x9 = get_nth_t(x8, L1)
    x10 = astuple(x6, x9)
    x11 = connect(x10, x8)
    x12 = connect(x10, x5)
    x13 = combine_f(x11, x12)
    O = underfill(I, x3, x13)
    return O
