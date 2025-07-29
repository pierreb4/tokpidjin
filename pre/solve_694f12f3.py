def solve_694f12f3_one(S, I):
    return fill(fill(I, ONE, compose(backdrop, inbox)(get_arg_rank_f(colorfilter(o_g(I, R4), FOUR), size, L1))), TWO, compose(backdrop, inbox)(get_arg_rank_f(colorfilter(o_g(I, R4), FOUR), size, F0)))


def solve_694f12f3(S, I):
    x1 = compose(backdrop, inbox)
    x2 = o_g(I, R4)
    x3 = colorfilter(x2, FOUR)
    x4 = get_arg_rank_f(x3, size, L1)
    x5 = x1(x4)
    x6 = fill(I, ONE, x5)
    x7 = get_arg_rank_f(x3, size, F0)
    x8 = x1(x7)
    O = fill(x6, TWO, x8)
    return O
