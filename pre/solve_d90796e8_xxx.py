def solve_d90796e8_one(S, I):
    return fill(cover(I, mfilter_f(sizefilter(o_g(I, R1), TWO), compose(lbind(contained, TWO), palette_f))), EIGHT, sfilter_f(mfilter_f(sizefilter(o_g(I, R1), TWO), compose(lbind(contained, TWO), palette_f)), matcher(rbind(get_nth_f, F0), THREE)))


def solve_d90796e8(S, I):
    x1 = o_g(I, R1)
    x2 = sizefilter(x1, TWO)
    x3 = lbind(contained, TWO)
    x4 = compose(x3, palette_f)
    x5 = mfilter_f(x2, x4)
    x6 = cover(I, x5)
    x7 = rbind(get_nth_f, F0)
    x8 = matcher(x7, THREE)
    x9 = sfilter_f(x5, x8)
    O = fill(x6, EIGHT, x9)
    return O
