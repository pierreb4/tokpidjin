def solve_d23f8c26_one(S, I):
    return fill(I, BLACK, sfilter_f(asindices(I), compose(flip, matcher(rbind(get_nth_f, L1), halve(width_t(I))))))


def solve_d23f8c26(S, I, x=0):
    x1 = asindices(I)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = width_t(I)
    if x == 3:
        return x3
    x4 = halve(x3)
    if x == 4:
        return x4
    x5 = matcher(x2, x4)
    if x == 5:
        return x5
    x6 = compose(flip, x5)
    if x == 6:
        return x6
    x7 = sfilter_f(x1, x6)
    if x == 7:
        return x7
    O = fill(I, BLACK, x7)
    return O
