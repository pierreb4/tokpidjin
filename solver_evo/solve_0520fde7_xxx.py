def solve_0520fde7_one(S, I):
    return replace(cellwise(lefthalf(mir_rot_t(I, R2)), mir_rot_t(righthalf(mir_rot_t(I, R2)), R2), ZERO), c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)))


def solve_0520fde7(S, I):
    x1 = mir_rot_t(I, R2)
    x2 = lefthalf(x1)
    x3 = righthalf(x1)
    x4 = mir_rot_t(x3, R2)
    x5 = cellwise(x2, x4, ZERO)
    x6 = identity(p_g)
    x7 = rbind(get_nth_t, F0)
    x8 = c_iz_n(S, x6, x7)
    x9 = c_zo_n(S, x6, x7)
    O = replace(x5, x8, x9)
    return O
