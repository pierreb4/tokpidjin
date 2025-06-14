def solve_694f12f3_one(S, I):
    return fill(fill(I, ONE, compose(backdrop, inbox)(get_arg_rank_f(colorfilter(o_g(I, R4), FOUR), size, L1))), TWO, compose(backdrop, inbox)(get_arg_rank_f(colorfilter(o_g(I, R4), FOUR), size, F0)))


def solve_694f12f3(S, I, x=0):
    x1 = compose(backdrop, inbox)
    if x == 1:
        return x1
    x2 = o_g(I, R4)
    if x == 2:
        return x2
    x3 = colorfilter(x2, FOUR)
    if x == 3:
        return x3
    x4 = get_arg_rank_f(x3, size, L1)
    if x == 4:
        return x4
    x5 = x1(x4)
    if x == 5:
        return x5
    x6 = fill(I, ONE, x5)
    if x == 6:
        return x6
    x7 = get_arg_rank_f(x3, size, F0)
    if x == 7:
        return x7
    x8 = x1(x7)
    if x == 8:
        return x8
    O = fill(x6, TWO, x8)
    return O
