def solve_22233c11_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(fork(difference, compose(toindices, fork(shift, compose(rbind(upscale_f, RED), rbind(mir_rot_f, R2)), chain(invert, halve, shape_f))), compose(lbind(mapply, fork(combine, hfrontier, vfrontier)), toindices)), o_g(I, R7)))


def solve_22233c11(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = rbind(upscale_f, RED)
    x5 = rbind(mir_rot_f, R2)
    x6 = compose(x4, x5)
    x7 = chain(invert, halve, shape_f)
    x8 = fork(shift, x6, x7)
    x9 = compose(toindices, x8)
    x10 = fork(combine, hfrontier, vfrontier)
    x11 = lbind(mapply, x10)
    x12 = compose(x11, toindices)
    x13 = fork(difference, x9, x12)
    x14 = o_g(I, R7)
    x15 = mapply(x13, x14)
    O = fill(I, x3, x15)
    return O
