def solve_f5b8619d_one(S, I):
    return vconcat(hconcat(underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1)))), underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1))))), hconcat(underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1)))), underfill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mapply(vfrontier, f_ofcolor(I, get_color_rank_t(I, L1))))))


def solve_f5b8619d(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = get_color_rank_t(I, L1)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, x4)
    if x == 5:
        return x5
    x6 = mapply(vfrontier, x5)
    if x == 6:
        return x6
    x7 = underfill(I, x3, x6)
    if x == 7:
        return x7
    x8 = hconcat(x7, x7)
    if x == 8:
        return x8
    O = vconcat(x8, x8)
    return O
