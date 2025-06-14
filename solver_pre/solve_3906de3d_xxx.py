def solve_3906de3d_one(S, I):
    return mir_rot_t(switch(apply(rbind(order, identity), switch(mir_rot_t(I, R6), ONE, TWO)), ONE, TWO), R3)


def solve_3906de3d(S, I, x=0):
    x1 = rbind(order, identity)
    if x == 1:
        return x1
    x2 = mir_rot_t(I, R6)
    if x == 2:
        return x2
    x3 = switch(x2, ONE, TWO)
    if x == 3:
        return x3
    x4 = apply(x1, x3)
    if x == 4:
        return x4
    x5 = switch(x4, ONE, TWO)
    if x == 5:
        return x5
    O = mir_rot_t(x5, R3)
    return O
