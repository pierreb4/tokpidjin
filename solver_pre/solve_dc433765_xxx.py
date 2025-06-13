def solve_dc433765_one(S, I):
    return move(I, recolor_i(THREE, f_ofcolor(I, THREE)), sign(subtract(get_nth_f(f_ofcolor(I, FOUR), F0), get_nth_f(f_ofcolor(I, THREE), F0))))


def solve_dc433765(S, I):
    x1 = f_ofcolor(I, THREE)
    x2 = recolor_i(THREE, x1)
    x3 = f_ofcolor(I, FOUR)
    x4 = get_nth_f(x3, F0)
    x5 = get_nth_f(x1, F0)
    x6 = subtract(x4, x5)
    x7 = sign(x6)
    O = move(I, x2, x7)
    return O
