def solve_1b60fb0c_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), get_arg_rank_f(apply(lbind(shift, f_ofcolor(mir_rot_t(I, R4), BLUE)), mapply(neighbors, neighbors(ORIGIN))), compose(size, lbind(intersection, f_ofcolor(I, BLUE))), F0))


def solve_1b60fb0c(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = mir_rot_t(I, R4)
    x5 = f_ofcolor(x4, BLUE)
    x6 = lbind(shift, x5)
    x7 = neighbors(ORIGIN)
    x8 = mapply(neighbors, x7)
    x9 = apply(x6, x8)
    x10 = f_ofcolor(I, BLUE)
    x11 = lbind(intersection, x10)
    x12 = compose(size, x11)
    x13 = get_arg_rank_f(x9, x12, F0)
    O = underfill(I, x3, x13)
    return O
