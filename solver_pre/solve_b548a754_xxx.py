def solve_b548a754_one(S, I):
    return fill(fill(I, get_color_rank_t(replace(I, EIGHT, ZERO), L1), backdrop(merge_f(o_g(I, R5)))), get_color_rank_t(replace(replace(I, EIGHT, ZERO), get_color_rank_t(replace(I, EIGHT, ZERO), L1), ZERO), L1), box(merge_f(o_g(I, R5))))


def solve_b548a754(S, I, x=0):
    x1 = replace(I, EIGHT, ZERO)
    if x == 1:
        return x1
    x2 = get_color_rank_t(x1, L1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    x5 = backdrop(x4)
    if x == 5:
        return x5
    x6 = fill(I, x2, x5)
    if x == 6:
        return x6
    x7 = replace(x1, x2, ZERO)
    if x == 7:
        return x7
    x8 = get_color_rank_t(x7, L1)
    if x == 8:
        return x8
    x9 = box(x4)
    if x == 9:
        return x9
    O = fill(x6, x8, x9)
    return O
