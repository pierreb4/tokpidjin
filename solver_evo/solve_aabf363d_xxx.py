def solve_aabf363d_one(S, I):
    return replace(replace(I, get_color_rank_t(I, L1), BLACK), get_color_rank_t(replace(I, get_color_rank_t(I, L1), BLACK), L1), get_color_rank_t(I, L1))


def solve_aabf363d(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = replace(I, x1, BLACK)
    x3 = get_color_rank_t(x2, L1)
    O = replace(x2, x3, x1)
    return O
