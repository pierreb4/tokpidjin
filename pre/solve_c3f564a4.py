def solve_c3f564a4_one(S, I):
    return paint(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), mapply(lbind(shift, toobject(difference(asindices(I), f_ofcolor(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), ZERO)), apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))))), pair(interval(invert(NINE), NINE, ONE), interval(NINE, invert(NINE), NEG_ONE))))


def solve_c3f564a4(S, I):
    x1 = rbind(get_rank, F0)
    x2 = lbind(apply, x1)
    x3 = mir_rot_t(I, R1)
    x4 = papply(pair, I, x3)
    x5 = apply(x2, x4)
    x6 = asindices(I)
    x7 = f_ofcolor(x5, ZERO)
    x8 = difference(x6, x7)
    x9 = toobject(x8, x5)
    x10 = lbind(shift, x9)
    x11 = invert(NINE)
    x12 = interval(x11, NINE, ONE)
    x13 = interval(NINE, x11, NEG_ONE)
    x14 = pair(x12, x13)
    x15 = mapply(x10, x14)
    O = paint(x5, x15)
    return O
