def solve_3345333e_one(S, I):
    return fill(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), get_color_rank_t(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), L1), get_arg_rank_f(apply(lbind(shift, mir_rot_f(f_ofcolor(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), get_color_rank_t(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), L1)), R2)), mapply(neighbors, neighbors(ORIGIN))), compose(size, rbind(intersection, f_ofcolor(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), get_color_rank_t(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), L1)))), F0))


def solve_3345333e(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = cover(I, x2)
    if x == 3:
        return x3
    x4 = get_color_rank_t(x3, L1)
    if x == 4:
        return x4
    x5 = f_ofcolor(x3, x4)
    if x == 5:
        return x5
    x6 = mir_rot_f(x5, R2)
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
    x11 = rbind(intersection, x5)
    if x == 11:
        return x11
    x12 = compose(size, x11)
    if x == 12:
        return x12
    x13 = get_arg_rank_f(x10, x12, F0)
    if x == 13:
        return x13
    O = fill(x3, x4, x13)
    return O
