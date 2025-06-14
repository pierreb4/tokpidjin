def solve_6455b5f5_one(S, I):
    return fill(paint(I, recolor_o(ONE, get_arg_rank_f(o_g(I, R4), size, F0))), EIGHT, merge_f(sizefilter(colorfilter(o_g(I, R4), ZERO), get_val_rank_f(o_g(I, R4), size, L1))))


def solve_6455b5f5(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = recolor_o(ONE, x2)
    if x == 3:
        return x3
    x4 = paint(I, x3)
    if x == 4:
        return x4
    x5 = colorfilter(x1, ZERO)
    if x == 5:
        return x5
    x6 = get_val_rank_f(x1, size, L1)
    if x == 6:
        return x6
    x7 = sizefilter(x5, x6)
    if x == 7:
        return x7
    x8 = merge_f(x7)
    if x == 8:
        return x8
    O = fill(x4, EIGHT, x8)
    return O
