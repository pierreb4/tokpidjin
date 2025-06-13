def solve_b0c4d837_one(S, I):
    return vconcat(vconcat(get_nth_t(hsplit(hconcat(canvas(CYAN, astuple(ONE, subtract(decrement(height_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), height_f(f_ofcolor(I, CYAN))))), canvas(BLACK, astuple(ONE, subtract(SIX, subtract(decrement(height_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), height_f(f_ofcolor(I, CYAN))))))), TWO), F0), mir_rot_t(get_nth_t(hsplit(hconcat(canvas(CYAN, astuple(ONE, subtract(decrement(height_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), height_f(f_ofcolor(I, CYAN))))), canvas(BLACK, astuple(ONE, subtract(SIX, subtract(decrement(height_f(f_ofcolor(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0))))), height_f(f_ofcolor(I, CYAN))))))), TWO), L1), R2)), canvas(BLACK, astuple(ONE, THREE)))


def solve_b0c4d837(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = f_ofcolor(I, x3)
    x5 = height_f(x4)
    x6 = decrement(x5)
    x7 = f_ofcolor(I, CYAN)
    x8 = height_f(x7)
    x9 = subtract(x6, x8)
    x10 = astuple(ONE, x9)
    x11 = canvas(CYAN, x10)
    x12 = subtract(SIX, x9)
    x13 = astuple(ONE, x12)
    x14 = canvas(BLACK, x13)
    x15 = hconcat(x11, x14)
    x16 = hsplit(x15, TWO)
    x17 = get_nth_t(x16, F0)
    x18 = get_nth_t(x16, L1)
    x19 = mir_rot_t(x18, R2)
    x20 = vconcat(x17, x19)
    x21 = astuple(ONE, THREE)
    x22 = canvas(BLACK, x21)
    O = vconcat(x20, x22)
    return O
