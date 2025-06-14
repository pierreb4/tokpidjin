def solve_42a50994_one(S, I):
    return cover(I, merge_f(sizefilter(o_g(I, R7), ONE)))


def solve_42a50994(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    O = cover(I, x3)
    return O
