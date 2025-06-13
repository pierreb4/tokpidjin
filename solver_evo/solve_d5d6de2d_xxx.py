def solve_d5d6de2d_one(S, I):
    return fill(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(compose(backdrop, inbox), difference(o_g(I, R5), sfilter_f(o_g(I, R5), square_f))))


def solve_d5d6de2d(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_iz_n(S, x1, x2)
    x4 = replace(I, x3, BLACK)
    x5 = c_zo_n(S, x1, x2)
    x6 = compose(backdrop, inbox)
    x7 = o_g(I, R5)
    x8 = sfilter_f(x7, square_f)
    x9 = difference(x7, x8)
    x10 = mapply(x6, x9)
    O = fill(x4, x5, x10)
    return O
