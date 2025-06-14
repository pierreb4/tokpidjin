def solve_47c1f68c_one(S, I):
    return replace(compress(cellwise(cellwise(I, mir_rot_t(I, R2), get_color_rank_t(I, L1)), mir_rot_t(cellwise(I, mir_rot_t(I, R2), get_color_rank_t(I, L1)), R0), get_color_rank_t(I, L1))), get_color_rank_t(I, L1), get_color_rank_f(merge_f(o_g(I, R7)), F0))


def solve_47c1f68c(S, I, x=0):
    x1 = mir_rot_t(I, R2)
    if x == 1:
        return x1
    x2 = get_color_rank_t(I, L1)
    if x == 2:
        return x2
    x3 = cellwise(I, x1, x2)
    if x == 3:
        return x3
    x4 = mir_rot_t(x3, R0)
    if x == 4:
        return x4
    x5 = cellwise(x3, x4, x2)
    if x == 5:
        return x5
    x6 = compress(x5)
    if x == 6:
        return x6
    x7 = o_g(I, R7)
    if x == 7:
        return x7
    x8 = merge_f(x7)
    if x == 8:
        return x8
    x9 = get_color_rank_f(x8, F0)
    if x == 9:
        return x9
    O = replace(x6, x2, x9)
    return O
