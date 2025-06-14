def solve_dae9d2b5_one(S, I):
    return fill(lefthalf(I), SIX, combine_f(f_ofcolor(lefthalf(I), FOUR), f_ofcolor(righthalf(I), THREE)))


def solve_dae9d2b5(S, I, x=0):
    x1 = lefthalf(I)
    if x == 1:
        return x1
    x2 = f_ofcolor(x1, FOUR)
    if x == 2:
        return x2
    x3 = righthalf(I)
    if x == 3:
        return x3
    x4 = f_ofcolor(x3, THREE)
    if x == 4:
        return x4
    x5 = combine_f(x2, x4)
    if x == 5:
        return x5
    O = fill(x1, SIX, x5)
    return O
