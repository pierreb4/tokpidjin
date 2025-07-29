def solve_b230c067_one(S, I):
    return fill(replace(I, EIGHT, ONE), TWO, extract(o_g(I, R7), matcher(normalize, get_common_rank_t(apply(normalize, totuple(o_g(I, R7))), L1))))


def solve_b230c067(S, I):
    x1 = replace(I, EIGHT, ONE)
    x2 = o_g(I, R7)
    x3 = totuple(x2)
    x4 = apply(normalize, x3)
    x5 = get_common_rank_t(x4, L1)
    x6 = matcher(normalize, x5)
    x7 = extract(x2, x6)
    O = fill(x1, TWO, x7)
    return O
