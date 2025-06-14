def solve_cd3c21df_one(S, I):
    return mir_rot_t(subgrid(get_arg_rank_t(remove_f(get_nth_t(order(fgpartition(mir_rot_t(I, R2)), size), L1), order(fgpartition(mir_rot_t(I, R2)), size)), chain(size, rbind(intersection, compose(toindices, normalize)(get_nth_t(order(fgpartition(mir_rot_t(I, R2)), size), L1))), chain(toindices, rbind(upscale_f, RED), normalize)), F0), mir_rot_t(I, R2)), R2)


def solve_cd3c21df(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = fgpartition(x1)
    if x == 2:
        return x2
    x3 = order(x2, size)
    if x == 3:
        return x3
    x4 = get_nth_t(x3, L1)
    if x == 4:
        return x4
    x5 = remove_f(x4, x3)
    if x == 5:
        return x5
    x6 = compose(toindices, normalize)
    if x == 6:
        return x6
    x7 = x6(x4)
    if x == 7:
        return x7
    x8 = rbind(intersection, x7)
    if x == 8:
        return x8
    x9 = rbind(upscale_f, RED)
    if x == 9:
        return x9
    x10 = chain(toindices, x9, normalize)
    if x == 10:
        return x10
    x11 = chain(size, x8, x10)
    if x == 11:
        return x11
    x12 = get_arg_rank_t(x5, x11, F0)
    if x == 12:
        return x12
    x13 = subgrid(x12, x1)
    if x == 13:
        return x13
    O = mir_rot_t(x13, R2)
    return O
