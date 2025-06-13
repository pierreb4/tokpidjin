def solve_e8593010_one(S, I):
    return replace(fill(fill(I, THREE, merge_f(sizefilter(o_g(I, R5), ONE))), TWO, merge_f(sizefilter(o_g(I, R5), TWO))), ZERO, ONE)


def solve_e8593010(S, I):
    x1 = o_g(I, R5)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    x4 = fill(I, THREE, x3)
    x5 = sizefilter(x1, TWO)
    x6 = merge_f(x5)
    x7 = fill(x4, TWO, x6)
    O = replace(x7, ZERO, ONE)
    return O
