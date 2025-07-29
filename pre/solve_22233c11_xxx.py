def solve_22233c11_one(S, I):
    return fill(I, EIGHT, mapply(fork(difference, compose(toindices, fork(shift, compose(rbind(upscale_f, TWO), rbind(mir_rot_f, R2)), chain(invert, halve, shape_f))), compose(lbind(mapply, fork(combine, hfrontier, vfrontier)), toindices)), o_g(I, R7)))


def solve_22233c11(S, I):
    x1 = rbind(upscale_f, TWO)
    x2 = rbind(mir_rot_f, R2)
    x3 = compose(x1, x2)
    x4 = chain(invert, halve, shape_f)
    x5 = fork(shift, x3, x4)
    x6 = compose(toindices, x5)
    x7 = fork(combine, hfrontier, vfrontier)
    x8 = lbind(mapply, x7)
    x9 = compose(x8, toindices)
    x10 = fork(difference, x6, x9)
    x11 = o_g(I, R7)
    x12 = mapply(x10, x11)
    O = fill(I, EIGHT, x12)
    return O
