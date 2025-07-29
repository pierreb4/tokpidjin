def solve_9af7a82c_one(S, I):
    return mir_rot_t(merge_t(apply(compose(rbind(mir_rot_t, R3), fork(vconcat, fork(canvas, color, compose(rbind(astuple, ONE), size)), compose(lbind(canvas, ZERO), chain(rbind(astuple, ONE), lbind(subtract, get_val_rank_f(o_g(I, R4), size, F0)), size)))), order(o_g(I, R4), size))), R3)


def solve_9af7a82c(S, I):
    x1 = rbind(mir_rot_t, R3)
    x2 = rbind(astuple, ONE)
    x3 = compose(x2, size)
    x4 = fork(canvas, color, x3)
    x5 = lbind(canvas, ZERO)
    x6 = o_g(I, R4)
    x7 = get_val_rank_f(x6, size, F0)
    x8 = lbind(subtract, x7)
    x9 = chain(x2, x8, size)
    x10 = compose(x5, x9)
    x11 = fork(vconcat, x4, x10)
    x12 = compose(x1, x11)
    x13 = order(x6, size)
    x14 = apply(x12, x13)
    x15 = merge_t(x14)
    O = mir_rot_t(x15, R3)
    return O
