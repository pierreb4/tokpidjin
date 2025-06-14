def solve_d4a91cb9_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), combine_f(connect(astuple(get_nth_f(get_nth_f(f_ofcolor(I, RED), F0), F0), get_nth_t(get_nth_f(f_ofcolor(I, CYAN), F0), L1)), get_nth_f(f_ofcolor(I, CYAN), F0)), connect(astuple(get_nth_f(get_nth_f(f_ofcolor(I, RED), F0), F0), get_nth_t(get_nth_f(f_ofcolor(I, CYAN), F0), L1)), get_nth_f(f_ofcolor(I, RED), F0))))


def solve_d4a91cb9(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, RED)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = get_nth_f(x5, F0)
    if x == 6:
        return x6
    x7 = f_ofcolor(I, CYAN)
    if x == 7:
        return x7
    x8 = get_nth_f(x7, F0)
    if x == 8:
        return x8
    x9 = get_nth_t(x8, L1)
    if x == 9:
        return x9
    x10 = astuple(x6, x9)
    if x == 10:
        return x10
    x11 = connect(x10, x8)
    if x == 11:
        return x11
    x12 = connect(x10, x5)
    if x == 12:
        return x12
    x13 = combine_f(x11, x12)
    if x == 13:
        return x13
    O = underfill(I, x3, x13)
    return O
