def solve_b548a754_one(S, I):
    return fill(fill(I, get_color_rank_t(replace(I, EIGHT, ZERO), L1), backdrop(merge_f(o_g(I, R5)))), get_color_rank_t(replace(replace(I, EIGHT, ZERO), get_color_rank_t(replace(I, EIGHT, ZERO), L1), ZERO), L1), box(merge_f(o_g(I, R5))))


def solve_b548a754(S, I):
    x1 = replace(I, EIGHT, ZERO)
    x2 = get_color_rank_t(x1, L1)
    x3 = o_g(I, R5)
    x4 = merge_f(x3)
    x5 = backdrop(x4)
    x6 = fill(I, x2, x5)
    x7 = replace(x1, x2, ZERO)
    x8 = get_color_rank_t(x7, L1)
    x9 = box(x4)
    O = fill(x6, x8, x9)
    return O
