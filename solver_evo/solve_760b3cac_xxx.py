def solve_760b3cac_one(S, I):
    return fill(I, CYAN, shift(mir_rot_f(f_ofcolor(I, CYAN), R2), tojvec(multiply(branch(equality(index(I, corner(f_ofcolor(I, YELLOW), R0)), YELLOW), NEG_ONE, BLUE), THREE))))


def solve_760b3cac(S, I):
    x1 = f_ofcolor(I, CYAN)
    x2 = mir_rot_f(x1, R2)
    x3 = f_ofcolor(I, YELLOW)
    x4 = corner(x3, R0)
    x5 = index(I, x4)
    x6 = equality(x5, YELLOW)
    x7 = branch(x6, NEG_ONE, BLUE)
    x8 = multiply(x7, THREE)
    x9 = tojvec(x8)
    x10 = shift(x2, x9)
    O = fill(I, CYAN, x10)
    return O
