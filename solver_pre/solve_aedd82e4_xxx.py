def solve_aedd82e4_one(S, I):
    return fill(I, ONE, merge_f(sizefilter(colorfilter(o_g(I, R4), TWO), ONE)))


def solve_aedd82e4(S, I):
    x1 = o_g(I, R4)
    x2 = colorfilter(x1, TWO)
    x3 = sizefilter(x2, ONE)
    x4 = merge_f(x3)
    O = fill(I, ONE, x4)
    return O
