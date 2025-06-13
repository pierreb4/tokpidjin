def solve_e8593010_one(S, I):
    return replace(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), merge_f(sizefilter(o_g(I, R5), ONE))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), merge_f(sizefilter(o_g(I, R5), TWO))), BLACK, BLUE)


def solve_e8593010(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F2)
    x3 = c_zo_n(S, x1, x2)
    x4 = o_g(I, R5)
    x5 = sizefilter(x4, ONE)
    x6 = merge_f(x5)
    x7 = fill(I, x3, x6)
    x8 = rbind(get_nth_t, F1)
    x9 = c_zo_n(S, x1, x8)
    x10 = sizefilter(x4, TWO)
    x11 = merge_f(x10)
    x12 = fill(x7, x9, x11)
    O = replace(x12, BLACK, BLUE)
    return O
