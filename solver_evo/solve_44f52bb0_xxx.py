def solve_44f52bb0_one(S, I):
    return canvas(branch(equality(mir_rot_t(I, R2), I), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1))), UNITY)


def solve_44f52bb0(S, I):
    x1 = mir_rot_t(I, R2)
    x2 = equality(x1, I)
    x3 = identity(p_g)
    x4 = rbind(get_nth_t, F0)
    x5 = c_zo_n(S, x3, x4)
    x6 = rbind(get_nth_t, F1)
    x7 = c_zo_n(S, x3, x6)
    x8 = branch(x2, x5, x7)
    O = canvas(x8, UNITY)
    return O
