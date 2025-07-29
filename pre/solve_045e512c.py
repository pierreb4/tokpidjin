def solve_045e512c_one(S, I):
    return paint(I, mapply(fork(recolor_o, color, compose(lbind(mapply, lbind(shift, get_arg_rank_f(o_g(I, R7), size, F0))), chain(rbind(apply, interval(FOUR, double(TEN), FOUR)), lbind(rbind, multiply), lbind(position, get_arg_rank_f(o_g(I, R7), size, F0))))), remove_f(get_arg_rank_f(o_g(I, R7), size, F0), o_g(I, R7))))


def solve_045e512c(S, I):
    x1 = o_g(I, R7)
    x2 = get_arg_rank_f(x1, size, F0)
    x3 = lbind(shift, x2)
    x4 = lbind(mapply, x3)
    x5 = double(TEN)
    x6 = interval(FOUR, x5, FOUR)
    x7 = rbind(apply, x6)
    x8 = lbind(rbind, multiply)
    x9 = lbind(position, x2)
    x10 = chain(x7, x8, x9)
    x11 = compose(x4, x10)
    x12 = fork(recolor_o, color, x11)
    x13 = remove_f(x2, x1)
    x14 = mapply(x12, x13)
    O = paint(I, x14)
    return O
