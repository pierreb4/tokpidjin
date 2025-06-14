def solve_eb5a1d5d_one(S, I):
    return fork(vconcat, identity, compose(rbind(mir_rot_t, R0), fork(remove, rbind(get_nth_f, L1), identity)))(mir_rot_t(fork(vconcat, identity, compose(rbind(mir_rot_t, R0), fork(remove, rbind(get_nth_f, L1), identity)))(compose(rbind(mir_rot_t, R1), dedupe)(compose(rbind(mir_rot_t, R1), dedupe)(I))), R1))


def solve_eb5a1d5d(S, I, x=0):
    x1 = rbind(mir_rot_t, R0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = fork(remove, x2, identity)
    if x == 3:
        return x3
    x4 = compose(x1, x3)
    if x == 4:
        return x4
    x5 = fork(vconcat, identity, x4)
    if x == 5:
        return x5
    x6 = rbind(mir_rot_t, R1)
    if x == 6:
        return x6
    x7 = compose(x6, dedupe)
    if x == 7:
        return x7
    x8 = x7(I)
    if x == 8:
        return x8
    x9 = x7(x8)
    if x == 9:
        return x9
    x10 = x5(x9)
    if x == 10:
        return x10
    x11 = mir_rot_t(x10, R1)
    if x == 11:
        return x11
    O = x5(x11)
    return O
