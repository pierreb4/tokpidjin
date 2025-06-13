def solve_a2fd1cf0_one(S, I):
    return underfill(I, CYAN, combine_f(connect(astuple(get_rank(astuple(col_row(f_ofcolor(I, RED), R1), col_row(f_ofcolor(I, GREEN), R1)), L1), col_row(f_ofcolor(I, GREEN), R2)), astuple(get_rank(astuple(col_row(f_ofcolor(I, RED), R1), col_row(f_ofcolor(I, GREEN), R1)), F0), col_row(f_ofcolor(I, GREEN), R2))), connect(astuple(col_row(f_ofcolor(I, RED), R1), get_rank(astuple(col_row(f_ofcolor(I, RED), R2), col_row(f_ofcolor(I, GREEN), R2)), L1)), astuple(col_row(f_ofcolor(I, RED), R1), get_rank(astuple(col_row(f_ofcolor(I, RED), R2), col_row(f_ofcolor(I, GREEN), R2)), F0)))))


def solve_a2fd1cf0(S, I):
    x1 = f_ofcolor(I, RED)
    x2 = col_row(x1, R1)
    x3 = f_ofcolor(I, GREEN)
    x4 = col_row(x3, R1)
    x5 = astuple(x2, x4)
    x6 = get_rank(x5, L1)
    x7 = col_row(x3, R2)
    x8 = astuple(x6, x7)
    x9 = get_rank(x5, F0)
    x10 = astuple(x9, x7)
    x11 = connect(x8, x10)
    x12 = col_row(x1, R2)
    x13 = astuple(x12, x7)
    x14 = get_rank(x13, L1)
    x15 = astuple(x2, x14)
    x16 = get_rank(x13, F0)
    x17 = astuple(x2, x16)
    x18 = connect(x15, x17)
    x19 = combine_f(x11, x18)
    O = underfill(I, CYAN, x19)
    return O
