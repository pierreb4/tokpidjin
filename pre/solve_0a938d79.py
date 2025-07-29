def solve_0a938d79_one(S, I):
    return branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(paint(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I), mapply(fork(recolor_i, color, chain(lbind(mapply, compose(vfrontier, tojvec)), rbind(rbind(interval, chain(double, decrement, width_f)(merge(fgpartition(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I))))), width_t(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I))), rbind(col_row, R2))), fgpartition(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I)))))


def solve_0a938d79(S, I):
    x1 = portrait_t(I)
    x2 = rbind(mir_rot_t, R1)
    x3 = branch(x1, x2, identity)
    x4 = x3(I)
    x5 = compose(vfrontier, tojvec)
    x6 = lbind(mapply, x5)
    x7 = chain(double, decrement, width_f)
    x8 = fgpartition(x4)
    x9 = merge(x8)
    x10 = x7(x9)
    x11 = rbind(interval, x10)
    x12 = width_t(x4)
    x13 = rbind(x11, x12)
    x14 = rbind(col_row, R2)
    x15 = chain(x6, x13, x14)
    x16 = fork(recolor_i, color, x15)
    x17 = mapply(x16, x8)
    x18 = paint(x4, x17)
    O = x3(x18)
    return O
