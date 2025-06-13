def solve_73251a56_one(S, I):
    return fill(replace(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), ZERO, get_color_rank_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), F0)), index(replace(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), ZERO, get_color_rank_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), F0)), ORIGIN), shoot(ORIGIN, UNITY))


def solve_73251a56(S, I):
    x1 = rbind(get_rank, F0)
    x2 = lbind(apply, x1)
    x3 = mir_rot_t(I, R1)
    x4 = papply(pair, I, x3)
    x5 = apply(x2, x4)
    x6 = get_color_rank_t(x5, F0)
    x7 = replace(x5, ZERO, x6)
    x8 = index(x7, ORIGIN)
    x9 = shoot(ORIGIN, UNITY)
    O = fill(x7, x8, x9)
    return O
