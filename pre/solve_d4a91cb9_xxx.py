def solve_d4a91cb9_one(S, I):
    return underfill(I, FOUR, combine_f(connect(astuple(get_nth_f(get_nth_f(f_ofcolor(I, TWO), F0), F0), get_nth_t(get_nth_f(f_ofcolor(I, EIGHT), F0), L1)), get_nth_f(f_ofcolor(I, EIGHT), F0)), connect(astuple(get_nth_f(get_nth_f(f_ofcolor(I, TWO), F0), F0), get_nth_t(get_nth_f(f_ofcolor(I, EIGHT), F0), L1)), get_nth_f(f_ofcolor(I, TWO), F0))))


def solve_d4a91cb9(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = get_nth_f(x1, F0)
    x3 = get_nth_f(x2, F0)
    x4 = f_ofcolor(I, EIGHT)
    x5 = get_nth_f(x4, F0)
    x6 = get_nth_t(x5, L1)
    x7 = astuple(x3, x6)
    x8 = connect(x7, x5)
    x9 = connect(x7, x2)
    x10 = combine_f(x8, x9)
    O = underfill(I, FOUR, x10)
    return O
