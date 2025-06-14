def solve_d406998b_one(S, I):
    return mir_rot_t(fill(mir_rot_t(I, R2), THREE, sfilter_f(f_ofcolor(mir_rot_t(I, R2), FIVE), compose(even, rbind(get_nth_f, L1)))), R2)


def solve_d406998b(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = f_ofcolor(x1, FIVE)
    if x == 2:
        return x2
    x3 = rbind(get_nth_f, L1)
    if x == 3:
        return x3
    x4 = compose(even, x3)
    if x == 4:
        return x4
    x5 = sfilter_f(x2, x4)
    if x == 5:
        return x5
    x6 = fill(x1, THREE, x5)
    if x == 6:
        return x6
    O = mir_rot_t(x6, R2)
    return O
