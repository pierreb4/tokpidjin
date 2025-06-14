def solve_4938f0c2_one(S, I):
    return branch(greater(size_f(o_g(I, R7)), FOUR), I, fill(fill(I, RED, shift(mir_rot_f(f_ofcolor(I, RED), R2), add(tojvec(width_f(f_ofcolor(I, RED))), ZERO_BY_TWO))), RED, shift(mir_rot_f(f_ofcolor(fill(I, RED, shift(mir_rot_f(f_ofcolor(I, RED), R2), add(tojvec(width_f(f_ofcolor(I, RED))), ZERO_BY_TWO))), RED), R0), add(toivec(height_f(f_ofcolor(I, RED))), TWO_BY_ZERO))))


def solve_4938f0c2(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = size_f(x1)
    if x == 2:
        return x2
    x3 = greater(x2, FOUR)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, RED)
    if x == 4:
        return x4
    x5 = mir_rot_f(x4, R2)
    if x == 5:
        return x5
    x6 = width_f(x4)
    if x == 6:
        return x6
    x7 = tojvec(x6)
    if x == 7:
        return x7
    x8 = add(x7, ZERO_BY_TWO)
    if x == 8:
        return x8
    x9 = shift(x5, x8)
    if x == 9:
        return x9
    x10 = fill(I, RED, x9)
    if x == 10:
        return x10
    x11 = f_ofcolor(x10, RED)
    if x == 11:
        return x11
    x12 = mir_rot_f(x11, R0)
    if x == 12:
        return x12
    x13 = height_f(x4)
    if x == 13:
        return x13
    x14 = toivec(x13)
    if x == 14:
        return x14
    x15 = add(x14, TWO_BY_ZERO)
    if x == 15:
        return x15
    x16 = shift(x12, x15)
    if x == 16:
        return x16
    x17 = fill(x10, RED, x16)
    if x == 17:
        return x17
    O = branch(x3, I, x17)
    return O
