def solve_39a8645d_one(S, I):
    return subgrid(extract(o_g(I, R7), matcher(color, get_common_rank_t(apply(color, totuple(o_g(I, R7))), F0))), I)


def solve_39a8645d(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = totuple(x1)
    if x == 2:
        return x2
    x3 = apply(color, x2)
    if x == 3:
        return x3
    x4 = get_common_rank_t(x3, F0)
    if x == 4:
        return x4
    x5 = matcher(color, x4)
    if x == 5:
        return x5
    x6 = extract(x1, x5)
    if x == 6:
        return x6
    O = subgrid(x6, I)
    return O
