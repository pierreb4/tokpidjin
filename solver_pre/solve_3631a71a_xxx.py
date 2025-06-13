def solve_3631a71a_one(S, I):
    return paint(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, NINE, ZERO), mir_rot_t(replace(I, NINE, ZERO), R1))), shift(merge(o_g(mir_rot_t(crop(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, NINE, ZERO), mir_rot_t(replace(I, NINE, ZERO), R1))), TWO_BY_TWO, subtract(shape_t(I), TWO_BY_TWO)), R2), R5)), TWO_BY_TWO))


def solve_3631a71a(S, I):
    x1 = rbind(get_rank, F0)
    x2 = lbind(apply, x1)
    x3 = replace(I, NINE, ZERO)
    x4 = mir_rot_t(x3, R1)
    x5 = papply(pair, x3, x4)
    x6 = apply(x2, x5)
    x7 = shape_t(I)
    x8 = subtract(x7, TWO_BY_TWO)
    x9 = crop(x6, TWO_BY_TWO, x8)
    x10 = mir_rot_t(x9, R2)
    x11 = o_g(x10, R5)
    x12 = merge(x11)
    x13 = shift(x12, TWO_BY_TWO)
    O = paint(x6, x13)
    return O
