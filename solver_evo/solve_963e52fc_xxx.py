def solve_963e52fc_one(S, I):
    return crop(mir_rot_t(merge_t(repeat(mir_rot_t(crop(I, corner(asobject(I), R0), astuple(height_f(asobject(I)), hperiod(asobject(I)))), R4), increment(divide(double(width_t(I)), hperiod(asobject(I)))))), R6), ORIGIN, astuple(height_f(asobject(I)), double(width_t(I))))


def solve_963e52fc(S, I, x=0):
    x1 = asobject(I)
    if x == 1:
        return x1
    x2 = corner(x1, R0)
    if x == 2:
        return x2
    x3 = height_f(x1)
    if x == 3:
        return x3
    x4 = hperiod(x1)
    if x == 4:
        return x4
    x5 = astuple(x3, x4)
    if x == 5:
        return x5
    x6 = crop(I, x2, x5)
    if x == 6:
        return x6
    x7 = mir_rot_t(x6, R4)
    if x == 7:
        return x7
    x8 = width_t(I)
    if x == 8:
        return x8
    x9 = double(x8)
    if x == 9:
        return x9
    x10 = divide(x9, x4)
    if x == 10:
        return x10
    x11 = increment(x10)
    if x == 11:
        return x11
    x12 = repeat(x7, x11)
    if x == 12:
        return x12
    x13 = merge_t(x12)
    if x == 13:
        return x13
    x14 = mir_rot_t(x13, R6)
    if x == 14:
        return x14
    x15 = astuple(x3, x9)
    if x == 15:
        return x15
    O = crop(x14, ORIGIN, x15)
    return O
