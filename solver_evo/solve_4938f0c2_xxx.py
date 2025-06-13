def solve_4938f0c2_one(S, I):
    return branch(greater(size_f(o_g(I, R7)), FOUR), I, fill(fill(I, RED, shift(mir_rot_f(f_ofcolor(I, RED), R2), add(tojvec(width_f(f_ofcolor(I, RED))), ZERO_BY_TWO))), RED, shift(mir_rot_f(f_ofcolor(fill(I, RED, shift(mir_rot_f(f_ofcolor(I, RED), R2), add(tojvec(width_f(f_ofcolor(I, RED))), ZERO_BY_TWO))), RED), R0), add(toivec(height_f(f_ofcolor(I, RED))), TWO_BY_ZERO))))


def solve_4938f0c2(S, I):
    x1 = o_g(I, R7)
    x2 = size_f(x1)
    x3 = greater(x2, FOUR)
    x4 = f_ofcolor(I, RED)
    x5 = mir_rot_f(x4, R2)
    x6 = width_f(x4)
    x7 = tojvec(x6)
    x8 = add(x7, ZERO_BY_TWO)
    x9 = shift(x5, x8)
    x10 = fill(I, RED, x9)
    x11 = f_ofcolor(x10, RED)
    x12 = mir_rot_f(x11, R0)
    x13 = height_f(x4)
    x14 = toivec(x13)
    x15 = add(x14, TWO_BY_ZERO)
    x16 = shift(x12, x15)
    x17 = fill(x10, RED, x16)
    O = branch(x3, I, x17)
    return O
