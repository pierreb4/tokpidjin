def solve_1190e5a7_one(S, I):
    return canvas(get_color_rank_t(I, F0), increment(apply(size, astuple(difference(frontiers(I), sfilter_f(frontiers(I), vline_o)), sfilter_f(frontiers(I), vline_o)))))


def solve_1190e5a7(S, I):
    x1 = get_color_rank_t(I, F0)
    x2 = frontiers(I)
    x3 = sfilter_f(x2, vline_o)
    x4 = difference(x2, x3)
    x5 = astuple(x4, x3)
    x6 = apply(size, x5)
    x7 = increment(x6)
    O = canvas(x1, x7)
    return O
