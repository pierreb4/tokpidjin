def solve_d4f3cd78_one(S, I):
    return fill(fill(I, EIGHT, delta(f_ofcolor(I, FIVE))), EIGHT, shoot(get_nth_f(difference(box(f_ofcolor(I, FIVE)), f_ofcolor(I, FIVE)), F0), position(box(f_ofcolor(I, FIVE)), difference(box(f_ofcolor(I, FIVE)), f_ofcolor(I, FIVE)))))


def solve_d4f3cd78(S, I):
    x1 = f_ofcolor(I, FIVE)
    x2 = delta(x1)
    x3 = fill(I, EIGHT, x2)
    x4 = box(x1)
    x5 = difference(x4, x1)
    x6 = get_nth_f(x5, F0)
    x7 = position(x4, x5)
    x8 = shoot(x6, x7)
    O = fill(x3, EIGHT, x8)
    return O
