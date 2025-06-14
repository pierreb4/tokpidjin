def solve_e76a88a6_one(S, I):
    return paint(I, mapply(lbind(shift, normalize(get_arg_rank_f(o_g(I, R1), numcolors_f, F0))), apply(rbind(corner, R0), remove_f(get_arg_rank_f(o_g(I, R1), numcolors_f, F0), o_g(I, R1)))))


def solve_e76a88a6(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, numcolors_f, F0)
    if x == 2:
        return x2
    x3 = normalize(x2)
    if x == 3:
        return x3
    x4 = lbind(shift, x3)
    if x == 4:
        return x4
    x5 = rbind(corner, R0)
    if x == 5:
        return x5
    x6 = remove_f(x2, x1)
    if x == 6:
        return x6
    x7 = apply(x5, x6)
    if x == 7:
        return x7
    x8 = mapply(x4, x7)
    if x == 8:
        return x8
    O = paint(I, x8)
    return O
