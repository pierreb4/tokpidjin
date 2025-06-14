def solve_a3325580_one(S, I):
    return mir_rot_t(merge_t(apply(rbind(canvas, astuple(ONE, get_val_rank_f(o_g(I, R5), size, F0))), apply(color, order(sizefilter(o_g(I, R5), get_val_rank_f(o_g(I, R5), size, F0)), rbind(col_row, R2))))), R1)


def solve_a3325580(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_val_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = astuple(ONE, x2)
    if x == 3:
        return x3
    x4 = rbind(canvas, x3)
    if x == 4:
        return x4
    x5 = sizefilter(x1, x2)
    if x == 5:
        return x5
    x6 = rbind(col_row, R2)
    if x == 6:
        return x6
    x7 = order(x5, x6)
    if x == 7:
        return x7
    x8 = apply(color, x7)
    if x == 8:
        return x8
    x9 = apply(x4, x8)
    if x == 9:
        return x9
    x10 = merge_t(x9)
    if x == 10:
        return x10
    O = mir_rot_t(x10, R1)
    return O
