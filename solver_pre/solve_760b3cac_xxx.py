def solve_760b3cac_one(S, I):
    return fill(I, EIGHT, shift(mir_rot_f(f_ofcolor(I, EIGHT), R2), tojvec(multiply(branch(equality(index(I, corner(f_ofcolor(I, FOUR), R0)), FOUR), NEG_ONE, ONE), THREE))))


def solve_760b3cac(S, I, x=0):
    x1 = f_ofcolor(I, EIGHT)
    if x == 1:
        return x1
    x2 = mir_rot_f(x1, R2)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, FOUR)
    if x == 3:
        return x3
    x4 = corner(x3, R0)
    if x == 4:
        return x4
    x5 = index(I, x4)
    if x == 5:
        return x5
    x6 = equality(x5, FOUR)
    if x == 6:
        return x6
    x7 = branch(x6, NEG_ONE, ONE)
    if x == 7:
        return x7
    x8 = multiply(x7, THREE)
    if x == 8:
        return x8
    x9 = tojvec(x8)
    if x == 9:
        return x9
    x10 = shift(x2, x9)
    if x == 10:
        return x10
    O = fill(I, EIGHT, x10)
    return O
