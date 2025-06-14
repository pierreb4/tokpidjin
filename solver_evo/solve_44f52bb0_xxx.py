def solve_44f52bb0_one(S, I):
    return canvas(branch(equality(mir_rot_t(I, R2), I), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1))), UNITY)


def solve_44f52bb0(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = equality(x1, I)
    if x == 2:
        return x2
    x3 = identity(p_g)
    if x == 3:
        return x3
    x4 = rbind(get_nth_t, F0)
    if x == 4:
        return x4
    x5 = c_zo_n(S, x3, x4)
    if x == 5:
        return x5
    x6 = rbind(get_nth_t, F1)
    if x == 6:
        return x6
    x7 = c_zo_n(S, x3, x6)
    if x == 7:
        return x7
    x8 = branch(x2, x5, x7)
    if x == 8:
        return x8
    O = canvas(x8, UNITY)
    return O
