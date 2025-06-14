def solve_5582e5ca_one(S, I):
    return canvas(get_color_rank_t(I, F0), THREE_BY_THREE)


def solve_5582e5ca(S, I, x=0):
    x1 = get_color_rank_t(I, F0)
    if x == 1:
        return x1
    O = canvas(x1, THREE_BY_THREE)
    return O
