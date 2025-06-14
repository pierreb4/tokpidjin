def solve_3618c87e_one(S, I):
    return move(I, merge_f(sizefilter(o_g(I, R5), ONE)), TWO_BY_ZERO)


def solve_3618c87e(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = sizefilter(x1, ONE)
    if x == 2:
        return x2
    x3 = merge_f(x2)
    if x == 3:
        return x3
    O = move(I, x3, TWO_BY_ZERO)
    return O
