def solve_928ad970_one(S, I):
    return fill(I, get_color_rank_t(trim(subgrid(f_ofcolor(I, FIVE), I)), L1), inbox(f_ofcolor(I, FIVE)))


def solve_928ad970(S, I):
    x1 = f_ofcolor(I, FIVE)
    x2 = subgrid(x1, I)
    x3 = trim(x2)
    x4 = get_color_rank_t(x3, L1)
    x5 = inbox(x1)
    O = fill(I, x4, x5)
    return O
