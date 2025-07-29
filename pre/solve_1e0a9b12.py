def solve_1e0a9b12_one(S, I):
    return mir_rot_t(apply(rbind(order, identity), mir_rot_t(I, R6)), R4)


def solve_1e0a9b12(S, I):
    x1 = rbind(order, identity)
    x2 = mir_rot_t(I, R6)
    x3 = apply(x1, x2)
    O = mir_rot_t(x3, R4)
    return O
