def solve_f5b8619d_one(S, I):
    return vconcat(hconcat(underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1)))), underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1))))), hconcat(underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1)))), underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1))))))


def solve_f5b8619d(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = get_color_rank_t(I, L1)
    x5 = f_ofcolor(I, x4)
    x6 = mapply(vfrontier, x5)
    x7 = underfill(I, x3, x6)
    x8 = hconcat(x7, x7)
    O = vconcat(x8, x8)
    return O
