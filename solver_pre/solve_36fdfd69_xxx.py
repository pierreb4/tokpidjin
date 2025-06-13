def solve_36fdfd69_one(S, I):
    return downscale(paint(fill(upscale_t(I, TWO), FOUR, mapply(delta, apply(merge, sfilter_f(product(colorfilter(o_g(upscale_t(I, TWO), R7), TWO), colorfilter(o_g(upscale_t(I, TWO), R7), TWO)), compose(lbind(greater, FIVE), fork(manhattan, rbind(get_nth_f, F0), rbind(get_nth_f, L1))))))), merge(colorfilter(o_g(upscale_t(I, TWO), R7), TWO))), TWO)


def solve_36fdfd69(S, I):
    x1 = upscale_t(I, TWO)
    x2 = o_g(x1, R7)
    x3 = colorfilter(x2, TWO)
    x4 = product(x3, x3)
    x5 = lbind(greater, FIVE)
    x6 = rbind(get_nth_f, F0)
    x7 = rbind(get_nth_f, L1)
    x8 = fork(manhattan, x6, x7)
    x9 = compose(x5, x8)
    x10 = sfilter_f(x4, x9)
    x11 = apply(merge, x10)
    x12 = mapply(delta, x11)
    x13 = fill(x1, FOUR, x12)
    x14 = merge(x3)
    x15 = paint(x13, x14)
    O = downscale(x15, TWO)
    return O
