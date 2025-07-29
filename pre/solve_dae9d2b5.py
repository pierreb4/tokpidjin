def solve_dae9d2b5_one(S, I):
    return fill(lefthalf(I), SIX, combine_f(f_ofcolor(lefthalf(I), FOUR), f_ofcolor(righthalf(I), THREE)))


def solve_dae9d2b5(S, I):
    x1 = lefthalf(I)
    x2 = f_ofcolor(x1, FOUR)
    x3 = righthalf(I)
    x4 = f_ofcolor(x3, THREE)
    x5 = combine_f(x2, x4)
    O = fill(x1, SIX, x5)
    return O
