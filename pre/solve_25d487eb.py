def solve_25d487eb_one(S, I):
    return underfill(I, get_color_rank_t(I, L1), shoot(center(f_ofcolor(I, get_color_rank_t(I, L1))), subtract(center(merge_f(o_g(I, R5))), center(f_ofcolor(I, get_color_rank_t(I, L1))))))


def solve_25d487eb(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = f_ofcolor(I, x1)
    x3 = center(x2)
    x4 = o_g(I, R5)
    x5 = merge_f(x4)
    x6 = center(x5)
    x7 = subtract(x6, x3)
    x8 = shoot(x3, x7)
    O = underfill(I, x1, x8)
    return O
