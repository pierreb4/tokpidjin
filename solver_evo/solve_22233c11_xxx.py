def solve_22233c11_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(fork(difference, compose(toindices, fork(shift, compose(rbind(upscale_f, RED), rbind(mir_rot_f, R2)), chain(invert, halve, shape_f))), compose(lbind(mapply, fork(combine, hfrontier, vfrontier)), toindices)), o_g(I, R7)))


def solve_22233c11(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(upscale_f, RED)
    if x == 4:
        return x4
    x5 = rbind(mir_rot_f, R2)
    if x == 5:
        return x5
    x6 = compose(x4, x5)
    if x == 6:
        return x6
    x7 = chain(invert, halve, shape_f)
    if x == 7:
        return x7
    x8 = fork(shift, x6, x7)
    if x == 8:
        return x8
    x9 = compose(toindices, x8)
    if x == 9:
        return x9
    x10 = fork(combine, hfrontier, vfrontier)
    if x == 10:
        return x10
    x11 = lbind(mapply, x10)
    if x == 11:
        return x11
    x12 = compose(x11, toindices)
    if x == 12:
        return x12
    x13 = fork(difference, x9, x12)
    if x == 13:
        return x13
    x14 = o_g(I, R7)
    if x == 14:
        return x14
    x15 = mapply(x13, x14)
    if x == 15:
        return x15
    O = fill(I, x3, x15)
    return O
