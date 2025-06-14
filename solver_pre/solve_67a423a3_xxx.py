def solve_67a423a3_one(S, I):
    return fill(I, FOUR, neighbors(get_nth_f(delta(merge_f(colorfilter(o_g(I, R5), get_color_rank_t(I, L1)))), F0)))


def solve_67a423a3(S, I, x=0):
    x1 = o_g(I, R5)
    if x == 1:
        return x1
    x2 = get_color_rank_t(I, L1)
    if x == 2:
        return x2
    x3 = colorfilter(x1, x2)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    x5 = delta(x4)
    if x == 5:
        return x5
    x6 = get_nth_f(x5, F0)
    if x == 6:
        return x6
    x7 = neighbors(x6)
    if x == 7:
        return x7
    O = fill(I, FOUR, x7)
    return O
