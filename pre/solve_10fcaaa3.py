def solve_10fcaaa3_one(S, I):
    return underfill(vconcat(hconcat(I, I), hconcat(I, I)), EIGHT, mapply(ineighbors, f_ofcolor(vconcat(hconcat(I, I), hconcat(I, I)), get_color_rank_t(I, L1))))


def solve_10fcaaa3(S, I):
    x1 = hconcat(I, I)
    x2 = vconcat(x1, x1)
    x3 = get_color_rank_t(I, L1)
    x4 = f_ofcolor(x2, x3)
    x5 = mapply(ineighbors, x4)
    O = underfill(x2, EIGHT, x5)
    return O
