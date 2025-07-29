def solve_b0c4d837_one(S, I):
    return vconcat(vconcat(get_nth_t(hsplit(hconcat(canvas(EIGHT, astuple(ONE, subtract(decrement(height_f(f_ofcolor(I, FIVE))), height_f(f_ofcolor(I, EIGHT))))), canvas(ZERO, astuple(ONE, subtract(SIX, subtract(decrement(height_f(f_ofcolor(I, FIVE))), height_f(f_ofcolor(I, EIGHT))))))), TWO), F0), mir_rot_t(get_nth_t(hsplit(hconcat(canvas(EIGHT, astuple(ONE, subtract(decrement(height_f(f_ofcolor(I, FIVE))), height_f(f_ofcolor(I, EIGHT))))), canvas(ZERO, astuple(ONE, subtract(SIX, subtract(decrement(height_f(f_ofcolor(I, FIVE))), height_f(f_ofcolor(I, EIGHT))))))), TWO), L1), R2)), canvas(ZERO, astuple(ONE, THREE)))


def solve_b0c4d837(S, I):
    x1 = f_ofcolor(I, FIVE)
    x2 = height_f(x1)
    x3 = decrement(x2)
    x4 = f_ofcolor(I, EIGHT)
    x5 = height_f(x4)
    x6 = subtract(x3, x5)
    x7 = astuple(ONE, x6)
    x8 = canvas(EIGHT, x7)
    x9 = subtract(SIX, x6)
    x10 = astuple(ONE, x9)
    x11 = canvas(ZERO, x10)
    x12 = hconcat(x8, x11)
    x13 = hsplit(x12, TWO)
    x14 = get_nth_t(x13, F0)
    x15 = get_nth_t(x13, L1)
    x16 = mir_rot_t(x15, R2)
    x17 = vconcat(x14, x16)
    x18 = astuple(ONE, THREE)
    x19 = canvas(ZERO, x18)
    O = vconcat(x17, x19)
    return O
