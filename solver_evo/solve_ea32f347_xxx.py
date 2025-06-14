def solve_ea32f347_one(S, I):
    return fill(fill(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F2))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), get_arg_rank_f(o_g(I, R5), size, F0)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), get_arg_rank_f(o_g(I, R5), size, L1))


def solve_ea32f347(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_iz_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = rbind(get_nth_t, F2)
    if x == 4:
        return x4
    x5 = c_zo_n(S, x1, x4)
    if x == 5:
        return x5
    x6 = replace(I, x3, x5)
    if x == 6:
        return x6
    x7 = c_zo_n(S, x1, x2)
    if x == 7:
        return x7
    x8 = o_g(I, R5)
    if x == 8:
        return x8
    x9 = get_arg_rank_f(x8, size, F0)
    if x == 9:
        return x9
    x10 = fill(x6, x7, x9)
    if x == 10:
        return x10
    x11 = rbind(get_nth_t, F1)
    if x == 11:
        return x11
    x12 = c_zo_n(S, x1, x11)
    if x == 12:
        return x12
    x13 = get_arg_rank_f(x8, size, L1)
    if x == 13:
        return x13
    O = fill(x10, x12, x13)
    return O
