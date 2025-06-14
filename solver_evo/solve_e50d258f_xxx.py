def solve_e50d258f_one(S, I):
    return subgrid(get_arg_rank_f(o_g(vconcat(I, canvas(c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), astuple(NINE, width_t(I)))), R1), rbind(colorcount_f, RED), F0), I)


def solve_e50d258f(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = width_t(I)
    if x == 4:
        return x4
    x5 = astuple(NINE, x4)
    if x == 5:
        return x5
    x6 = canvas(x3, x5)
    if x == 6:
        return x6
    x7 = vconcat(I, x6)
    if x == 7:
        return x7
    x8 = o_g(x7, R1)
    if x == 8:
        return x8
    x9 = rbind(colorcount_f, RED)
    if x == 9:
        return x9
    x10 = get_arg_rank_f(x8, x9, F0)
    if x == 10:
        return x10
    O = subgrid(x10, I)
    return O
