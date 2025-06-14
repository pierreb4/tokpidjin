def solve_bd4472b8_one(S, I):
    return vconcat(crop(I, ORIGIN, astuple(TWO, width_t(I))), merge_t(repeat(hupscale(mir_rot_t(tophalf(crop(I, ORIGIN, astuple(TWO, width_t(I)))), R1), width_t(I)), RED)))


def solve_bd4472b8(S, I, x=0):
    x1 = width_t(I)
    if x == 1:
        return x1
    x2 = astuple(TWO, x1)
    if x == 2:
        return x2
    x3 = crop(I, ORIGIN, x2)
    if x == 3:
        return x3
    x4 = tophalf(x3)
    if x == 4:
        return x4
    x5 = mir_rot_t(x4, R1)
    if x == 5:
        return x5
    x6 = hupscale(x5, x1)
    if x == 6:
        return x6
    x7 = repeat(x6, RED)
    if x == 7:
        return x7
    x8 = merge_t(x7)
    if x == 8:
        return x8
    O = vconcat(x3, x8)
    return O
