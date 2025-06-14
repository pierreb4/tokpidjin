def solve_e8593010_one(S, I):
    return replace(fill(fill(I, THREE, merge_f(sizefilter(o_g(I, R5), ONE))), TWO, merge_f(sizefilter(o_g(I, R5), TWO))), ZERO, ONE)


def solve_e8593010(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    x4 = fill(I, THREE, x3)
    if x == 4:
        return x4
    x5 = sizefilter(x1, TWO)
    if x == 5:
        return x5
    x6 = merge_f(x5)
    if x == 6:
        return x6
    x7 = fill(x4, TWO, x6)
    if x == 7:
        return x7
    O = replace(x7, ZERO, ONE)
    return O
