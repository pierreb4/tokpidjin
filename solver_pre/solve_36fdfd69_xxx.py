def solve_36fdfd69_one(S, I):
    return downscale(paint(fill(upscale_t(I, TWO), FOUR, mapply(delta, apply(merge, sfilter_f(product(colorfilter(o_g(upscale_t(I, TWO), R7), TWO), colorfilter(o_g(upscale_t(I, TWO), R7), TWO)), compose(lbind(greater, FIVE), fork(manhattan, rbind(get_nth_f, F0), rbind(get_nth_f, L1))))))), merge(colorfilter(o_g(upscale_t(I, TWO), R7), TWO))), TWO)


def solve_36fdfd69(S, I, x=0):
    x1 = upscale_t(I, TWO)
    if x == 1:
        return x1
    x2 = o_g(x1, R7)
    if x == 2:
        return x2
    x3 = colorfilter(x2, TWO)
    if x == 3:
        return x3
    x4 = product(x3, x3)
    if x == 4:
        return x4
    x5 = lbind(greater, FIVE)
    if x == 5:
        return x5
    x6 = rbind(get_nth_f, F0)
    if x == 6:
        return x6
    x7 = rbind(get_nth_f, L1)
    if x == 7:
        return x7
    x8 = fork(manhattan, x6, x7)
    if x == 8:
        return x8
    x9 = compose(x5, x8)
    if x == 9:
        return x9
    x10 = sfilter_f(x4, x9)
    if x == 10:
        return x10
    x11 = apply(merge, x10)
    if x == 11:
        return x11
    x12 = mapply(delta, x11)
    if x == 12:
        return x12
    x13 = fill(x1, FOUR, x12)
    if x == 13:
        return x13
    x14 = merge(x3)
    if x == 14:
        return x14
    x15 = paint(x13, x14)
    if x == 15:
        return x15
    O = downscale(x15, TWO)
    return O
