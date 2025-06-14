def solve_cf98881b_one(S, I):
    return fill(fill(get_nth_t(remove_t(get_nth_t(hsplit(I, THREE), F0), hsplit(I, THREE)), L1), NINE, f_ofcolor(get_nth_t(remove_t(get_nth_t(hsplit(I, THREE), F0), hsplit(I, THREE)), F0), NINE)), FOUR, f_ofcolor(get_nth_t(hsplit(I, THREE), F0), FOUR))


def solve_cf98881b(S, I, x=0):
    x1 = hsplit(I, THREE)
    if x == 1:
        return x1
    x2 = get_nth_t(x1, F0)
    if x == 2:
        return x2
    x3 = remove_t(x2, x1)
    if x == 3:
        return x3
    x4 = get_nth_t(x3, L1)
    if x == 4:
        return x4
    x5 = get_nth_t(x3, F0)
    if x == 5:
        return x5
    x6 = f_ofcolor(x5, NINE)
    if x == 6:
        return x6
    x7 = fill(x4, NINE, x6)
    if x == 7:
        return x7
    x8 = f_ofcolor(x2, FOUR)
    if x == 8:
        return x8
    O = fill(x7, FOUR, x8)
    return O
