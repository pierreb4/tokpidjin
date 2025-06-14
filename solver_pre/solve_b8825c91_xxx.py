def solve_b8825c91_one(S, I):
    return mir_rot_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, FOUR, ZERO), mir_rot_t(replace(I, FOUR, ZERO), R1))), mir_rot_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, FOUR, ZERO), mir_rot_t(replace(I, FOUR, ZERO), R1))), R3))), R3)


def solve_b8825c91(S, I, x=0):
    x1 = rbind(get_rank, F0)
    if x == 1:
        return x1
    x2 = lbind(apply, x1)
    if x == 2:
        return x2
    x3 = replace(I, FOUR, ZERO)
    if x == 3:
        return x3
    x4 = mir_rot_t(x3, R1)
    if x == 4:
        return x4
    x5 = papply(pair, x3, x4)
    if x == 5:
        return x5
    x6 = apply(x2, x5)
    if x == 6:
        return x6
    x7 = mir_rot_t(x6, R3)
    if x == 7:
        return x7
    x8 = papply(pair, x6, x7)
    if x == 8:
        return x8
    x9 = apply(x2, x8)
    if x == 9:
        return x9
    O = mir_rot_t(x9, R3)
    return O
