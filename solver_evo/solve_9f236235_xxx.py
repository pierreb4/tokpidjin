def solve_9f236235_one(S, I):
    return downscale(mir_rot_t(compress(I), R2), get_val_rank_f(colorfilter(o_g(I, R4), BLACK), width_f, L1))


def solve_9f236235(S, I, x=0):
    x1 = compress(I)
    if x == 1:
        return x1
    x2 = mir_rot_t(x1, R2)
    if x == 2:
        return x2
    x3 = o_g(I, R4)
    if x == 3:
        return x3
    x4 = colorfilter(x3, BLACK)
    if x == 4:
        return x4
    x5 = get_val_rank_f(x4, width_f, L1)
    if x == 5:
        return x5
    O = downscale(x2, x5)
    return O
