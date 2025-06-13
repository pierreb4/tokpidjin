def solve_cf98881b_one(S, I):
    return fill(fill(get_nth_t(remove_t(get_nth_t(hsplit(I, THREE), F0), hsplit(I, THREE)), L1), BURGUNDY, f_ofcolor(get_nth_t(remove_t(get_nth_t(hsplit(I, THREE), F0), hsplit(I, THREE)), F0), BURGUNDY)), YELLOW, f_ofcolor(get_nth_t(hsplit(I, THREE), F0), YELLOW))


def solve_cf98881b(S, I):
    x1 = hsplit(I, THREE)
    x2 = get_nth_t(x1, F0)
    x3 = remove_t(x2, x1)
    x4 = get_nth_t(x3, L1)
    x5 = get_nth_t(x3, F0)
    x6 = f_ofcolor(x5, BURGUNDY)
    x7 = fill(x4, BURGUNDY, x6)
    x8 = f_ofcolor(x2, YELLOW)
    O = fill(x7, YELLOW, x8)
    return O
