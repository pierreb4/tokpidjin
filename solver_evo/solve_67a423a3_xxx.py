def solve_67a423a3_one(S, I):
    return fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), neighbors(get_nth_f(delta(merge_f(colorfilter(o_g(I, R5), get_color_rank_t(I, L1)))), F0)))


def solve_67a423a3(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = o_g(I, R5)
    if x == 4:
        return x4
    x5 = get_color_rank_t(I, L1)
    if x == 5:
        return x5
    x6 = colorfilter(x4, x5)
    if x == 6:
        return x6
    x7 = merge_f(x6)
    if x == 7:
        return x7
    x8 = delta(x7)
    if x == 8:
        return x8
    x9 = get_nth_f(x8, F0)
    if x == 9:
        return x9
    x10 = neighbors(x9)
    if x == 10:
        return x10
    O = fill(I, x3, x10)
    return O
