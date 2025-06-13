def solve_f8b3ba0a_one(S, I):
    return crop(merge_t(apply(rbind(canvas, UNITY), order(palette_t(compress(I)), compose(invert, lbind(colorcount_t, compress(I)))))), DOWN, astuple(THREE, ONE))


def solve_f8b3ba0a(S, I):
    x1 = rbind(canvas, UNITY)
    x2 = compress(I)
    x3 = palette_t(x2)
    x4 = lbind(colorcount_t, x2)
    x5 = compose(invert, x4)
    x6 = order(x3, x5)
    x7 = apply(x1, x6)
    x8 = merge_t(x7)
    x9 = astuple(THREE, ONE)
    O = crop(x8, DOWN, x9)
    return O
