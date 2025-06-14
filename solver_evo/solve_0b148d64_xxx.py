def solve_0b148d64_one(S, I):
    return subgrid(f_ofcolor(I, get_color_rank_t(I, L1)), I)


def solve_0b148d64(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    O = subgrid(x2, I)
    return O
