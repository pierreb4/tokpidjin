def solve_855e0971_one(S, I):
    return branch(positive(size_f(sfilter_f(frontiers(I), hline_o))), identity, rbind(mir_rot_t, R1))(fill(branch(positive(size_f(sfilter_f(frontiers(I), hline_o))), identity, rbind(mir_rot_t, R1))(I), ZERO, mapply(fork(intersection, toindices, fork(shift, chain(lbind(mapply, vfrontier), rbind(f_ofcolor, ZERO), rbind(subgrid, branch(positive(size_f(sfilter_f(frontiers(I), hline_o))), identity, rbind(mir_rot_t, R1))(I))), rbind(corner, R0))), sfilter_f(partition(branch(positive(size_f(sfilter_f(frontiers(I), hline_o))), identity, rbind(mir_rot_t, R1))(I)), compose(flip, matcher(color, ZERO))))))


def solve_855e0971(S, I, x=0):
    x1 = frontiers(I)
    if x == 1:
        return x1
    x2 = sfilter_f(x1, hline_o)
    if x == 2:
        return x2
    x3 = size_f(x2)
    if x == 3:
        return x3
    x4 = positive(x3)
    if x == 4:
        return x4
    x5 = rbind(mir_rot_t, R1)
    if x == 5:
        return x5
    x6 = branch(x4, identity, x5)
    if x == 6:
        return x6
    x7 = x6(I)
    if x == 7:
        return x7
    x8 = lbind(mapply, vfrontier)
    if x == 8:
        return x8
    x9 = rbind(f_ofcolor, ZERO)
    if x == 9:
        return x9
    x10 = rbind(subgrid, x7)
    if x == 10:
        return x10
    x11 = chain(x8, x9, x10)
    if x == 11:
        return x11
    x12 = rbind(corner, R0)
    if x == 12:
        return x12
    x13 = fork(shift, x11, x12)
    if x == 13:
        return x13
    x14 = fork(intersection, toindices, x13)
    if x == 14:
        return x14
    x15 = partition(x7)
    if x == 15:
        return x15
    x16 = matcher(color, ZERO)
    if x == 16:
        return x16
    x17 = compose(flip, x16)
    if x == 17:
        return x17
    x18 = sfilter_f(x15, x17)
    if x == 18:
        return x18
    x19 = mapply(x14, x18)
    if x == 19:
        return x19
    x20 = fill(x7, ZERO, x19)
    if x == 20:
        return x20
    O = x6(x20)
    return O
