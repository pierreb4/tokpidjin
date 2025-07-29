def solve_868de0fa_one(S, I):
    return fill(fill(I, TWO, merge_f(sfilter_f(sfilter_f(o_g(I, R4), square_f), compose(even, height_f)))), SEVEN, merge_f(difference(sfilter_f(o_g(I, R4), square_f), sfilter_f(sfilter_f(o_g(I, R4), square_f), compose(even, height_f)))))


def solve_868de0fa(S, I):
    x1 = o_g(I, R4)
    x2 = sfilter_f(x1, square_f)
    x3 = compose(even, height_f)
    x4 = sfilter_f(x2, x3)
    x5 = merge_f(x4)
    x6 = fill(I, TWO, x5)
    x7 = difference(x2, x4)
    x8 = merge_f(x7)
    O = fill(x6, SEVEN, x8)
    return O
