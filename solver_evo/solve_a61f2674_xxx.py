def solve_a61f2674_one(S, I):
    return paint(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), combine_f(recolor_o(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), get_arg_rank_f(o_g(I, R5), size, F0)), recolor_o(c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), get_arg_rank_f(o_g(I, R5), size, L1))))


def solve_a61f2674(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = replace(I, x3, BLACK)
    x5 = c_zo_n(S, x1, x2)
    x6 = o_g(I, R5)
    x7 = get_arg_rank_f(x6, size, F0)
    x8 = recolor_o(x5, x7)
    x9 = rbind(get_nth_t, F1)
    x10 = c_zo_n(S, x1, x9)
    x11 = get_arg_rank_f(x6, size, L1)
    x12 = recolor_o(x10, x11)
    x13 = combine_f(x8, x12)
    O = paint(x4, x13)
    return O
