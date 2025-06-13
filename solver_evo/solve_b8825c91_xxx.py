def solve_b8825c91_one(S, I):
    return mir_rot_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), mir_rot_t(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), R1))), mir_rot_t(apply(lbind(apply, rbind(get_rank, F0)), papply(pair, replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), mir_rot_t(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), R1))), R3))), R3)


def solve_b8825c91(S, I):
    x1 = rbind(get_rank, F0)
    x2 = lbind(apply, x1)
    x3 = identity(p_g)
    x4 = rbind(get_nth_t, F0)
    x5 = c_iz_n(S, x3, x4)
    x6 = replace(I, x5, BLACK)
    x7 = mir_rot_t(x6, R1)
    x8 = papply(pair, x6, x7)
    x9 = apply(x2, x8)
    x10 = mir_rot_t(x9, R3)
    x11 = papply(pair, x9, x10)
    x12 = apply(x2, x11)
    O = mir_rot_t(x12, R3)
    return O
