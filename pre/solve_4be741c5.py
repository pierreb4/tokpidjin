def solve_4be741c5_one(S, I):
    return branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(apply(dedupe, crop(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I), ORIGIN, astuple(ONE, branch(portrait_t(I), height_t, width_t)(I)))))


def solve_4be741c5(S, I):
    x1 = portrait_t(I)
    x2 = rbind(mir_rot_t, R1)
    x3 = branch(x1, x2, identity)
    x4 = x3(I)
    x5 = branch(x1, height_t, width_t)
    x6 = x5(I)
    x7 = astuple(ONE, x6)
    x8 = crop(x4, ORIGIN, x7)
    x9 = apply(dedupe, x8)
    O = x3(x9)
    return O
