def solve_ea32f347_one(S, I):
    return fill(fill(replace(I, FIVE, FOUR), ONE, get_arg_rank_f(o_g(I, R5), size, F0)), TWO, get_arg_rank_f(o_g(I, R5), size, L1))


def solve_ea32f347(S, I):
    x1 = replace(I, FIVE, FOUR)
    x2 = o_g(I, R5)
    x3 = get_arg_rank_f(x2, size, F0)
    x4 = fill(x1, ONE, x3)
    x5 = get_arg_rank_f(x2, size, L1)
    O = fill(x4, TWO, x5)
    return O
