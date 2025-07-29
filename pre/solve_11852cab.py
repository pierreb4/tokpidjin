def solve_11852cab_one(S, I):
    return paint(paint(paint(paint(I, mir_rot_f(merge_f(o_g(I, R7)), R0)), mir_rot_f(merge_f(o_g(I, R7)), R2)), mir_rot_f(merge_f(o_g(I, R7)), R1)), mir_rot_f(merge_f(o_g(I, R7)), R3))


def solve_11852cab(S, I):
    x1 = o_g(I, R7)
    x2 = merge_f(x1)
    x3 = mir_rot_f(x2, R0)
    x4 = paint(I, x3)
    x5 = mir_rot_f(x2, R2)
    x6 = paint(x4, x5)
    x7 = mir_rot_f(x2, R1)
    x8 = paint(x6, x7)
    x9 = mir_rot_f(x2, R3)
    O = paint(x8, x9)
    return O
