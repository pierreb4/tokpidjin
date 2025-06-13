def solve_5168d44c_one(S, I):
    return move(I, recolor_i(TWO, f_ofcolor(I, TWO)), branch(equality(height_f(f_ofcolor(I, THREE)), ONE), ZERO_BY_TWO, TWO_BY_ZERO))


def solve_5168d44c(S, I):
    x1 = f_ofcolor(I, TWO)
    x2 = recolor_i(TWO, x1)
    x3 = f_ofcolor(I, THREE)
    x4 = height_f(x3)
    x5 = equality(x4, ONE)
    x6 = branch(x5, ZERO_BY_TWO, TWO_BY_ZERO)
    O = move(I, x2, x6)
    return O
