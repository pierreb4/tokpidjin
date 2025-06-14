def solve_868de0fa_one(S, I):
    return fill(fill(I, TWO, merge_f(sfilter_f(sfilter_f(o_g(I, R4), square_f), compose(even, height_f)))), SEVEN, merge_f(difference(sfilter_f(o_g(I, R4), square_f), sfilter_f(sfilter_f(o_g(I, R4), square_f), compose(even, height_f)))))


def solve_868de0fa(S, I, x=0):
    x1 = o_g(I, R4)
    if x == 1:
        return x1
    x2 = sfilter_f(x1, square_f)
    if x == 2:
        return x2
    x3 = compose(even, height_f)
    if x == 3:
        return x3
    x4 = sfilter_f(x2, x3)
    if x == 4:
        return x4
    x5 = merge_f(x4)
    if x == 5:
        return x5
    x6 = fill(I, TWO, x5)
    if x == 6:
        return x6
    x7 = difference(x2, x4)
    if x == 7:
        return x7
    x8 = merge_f(x7)
    if x == 8:
        return x8
    O = fill(x6, SEVEN, x8)
    return O
