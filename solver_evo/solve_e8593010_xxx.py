def solve_e8593010_one(S, I):
    return replace(fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F2)), merge_f(sizefilter(o_g(I, R5), ONE))), c_zo_n(S, identity(p_g), rbind(get_nth_t, F1)), merge_f(sizefilter(o_g(I, R5), TWO))), BLACK, BLUE)


def solve_e8593010(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F2)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R5)
    if x == 4:
        return x4
    x5 = sizefilter(x4, ONE)
    if x == 5:
        return x5
    x6 = merge_f(x5)
    if x == 6:
        return x6
    x7 = fill(I, x3, x6)
    if x == 7:
        return x7
    x8 = rbind(get_nth_t, F1)
    if x == 8:
        return x8
    x9 = c_zo_n(S, x1, x8)
    if x == 9:
        return x9
    x10 = sizefilter(x4, TWO)
    if x == 10:
        return x10
    x11 = merge_f(x10)
    if x == 11:
        return x11
    x12 = fill(x7, x9, x11)
    if x == 12:
        return x12
    O = replace(x12, BLACK, BLUE)
    return O
