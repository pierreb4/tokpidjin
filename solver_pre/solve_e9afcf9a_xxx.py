def solve_e9afcf9a_one(S, I):
    return hconcat(hconcat(hconcat(crop(I, ORIGIN, astuple(TWO, ONE)), mir_rot_t(crop(I, ORIGIN, astuple(TWO, ONE)), R0)), hconcat(crop(I, ORIGIN, astuple(TWO, ONE)), mir_rot_t(crop(I, ORIGIN, astuple(TWO, ONE)), R0))), hconcat(crop(I, ORIGIN, astuple(TWO, ONE)), mir_rot_t(crop(I, ORIGIN, astuple(TWO, ONE)), R0)))


def solve_e9afcf9a(S, I, x=0):
    x1 = astuple(TWO, ONE)
    if x == 1:
        return x1
    x2 = crop(I, ORIGIN, x1)
    if x == 2:
        return x2
    x3 = mir_rot_t(x2, R0)
    if x == 3:
        return x3
    x4 = hconcat(x2, x3)
    if x == 4:
        return x4
    x5 = hconcat(x4, x4)
    if x == 5:
        return x5
    O = hconcat(x5, x4)
    return O
