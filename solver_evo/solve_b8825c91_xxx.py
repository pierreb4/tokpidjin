def solve_b8825c91_one(S, I):
    return mir_rot_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), mir_rot_t(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), R1))), mir_rot_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), mir_rot_t(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), R1))), R3))), R3)


def solve_b8825c91(S, I, x=0):
    x1 = rbind(get_rank, F0)
    if x == 1:
        return x1
    x2 = lbind(apply, x1)
    if x == 2:
        return x2
    x3 = identity(p_g)
    if x == 3:
        return x3
    x4 = rbind(get_nth_t, F0)
    if x == 4:
        return x4
    x5 = c_iz_n(S, x3, x4)
    if x == 5:
        return x5
    x6 = replace(I, x5, BLACK)
    if x == 6:
        return x6
    x7 = mir_rot_t(x6, R1)
    if x == 7:
        return x7
    x8 = papply(pair, x6, x7)
    if x == 8:
        return x8
    x9 = apply(x2, x8)
    if x == 9:
        return x9
    x10 = mir_rot_t(x9, R3)
    if x == 10:
        return x10
    x11 = papply(pair, x9, x10)
    if x == 11:
        return x11
    x12 = apply(x2, x11)
    if x == 12:
        return x12
    O = mir_rot_t(x12, R3)
    return O
