def solve_a2fd1cf0_one(S, I):
    return underfill(I, CYAN, combine_f(connect(astuple(get_rank(astuple(col_row(f_ofcolor(I, RED), R1), col_row(f_ofcolor(I, GREEN), R1)), L1), col_row(f_ofcolor(I, GREEN), R2)), astuple(get_rank(astuple(col_row(f_ofcolor(I, RED), R1), col_row(f_ofcolor(I, GREEN), R1)), F0), col_row(f_ofcolor(I, GREEN), R2))), connect(astuple(col_row(f_ofcolor(I, RED), R1), get_rank(astuple(col_row(f_ofcolor(I, RED), R2), col_row(f_ofcolor(I, GREEN), R2)), L1)), astuple(col_row(f_ofcolor(I, RED), R1), get_rank(astuple(col_row(f_ofcolor(I, RED), R2), col_row(f_ofcolor(I, GREEN), R2)), F0)))))


def solve_a2fd1cf0(S, I, x=0):
    x1 = f_ofcolor(I, RED)
    if x == 1:
        return x1
    x2 = col_row(x1, R1)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, GREEN)
    if x == 3:
        return x3
    x4 = col_row(x3, R1)
    if x == 4:
        return x4
    x5 = astuple(x2, x4)
    if x == 5:
        return x5
    x6 = get_rank(x5, L1)
    if x == 6:
        return x6
    x7 = col_row(x3, R2)
    if x == 7:
        return x7
    x8 = astuple(x6, x7)
    if x == 8:
        return x8
    x9 = get_rank(x5, F0)
    if x == 9:
        return x9
    x10 = astuple(x9, x7)
    if x == 10:
        return x10
    x11 = connect(x8, x10)
    if x == 11:
        return x11
    x12 = col_row(x1, R2)
    if x == 12:
        return x12
    x13 = astuple(x12, x7)
    if x == 13:
        return x13
    x14 = get_rank(x13, L1)
    if x == 14:
        return x14
    x15 = astuple(x2, x14)
    if x == 15:
        return x15
    x16 = get_rank(x13, F0)
    if x == 16:
        return x16
    x17 = astuple(x2, x16)
    if x == 17:
        return x17
    x18 = connect(x15, x17)
    if x == 18:
        return x18
    x19 = combine_f(x11, x18)
    if x == 19:
        return x19
    O = underfill(I, CYAN, x19)
    return O
