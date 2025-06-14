def solve_10fcaaa3_one(S, I):
    return underfill(vconcat(hconcat(I, I), hconcat(I, I)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(ineighbors, f_ofcolor(vconcat(hconcat(I, I), hconcat(I, I)), get_color_rank_t(I, L1))))


def solve_10fcaaa3(S, I, x=0):
    x1 = hconcat(I, I)
    if x == 1:
        return x1
    x2 = vconcat(x1, x1)
    if x == 2:
        return x2
    x3 = identity(p_g)
    if x == 3:
        return x3
    x4 = rbind(get_nth_t, F0)
    if x == 4:
        return x4
    x5 = c_zo_n(S, x3, x4)
    if x == 5:
        return x5
    x6 = get_color_rank_t(I, L1)
    if x == 6:
        return x6
    x7 = f_ofcolor(x2, x6)
    if x == 7:
        return x7
    x8 = mapply(ineighbors, x7)
    if x == 8:
        return x8
    O = underfill(x2, x5, x8)
    return O
