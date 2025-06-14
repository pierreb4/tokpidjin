def solve_cdecee7f_one(S, I):
    return vconcat(vconcat(crop(merge_t(hsplit(hconcat(mir_rot_t(merge_t(apply(rbind(canvas, UNITY), apply(color, order(o_g(I, R5), rbind(col_row, R2))))), R1), canvas(BLACK, astuple(ONE, subtract(NINE, size_f(o_g(I, R5)))))), THREE)), ORIGIN, astuple(ONE, THREE)), mir_rot_t(crop(merge_t(hsplit(hconcat(mir_rot_t(merge_t(apply(rbind(canvas, UNITY), apply(color, order(o_g(I, R5), rbind(col_row, R2))))), R1), canvas(BLACK, astuple(ONE, subtract(NINE, size_f(o_g(I, R5)))))), THREE)), DOWN, astuple(ONE, THREE)), R2)), crop(merge_t(hsplit(hconcat(mir_rot_t(merge_t(apply(rbind(canvas, UNITY), apply(color, order(o_g(I, R5), rbind(col_row, R2))))), R1), canvas(BLACK, astuple(ONE, subtract(NINE, size_f(o_g(I, R5)))))), THREE)), TWO_BY_ZERO, astuple(ONE, THREE)))


def solve_cdecee7f(S, I, x=0):
    x1 = rbind(canvas, UNITY)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = rbind(col_row, R2)
    if x == 3:
        return x3
    x4 = order(x2, x3)
    if x == 4:
        return x4
    x5 = apply(color, x4)
    if x == 5:
        return x5
    x6 = apply(x1, x5)
    if x == 6:
        return x6
    x7 = merge_t(x6)
    if x == 7:
        return x7
    x8 = mir_rot_t(x7, R1)
    if x == 8:
        return x8
    x9 = size_f(x2)
    if x == 9:
        return x9
    x10 = subtract(NINE, x9)
    if x == 10:
        return x10
    x11 = astuple(ONE, x10)
    if x == 11:
        return x11
    x12 = canvas(BLACK, x11)
    if x == 12:
        return x12
    x13 = hconcat(x8, x12)
    if x == 13:
        return x13
    x14 = hsplit(x13, THREE)
    if x == 14:
        return x14
    x15 = merge_t(x14)
    if x == 15:
        return x15
    x16 = astuple(ONE, THREE)
    if x == 16:
        return x16
    x17 = crop(x15, ORIGIN, x16)
    if x == 17:
        return x17
    x18 = crop(x15, DOWN, x16)
    if x == 18:
        return x18
    x19 = mir_rot_t(x18, R2)
    if x == 19:
        return x19
    x20 = vconcat(x17, x19)
    if x == 20:
        return x20
    x21 = crop(x15, TWO_BY_ZERO, x16)
    if x == 21:
        return x21
    O = vconcat(x20, x21)
    return O
