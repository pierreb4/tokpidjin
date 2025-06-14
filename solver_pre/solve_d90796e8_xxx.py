def solve_d90796e8_one(S, I):
    return fill(cover(I, mfilter_f(sizefilter(o_g(I, R1), TWO), compose(lbind(contained, TWO), palette_f))), EIGHT, sfilter_f(mfilter_f(sizefilter(o_g(I, R1), TWO), compose(lbind(contained, TWO), palette_f)), matcher(rbind(get_nth_f, F0), THREE)))


def solve_d90796e8(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = sizefilter(x1, TWO)
    if x == 2:
        return x2
    x3 = lbind(contained, TWO)
    if x == 3:
        return x3
    x4 = compose(x3, palette_f)
    if x == 4:
        return x4
    x5 = mfilter_f(x2, x4)
    if x == 5:
        return x5
    x6 = cover(I, x5)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, F0)
    if x == 7:
        return x7
    x8 = matcher(x7, THREE)
    if x == 8:
        return x8
    x9 = sfilter_f(x5, x8)
    if x == 9:
        return x9
    O = fill(x6, EIGHT, x9)
    return O
