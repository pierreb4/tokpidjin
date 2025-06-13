def solve_d90796e8_one(S, I):
    return fill(cover(I, mfilter_f(sizefilter(o_g(I, R1), TWO), compose(lbind(contained, RED), palette_f))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), sfilter_f(mfilter_f(sizefilter(o_g(I, R1), TWO), compose(lbind(contained, RED), palette_f)), matcher(rbind(get_nth_f, F0), GREEN)))


def solve_d90796e8(S, I):
    x1 = o_g(I, R1)
    x2 = sizefilter(x1, TWO)
    x3 = lbind(contained, RED)
    x4 = compose(x3, palette_f)
    x5 = mfilter_f(x2, x4)
    x6 = cover(I, x5)
    x7 = identity(p_g)
    x8 = rbind(get_nth_t, F0)
    x9 = c_zo_n(S, x7, x8)
    x10 = rbind(get_nth_f, F0)
    x11 = matcher(x10, GREEN)
    x12 = sfilter_f(x5, x11)
    O = fill(x6, x9, x12)
    return O
