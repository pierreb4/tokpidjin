def solve_f5b8619d_one(S, I):
    return vconcat(hconcat(underfill(I, EIGHT, mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1)))), underfill(I, EIGHT, mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1))))), hconcat(underfill(I, EIGHT, mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1)))), underfill(I, EIGHT, mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1))))))


def solve_f5b8619d(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = f_ofcolor(I, x1)
    x3 = mapply(vfrontier, x2)
    x4 = underfill(I, EIGHT, x3)
    x5 = hconcat(x4, x4)
    O = vconcat(x5, x5)
    return O
