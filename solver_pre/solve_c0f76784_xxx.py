def solve_c0f76784_one(S, I):
    return fill(fill(fill(I, SEVEN, merge_f(sfilter_f(colorfilter(o_g(I, R4), ZERO), square_f))), EIGHT, get_arg_rank_f(sfilter_f(colorfilter(o_g(I, R4), ZERO), square_f), size, F0)), SIX, merge_f(sizefilter(sfilter_f(colorfilter(o_g(I, R4), ZERO), square_f), ONE)))


def solve_c0f76784(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = colorfilter(x1, ZERO)
    if x == 2:
        return x2
    x3 = sfilter_f(x2, square_f)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    x5 = fill(I, SEVEN, x4)
    if x == 5:
        return x5
    x6 = get_arg_rank_f(x3, size, F0)
    if x == 6:
        return x6
    x7 = fill(x5, EIGHT, x6)
    if x == 7:
        return x7
    x8 = sizefilter(x3, ONE)
    if x == 8:
        return x8
    x9 = merge_f(x8)
    if x == 9:
        return x9
    O = fill(x7, SIX, x9)
    return O
