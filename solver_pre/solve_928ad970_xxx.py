def solve_928ad970_one(S, I):
    return fill(I, get_color_rank_t(trim(subgrid(f_ofcolor(I, FIVE), I)), L1), inbox(f_ofcolor(I, FIVE)))


def solve_928ad970(S, I, x=0):
    x1 = f_ofcolor(I, FIVE)
    if x == 1:
        return x1
    x2 = subgrid(x1, I)
    if x == 2:
        return x2
    x3 = trim(x2)
    if x == 3:
        return x3
    x4 = get_color_rank_t(x3, L1)
    if x == 4:
        return x4
    x5 = inbox(x1)
    if x == 5:
        return x5
    O = fill(I, x4, x5)
    return O
