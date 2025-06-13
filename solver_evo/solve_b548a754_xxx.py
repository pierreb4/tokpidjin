def solve_b548a754_one(S, I):
    return fill(fill(I, get_color_rank_t(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), L1), backdrop(merge_f(o_g(I, R5)))), get_color_rank_t(replace(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), get_color_rank_t(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), L1), BLACK), L1), box(merge_f(o_g(I, R5))))


def solve_b548a754(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = replace(I, x3, BLACK)
    x5 = get_color_rank_t(x4, L1)
    x6 = o_g(I, R5)
    x7 = merge_f(x6)
    x8 = backdrop(x7)
    x9 = fill(I, x5, x8)
    x10 = replace(x4, x5, BLACK)
    x11 = get_color_rank_t(x10, L1)
    x12 = box(x7)
    O = fill(x9, x11, x12)
    return O
