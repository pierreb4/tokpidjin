def solve_39a8645d_one(S, I):
    return subgrid(extract(o_g(I, R7), matcher(color, get_common_rank_t(apply(color, totuple(o_g(I, R7))), F0))), I)


def solve_39a8645d(S, I):
    x1 = o_g(I, R7)
    x2 = totuple(x1)
    x3 = apply(color, x2)
    x4 = get_common_rank_t(x3, F0)
    x5 = matcher(color, x4)
    x6 = extract(x1, x5)
    O = subgrid(x6, I)
    return O
