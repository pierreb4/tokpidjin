def solve_d406998b_one(S, I):
    return mir_rot_t(fill(mir_rot_t(I, R2), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), sfilter_f(f_ofcolor(mir_rot_t(I, R2), GRAY), compose(even, rbind(get_nth_f, L1)))), R2)


def solve_d406998b(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = identity(p_g)
    if x == 2:
        return x2
    x3 = rbind(get_nth_t, F0)
    if x == 3:
        return x3
    x4 = c_zo_n(S, x2, x3)
    if x == 4:
        return x4
    x5 = f_ofcolor(x1, GRAY)
    if x == 5:
        return x5
    x6 = rbind(get_nth_f, L1)
    if x == 6:
        return x6
    x7 = compose(even, x6)
    if x == 7:
        return x7
    x8 = sfilter_f(x5, x7)
    if x == 8:
        return x8
    x9 = fill(x1, x4, x8)
    if x == 9:
        return x9
    O = mir_rot_t(x9, R2)
    return O
