def solve_1bfc4729_one(S, I):
    return vconcat(fill(tophalf(I), get_color_rank_t(tophalf(I), L1), combine(hfrontier(TWO_BY_ZERO), box(asindices(I)))), replace(mir_rot_t(fill(tophalf(I), get_color_rank_t(tophalf(I), L1), combine(hfrontier(TWO_BY_ZERO), box(asindices(I)))), R0), get_color_rank_t(tophalf(I), L1), get_color_rank_t(bottomhalf(I), L1)))


def solve_1bfc4729(S, I):
    x1 = tophalf(I)
    x2 = get_color_rank_t(x1, L1)
    x3 = hfrontier(TWO_BY_ZERO)
    x4 = asindices(I)
    x5 = box(x4)
    x6 = combine(x3, x5)
    x7 = fill(x1, x2, x6)
    x8 = mir_rot_t(x7, R0)
    x9 = bottomhalf(I)
    x10 = get_color_rank_t(x9, L1)
    x11 = replace(x8, x2, x10)
    O = vconcat(x7, x11)
    return O
