def solve_1190e5a7_one(S, I):
    return canvas(get_color_rank_t(I, F0), increment(apply(size, astuple(difference(frontiers(I), sfilter_f(frontiers(I), vline_o)), sfilter_f(frontiers(I), vline_o)))))


def solve_1190e5a7(S, I, x=0):
    x1 = get_color_rank_t(I, F0)
    if x == 1:
        return x1
    x2 = frontiers(I)
    if x == 2:
        return x2
    x3 = sfilter_f(x2, vline_o)
    if x == 3:
        return x3
    x4 = difference(x2, x3)
    if x == 4:
        return x4
    x5 = astuple(x4, x3)
    if x == 5:
        return x5
    x6 = apply(size, x5)
    if x == 6:
        return x6
    x7 = increment(x6)
    if x == 7:
        return x7
    O = canvas(x1, x7)
    return O
