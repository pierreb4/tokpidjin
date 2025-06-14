def solve_91714a58_one(S, I):
    return fill(paint(canvas(BLACK, shape_t(I)), get_arg_rank_f(o_g(I, R5), size, F0)), BLACK, sfilter_f(asindices(I), compose(lbind(greater, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1))), chain(rbind(colorcount_f, get_color_rank_f(get_arg_rank_f(o_g(I, R5), size, F0), F0)), rbind(toobject, paint(canvas(BLACK, shape_t(I)), get_arg_rank_f(o_g(I, R5), size, F0))), neighbors))))


def solve_91714a58(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = canvas(BLACK, x1)
    if x == 2:
        return x2
    x3 = o_g(I, R5)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, F0)
    if x == 4:
        return x4
    x5 = paint(x2, x4)
    if x == 5:
        return x5
    x6 = asindices(I)
    if x == 6:
        return x6
    x7 = identity(p_g)
    if x == 7:
        return x7
    x8 = rbind(get_nth_t, F1)
    if x == 8:
        return x8
    x9 = c_iz_n(S, x7, x8)
    if x == 9:
        return x9
    x10 = lbind(greater, x9)
    if x == 10:
        return x10
    x11 = get_color_rank_f(x4, F0)
    if x == 11:
        return x11
    x12 = rbind(colorcount_f, x11)
    if x == 12:
        return x12
    x13 = rbind(toobject, x5)
    if x == 13:
        return x13
    x14 = chain(x12, x13, neighbors)
    if x == 14:
        return x14
    x15 = compose(x10, x14)
    if x == 15:
        return x15
    x16 = sfilter_f(x6, x15)
    if x == 16:
        return x16
    O = fill(x5, BLACK, x16)
    return O
