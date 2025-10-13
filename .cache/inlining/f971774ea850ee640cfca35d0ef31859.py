def solve(S, I, C):
    return move(I, recolor_i(RED, f_ofcolor(I, RED)), branch(equality(height_f(f_ofcolor(I, GREEN)), ONE), ZERO_BY_TWO, TWO_BY_ZERO))