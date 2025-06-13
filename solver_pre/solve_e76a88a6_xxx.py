def solve_e76a88a6_one(S, I):
    return paint(I, mapply(lbind(shift, normalize(get_arg_rank_f(o_g(I, R1), numcolors_f, F0))), apply(rbind(corner, R0), remove_f(get_arg_rank_f(o_g(I, R1), numcolors_f, F0), o_g(I, R1)))))


def solve_e76a88a6(S, I):
    x1 = o_g(I, R1)
    x2 = get_arg_rank_f(x1, numcolors_f, F0)
    x3 = normalize(x2)
    x4 = lbind(shift, x3)
    x5 = rbind(corner, R0)
    x6 = remove_f(x2, x1)
    x7 = apply(x5, x6)
    x8 = mapply(x4, x7)
    O = paint(I, x8)
    return O
