def solve_d4f3cd78_one(S, I):
    return fill(fill(I, EIGHT, delta(f_ofcolor(I, FIVE))), EIGHT, shoot(get_nth_f(difference(box(f_ofcolor(I, FIVE)), f_ofcolor(I, FIVE)), F0), position(box(f_ofcolor(I, FIVE)), difference(box(f_ofcolor(I, FIVE)), f_ofcolor(I, FIVE)))))


def solve_d4f3cd78(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = delta(x1)
    if x == 2:
        return x2
    x3 = fill(I, EIGHT, x2)
    if x == 3:
        return x3
    x4 = box(x1)
    if x == 4:
        return x4
    x5 = difference(x4, x1)
    if x == 5:
        return x5
    x6 = get_nth_f(x5, F0)
    if x == 6:
        return x6
    x7 = position(x4, x5)
    if x == 7:
        return x7
    x8 = shoot(x6, x7)
    if x == 8:
        return x8
    O = fill(x3, EIGHT, x8)
    return O
