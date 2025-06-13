def solve_23b5c85d_one(S, I):
    return subgrid(f_ofcolor(I, get_color_rank_t(I, L1)), I)


def solve_23b5c85d(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = f_ofcolor(I, x1)
    O = subgrid(x2, I)
    return O
