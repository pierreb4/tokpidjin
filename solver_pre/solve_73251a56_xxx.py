def solve_73251a56_one(S, I):
    return fill(replace(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), ZERO, get_color_rank_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), F0)), index(replace(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), ZERO, get_color_rank_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, I, mir_rot_t(I, R1))), F0)), ORIGIN), shoot(ORIGIN, UNITY))


def solve_73251a56(S, I, x=0):
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
    x6 = get_color_rank_t(x5, F0)
    if x == 6:
        return x6
    x7 = replace(x5, ZERO, x6)
    if x == 7:
        return x7
    x8 = index(x7, ORIGIN)
    if x == 8:
        return x8
    x9 = shoot(ORIGIN, UNITY)
    if x == 9:
        return x9
    O = fill(x7, x8, x9)
    return O
