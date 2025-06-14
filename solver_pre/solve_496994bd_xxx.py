def solve_496994bd_one(S, I):
    return vconcat(crop(I, ORIGIN, astuple(halve(height_t(I)), width_t(I))), mir_rot_t(crop(I, ORIGIN, astuple(halve(height_t(I)), width_t(I))), R0))


def solve_496994bd(S, I, x=0):
    x1 = height_t(I)
    if x == 1:
        return x1
    x2 = halve(x1)
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
    O = vconcat(x5, x6)
    return O
