def solve_855e0971_one(S, I):
    return branch(positive(size_f(sfilter_f(frontiers(I), hline_o))), identity, rbind(mir_rot_t, R1))(fill(branch(positive(size_f(sfilter_f(frontiers(I), hline_o))), identity, rbind(mir_rot_t, R1))(I), ZERO, mapply(fork(intersection, toindices, fork(shift, chain(lbind(mapply, vfrontier), rbind(f_ofcolor, ZERO), rbind(subgrid, branch(positive(size_f(sfilter_f(frontiers(I), hline_o))), identity, rbind(mir_rot_t, R1))(I))), rbind(corner, R0))), sfilter_f(partition(branch(positive(size_f(sfilter_f(frontiers(I), hline_o))), identity, rbind(mir_rot_t, R1))(I)), compose(flip, matcher(color, ZERO))))))


def solve_855e0971(S, I):
    x1 = frontiers(I)
    x2 = sfilter_f(x1, hline_o)
    x3 = size_f(x2)
    x4 = positive(x3)
    x5 = rbind(mir_rot_t, R1)
    x6 = branch(x4, identity, x5)
    x7 = x6(I)
    x8 = lbind(mapply, vfrontier)
    x9 = rbind(f_ofcolor, ZERO)
    x10 = rbind(subgrid, x7)
    x11 = chain(x8, x9, x10)
    x12 = rbind(corner, R0)
    x13 = fork(shift, x11, x12)
    x14 = fork(intersection, toindices, x13)
    x15 = partition(x7)
    x16 = matcher(color, ZERO)
    x17 = compose(flip, x16)
    x18 = sfilter_f(x15, x17)
    x19 = mapply(x14, x18)
    x20 = fill(x7, ZERO, x19)
    O = x6(x20)
    return O
