def solve_d406998b_one(S, I):
    return mir_rot_t(fill(mir_rot_t(I, R2), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), sfilter_f(f_ofcolor(mir_rot_t(I, R2), GRAY), compose(even, rbind(get_nth_f, L1)))), R2)


def solve_d406998b(S, I):
    x1 = mir_rot_t(I, R2)
    x2 = identity(p_g)
    x3 = rbind(get_nth_t, F0)
    x4 = c_zo_n(S, x2, x3)
    x5 = f_ofcolor(x1, GRAY)
    x6 = rbind(get_nth_f, L1)
    x7 = compose(even, x6)
    x8 = sfilter_f(x5, x7)
    x9 = fill(x1, x4, x8)
    O = mir_rot_t(x9, R2)
    return O
