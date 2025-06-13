def solve_cdecee7f_one(S, I):
    return vconcat(vconcat(crop(merge_t(hsplit(hconcat(mir_rot_t(merge_t(apply(rbind(canvas, UNITY), apply(color, order(o_g(I, R5), rbind(col_row, R2))))), R1), canvas(BLACK, astuple(ONE, subtract(NINE, size_f(o_g(I, R5)))))), THREE)), ORIGIN, astuple(ONE, THREE)), mir_rot_t(crop(merge_t(hsplit(hconcat(mir_rot_t(merge_t(apply(rbind(canvas, UNITY), apply(color, order(o_g(I, R5), rbind(col_row, R2))))), R1), canvas(BLACK, astuple(ONE, subtract(NINE, size_f(o_g(I, R5)))))), THREE)), DOWN, astuple(ONE, THREE)), R2)), crop(merge_t(hsplit(hconcat(mir_rot_t(merge_t(apply(rbind(canvas, UNITY), apply(color, order(o_g(I, R5), rbind(col_row, R2))))), R1), canvas(BLACK, astuple(ONE, subtract(NINE, size_f(o_g(I, R5)))))), THREE)), TWO_BY_ZERO, astuple(ONE, THREE)))


def solve_cdecee7f(S, I):
    x1 = rbind(canvas, UNITY)
    x2 = o_g(I, R5)
    x3 = rbind(col_row, R2)
    x4 = order(x2, x3)
    x5 = apply(color, x4)
    x6 = apply(x1, x5)
    x7 = merge_t(x6)
    x8 = mir_rot_t(x7, R1)
    x9 = size_f(x2)
    x10 = subtract(NINE, x9)
    x11 = astuple(ONE, x10)
    x12 = canvas(BLACK, x11)
    x13 = hconcat(x8, x12)
    x14 = hsplit(x13, THREE)
    x15 = merge_t(x14)
    x16 = astuple(ONE, THREE)
    x17 = crop(x15, ORIGIN, x16)
    x18 = crop(x15, DOWN, x16)
    x19 = mir_rot_t(x18, R2)
    x20 = vconcat(x17, x19)
    x21 = crop(x15, TWO_BY_ZERO, x16)
    O = vconcat(x20, x21)
    return O
