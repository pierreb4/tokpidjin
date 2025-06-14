def solve_de1cd16c_one(S, I):
    return canvas(get_color_rank_t(get_arg_rank_f(apply(rbind(subgrid, I), difference(o_g(I, R4), sizefilter(o_g(I, R4), ONE))), rbind(colorcount_t, get_color_rank_t(I, L1)), F0), F0), UNITY)


def solve_de1cd16c(S, I, x=0):
    x1 = rbind(subgrid, I)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = sizefilter(x2, ONE)
    if x == 3:
        return x3
    x4 = difference(x2, x3)
    if x == 4:
        return x4
    x5 = apply(x1, x4)
    if x == 5:
        return x5
    x6 = get_color_rank_t(I, L1)
    if x == 6:
        return x6
    x7 = rbind(colorcount_t, x6)
    if x == 7:
        return x7
    x8 = get_arg_rank_f(x5, x7, F0)
    if x == 8:
        return x8
    x9 = get_color_rank_t(x8, F0)
    if x == 9:
        return x9
    O = canvas(x9, UNITY)
    return O
