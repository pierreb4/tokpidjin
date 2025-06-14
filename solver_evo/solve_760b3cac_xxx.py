def solve_760b3cac_one(S, I):
    return fill(I, CYAN, shift(mir_rot_f(f_ofcolor(I, CYAN), R2), tojvec(multiply(branch(equality(index(I, corner(f_ofcolor(I, YELLOW), R0)), YELLOW), NEG_ONE, BLUE), THREE))))


def solve_760b3cac(S, I, x=0):
    x1 = f_ofcolor(I, CYAN)
    if x == 1:
        return x1
    x2 = mir_rot_f(x1, R2)
    if x == 2:
        return x2
    x3 = f_ofcolor(I, YELLOW)
    if x == 3:
        return x3
    x4 = corner(x3, R0)
    if x == 4:
        return x4
    x5 = index(I, x4)
    if x == 5:
        return x5
    x6 = equality(x5, YELLOW)
    if x == 6:
        return x6
    x7 = branch(x6, NEG_ONE, BLUE)
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
    O = fill(I, CYAN, x10)
    return O
