def solve_3631a71a_one(S, I):
    return paint(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, NINE, ZERO), mir_rot_t(replace(I, NINE, ZERO), R1))), shift(merge(o_g(mir_rot_t(crop(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, NINE, ZERO), mir_rot_t(replace(I, NINE, ZERO), R1))), TWO_BY_TWO, subtract(shape_t(I), TWO_BY_TWO)), R2), R5)), TWO_BY_TWO))


def solve_3631a71a(S, I, x=0):
    x1 = rbind(get_rank, F0)
    if x == 1:
        return x1
    x2 = lbind(apply, x1)
    if x == 2:
        return x2
    x3 = replace(I, NINE, ZERO)
    if x == 3:
        return x3
    x4 = mir_rot_t(x3, R1)
    if x == 4:
        return x4
    x5 = papply(pair, x3, x4)
    if x == 5:
        return x5
    x6 = apply(x2, x5)
    if x == 6:
        return x6
    x7 = shape_t(I)
    if x == 7:
        return x7
    x8 = subtract(x7, TWO_BY_TWO)
    if x == 8:
        return x8
    x9 = crop(x6, TWO_BY_TWO, x8)
    if x == 9:
        return x9
    x10 = mir_rot_t(x9, R2)
    if x == 10:
        return x10
    x11 = o_g(x10, R5)
    if x == 11:
        return x11
    x12 = merge(x11)
    if x == 12:
        return x12
    x13 = shift(x12, TWO_BY_TWO)
    if x == 13:
        return x13
    O = paint(x6, x13)
    return O
