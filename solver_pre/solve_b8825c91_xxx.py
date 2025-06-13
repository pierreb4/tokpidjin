def solve_b8825c91_one(S, I):
    return mir_rot_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, FOUR, ZERO), mir_rot_t(replace(I, FOUR, ZERO), R1))), mir_rot_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, FOUR, ZERO), mir_rot_t(replace(I, FOUR, ZERO), R1))), R3))), R3)


def solve_b8825c91(S, I):
    x1 = rbind(get_rank, F0)
    x2 = lbind(apply, x1)
    x3 = replace(I, FOUR, ZERO)
    x4 = mir_rot_t(x3, R1)
    x5 = papply(pair, x3, x4)
    x6 = apply(x2, x5)
    x7 = mir_rot_t(x6, R3)
    x8 = papply(pair, x6, x7)
    x9 = apply(x2, x8)
    O = mir_rot_t(x9, R3)
    return O
