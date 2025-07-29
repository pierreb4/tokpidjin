def solve_e26a3af2_one(S, I):
    return branch(greater(compose(size, dedupe)(apply(rbind(get_common_rank, F0), mir_rot_t(I, R4))), compose(size, dedupe)(apply(rbind(get_common_rank, F0), I))), vupscale, hupscale)(branch(greater(compose(size, dedupe)(apply(rbind(get_common_rank, F0), mir_rot_t(I, R4))), compose(size, dedupe)(apply(rbind(get_common_rank, F0), I))), repeat(apply(rbind(get_common_rank, F0), mir_rot_t(I, R4)), ONE), mir_rot_t(repeat(apply(rbind(get_common_rank, F0), I), ONE), R4)), branch(greater(compose(size, dedupe)(apply(rbind(get_common_rank, F0), mir_rot_t(I, R4))), compose(size, dedupe)(apply(rbind(get_common_rank, F0), I))), height_t, width_t)(I))


def solve_e26a3af2(S, I):
    x1 = compose(size, dedupe)
    x2 = rbind(get_common_rank, F0)
    x3 = mir_rot_t(I, R4)
    x4 = apply(x2, x3)
    x5 = x1(x4)
    x6 = apply(x2, I)
    x7 = x1(x6)
    x8 = greater(x5, x7)
    x9 = branch(x8, vupscale, hupscale)
    x10 = repeat(x4, ONE)
    x11 = repeat(x6, ONE)
    x12 = mir_rot_t(x11, R4)
    x13 = branch(x8, x10, x12)
    x14 = branch(x8, height_t, width_t)
    x15 = x14(I)
    O = x9(x13, x15)
    return O
