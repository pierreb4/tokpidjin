def solve_4be741c5_one(S, I):
    return branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(apply(dedupe, crop(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I), ORIGIN, astuple(ONE, branch(portrait_t(I), height_t, width_t)(I)))))


def solve_4be741c5(S, I, x=0):
    x1 = portrait_t(I)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_t, R1)
    if x == 2:
        return x2
    x3 = branch(x1, x2, identity)
    if x == 3:
        return x3
    x4 = x3(I)
    if x == 4:
        return x4
    x5 = branch(x1, height_t, width_t)
    if x == 5:
        return x5
    x6 = x5(I)
    if x == 6:
        return x6
    x7 = astuple(ONE, x6)
    if x == 7:
        return x7
    x8 = crop(x4, ORIGIN, x7)
    if x == 8:
        return x8
    x9 = apply(dedupe, x8)
    if x == 9:
        return x9
    O = x3(x9)
    return O
