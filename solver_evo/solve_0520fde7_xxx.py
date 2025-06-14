def solve_0520fde7_one(S, I):
    return replace(cellwise(lefthalf(mir_rot_t(I, R2)), mir_rot_t(righthalf(mir_rot_t(I, R2)), R2), ZERO), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


def solve_0520fde7(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = lefthalf(x1)
    if x == 2:
        return x2
    x3 = righthalf(x1)
    if x == 3:
        return x3
    x4 = mir_rot_t(x3, R2)
    if x == 4:
        return x4
    x5 = cellwise(x2, x4, ZERO)
    if x == 5:
        return x5
    x6 = identity(p_g)
    if x == 6:
        return x6
    x7 = rbind(get_nth_t, F0)
    if x == 7:
        return x7
    x8 = c_iz_n(S, x6, x7)
    if x == 8:
        return x8
    x9 = c_zo_n(S, x6, x7)
    if x == 9:
        return x9
    O = replace(x5, x8, x9)
    return O
