def solve_9f236235_one(S, I):
    return downscale(mir_rot_t(compress(I), R2), get_val_rank_f(o_g(I, R4), width_f, L1))


def solve_9f236235(S, I):
    x1 = compress(I)
    x2 = mir_rot_t(x1, R2)
    x3 = o_g(I, R4)
    x4 = get_val_rank_f(x3, width_f, L1)
    O = downscale(x2, x4)
    return O
