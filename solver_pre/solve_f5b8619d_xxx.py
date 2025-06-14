def solve_f5b8619d_one(S, I):
    return vconcat(hconcat(underfill(I, EIGHT, mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1)))), underfill(I, EIGHT, mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1))))), hconcat(underfill(I, EIGHT, mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1)))), underfill(I, EIGHT, mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1))))))


def solve_f5b8619d(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = f_ofcolor(I, x1)
    if x == 2:
        return x2
    x3 = mapply(vfrontier, x2)
    if x == 3:
        return x3
    x4 = underfill(I, EIGHT, x3)
    if x == 4:
        return x4
    x5 = hconcat(x4, x4)
    if x == 5:
        return x5
    O = vconcat(x5, x5)
    return O
