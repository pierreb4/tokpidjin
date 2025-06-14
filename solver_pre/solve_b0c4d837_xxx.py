def solve_b0c4d837_one(S, I):
    return vconcat(vconcat(get_nth_t(hsplit(hconcat(canvas(EIGHT, astuple(ONE, subtract(decrement(height_f(f_ofcolor(I, FIVE))), height_f(f_ofcolor(I, EIGHT))))), canvas(ZERO, astuple(ONE, subtract(SIX, subtract(decrement(height_f(f_ofcolor(I, FIVE))), height_f(f_ofcolor(I, EIGHT))))))), TWO), F0), mir_rot_t(get_nth_t(hsplit(hconcat(canvas(EIGHT, astuple(ONE, subtract(decrement(height_f(f_ofcolor(I, FIVE))), height_f(f_ofcolor(I, EIGHT))))), canvas(ZERO, astuple(ONE, subtract(SIX, subtract(decrement(height_f(f_ofcolor(I, FIVE))), height_f(f_ofcolor(I, EIGHT))))))), TWO), L1), R2)), canvas(ZERO, astuple(ONE, THREE)))


def solve_b0c4d837(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = height_f(x1)
    if x == 2:
        return x2
    x3 = decrement(x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = height_f(x4)
    if x == 5:
        return x5
    x6 = subtract(x3, x5)
    if x == 6:
        return x6
    x7 = astuple(ONE, x6)
    if x == 7:
        return x7
    x8 = canvas(EIGHT, x7)
    if x == 8:
        return x8
    x9 = subtract(SIX, x6)
    if x == 9:
        return x9
    x10 = astuple(ONE, x9)
    if x == 10:
        return x10
    x11 = canvas(ZERO, x10)
    if x == 11:
        return x11
    x12 = hconcat(x8, x11)
    if x == 12:
        return x12
    x13 = hsplit(x12, TWO)
    if x == 13:
        return x13
    x14 = get_nth_t(x13, F0)
    if x == 14:
        return x14
    x15 = get_nth_t(x13, L1)
    if x == 15:
        return x15
    x16 = mir_rot_t(x15, R2)
    if x == 16:
        return x16
    x17 = vconcat(x14, x16)
    if x == 17:
        return x17
    x18 = astuple(ONE, THREE)
    if x == 18:
        return x18
    x19 = canvas(ZERO, x18)
    if x == 19:
        return x19
    O = vconcat(x17, x19)
    return O
