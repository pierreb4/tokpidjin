def solve_ce602527_one(S, I):
    return mir_rot_t(subgrid(get_arg_rank_t(remove_f(get_nth_t(order(fgpartition(mir_rot_t(I, R2)), size), L1), order(fgpartition(mir_rot_t(I, R2)), size)), chain(size, rbind(intersection, compose(toindices, normalize)(get_nth_t(order(fgpartition(mir_rot_t(I, R2)), size), L1))), chain(toindices, rbind(upscale_f, TWO), normalize)), F0), mir_rot_t(I, R2)), R2)


def solve_ce602527(S, I):
    x1 = mir_rot_t(I, R2)
    x2 = fgpartition(x1)
    x3 = order(x2, size)
    x4 = get_nth_t(x3, L1)
    x5 = remove_f(x4, x3)
    x6 = compose(toindices, normalize)
    x7 = x6(x4)
    x8 = rbind(intersection, x7)
    x9 = rbind(upscale_f, TWO)
    x10 = chain(toindices, x9, normalize)
    x11 = chain(size, x8, x10)
    x12 = get_arg_rank_t(x5, x11, F0)
    x13 = subgrid(x12, x1)
    O = mir_rot_t(x13, R2)
    return O
