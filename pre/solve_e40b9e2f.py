def solve_e40b9e2f_one(S, I):
    return paint(paint(I, get_arg_rank_f(apply(lbind(shift, compose(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))(get_nth_f(o_g(I, R3), F0))), mapply(neighbors, neighbors(ORIGIN))), lbind(intersection, get_nth_f(o_g(I, R3), F0)), F0)), get_arg_rank_f(apply(lbind(shift, compose(rbind(mir_rot_f, R2), rbind(mir_rot_f, R1))(get_nth_f(o_g(paint(I, get_arg_rank_f(apply(lbind(shift, compose(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))(get_nth_f(o_g(I, R3), F0))), mapply(neighbors, neighbors(ORIGIN))), lbind(intersection, get_nth_f(o_g(I, R3), F0)), F0)), R3), F0))), mapply(neighbors, neighbors(ORIGIN))), compose(size, lbind(intersection, get_nth_f(o_g(I, R3), F0))), F0))


def solve_e40b9e2f(S, I):
    x1 = rbind(mir_rot_f, R0)
    x2 = rbind(mir_rot_f, R2)
    x3 = compose(x1, x2)
    x4 = o_g(I, R3)
    x5 = get_nth_f(x4, F0)
    x6 = x3(x5)
    x7 = lbind(shift, x6)
    x8 = neighbors(ORIGIN)
    x9 = mapply(neighbors, x8)
    x10 = apply(x7, x9)
    x11 = lbind(intersection, x5)
    x12 = get_arg_rank_f(x10, x11, F0)
    x13 = paint(I, x12)
    x14 = rbind(mir_rot_f, R1)
    x15 = compose(x2, x14)
    x16 = o_g(x13, R3)
    x17 = get_nth_f(x16, F0)
    x18 = x15(x17)
    x19 = lbind(shift, x18)
    x20 = apply(x19, x9)
    x21 = compose(size, x11)
    x22 = get_arg_rank_f(x20, x21, F0)
    O = paint(x13, x22)
    return O
