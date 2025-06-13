def solve_ea32f347_one(S, I):
    return fill(fill(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), get_arg_rank_f(o_g(I, R5), size, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), get_arg_rank_f(o_g(I, R5), size, L1))


def solve_ea32f347(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = rbind(get_nth_t, F2)
    x5 = c_zo_n(S, x1, x4)
    x6 = replace(I, x3, x5)
    x7 = c_zo_n(S, x1, x2)
    x8 = o_g(I, R5)
    x9 = get_arg_rank_f(x8, size, F0)
    x10 = fill(x6, x7, x9)
    x11 = rbind(get_nth_t, F1)
    x12 = c_zo_n(S, x1, x11)
    x13 = get_arg_rank_f(x8, size, L1)
    O = fill(x10, x12, x13)
    return O
