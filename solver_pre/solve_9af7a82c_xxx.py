def solve_9af7a82c_one(S, I):
    return mir_rot_t(merge_t(apply(compose(rbind(mir_rot_t, R3), fork(vconcat, fork(canvas, color, compose(rbind(astuple, ONE), size)), compose(lbind(canvas, ZERO), chain(rbind(astuple, ONE), lbind(subtract, get_val_rank_f(o_g(I, R4), size, F0)), size)))), order(o_g(I, R4), size))), R3)


def solve_9af7a82c(S, I, x=0):
    x1 = rbind(mir_rot_t, R3)
    if x == 1:
        return x1
    x2 = rbind(astuple, ONE)
    if x == 2:
        return x2
    x3 = compose(x2, size)
    if x == 3:
        return x3
    x4 = fork(canvas, color, x3)
    if x == 4:
        return x4
    x5 = lbind(canvas, ZERO)
    if x == 5:
        return x5
    x6 = o_g(I, R4)
    if x == 6:
        return x6
    x7 = get_val_rank_f(x6, size, F0)
    if x == 7:
        return x7
    x8 = lbind(subtract, x7)
    if x == 8:
        return x8
    x9 = chain(x2, x8, size)
    if x == 9:
        return x9
    x10 = compose(x5, x9)
    if x == 10:
        return x10
    x11 = fork(vconcat, x4, x10)
    if x == 11:
        return x11
    x12 = compose(x1, x11)
    if x == 12:
        return x12
    x13 = order(x6, size)
    if x == 13:
        return x13
    x14 = apply(x12, x13)
    if x == 14:
        return x14
    x15 = merge_t(x14)
    if x == 15:
        return x15
    O = mir_rot_t(x15, R3)
    return O
