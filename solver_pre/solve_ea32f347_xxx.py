def solve_ea32f347_one(S, I):
    return fill(fill(replace(I, FIVE, FOUR), ONE, get_arg_rank_f(o_g(I, R5), size, F0)), TWO, get_arg_rank_f(o_g(I, R5), size, L1))


def solve_ea32f347(S, I, x=0):
    x1 = replace(I, FIVE, FOUR)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x2, size, F0)
    if x == 3:
        return x3
    x4 = fill(x1, ONE, x3)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x2, size, L1)
    if x == 5:
        return x5
    O = fill(x4, TWO, x5)
    return O
