def solve_2dc579da_one(S, I):
    return get_arg_rank_t(mapply(rbind(hsplit, TWO), vsplit(I, TWO)), numcolors_t, F0)


def solve_2dc579da(S, I):
    x1 = rbind(hsplit, TWO)
    x2 = vsplit(I, TWO)
    x3 = mapply(x1, x2)
    O = get_arg_rank_t(x3, numcolors_t, F0)
    return O
