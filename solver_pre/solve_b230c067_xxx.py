def solve_b230c067_one(S, I):
    return fill(replace(I, EIGHT, ONE), TWO, extract(o_g(I, R7), matcher(normalize, get_common_rank_t(apply(normalize, totuple(o_g(I, R7))), L1))))


def solve_b230c067(S, I, x=0):
    x1 = replace(I, EIGHT, ONE)
    if x == 1:
        return x1
    x2 = o_g(I, R7)
    if x == 2:
        return x2
    x3 = totuple(x2)
    if x == 3:
        return x3
    x4 = apply(normalize, x3)
    if x == 4:
        return x4
    x5 = get_common_rank_t(x4, L1)
    if x == 5:
        return x5
    x6 = matcher(normalize, x5)
    if x == 6:
        return x6
    x7 = extract(x2, x6)
    if x == 7:
        return x7
    O = fill(x1, TWO, x7)
    return O
