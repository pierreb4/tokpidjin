def solve_e26a3af2_one(S, I):
    return branch(greater(compose(size, dedupe)(apply(rbind(get_common_rank, F0), mir_rot_t(I, R4))), compose(size, dedupe)(apply(rbind(get_common_rank, F0), I))), vupscale, hupscale)(branch(greater(compose(size, dedupe)(apply(rbind(get_common_rank, F0), mir_rot_t(I, R4))), compose(size, dedupe)(apply(rbind(get_common_rank, F0), I))), repeat(apply(rbind(get_common_rank, F0), mir_rot_t(I, R4)), ONE), mir_rot_t(repeat(apply(rbind(get_common_rank, F0), I), ONE), R4)), branch(greater(compose(size, dedupe)(apply(rbind(get_common_rank, F0), mir_rot_t(I, R4))), compose(size, dedupe)(apply(rbind(get_common_rank, F0), I))), height_t, width_t)(I))


def solve_e26a3af2(S, I, x=0):
    x1 = compose(size, dedupe)
    if x == 1:
        return x1
    x2 = rbind(get_common_rank, F0)
    if x == 2:
        return x2
    x3 = mir_rot_t(I, R4)
    if x == 3:
        return x3
    x4 = apply(x2, x3)
    if x == 4:
        return x4
    x5 = x1(x4)
    if x == 5:
        return x5
    x6 = apply(x2, I)
    if x == 6:
        return x6
    x7 = x1(x6)
    if x == 7:
        return x7
    x8 = greater(x5, x7)
    if x == 8:
        return x8
    x9 = branch(x8, vupscale, hupscale)
    if x == 9:
        return x9
    x10 = repeat(x4, ONE)
    if x == 10:
        return x10
    x11 = repeat(x6, ONE)
    if x == 11:
        return x11
    x12 = mir_rot_t(x11, R4)
    if x == 12:
        return x12
    x13 = branch(x8, x10, x12)
    if x == 13:
        return x13
    x14 = branch(x8, height_t, width_t)
    if x == 14:
        return x14
    x15 = x14(I)
    if x == 15:
        return x15
    O = x9(x13, x15)
    return O
