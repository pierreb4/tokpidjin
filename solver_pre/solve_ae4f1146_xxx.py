def solve_ae4f1146_one(S, I):
    return subgrid(get_arg_rank_f(o_g(I, R1), rbind(colorcount_f, ONE), F0), I)


def solve_ae4f1146(S, I):
    x1 = o_g(I, R1)
    x2 = rbind(colorcount_f, ONE)
    x3 = get_arg_rank_f(x1, x2, F0)
    O = subgrid(x3, I)
    return O
