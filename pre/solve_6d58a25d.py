def solve_6d58a25d_one(S, I):
    return underfill(I, color(merge_f(remove_f(get_arg_rank_f(o_g(I, R7), size, F0), o_g(I, R7)))), mapply(chain(rbind(sfilter, compose(rbind(greater, increment(col_row(get_arg_rank_f(o_g(I, R7), size, F0), R1))), rbind(get_nth_f, F0))), vfrontier, center), sfilter_f(remove_f(get_arg_rank_f(o_g(I, R7), size, F0), o_g(I, R7)), fork(both, rbind(vmatching, get_arg_rank_f(o_g(I, R7), size, F0)), compose(rbind(greater, col_row(get_arg_rank_f(o_g(I, R7), size, F0), R1)), rbind(col_row, R1))))))


def solve_6d58a25d(S, I):
    x1 = o_g(I, R7)
    x2 = get_arg_rank_f(x1, size, F0)
    x3 = remove_f(x2, x1)
    x4 = merge_f(x3)
    x5 = color(x4)
    x6 = col_row(x2, R1)
    x7 = increment(x6)
    x8 = rbind(greater, x7)
    x9 = rbind(get_nth_f, F0)
    x10 = compose(x8, x9)
    x11 = rbind(sfilter, x10)
    x12 = chain(x11, vfrontier, center)
    x13 = rbind(vmatching, x2)
    x14 = rbind(greater, x6)
    x15 = rbind(col_row, R1)
    x16 = compose(x14, x15)
    x17 = fork(both, x13, x16)
    x18 = sfilter_f(x3, x17)
    x19 = mapply(x12, x18)
    O = underfill(I, x5, x19)
    return O
