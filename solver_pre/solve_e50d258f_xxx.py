def solve_e50d258f_one(S, I):
    return subgrid(get_arg_rank_f(o_g(vconcat(I, canvas(ZERO, astuple(NINE, width_t(I)))), R1), rbind(colorcount_f, TWO), F0), I)


def solve_e50d258f(S, I, x=0):
    x1 = width_t(I)
    if x == 1:
        return x1
    x2 = astuple(NINE, x1)
    if x == 2:
        return x2
    x3 = canvas(ZERO, x2)
    if x == 3:
        return x3
    x4 = vconcat(I, x3)
    if x == 4:
        return x4
    x5 = o_g(x4, R1)
    if x == 5:
        return x5
    x6 = rbind(colorcount_f, TWO)
    if x == 6:
        return x6
    x7 = get_arg_rank_f(x5, x6, F0)
    if x == 7:
        return x7
    O = subgrid(x7, I)
    return O
