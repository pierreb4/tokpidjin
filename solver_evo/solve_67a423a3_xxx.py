def solve_67a423a3_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), neighbors(get_nth_f(delta(merge_f(colorfilter(o_g(I, R5), get_color_rank_t(I, L1)))), F0)))


def solve_67a423a3(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R5)
    x5 = get_color_rank_t(I, L1)
    x6 = colorfilter(x4, x5)
    x7 = merge_f(x6)
    x8 = delta(x7)
    x9 = get_nth_f(x8, F0)
    x10 = neighbors(x9)
    O = fill(I, x3, x10)
    return O
