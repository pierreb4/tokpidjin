def solve_b548a754_one(S, I):
    return fill(fill(I, get_color_rank_t(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), L1), backdrop(merge_f(o_g(I, R5)))), get_color_rank_t(replace(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), get_color_rank_t(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), L1), BLACK), L1), box(merge_f(o_g(I, R5))))


def solve_b548a754(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = replace(I, x3, BLACK)
    if x == 4:
        return x4
    x5 = get_color_rank_t(x4, L1)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = merge_f(x6)
    if x == 7:
        return x7
    x8 = backdrop(x7)
    if x == 8:
        return x8
    x9 = fill(I, x5, x8)
    if x == 9:
        return x9
    x10 = replace(x4, x5, BLACK)
    if x == 10:
        return x10
    x11 = get_color_rank_t(x10, L1)
    if x == 11:
        return x11
    x12 = box(x7)
    if x == 12:
        return x12
    O = fill(x9, x11, x12)
    return O
