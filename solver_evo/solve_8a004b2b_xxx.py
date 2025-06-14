def solve_8a004b2b_one(S, I):
    return paint(subgrid(f_ofcolor(I, YELLOW), I), shift(upscale_f(normalize_o(get_arg_rank_f(o_g(I, R3), rbind(col_row, R0), F0)), divide(width_f(merge_f(o_g(replace(subgrid(f_ofcolor(I, YELLOW), I), YELLOW, BLACK), R5))), width_f(get_arg_rank_f(o_g(I, R3), rbind(col_row, R0), F0)))), corner(merge_f(o_g(replace(subgrid(f_ofcolor(I, YELLOW), I), YELLOW, BLACK), R5)), R0)))


def solve_8a004b2b(S, I, x=0):
    x1 = f_ofcolor(I, YELLOW)
    if x == 1:
        return x1
    x2 = subgrid(x1, I)
    if x == 2:
        return x2
    x3 = o_g(I, R3)
    if x == 3:
        return x3
    x4 = rbind(col_row, R0)
    if x == 4:
        return x4
    x5 = get_arg_rank_f(x3, x4, F0)
    if x == 5:
        return x5
    x6 = normalize_o(x5)
    if x == 6:
        return x6
    x7 = replace(x2, YELLOW, BLACK)
    if x == 7:
        return x7
    x8 = o_g(x7, R5)
    if x == 8:
        return x8
    x9 = merge_f(x8)
    if x == 9:
        return x9
    x10 = width_f(x9)
    if x == 10:
        return x10
    x11 = width_f(x5)
    if x == 11:
        return x11
    x12 = divide(x10, x11)
    if x == 12:
        return x12
    x13 = upscale_f(x6, x12)
    if x == 13:
        return x13
    x14 = corner(x9, R0)
    if x == 14:
        return x14
    x15 = shift(x13, x14)
    if x == 15:
        return x15
    O = paint(x2, x15)
    return O
