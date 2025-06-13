def solve_6cdd2623_one(S, I):
    return fill(cover(I, merge_f(fgpartition(I))), get_color_rank_t(I, L1), mfilter_f(prapply(connect, f_ofcolor(I, get_color_rank_t(I, L1)), f_ofcolor(I, get_color_rank_t(I, L1))), fork(both, fork(either, hline_i, vline_i), chain(positive, size, rbind(difference, box(merge_f(fgpartition(I))))))))


def solve_6cdd2623(S, I):
    x1 = fgpartition(I)
    x2 = merge_f(x1)
    x3 = cover(I, x2)
    x4 = get_color_rank_t(I, L1)
    x5 = f_ofcolor(I, x4)
    x6 = prapply(connect, x5, x5)
    x7 = fork(either, hline_i, vline_i)
    x8 = box(x2)
    x9 = rbind(difference, x8)
    x10 = chain(positive, size, x9)
    x11 = fork(both, x7, x10)
    x12 = mfilter_f(x6, x11)
    O = fill(x3, x4, x12)
    return O
