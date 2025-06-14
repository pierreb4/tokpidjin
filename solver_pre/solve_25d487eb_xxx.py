def solve_25d487eb_one(S, I):
    return underfill(I, get_color_rank_t(I, L1), shoot(center(f_ofcolor(I, get_color_rank_t(I, L1))), subtract(center(merge_f(o_g(I, R5))), center(f_ofcolor(I, get_color_rank_t(I, L1))))))


def solve_25d487eb(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = center(x2)
    if x == 3:
        return x3
    x4 = o_g(I, R5)
    if x == 4:
        return x4
    x5 = merge_f(x4)
    if x == 5:
        return x5
    x6 = center(x5)
    if x == 6:
        return x6
    x7 = subtract(x6, x3)
    if x == 7:
        return x7
    x8 = shoot(x3, x7)
    if x == 8:
        return x8
    O = underfill(I, x1, x8)
    return O
