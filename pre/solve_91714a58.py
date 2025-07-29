def solve_91714a58_one(S, I):
    return fill(paint(canvas(ZERO, shape_t(I)), get_arg_rank_f(o_g(I, R5), size, F0)), ZERO, sfilter_f(asindices(I), compose(lbind(greater, THREE), chain(rbind(colorcount_f, get_color_rank_f(get_arg_rank_f(o_g(I, R5), size, F0), F0)), rbind(toobject, paint(canvas(ZERO, shape_t(I)), get_arg_rank_f(o_g(I, R5), size, F0))), neighbors))))


def solve_91714a58(S, I):
    x1 = shape_t(I)
    x2 = canvas(ZERO, x1)
    x3 = o_g(I, R5)
    x4 = get_arg_rank_f(x3, size, F0)
    x5 = paint(x2, x4)
    x6 = asindices(I)
    x7 = lbind(greater, THREE)
    x8 = get_color_rank_f(x4, F0)
    x9 = rbind(colorcount_f, x8)
    x10 = rbind(toobject, x5)
    x11 = chain(x9, x10, neighbors)
    x12 = compose(x7, x11)
    x13 = sfilter_f(x6, x12)
    O = fill(x5, ZERO, x13)
    return O
