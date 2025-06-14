def solve_ba97ae07_one(S, I):
    return fill(I, get_common_rank_t(apply(color, totuple(o_g(I, R5))), F0), backdrop(f_ofcolor(I, get_common_rank_t(apply(color, totuple(o_g(I, R5))), F0))))


def solve_ba97ae07(S, I, x=0):
    x1 = o_g(I, R5)
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
    x5 = f_ofcolor(I, x4)
    if x == 5:
        return x5
    x6 = backdrop(x5)
    if x == 6:
        return x6
    O = fill(I, x4, x6)
    return O
