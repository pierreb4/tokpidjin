def solve_a61f2674_one(S, I):
    return paint(replace(I, FIVE, ZERO), combine_f(recolor_o(ONE, get_arg_rank_f(o_g(I, R5), size, F0)), recolor_o(TWO, get_arg_rank_f(o_g(I, R5), size, L1))))


def solve_a61f2674(S, I):
    x1 = replace(I, FIVE, ZERO)
    x2 = o_g(I, R5)
    x3 = get_arg_rank_f(x2, size, F0)
    x4 = recolor_o(ONE, x3)
    x5 = get_arg_rank_f(x2, size, L1)
    x6 = recolor_o(TWO, x5)
    x7 = combine_f(x4, x6)
    O = paint(x1, x7)
    return O
