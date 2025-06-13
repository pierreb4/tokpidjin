def solve_93b581b8_one(S, I):
    return fill(underpaint(I, shift(upscale_f(chain(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1), merge)(fgpartition(I)), THREE), astuple(NEG_TWO, NEG_TWO))), ZERO, difference(mapply(fork(combine, hfrontier, vfrontier), toindices(chain(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1), merge)(fgpartition(I)))), toindices(chain(rbind(mir_rot_f, R3), rbind(mir_rot_f, R1), merge)(fgpartition(I)))))


def solve_93b581b8(S, I):
    x1 = rbind(mir_rot_f, R3)
    x2 = rbind(mir_rot_f, R1)
    x3 = chain(x1, x2, merge)
    x4 = fgpartition(I)
    x5 = x3(x4)
    x6 = upscale_f(x5, THREE)
    x7 = astuple(NEG_TWO, NEG_TWO)
    x8 = shift(x6, x7)
    x9 = underpaint(I, x8)
    x10 = fork(combine, hfrontier, vfrontier)
    x11 = toindices(x5)
    x12 = mapply(x10, x11)
    x13 = difference(x12, x11)
    O = fill(x9, ZERO, x13)
    return O
