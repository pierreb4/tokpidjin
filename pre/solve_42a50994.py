def solve_42a50994_one(S, I):
    return cover(I, merge_f(sizefilter(o_g(I, R7), ONE)))


def solve_42a50994(S, I):
    x1 = o_g(I, R7)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    O = cover(I, x3)
    return O
