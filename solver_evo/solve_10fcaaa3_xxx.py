def solve_10fcaaa3_one(S, I):
    return underfill(vconcat(hconcat(I, I), hconcat(I, I)), c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(ineighbors, f_ofcolor(vconcat(hconcat(I, I), hconcat(I, I)), get_color_rank_t(I, L1))))


def solve_10fcaaa3(S, I):
    x1 = hconcat(I, I)
    x2 = vconcat(x1, x1)
    x3 = identity(p_g)
    x4 = rbind(get_nth_t, F0)
    x5 = c_zo_n(S, x3, x4)
    x6 = get_color_rank_t(I, L1)
    x7 = f_ofcolor(x2, x6)
    x8 = mapply(ineighbors, x7)
    O = underfill(x2, x5, x8)
    return O
