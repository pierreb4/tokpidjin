def solve_68b16354_one(S, I):
    return mir_rot_t(I, identity(a_mr(S)))


def solve_68b16354(S, I, x=0):
    x1 = a_mr(S)
    if x == 1:
        return x1
    x2 = identity(x1)
    if x == 2:
        return x2
    O = mir_rot_t(I, x2)
    return O
