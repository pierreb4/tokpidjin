def solve_e40b9e2f_one(S, I):
    return paint(paint(I, get_arg_rank_f(apply(lbind(shift, compose(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))(get_nth_f(o_g(I, R3), F0))), mapply(neighbors, neighbors(ORIGIN))), lbind(intersection, get_nth_f(o_g(I, R3), F0)), F0)), get_arg_rank_f(apply(lbind(shift, compose(rbind(mir_rot_f, R2), rbind(mir_rot_f, R1))(get_nth_f(o_g(paint(I, get_arg_rank_f(apply(lbind(shift, compose(rbind(mir_rot_f, R0), rbind(mir_rot_f, R2))(get_nth_f(o_g(I, R3), F0))), mapply(neighbors, neighbors(ORIGIN))), lbind(intersection, get_nth_f(o_g(I, R3), F0)), F0)), R3), F0))), mapply(neighbors, neighbors(ORIGIN))), compose(size, lbind(intersection, get_nth_f(o_g(I, R3), F0))), F0))


def solve_e40b9e2f(S, I, x=0):
    x1 = rbind(mir_rot_f, R0)
    if x == 1:
        return x1
    x2 = rbind(mir_rot_f, R2)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R3)
    if x == 4:
        return x4
    x5 = get_nth_f(x4, F0)
    if x == 5:
        return x5
    x6 = x3(x5)
    if x == 6:
        return x6
    x7 = lbind(shift, x6)
    if x == 7:
        return x7
    x8 = neighbors(ORIGIN)
    if x == 8:
        return x8
    x9 = mapply(neighbors, x8)
    if x == 9:
        return x9
    x10 = apply(x7, x9)
    if x == 10:
        return x10
    x11 = lbind(intersection, x5)
    if x == 11:
        return x11
    x12 = get_arg_rank_f(x10, x11, F0)
    if x == 12:
        return x12
    x13 = paint(I, x12)
    if x == 13:
        return x13
    x14 = rbind(mir_rot_f, R1)
    if x == 14:
        return x14
    x15 = compose(x2, x14)
    if x == 15:
        return x15
    x16 = o_g(x13, R3)
    if x == 16:
        return x16
    x17 = get_nth_f(x16, F0)
    if x == 17:
        return x17
    x18 = x15(x17)
    if x == 18:
        return x18
    x19 = lbind(shift, x18)
    if x == 19:
        return x19
    x20 = apply(x19, x9)
    if x == 20:
        return x20
    x21 = compose(size, x11)
    if x == 21:
        return x21
    x22 = get_arg_rank_f(x20, x21, F0)
    if x == 22:
        return x22
    O = paint(x13, x22)
    return O
