def solve_8731374e_one(S, I):
    return fill(mir_rot_t(merge(sfilter_t(vsplit(mir_rot_t(merge(sfilter_t(vsplit(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I), height_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, YELLOW), numcolors_t))), R4), width_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, YELLOW), numcolors_t))), R6), get_color_rank_t(mir_rot_t(merge(sfilter_t(vsplit(mir_rot_t(merge(sfilter_t(vsplit(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I), height_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, YELLOW), numcolors_t))), R4), width_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, YELLOW), numcolors_t))), R6), L1), mapply(fork(combine, vfrontier, hfrontier), f_ofcolor(mir_rot_t(merge(sfilter_t(vsplit(mir_rot_t(merge(sfilter_t(vsplit(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I), height_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, YELLOW), numcolors_t))), R4), width_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, YELLOW), numcolors_t))), R6), get_color_rank_t(mir_rot_t(merge(sfilter_t(vsplit(mir_rot_t(merge(sfilter_t(vsplit(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I), height_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, YELLOW), numcolors_t))), R4), width_t(subgrid(get_arg_rank_f(o_g(I, R4), size, F0), I))), compose(lbind(greater, YELLOW), numcolors_t))), R6), L1))))


def solve_8731374e(S, I):
    x1 = o_g(I, R4)
    x2 = get_arg_rank_f(x1, size, F0)
    x3 = subgrid(x2, I)
    x4 = height_t(x3)
    x5 = vsplit(x3, x4)
    x6 = lbind(greater, YELLOW)
    x7 = compose(x6, numcolors_t)
    x8 = sfilter_t(x5, x7)
    x9 = merge(x8)
    x10 = mir_rot_t(x9, R4)
    x11 = width_t(x3)
    x12 = vsplit(x10, x11)
    x13 = sfilter_t(x12, x7)
    x14 = merge(x13)
    x15 = mir_rot_t(x14, R6)
    x16 = get_color_rank_t(x15, L1)
    x17 = fork(combine, vfrontier, hfrontier)
    x18 = f_ofcolor(x15, x16)
    x19 = mapply(x17, x18)
    O = fill(x15, x16, x19)
    return O
