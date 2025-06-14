def solve_0a938d79_one(S, I):
    return branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(paint(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I), mapply(fork(recolor_i, color, chain(lbind(mapply, compose(vfrontier, tojvec)), rbind(rbind(interval, chain(double, decrement, width_f)(merge(fgpartition(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I))))), width_t(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I))), rbind(col_row, R2))), fgpartition(branch(portrait_t(I), rbind(mir_rot_t, R1), identity)(I)))))


def solve_0a938d79(S, I, x=0):
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
    x5 = compose(vfrontier, tojvec)
    if x == 5:
        return x5
    x6 = lbind(mapply, x5)
    if x == 6:
        return x6
    x7 = chain(double, decrement, width_f)
    if x == 7:
        return x7
    x8 = fgpartition(x4)
    if x == 8:
        return x8
    x9 = merge(x8)
    if x == 9:
        return x9
    x10 = x7(x9)
    if x == 10:
        return x10
    x11 = rbind(interval, x10)
    if x == 11:
        return x11
    x12 = width_t(x4)
    if x == 12:
        return x12
    x13 = rbind(x11, x12)
    if x == 13:
        return x13
    x14 = rbind(col_row, R2)
    if x == 14:
        return x14
    x15 = chain(x6, x13, x14)
    if x == 15:
        return x15
    x16 = fork(recolor_i, color, x15)
    if x == 16:
        return x16
    x17 = mapply(x16, x8)
    if x == 17:
        return x17
    x18 = paint(x4, x17)
    if x == 18:
        return x18
    O = x3(x18)
    return O
