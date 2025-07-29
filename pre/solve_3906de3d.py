def solve_3906de3d_one(S, I):
    return mir_rot_t(switch(apply(rbind(order, identity), switch(mir_rot_t(I, R6), ONE, TWO)), ONE, TWO), R3)


def solve_3906de3d(S, I):
    x1 = rbind(order, identity)
    x2 = mir_rot_t(I, R6)
    x3 = switch(x2, ONE, TWO)
    x4 = apply(x1, x3)
    x5 = switch(x4, ONE, TWO)
    O = mir_rot_t(x5, R3)
    return O
