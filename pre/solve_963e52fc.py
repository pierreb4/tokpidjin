def solve_963e52fc_one(S, I):
    return crop(mir_rot_t(merge_t(repeat(mir_rot_t(crop(I, corner(asobject(I), R0), astuple(height_f(asobject(I)), hperiod(asobject(I)))), R4), increment(divide(double(width_t(I)), hperiod(asobject(I)))))), R6), ORIGIN, astuple(height_f(asobject(I)), double(width_t(I))))


def solve_963e52fc(S, I):
    x1 = asobject(I)
    x2 = corner(x1, R0)
    x3 = height_f(x1)
    x4 = hperiod(x1)
    x5 = astuple(x3, x4)
    x6 = crop(I, x2, x5)
    x7 = mir_rot_t(x6, R4)
    x8 = width_t(I)
    x9 = double(x8)
    x10 = divide(x9, x4)
    x11 = increment(x10)
    x12 = repeat(x7, x11)
    x13 = merge_t(x12)
    x14 = mir_rot_t(x13, R6)
    x15 = astuple(x3, x9)
    O = crop(x14, ORIGIN, x15)
    return O
