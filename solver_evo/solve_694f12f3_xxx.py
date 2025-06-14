def solve_694f12f3_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), compose(backdrop, inbox)(get_arg_rank_f(colorfilter(o_g(I, R4), YELLOW), size, L1))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), compose(backdrop, inbox)(get_arg_rank_f(colorfilter(o_g(I, R4), YELLOW), size, F0)))


def solve_694f12f3(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = compose(backdrop, inbox)
    if x == 4:
        return x4
    x5 = o_g(I, R4)
    if x == 5:
        return x5
    x6 = colorfilter(x5, YELLOW)
    if x == 6:
        return x6
    x7 = get_arg_rank_f(x6, size, L1)
    if x == 7:
        return x7
    x8 = x4(x7)
    if x == 8:
        return x8
    x9 = fill(I, x3, x8)
    if x == 9:
        return x9
    x10 = rbind(get_nth_t, F1)
    if x == 10:
        return x10
    x11 = c_zo_n(S, x1, x10)
    if x == 11:
        return x11
    x12 = get_arg_rank_f(x6, size, F0)
    if x == 12:
        return x12
    x13 = x4(x12)
    if x == 13:
        return x13
    O = fill(x9, x11, x13)
    return O
