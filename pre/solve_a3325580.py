def solve_a3325580_one(S, I):
    return mir_rot_t(merge_t(apply(rbind(canvas, astuple(ONE, get_val_rank_f(o_g(I, R5), size, F0))), apply(color, order(sizefilter(o_g(I, R5), get_val_rank_f(o_g(I, R5), size, F0)), rbind(col_row, R2))))), R1)


def solve_a3325580(S, I):
    x1 = o_g(I, R5)
    x2 = get_val_rank_f(x1, size, F0)
    x3 = astuple(ONE, x2)
    x4 = rbind(canvas, x3)
    x5 = sizefilter(x1, x2)
    x6 = rbind(col_row, R2)
    x7 = order(x5, x6)
    x8 = apply(color, x7)
    x9 = apply(x4, x8)
    x10 = merge_t(x9)
    O = mir_rot_t(x10, R1)
    return O
