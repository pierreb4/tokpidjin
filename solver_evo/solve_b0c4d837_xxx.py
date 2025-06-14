def solve_b0c4d837_one(S, I):
    return vconcat(vconcat(get_nth_t(hsplit(hconcat(canvas(CYAN, astuple(ONE, subtract(decrement(height_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), height_f(f_ofcolor(I, CYAN))))), canvas(BLACK, astuple(ONE, subtract(SIX, subtract(decrement(height_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), height_f(f_ofcolor(I, CYAN))))))), TWO), F0), mir_rot_t(get_nth_t(hsplit(hconcat(canvas(CYAN, astuple(ONE, subtract(decrement(height_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), height_f(f_ofcolor(I, CYAN))))), canvas(BLACK, astuple(ONE, subtract(SIX, subtract(decrement(height_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), height_f(f_ofcolor(I, CYAN))))))), TWO), L1), R2)), canvas(BLACK, astuple(ONE, THREE)))


def solve_b0c4d837(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, x3)
    if x == 4:
        return x4
    x5 = height_f(x4)
    if x == 5:
        return x5
    x6 = decrement(x5)
    if x == 6:
        return x6
    x7 = f_ofcolor(I, CYAN)
    if x == 7:
        return x7
    x8 = height_f(x7)
    if x == 8:
        return x8
    x9 = subtract(x6, x8)
    if x == 9:
        return x9
    x10 = astuple(ONE, x9)
    if x == 10:
        return x10
    x11 = canvas(CYAN, x10)
    if x == 11:
        return x11
    x12 = subtract(SIX, x9)
    if x == 12:
        return x12
    x13 = astuple(ONE, x12)
    if x == 13:
        return x13
    x14 = canvas(BLACK, x13)
    if x == 14:
        return x14
    x15 = hconcat(x11, x14)
    if x == 15:
        return x15
    x16 = hsplit(x15, TWO)
    if x == 16:
        return x16
    x17 = get_nth_t(x16, F0)
    if x == 17:
        return x17
    x18 = get_nth_t(x16, L1)
    if x == 18:
        return x18
    x19 = mir_rot_t(x18, R2)
    if x == 19:
        return x19
    x20 = vconcat(x17, x19)
    if x == 20:
        return x20
    x21 = astuple(ONE, THREE)
    if x == 21:
        return x21
    x22 = canvas(BLACK, x21)
    if x == 22:
        return x22
    O = vconcat(x20, x22)
    return O
