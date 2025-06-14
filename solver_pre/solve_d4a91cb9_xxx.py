def solve_d4a91cb9_one(S, I):
    return underfill(I, FOUR, combine_f(connect(astuple(get_nth_f(get_nth_f(f_ofcolor(I, TWO), F0), F0), get_nth_t(get_nth_f(f_ofcolor(I, EIGHT), F0), L1)), get_nth_f(f_ofcolor(I, EIGHT), F0)), connect(astuple(get_nth_f(get_nth_f(f_ofcolor(I, TWO), F0), F0), get_nth_t(get_nth_f(f_ofcolor(I, EIGHT), F0), L1)), get_nth_f(f_ofcolor(I, TWO), F0))))


def solve_d4a91cb9(S, I, x=0):
    x1 = f_ofcolor(I, TWO)
    if x == 1:
        return x1
    x2 = get_nth_f(x1, F0)
    if x == 2:
        return x2
    x3 = get_nth_f(x2, F0)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = get_nth_t(x5, L1)
    if x == 6:
        return x6
    x7 = astuple(x3, x6)
    if x == 7:
        return x7
    x8 = connect(x7, x5)
    if x == 8:
        return x8
    x9 = connect(x7, x2)
    if x == 9:
        return x9
    x10 = combine_f(x8, x9)
    if x == 10:
        return x10
    O = underfill(I, FOUR, x10)
    return O
