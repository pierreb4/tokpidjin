def solve_93b581b8_one(S, I):
    return fill(underpaint(I, shift(upscale_f(chain(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1), merge)(fgpartition(I)), THREE), astuple(NEG_TWO, NEG_TWO))), BLACK, difference(mapply(fork(combine, hfrontier, vfrontier), toindices(chain(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1), merge)(fgpartition(I)))), toindices(chain(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1), merge)(fgpartition(I)))))


def solve_93b581b8(S, I, x=0):
    x1 = rbind(mir_rot_f, R3)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_f, R1)
    if x == 2:
        return x2
    x3 = chain(x1, x2, merge)
    if x == 3:
        return x3
    x4 = fgpartition(I)
    if x == 4:
        return x4
    x5 = x3(x4)
    if x == 5:
        return x5
    x6 = upscale_f(x5, THREE)
    if x == 6:
        return x6
    x7 = astuple(NEG_TWO, NEG_TWO)
    if x == 7:
        return x7
    x8 = shift(x6, x7)
    if x == 8:
        return x8
    x9 = underpaint(I, x8)
    if x == 9:
        return x9
    x10 = fork(combine, hfrontier, vfrontier)
    if x == 10:
        return x10
    x11 = toindices(x5)
    if x == 11:
        return x11
    x12 = mapply(x10, x11)
    if x == 12:
        return x12
    x13 = difference(x12, x11)
    if x == 13:
        return x13
    O = fill(x9, BLACK, x13)
    return O
