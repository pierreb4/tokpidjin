def solve_1bfc4729_one(S, I):
    return vconcat(fill(tophalf(I), get_color_rank_t(tophalf(I), L1), combine(hfrontier(TWO_BY_ZERO), box(asindices(I)))), replace(mir_rot_t(fill(tophalf(I), get_color_rank_t(tophalf(I), L1), combine(hfrontier(TWO_BY_ZERO), box(asindices(I)))), R0), get_color_rank_t(tophalf(I), L1), get_color_rank_t(bottomhalf(I), L1)))


def solve_1bfc4729(S, I, x=0):
    x1 = tophalf(I)
    if x == 1:
        return x1
    x2 = get_color_rank_t(x1, L1)
    if x == 2:
        return x2
    x3 = hfrontier(TWO_BY_ZERO)
    if x == 3:
        return x3
    x4 = asindices(I)
    if x == 4:
        return x4
    x5 = box(x4)
    if x == 5:
        return x5
    x6 = combine(x3, x5)
    if x == 6:
        return x6
    x7 = fill(x1, x2, x6)
    if x == 7:
        return x7
    x8 = mir_rot_t(x7, R0)
    if x == 8:
        return x8
    x9 = bottomhalf(I)
    if x == 9:
        return x9
    x10 = get_color_rank_t(x9, L1)
    if x == 10:
        return x10
    x11 = replace(x8, x2, x10)
    if x == 11:
        return x11
    O = vconcat(x7, x11)
    return O
