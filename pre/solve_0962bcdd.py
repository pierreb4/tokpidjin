def solve_0962bcdd_one(S, I):
    return fill(fill(I, get_color_rank_t(replace(I, ZERO, get_color_rank_t(I, L1)), L1), mapply(dneighbors, f_ofcolor(I, get_color_rank_t(replace(I, ZERO, get_color_rank_t(I, L1)), L1)))), get_color_rank_t(I, L1), mapply(fork(combine, fork(connect, rbind(corner, R0), rbind(corner, R3)), fork(connect, rbind(corner, R2), rbind(corner, R1))), o_g(fill(I, get_color_rank_t(replace(I, ZERO, get_color_rank_t(I, L1)), L1), mapply(dneighbors, f_ofcolor(I, get_color_rank_t(replace(I, ZERO, get_color_rank_t(I, L1)), L1)))), R3)))


def solve_0962bcdd(S, I):
    x1 = get_color_rank_t(I, L1)
    x2 = replace(I, ZERO, x1)
    x3 = get_color_rank_t(x2, L1)
    x4 = f_ofcolor(I, x3)
    x5 = mapply(dneighbors, x4)
    x6 = fill(I, x3, x5)
    x7 = rbind(corner, R0)
    x8 = rbind(corner, R3)
    x9 = fork(connect, x7, x8)
    x10 = rbind(corner, R2)
    x11 = rbind(corner, R1)
    x12 = fork(connect, x10, x11)
    x13 = fork(combine, x9, x12)
    x14 = o_g(x6, R3)
    x15 = mapply(x13, x14)
    O = fill(x6, x1, x15)
    return O
