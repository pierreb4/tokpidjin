def solve_6d58a25d_one(S, I):
    return underfill(I, color(merge_f(remove_f(get_arg_rank_f(o_g(I, R7), size, F0), o_g(I, R7)))), mapply(chain(rbind(sfilter, compose(rbind(greater, increment(col_row(get_arg_rank_f(o_g(I, R7), size, F0), R1))), rbind(get_nth_f, F0))), vfrontier, center), sfilter_f(remove_f(get_arg_rank_f(o_g(I, R7), size, F0), o_g(I, R7)), fork(both, rbind(vmatching, get_arg_rank_f(o_g(I, R7), size, F0)), compose(rbind(greater, col_row(get_arg_rank_f(o_g(I, R7), size, F0), R1)), rbind(col_row, R1))))))


def solve_6d58a25d(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = remove_f(x2, x1)
    if x == 3:
        return x3
    x4 = merge_f(x3)
    if x == 4:
        return x4
    x5 = color(x4)
    if x == 5:
        return x5
    x6 = col_row(x2, R1)
    if x == 6:
        return x6
    x7 = increment(x6)
    if x == 7:
        return x7
    x8 = rbind(greater, x7)
    if x == 8:
        return x8
    x9 = rbind(get_nth_f, F0)
    if x == 9:
        return x9
    x10 = compose(x8, x9)
    if x == 10:
        return x10
    x11 = rbind(sfilter, x10)
    if x == 11:
        return x11
    x12 = chain(x11, vfrontier, center)
    if x == 12:
        return x12
    x13 = rbind(vmatching, x2)
    if x == 13:
        return x13
    x14 = rbind(greater, x6)
    if x == 14:
        return x14
    x15 = rbind(col_row, R1)
    if x == 15:
        return x15
    x16 = compose(x14, x15)
    if x == 16:
        return x16
    x17 = fork(both, x13, x16)
    if x == 17:
        return x17
    x18 = sfilter_f(x3, x17)
    if x == 18:
        return x18
    x19 = mapply(x12, x18)
    if x == 19:
        return x19
    O = underfill(I, x5, x19)
    return O
