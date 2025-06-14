def solve_a61f2674_one(S, I):
    return paint(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), combine_f(recolor_o(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), get_arg_rank_f(o_g(I, R5), size, F0)), recolor_o(c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), get_arg_rank_f(o_g(I, R5), size, L1))))


def solve_a61f2674(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = replace(I, x3, BLACK)
    if x == 4:
        return x4
    x5 = c_zo_n(S, x1, x2)
    if x == 5:
        return x5
    x6 = o_g(I, R5)
    if x == 6:
        return x6
    x7 = get_arg_rank_f(x6, size, F0)
    if x == 7:
        return x7
    x8 = recolor_o(x5, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_t, F1)
    if x == 9:
        return x9
    x10 = c_zo_n(S, x1, x9)
    if x == 10:
        return x10
    x11 = get_arg_rank_f(x6, size, L1)
    if x == 11:
        return x11
    x12 = recolor_o(x10, x11)
    if x == 12:
        return x12
    x13 = combine_f(x8, x12)
    if x == 13:
        return x13
    O = paint(x4, x13)
    return O
