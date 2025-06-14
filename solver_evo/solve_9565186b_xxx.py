def solve_9565186b_one(S, I):
    return paint(canvas(c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), shape_t(I)), get_arg_rank_f(o_g(I, R4), size, F0))


def solve_9565186b(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = shape_t(I)
    if x == 4:
        return x4
    x5 = canvas(x3, x4)
    if x == 5:
        return x5
    x6 = o_g(I, R4)
    if x == 6:
        return x6
    x7 = get_arg_rank_f(x6, size, F0)
    if x == 7:
        return x7
    O = paint(x5, x7)
    return O
