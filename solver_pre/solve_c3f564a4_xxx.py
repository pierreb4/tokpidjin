def solve_c3f564a4_one(S, I):
    return paint(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), mapply(lbind(shift, toobject(difference(asindices(I), f_ofcolor(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), ZERO)), apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))))), pair(interval(invert(NINE), NINE, ONE), interval(NINE, invert(NINE), NEG_ONE))))


def solve_c3f564a4(S, I, x=0):
    x1 = rbind(get_rank, F0)
    if x == 1:
        return x1
    x2 = lbind(apply, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(I, R1)
    if x == 3:
        return x3
    x4 = papply(pair, I, x3)
    if x == 4:
        return x4
    x5 = apply(x2, x4)
    if x == 5:
        return x5
    x6 = asindices(I)
    if x == 6:
        return x6
    x7 = f_ofcolor(x5, ZERO)
    if x == 7:
        return x7
    x8 = difference(x6, x7)
    if x == 8:
        return x8
    x9 = toobject(x8, x5)
    if x == 9:
        return x9
    x10 = lbind(shift, x9)
    if x == 10:
        return x10
    x11 = invert(NINE)
    if x == 11:
        return x11
    x12 = interval(x11, NINE, ONE)
    if x == 12:
        return x12
    x13 = interval(NINE, x11, NEG_ONE)
    if x == 13:
        return x13
    x14 = pair(x12, x13)
    if x == 14:
        return x14
    x15 = mapply(x10, x14)
    if x == 15:
        return x15
    O = paint(x5, x15)
    return O
