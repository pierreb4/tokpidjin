def solve_0962bcdd_one(S, I):
    return fill(fill(I, get_color_rank_t(replace(I, ZERO, get_color_rank_t(I, L1)), L1), mapply(dneighbors, f_ofcolor(I, get_color_rank_t(replace(I, ZERO, get_color_rank_t(I, L1)), L1)))), get_color_rank_t(I, L1), mapply(fork(combine, fork(connect, rbind(corner, R0), rbind(corner, R3)), fork(connect, rbind(corner, R2), rbind(corner, R1))), o_g(fill(I, get_color_rank_t(replace(I, ZERO, get_color_rank_t(I, L1)), L1), mapply(dneighbors, f_ofcolor(I, get_color_rank_t(replace(I, ZERO, get_color_rank_t(I, L1)), L1)))), R3)))


def solve_0962bcdd(S, I, x=0):
    x1 = get_color_rank_t(I, L1)
    if x == 1:
        return x1
    x2 = replace(I, ZERO, x1)
    if x == 2:
        return x2
    x3 = get_color_rank_t(x2, L1)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, x3)
    if x == 4:
        return x4
    x5 = mapply(dneighbors, x4)
    if x == 5:
        return x5
    x6 = fill(I, x3, x5)
    if x == 6:
        return x6
    x7 = rbind(corner, R0)
    if x == 7:
        return x7
    x8 = rbind(corner, R3)
    if x == 8:
        return x8
    x9 = fork(connect, x7, x8)
    if x == 9:
        return x9
    x10 = rbind(corner, R2)
    if x == 10:
        return x10
    x11 = rbind(corner, R1)
    if x == 11:
        return x11
    x12 = fork(connect, x10, x11)
    if x == 12:
        return x12
    x13 = fork(combine, x9, x12)
    if x == 13:
        return x13
    x14 = o_g(x6, R3)
    if x == 14:
        return x14
    x15 = mapply(x13, x14)
    if x == 15:
        return x15
    O = fill(x6, x1, x15)
    return O
