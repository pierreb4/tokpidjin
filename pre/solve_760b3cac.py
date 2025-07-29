def solve_760b3cac_one(S, I):
    return fill(I, EIGHT, shift(mir_rot_f(f_ofcolor(I, EIGHT), R2), tojvec(multiply(branch(equality(index(I, corner(f_ofcolor(I, FOUR), R0)), FOUR), NEG_ONE, ONE), THREE))))


def solve_760b3cac(S, I):
    x1 = f_ofcolor(I, EIGHT)
    x2 = mir_rot_f(x1, R2)
    x3 = f_ofcolor(I, FOUR)
    x4 = corner(x3, R0)
    x5 = index(I, x4)
    x6 = equality(x5, FOUR)
    x7 = branch(x6, NEG_ONE, ONE)
    x8 = multiply(x7, THREE)
    x9 = tojvec(x8)
    x10 = shift(x2, x9)
    O = fill(I, EIGHT, x10)
    return O
