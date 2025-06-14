def solve_1b60fb0c_one(S, I):
    return underfill(I, TWO, get_arg_rank_f(apply(lbind(shift, f_ofcolor(mir_rot_t(I, R4), ONE)), mapply(neighbors, neighbors(ORIGIN))), compose(size, lbind(intersection, f_ofcolor(I, ONE))), F0))


def solve_1b60fb0c(S, I, x=0):
    x1 = mir_rot_t(I, R4)
    if x == 1:
        return x1
    x2 = f_ofcolor(x1, ONE)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = neighbors(ORIGIN)
    if x == 4:
        return x4
    x5 = mapply(neighbors, x4)
    if x == 5:
        return x5
    x6 = apply(x3, x5)
    if x == 6:
        return x6
    x7 = f_ofcolor(I, ONE)
    if x == 7:
        return x7
    x8 = lbind(intersection, x7)
    if x == 8:
        return x8
    x9 = compose(size, x8)
    if x == 9:
        return x9
    x10 = get_arg_rank_f(x6, x9, F0)
    if x == 10:
        return x10
    O = underfill(I, TWO, x10)
    return O
