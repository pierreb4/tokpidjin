def solve_10fcaaa3_one(S, I):
    return underfill(vconcat(hconcat(I, I), hconcat(I, I)), EIGHT, mapply(ineighbors, f_ofcolor(vconcat(hconcat(I, I), hconcat(I, I)), get_color_rank_t(I, L1))))


def solve_10fcaaa3(S, I, x=0):
    x1 = hconcat(I, I)
    if x == 1:
        return x1
    x2 = vconcat(x1, x1)
    if x == 2:
        return x2
    x3 = get_color_rank_t(I, L1)
    if x == 3:
        return x3
    x4 = f_ofcolor(x2, x3)
    if x == 4:
        return x4
    x5 = mapply(ineighbors, x4)
    if x == 5:
        return x5
    O = underfill(x2, EIGHT, x5)
    return O
