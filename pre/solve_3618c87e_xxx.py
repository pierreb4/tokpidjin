def solve_3618c87e_one(S, I):
    return move(I, merge_f(sizefilter(o_g(I, R5), ONE)), TWO_BY_ZERO)


def solve_3618c87e(S, I):
    x1 = o_g(I, R5)
    x2 = sizefilter(x1, ONE)
    x3 = merge_f(x2)
    O = move(I, x3, TWO_BY_ZERO)
    return O
