def solve_a61f2674_one(S, I):
    return paint(replace(I, FIVE, ZERO), combine_f(recolor_o(ONE, get_arg_rank_f(o_g(I, R5), size, F0)), recolor_o(TWO, get_arg_rank_f(o_g(I, R5), size, L1))))


def solve_a61f2674(S, I, x=0):
    x1 = replace(I, FIVE, ZERO)
    if x == 1:
        return x1
    x2 = o_g(I, R5)
    if x == 2:
        return x2
    x3 = get_arg_rank_f(x2, size, F0)
    if x == 3:
        return x3
    x4 = recolor_o(ONE, x3)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x2, size, L1)
    if x == 5:
        return x5
    x6 = recolor_o(TWO, x5)
    if x == 6:
        return x6
    x7 = combine_f(x4, x6)
    if x == 7:
        return x7
    O = paint(x1, x7)
    return O
