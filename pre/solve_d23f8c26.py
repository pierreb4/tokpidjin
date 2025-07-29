def solve_d23f8c26_one(S, I):
    return fill(I, ZERO, sfilter_f(asindices(I), compose(flip, matcher(rbind(get_nth_f, L1), halve(width_t(I))))))


def solve_d23f8c26(S, I):
    x1 = asindices(I)
    x2 = rbind(get_nth_f, L1)
    x3 = width_t(I)
    x4 = halve(x3)
    x5 = matcher(x2, x4)
    x6 = compose(flip, x5)
    x7 = sfilter_f(x1, x6)
    O = fill(I, ZERO, x7)
    return O
