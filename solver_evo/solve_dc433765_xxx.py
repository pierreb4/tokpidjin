def solve_dc433765_one(S, I):
    return move(I, recolor_i(GREEN, f_ofcolor(I, GREEN)), sign(subtract(get_nth_f(f_ofcolor(I, YELLOW), F0), get_nth_f(f_ofcolor(I, GREEN), F0))))


def solve_dc433765(S, I, x=0):
    x1 = f_ofcolor(I, GREEN)
    if x == 1:
        return x1
    x2 = recolor_i(GREEN, x1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, YELLOW)
    if x == 3:
        return x3
    x4 = get_nth_f(x3, F0)
    if x == 4:
        return x4
    x5 = get_nth_f(x1, F0)
    if x == 5:
        return x5
    x6 = subtract(x4, x5)
    if x == 6:
        return x6
    x7 = sign(x6)
    if x == 7:
        return x7
    O = move(I, x2, x7)
    return O
