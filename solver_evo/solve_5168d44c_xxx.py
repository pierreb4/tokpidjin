def solve_5168d44c_one(S, I):
    return move(I, recolor_i(RED, f_ofcolor(I, RED)), branch(equality(height_f(f_ofcolor(I, GREEN)), BLUE), ZERO_BY_TWO, TWO_BY_ZERO))


def solve_5168d44c(S, I, x=0):
    x1 = f_ofcolor(I, RED)
    if x == 1:
        return x1
    x2 = recolor_i(RED, x1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, GREEN)
    if x == 3:
        return x3
    x4 = height_f(x3)
    if x == 4:
        return x4
    x5 = equality(x4, BLUE)
    if x == 5:
        return x5
    x6 = branch(x5, ZERO_BY_TWO, TWO_BY_ZERO)
    if x == 6:
        return x6
    O = move(I, x2, x6)
    return O
