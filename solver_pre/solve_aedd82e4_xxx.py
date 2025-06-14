def solve_aedd82e4_one(S, I):
    return fill(I, ONE, merge_f(sizefilter(colorfilter(o_g(I, R4), TWO), ONE)))


def solve_aedd82e4(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, TWO)
    if x == 2:
        return x2
    x3 = sizefilter(x2, ONE)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    O = fill(I, ONE, x4)
    return O
