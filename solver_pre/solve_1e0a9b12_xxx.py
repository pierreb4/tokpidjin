def solve_1e0a9b12_one(S, I):
    return mir_rot_t(apply(rbind(order, identity), mir_rot_t(I, R6)), R4)


def solve_1e0a9b12(S, I, x=0):
    x1 = rbind(order, identity)
    if x == 1:
        return x1
    x2 = mir_rot_t(I, R6)
    if x == 2:
        return x2
    x3 = apply(x1, x2)
    if x == 3:
        return x3
    O = mir_rot_t(x3, R4)
    return O
