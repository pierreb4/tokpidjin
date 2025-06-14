def solve_8e5a5113_one(S, I):
    return paint(I, mpapply(shift, apply(asobject, astuple(mir_rot_t(crop(I, ORIGIN, THREE_BY_THREE), R4), mir_rot_t(crop(I, ORIGIN, THREE_BY_THREE), R5))), apply(tojvec, astuple(FOUR, EIGHT))))


def solve_8e5a5113(S, I, x=0):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    if x == 1:
        return x1
    x2 = mir_rot_t(x1, R4)
    if x == 2:
        return x2
    x3 = mir_rot_t(x1, R5)
    if x == 3:
        return x3
    x4 = astuple(x2, x3)
    if x == 4:
        return x4
    x5 = apply(asobject, x4)
    if x == 5:
        return x5
    x6 = astuple(FOUR, EIGHT)
    if x == 6:
        return x6
    x7 = apply(tojvec, x6)
    if x == 7:
        return x7
    x8 = mpapply(shift, x5, x7)
    if x == 8:
        return x8
    O = paint(I, x8)
    return O
