def solve_bd4472b8_one(S, I):
    return vconcat(crop(I, ORIGIN, astuple(TWO, width_t(I))), merge_t(repeat(hupscale(mir_rot_t(tophalf(crop(I, ORIGIN, astuple(TWO, width_t(I)))), R1), width_t(I)), RED)))


def solve_bd4472b8(S, I):
    x1 = width_t(I)
    x2 = astuple(TWO, x1)
    x3 = crop(I, ORIGIN, x2)
    x4 = tophalf(x3)
    x5 = mir_rot_t(x4, R1)
    x6 = hupscale(x5, x1)
    x7 = repeat(x6, RED)
    x8 = merge_t(x7)
    O = vconcat(x3, x8)
    return O
