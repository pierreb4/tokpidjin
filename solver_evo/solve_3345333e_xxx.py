def solve_3345333e_one(S, I):
    return fill(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), get_color_rank_t(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), L1), get_arg_rank_f(apply(lbind(shift, mir_rot_f(f_ofcolor(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), get_color_rank_t(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), L1)), R2)), mapply(neighbors, neighbors(ORIGIN))), compose(size, rbind(intersection, f_ofcolor(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), get_color_rank_t(cover(I, f_ofcolor(I, get_color_rank_t(I, L1))), L1)))), F0))


def solve_3345333e(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = f_ofcolor(I, x1)
    x3 = cover(I, x2)
    x4 = get_color_rank_t(x3, L1)
    x5 = f_ofcolor(x3, x4)
    x6 = mir_rot_f(x5, R2)
    x7 = lbind(shift, x6)
    x8 = neighbors(ORIGIN)
    x9 = mapply(neighbors, x8)
    x10 = apply(x7, x9)
    x11 = rbind(intersection, x5)
    x12 = compose(size, x11)
    x13 = get_arg_rank_f(x10, x12, F0)
    O = fill(x3, x4, x13)
    return O
