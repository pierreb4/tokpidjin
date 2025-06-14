def solve_aabf363d_one(S, I):
    return replace(replace(I, get_color_rank_t(I, L1), ZERO), get_color_rank_t(replace(I, get_color_rank_t(I, L1), ZERO), L1), get_color_rank_t(I, L1))


def solve_aabf363d(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = replace(I, x1, ZERO)
    if x == 2:
        return x2
    x3 = get_color_rank_t(x2, L1)
    if x == 3:
        return x3
    O = replace(x2, x3, x1)
    return O
