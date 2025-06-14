def solve_91714a58_one(S, I):
    return fill(paint(canvas(ZERO, shape_t(I)), get_arg_rank_f(o_g(I, R5), size, F0)), ZERO, sfilter_f(asindices(I), compose(lbind(greater, THREE), chain(rbind(colorcount_f, get_color_rank_f(get_arg_rank_f(o_g(I, R5), size, F0), F0)), rbind(toobject, paint(canvas(ZERO, shape_t(I)), get_arg_rank_f(o_g(I, R5), size, F0))), neighbors))))


def solve_91714a58(S, I, x=0):
    x1 = shape_t(I)
    if x == 1:
        return x1
    x2 = canvas(ZERO, x1)
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
    x7 = lbind(greater, THREE)
    if x == 7:
        return x7
    x8 = get_color_rank_f(x4, F0)
    if x == 8:
        return x8
    x9 = rbind(colorcount_f, x8)
    if x == 9:
        return x9
    x10 = rbind(toobject, x5)
    if x == 10:
        return x10
    x11 = chain(x9, x10, neighbors)
    if x == 11:
        return x11
    x12 = compose(x7, x11)
    if x == 12:
        return x12
    x13 = sfilter_f(x6, x12)
    if x == 13:
        return x13
    O = fill(x5, ZERO, x13)
    return O
