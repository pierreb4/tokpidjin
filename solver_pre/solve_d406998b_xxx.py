def solve_d406998b_one(S, I):
    return mir_rot_t(fill(mir_rot_t(I, R2), THREE, sfilter_f(f_ofcolor(mir_rot_t(I, R2), FIVE), compose(even, rbind(get_nth_f, L1)))), R2)


def solve_d406998b(S, I):
    x1 = mir_rot_t(I, R2)
    x2 = f_ofcolor(x1, FIVE)
    x3 = rbind(get_nth_f, L1)
    x4 = compose(even, x3)
    x5 = sfilter_f(x2, x4)
    x6 = fill(x1, THREE, x5)
    O = mir_rot_t(x6, R2)
    return O
