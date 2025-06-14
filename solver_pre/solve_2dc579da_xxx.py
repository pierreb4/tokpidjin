def solve_2dc579da_one(S, I):
    return get_arg_rank_t(mapply(rbind(hsplit, TWO), vsplit(I, TWO)), numcolors_t, F0)


def solve_2dc579da(S, I, x=0):
    x1 = rbind(hsplit, TWO)
    if x == 1:
        return x1
    x2 = vsplit(I, TWO)
    if x == 2:
        return x2
    x3 = mapply(x1, x2)
    if x == 3:
        return x3
    O = get_arg_rank_t(x3, numcolors_t, F0)
    return O
