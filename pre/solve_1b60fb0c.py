def solve_1b60fb0c_one(S, I):
    return underfill(I, TWO, get_arg_rank_f(apply(lbind(shift, f_ofcolor(mir_rot_t(I, R4), ONE)), mapply(neighbors, neighbors(ORIGIN))), compose(size, lbind(intersection, f_ofcolor(I, ONE))), F0))


def solve_1b60fb0c(S, I):
    x1 = mir_rot_t(I, R4)
    x2 = f_ofcolor(x1, ONE)
    x3 = lbind(shift, x2)
    x4 = neighbors(ORIGIN)
    x5 = mapply(neighbors, x4)
    x6 = apply(x3, x5)
    x7 = f_ofcolor(I, ONE)
    x8 = lbind(intersection, x7)
    x9 = compose(size, x8)
    x10 = get_arg_rank_f(x6, x9, F0)
    O = underfill(I, TWO, x10)
    return O
