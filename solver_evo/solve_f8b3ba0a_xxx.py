def solve_f8b3ba0a_one(S, I):
    return crop(merge_t(apply(rbind(canvas, UNITY), order(palette_t(compress(I)), compose(invert, lbind(colorcount_t, compress(I)))))), DOWN, astuple(THREE, ONE))


def solve_f8b3ba0a(S, I, x=0):
    x1 = rbind(canvas, UNITY)
    if x == 1:
        return x1
    x2 = compress(I)
    if x == 2:
        return x2
    x3 = palette_t(x2)
    if x == 3:
        return x3
    x4 = lbind(colorcount_t, x2)
    if x == 4:
        return x4
    x5 = compose(invert, x4)
    if x == 5:
        return x5
    x6 = order(x3, x5)
    if x == 6:
        return x6
    x7 = apply(x1, x6)
    if x == 7:
        return x7
    x8 = merge_t(x7)
    if x == 8:
        return x8
    x9 = astuple(THREE, ONE)
    if x == 9:
        return x9
    O = crop(x8, DOWN, x9)
    return O
