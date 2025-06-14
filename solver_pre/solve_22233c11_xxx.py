def solve_22233c11_one(S, I):
    return fill(I, EIGHT, mapply(fork(difference, compose(toindices, fork(shift, compose(rbind(upscale_f, TWO), rbind(mir_rot_f, R2)), chain(invert, halve, shape_f))), compose(lbind(mapply, fork(combine, hfrontier, vfrontier)), toindices)), o_g(I, R7)))


def solve_22233c11(S, I, x=0):
    x1 = rbind(upscale_f, TWO)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_f, R2)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = chain(invert, halve, shape_f)
    if x == 4:
        return x4
    x5 = fork(shift, x3, x4)
    if x == 5:
        return x5
    x6 = compose(toindices, x5)
    if x == 6:
        return x6
    x7 = fork(combine, hfrontier, vfrontier)
    if x == 7:
        return x7
    x8 = lbind(mapply, x7)
    if x == 8:
        return x8
    x9 = compose(x8, toindices)
    if x == 9:
        return x9
    x10 = fork(difference, x6, x9)
    if x == 10:
        return x10
    x11 = o_g(I, R7)
    if x == 11:
        return x11
    x12 = mapply(x10, x11)
    if x == 12:
        return x12
    O = fill(I, EIGHT, x12)
    return O
