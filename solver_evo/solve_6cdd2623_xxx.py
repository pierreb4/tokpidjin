def solve_6cdd2623_one(S, I):
    return fill(cover(I, merge_f(fgpartition(I))), get_color_rank_t(I, L1), mfilter_f(prapply(connect, f_ofcolor(I, get_color_rank_t(I, L1)), f_ofcolor(I, get_color_rank_t(I, L1))), fork(both, fork(either, hline_i, vline_i), chain(positive, size, rbind(difference, box(merge_f(fgpartition(I))))))))


def solve_6cdd2623(S, I, x=0):
    x1 = fgpartition(I)
    if x == 1:
        return x1
    x2 = merge_f(x1)
    if x == 2:
        return x2
    x3 = cover(I, x2)
    if x == 3:
        return x3
    x4 = get_color_rank_t(I, L1)
    if x == 4:
        return x4
    x5 = f_ofcolor(I, x4)
    if x == 5:
        return x5
    x6 = prapply(connect, x5, x5)
    if x == 6:
        return x6
    x7 = fork(either, hline_i, vline_i)
    if x == 7:
        return x7
    x8 = box(x2)
    if x == 8:
        return x8
    x9 = rbind(difference, x8)
    if x == 9:
        return x9
    x10 = chain(positive, size, x9)
    if x == 10:
        return x10
    x11 = fork(both, x7, x10)
    if x == 11:
        return x11
    x12 = mfilter_f(x6, x11)
    if x == 12:
        return x12
    O = fill(x3, x4, x12)
    return O
