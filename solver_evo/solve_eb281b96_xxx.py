def solve_eb281b96_one(S, I):
    return vconcat(vconcat(I, mir_rot_t(crop(I, ORIGIN, astuple(decrement(height_t(I)), width_t(I))), R0)), crop(vconcat(I, mir_rot_t(crop(I, ORIGIN, astuple(decrement(height_t(I)), width_t(I))), R0)), DOWN, astuple(double(decrement(height_t(I))), width_t(I))))


def solve_eb281b96(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = decrement(x1)
    if x == 2:
        return x2
    x3 = width_t(I)
    if x == 3:
        return x3
    x4 = astuple(x2, x3)
    if x == 4:
        return x4
    x5 = crop(I, ORIGIN, x4)
    if x == 5:
        return x5
    x6 = mir_rot_t(x5, R0)
    if x == 6:
        return x6
    x7 = vconcat(I, x6)
    if x == 7:
        return x7
    x8 = double(x2)
    if x == 8:
        return x8
    x9 = astuple(x8, x3)
    if x == 9:
        return x9
    x10 = crop(x7, DOWN, x9)
    if x == 10:
        return x10
    O = vconcat(x7, x10)
    return O
