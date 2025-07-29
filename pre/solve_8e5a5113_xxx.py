def solve_8e5a5113_one(S, I):
    return paint(I, mpapply(shift, apply(asobject, astuple(mir_rot_t(crop(I, ORIGIN, THREE_BY_THREE), R4), mir_rot_t(crop(I, ORIGIN, THREE_BY_THREE), R5))), apply(tojvec, astuple(FOUR, EIGHT))))


def solve_8e5a5113(S, I):
    x1 = crop(I, ORIGIN, THREE_BY_THREE)
    x2 = mir_rot_t(x1, R4)
    x3 = mir_rot_t(x1, R5)
    x4 = astuple(x2, x3)
    x5 = apply(asobject, x4)
    x6 = astuple(FOUR, EIGHT)
    x7 = apply(tojvec, x6)
    x8 = mpapply(shift, x5, x7)
    O = paint(I, x8)
    return O
