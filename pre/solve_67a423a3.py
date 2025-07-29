def solve_67a423a3_one(S, I):
    return fill(I, FOUR, neighbors(get_nth_f(delta(merge_f(colorfilter(o_g(I, R5), get_color_rank_t(I, L1)))), F0)))


def solve_67a423a3(S, I):
    x1 = o_g(I, R5)
    x2 = get_color_rank_t(I, L1)
    x3 = colorfilter(x1, x2)
    x4 = merge_f(x3)
    x5 = delta(x4)
    x6 = get_nth_f(x5, F0)
    x7 = neighbors(x6)
    O = fill(I, FOUR, x7)
    return O
