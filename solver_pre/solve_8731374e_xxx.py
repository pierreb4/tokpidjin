def solve_8731374e_one(S, I):
    return fill(mir_rot_t(merge(sfilter_t(vsplit(mir_rot_t(merge(sfilter_t(vsplit(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I), height_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, FOUR), numcolors_t))), R4), width_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, FOUR), numcolors_t))), R6), get_color_rank_t(mir_rot_t(merge(sfilter_t(vsplit(mir_rot_t(merge(sfilter_t(vsplit(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I), height_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, FOUR), numcolors_t))), R4), width_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, FOUR), numcolors_t))), R6), L1), mapply(fork(combine, vfrontier, hfrontier), f_ofcolor(mir_rot_t(merge(sfilter_t(vsplit(mir_rot_t(merge(sfilter_t(vsplit(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I), height_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, FOUR), numcolors_t))), R4), width_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, FOUR), numcolors_t))), R6), get_color_rank_t(mir_rot_t(merge(sfilter_t(vsplit(mir_rot_t(merge(sfilter_t(vsplit(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I), height_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, FOUR), numcolors_t))), R4), width_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, FOUR), numcolors_t))), R6), L1))))


def solve_8731374e(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = subgrid(x2, I)
    if x == 3:
        return x3
    x4 = height_t(x3)
    if x == 4:
        return x4
    x5 = vsplit(x3, x4)
    if x == 5:
        return x5
    x6 = lbind(greater, FOUR)
    if x == 6:
        return x6
    x7 = compose(x6, numcolors_t)
    if x == 7:
        return x7
    x8 = sfilter_t(x5, x7)
    if x == 8:
        return x8
    x9 = merge(x8)
    if x == 9:
        return x9
    x10 = mir_rot_t(x9, R4)
    if x == 10:
        return x10
    x11 = width_t(x3)
    if x == 11:
        return x11
    x12 = vsplit(x10, x11)
    if x == 12:
        return x12
    x13 = sfilter_t(x12, x7)
    if x == 13:
        return x13
    x14 = merge(x13)
    if x == 14:
        return x14
    x15 = mir_rot_t(x14, R6)
    if x == 15:
        return x15
    x16 = get_color_rank_t(x15, L1)
    if x == 16:
        return x16
    x17 = fork(combine, vfrontier, hfrontier)
    if x == 17:
        return x17
    x18 = f_ofcolor(x15, x16)
    if x == 18:
        return x18
    x19 = mapply(x17, x18)
    if x == 19:
        return x19
    O = fill(x15, x16, x19)
    return O
