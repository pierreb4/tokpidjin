def solve_eb281b96_one(S, I):
    return vconcat(vconcat(I, mir_rot_t(crop(I, ORIGIN, astuple(decrement(height_t(I)), width_t(I))), R0)), crop(vconcat(I, mir_rot_t(crop(I, ORIGIN, astuple(decrement(height_t(I)), width_t(I))), R0)), DOWN, astuple(double(decrement(height_t(I))), width_t(I))))


def solve_eb281b96(S, I):
    x1 = height_t(I)
    x2 = decrement(x1)
    x3 = width_t(I)
    x4 = astuple(x2, x3)
    x5 = crop(I, ORIGIN, x4)
    x6 = mir_rot_t(x5, R0)
    x7 = vconcat(I, x6)
    x8 = double(x2)
    x9 = astuple(x8, x3)
    x10 = crop(x7, DOWN, x9)
    O = vconcat(x7, x10)
    return O
