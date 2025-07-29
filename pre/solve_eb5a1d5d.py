def solve_eb5a1d5d_one(S, I):
    return fork(vconcat, identity, compose(rbind(mir_rot_t, R0), fork(remove, rbind(get_nth_f, L1), identity)))(mir_rot_t(fork(vconcat, identity, compose(rbind(mir_rot_t, R0), fork(remove, rbind(get_nth_f, L1), identity)))(compose(rbind(mir_rot_t, R1), dedupe)(compose(rbind(mir_rot_t, R1), dedupe)(I))), R1))


def solve_eb5a1d5d(S, I):
    x1 = rbind(mir_rot_t, R0)
    x2 = rbind(get_nth_f, L1)
    x3 = fork(remove, x2, identity)
    x4 = compose(x1, x3)
    x5 = fork(vconcat, identity, x4)
    x6 = rbind(mir_rot_t, R1)
    x7 = compose(x6, dedupe)
    x8 = x7(I)
    x9 = x7(x8)
    x10 = x5(x9)
    x11 = mir_rot_t(x10, R1)
    O = x5(x11)
    return O
