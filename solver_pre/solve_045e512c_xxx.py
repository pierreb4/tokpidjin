def solve_045e512c_one(S, I):
    return paint(I, mapply(fork(recolor_o, color, compose(lbind(mapply, lbind(shift, get_arg_rank_f(o_g(I, R7), size, F0))), chain(rbind(apply, interval(FOUR, double(TEN), FOUR)), lbind(rbind, multiply), lbind(position, get_arg_rank_f(o_g(I, R7), size, F0))))), remove_f(get_arg_rank_f(o_g(I, R7), size, F0), o_g(I, R7))))


def solve_045e512c(S, I, x=0):
    x1 = o_g(I, R7)
    if x == 1:
        return x1
    x2 = get_arg_rank_f(x1, size, F0)
    if x == 2:
        return x2
    x3 = lbind(shift, x2)
    if x == 3:
        return x3
    x4 = lbind(mapply, x3)
    if x == 4:
        return x4
    x5 = double(TEN)
    if x == 5:
        return x5
    x6 = interval(FOUR, x5, FOUR)
    if x == 6:
        return x6
    x7 = rbind(apply, x6)
    if x == 7:
        return x7
    x8 = lbind(rbind, multiply)
    if x == 8:
        return x8
    x9 = lbind(position, x2)
    if x == 9:
        return x9
    x10 = chain(x7, x8, x9)
    if x == 10:
        return x10
    x11 = compose(x4, x10)
    if x == 11:
        return x11
    x12 = fork(recolor_o, color, x11)
    if x == 12:
        return x12
    x13 = remove_f(x2, x1)
    if x == 13:
        return x13
    x14 = mapply(x12, x13)
    if x == 14:
        return x14
    O = paint(I, x14)
    return O
