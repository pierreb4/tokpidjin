def solve_11852cab_one(S, I):
    return paint(paint(paint(paint(I, mir_rot_f(merge_f(o_g(I, R7)), R0)), mir_rot_f(merge_f(o_g(I, R7)), R2)), mir_rot_f(merge_f(o_g(I, R7)), R1)), mir_rot_f(merge_f(o_g(I, R7)), R3))


def solve_11852cab(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = mir_rot_f(x2, R0)
    if x == 3:
        return x3
    x4 = paint(I, x3)
    if x == 4:
        return x4
    x5 = mir_rot_f(x2, R2)
    if x == 5:
        return x5
    x6 = paint(x4, x5)
    if x == 6:
        return x6
    x7 = mir_rot_f(x2, R1)
    if x == 7:
        return x7
    x8 = paint(x6, x7)
    if x == 8:
        return x8
    x9 = mir_rot_f(x2, R3)
    if x == 9:
        return x9
    O = paint(x8, x9)
    return O
