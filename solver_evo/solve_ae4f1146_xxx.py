def solve_ae4f1146_one(S, I):
    return subgrid(get_arg_rank_f(o_g(I, R1), rbind(colorcount_f, BLUE), F0), I)


def solve_ae4f1146(S, I, x=0):
    x1 = o_g(I, R1)
    if x == 1:
        return x1
    x2 = rbind(colorcount_f, BLUE)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x1, x2, F0)
    if x == 3:
        return x3
    O = subgrid(x3, I)
    return O
