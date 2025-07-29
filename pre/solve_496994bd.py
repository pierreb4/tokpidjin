def solve_496994bd_one(S, I):
    return vconcat(crop(I, ORIGIN, astuple(halve(height_t(I)), width_t(I))), mir_rot_t(crop(I, ORIGIN, astuple(halve(height_t(I)), width_t(I))), R0))


def solve_496994bd(S, I):
    x1 = height_t(I)
    x2 = halve(x1)
    x3 = width_t(I)
    x4 = astuple(x2, x3)
    x5 = crop(I, ORIGIN, x4)
    x6 = mir_rot_t(x5, R0)
    O = vconcat(x5, x6)
    return O
