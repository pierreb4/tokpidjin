def solve_8a004b2b_one(S, I):
    return paint(subgrid(f_ofcolor(I, FOUR), I), shift(upscale_f(normalize_o(get_arg_rank_f(o_g(I, R3), rbind(col_row, R0), F0)), divide(width_f(merge_f(o_g(replace(subgrid(f_ofcolor(I, FOUR), I), FOUR, ZERO), R5))), width_f(get_arg_rank_f(o_g(I, R3), rbind(col_row, R0), F0)))), corner(merge_f(o_g(replace(subgrid(f_ofcolor(I, FOUR), I), FOUR, ZERO), R5)), R0)))


def solve_8a004b2b(S, I):
    x1 = f_ofcolor(I, FOUR)
    x2 = subgrid(x1, I)
    x3 = o_g(I, R3)
    x4 = rbind(col_row, R0)
    x5 = get_arg_rank_f(x3, x4, F0)
    x6 = normalize_o(x5)
    x7 = replace(x2, FOUR, ZERO)
    x8 = o_g(x7, R5)
    x9 = merge_f(x8)
    x10 = width_f(x9)
    x11 = width_f(x5)
    x12 = divide(x10, x11)
    x13 = upscale_f(x6, x12)
    x14 = corner(x9, R0)
    x15 = shift(x13, x14)
    O = paint(x2, x15)
    return O
