def solve_d5d6de2d_one(S, I):
    return fill(replace(I, c_iz_n(S, identity(p_g), rbind(get_nth_t, F0)), BLACK), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(compose(backdrop, inbox), difference(o_g(I, R5), sfilter_f(o_g(I, R5), square_f))))


def solve_d5d6de2d(S, I, x=0):
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
    x6 = compose(backdrop, inbox)
    if x == 6:
        return x6
    x7 = o_g(I, R5)
    if x == 7:
        return x7
    x8 = sfilter_f(x7, square_f)
    if x == 8:
        return x8
    x9 = difference(x7, x8)
    if x == 9:
        return x9
    x10 = mapply(x6, x9)
    if x == 10:
        return x10
    O = fill(x4, x5, x10)
    return O
