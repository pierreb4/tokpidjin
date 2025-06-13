def solve_91714a58_one(S, I):
    return fill(paint(canvas(BLACK, shape_t(I)), get_arg_rank_f(o_g(I, R5), size, F0)), BLACK, sfilter_f(asindices(I), compose(lbind(greater, c_iz_n(S, identity(p_g), rbind(get_nth_t, F1))), chain(rbind(colorcount_f, get_color_rank_f(get_arg_rank_f(o_g(I, R5), size, F0), F0)), rbind(toobject, paint(canvas(BLACK, shape_t(I)), get_arg_rank_f(o_g(I, R5), size, F0))), neighbors))))


def solve_91714a58(S, I):
    x1 = shape_t(I)
    x2 = canvas(BLACK, x1)
    x3 = o_g(I, R5)
    x4 = get_arg_rank_f(x3, size, F0)
    x5 = paint(x2, x4)
    x6 = asindices(I)
    x7 = identity(p_g)
    x8 = rbind(get_nth_t, F1)
    x9 = c_iz_n(S, x7, x8)
    x10 = lbind(greater, x9)
    x11 = get_color_rank_f(x4, F0)
    x12 = rbind(colorcount_f, x11)
    x13 = rbind(toobject, x5)
    x14 = chain(x12, x13, neighbors)
    x15 = compose(x10, x14)
    x16 = sfilter_f(x6, x15)
    O = fill(x5, BLACK, x16)
    return O
