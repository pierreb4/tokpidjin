def solve_e9afcf9a_one(S, I):
    return hconcat(hconcat(hconcat(crop(I, ORIGIN, astuple(TWO, ONE)), mir_rot_t(crop(I, ORIGIN, astuple(TWO, ONE)), R0)), hconcat(crop(I, ORIGIN, astuple(TWO, ONE)), mir_rot_t(crop(I, ORIGIN, astuple(TWO, ONE)), R0))), hconcat(crop(I, ORIGIN, astuple(TWO, ONE)), mir_rot_t(crop(I, ORIGIN, astuple(TWO, ONE)), R0)))


def solve_e9afcf9a(S, I):
    x1 = astuple(TWO, ONE)
    x2 = crop(I, ORIGIN, x1)
    x3 = mir_rot_t(x2, R0)
    x4 = hconcat(x2, x3)
    x5 = hconcat(x4, x4)
    O = hconcat(x5, x4)
    return O
