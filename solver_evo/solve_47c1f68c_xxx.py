def solve_47c1f68c_one(S, I):
    return replace(compress(cellwise(cellwise(I, mir_rot_t(I, R2), get_color_rank_t(I, L1)), mir_rot_t(cellwise(I, mir_rot_t(I, R2), get_color_rank_t(I, L1)), R0), get_color_rank_t(I, L1))), get_color_rank_t(I, L1), get_color_rank_f(merge_f(o_g(I, R7)), F0))


def solve_47c1f68c(S, I):
    x1 = mir_rot_t(I, R2)
    x2 = get_color_rank_t(I, L1)
    x3 = cellwise(I, x1, x2)
    x4 = mir_rot_t(x3, R0)
    x5 = cellwise(x3, x4, x2)
    x6 = compress(x5)
    x7 = o_g(I, R7)
    x8 = merge_f(x7)
    x9 = get_color_rank_f(x8, F0)
    O = replace(x6, x2, x9)
    return O
