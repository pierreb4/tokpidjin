def solve_d90796e8_one(S, I):
    return fill(cover(I, mfilter_f(sizefilter(o_g(I, R1), TWO), compose(lbind(contained, RED), palette_f))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), sfilter_f(mfilter_f(sizefilter(o_g(I, R1), TWO), compose(lbind(contained, RED), palette_f)), matcher(rbind(get_nth_f, F0), GREEN)))


def solve_d90796e8(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = sizefilter(x1, TWO)
    if x == 2:
        return x2
    x3 = lbind(contained, RED)
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
    x7 = identity(p_g)
    if x == 7:
        return x7
    x8 = rbind(get_nth_t, F0)
    if x == 8:
        return x8
    x9 = c_zo_n(S, x7, x8)
    if x == 9:
        return x9
    x10 = rbind(get_nth_f, F0)
    if x == 10:
        return x10
    x11 = matcher(x10, GREEN)
    if x == 11:
        return x11
    x12 = sfilter_f(x5, x11)
    if x == 12:
        return x12
    O = fill(x6, x9, x12)
    return O
