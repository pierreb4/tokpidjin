def solve_1b60fb0c_one(S, I):
    return underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), get_arg_rank_f(apply(lbind(shift, f_ofcolor(mir_rot_t(I, R4), BLUE)), mapply(neighbors, neighbors(ORIGIN))), compose(size, lbind(intersection, f_ofcolor(I, BLUE))), F0))


def solve_1b60fb0c(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = mir_rot_t(I, R4)
    if x == 4:
        return x4
    x5 = f_ofcolor(x4, BLUE)
    if x == 5:
        return x5
    x6 = lbind(shift, x5)
    if x == 6:
        return x6
    x7 = neighbors(ORIGIN)
    if x == 7:
        return x7
    x8 = mapply(neighbors, x7)
    if x == 8:
        return x8
    x9 = apply(x6, x8)
    if x == 9:
        return x9
    x10 = f_ofcolor(I, BLUE)
    if x == 10:
        return x10
    x11 = lbind(intersection, x10)
    if x == 11:
        return x11
    x12 = compose(size, x11)
    if x == 12:
        return x12
    x13 = get_arg_rank_f(x9, x12, F0)
    if x == 13:
        return x13
    O = underfill(I, x3, x13)
    return O
