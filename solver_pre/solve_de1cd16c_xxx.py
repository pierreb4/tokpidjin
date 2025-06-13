def solve_de1cd16c_one(S, I):
    return canvas(get_color_rank_t(get_arg_rank_f(apply(rbind(subgrid, I), difference(o_g(I, R4), sizefilter(o_g(I, R4), ONE))), rbind(colorcount_t, get_color_rank_t(I, L1)), F0), F0), UNITY)


def solve_de1cd16c(S, I):
    x1 = rbind(subgrid, I)
    x2 = o_g(I, R4)
    x3 = sizefilter(x2, ONE)
    x4 = difference(x2, x3)
    x5 = apply(x1, x4)
    x6 = get_color_rank_t(I, L1)
    x7 = rbind(colorcount_t, x6)
    x8 = get_arg_rank_f(x5, x7, F0)
    x9 = get_color_rank_t(x8, F0)
    O = canvas(x9, UNITY)
    return O
