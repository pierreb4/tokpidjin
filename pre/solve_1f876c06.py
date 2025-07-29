def solve_1f876c06_one(S, I):
    return paint(I, mapply(fork(recolor_i, color, fork(connect, compose(rbind(get_nth_f, L1), rbind(get_nth_f, F0)), power(rbind(get_nth_f, L1), TWO))), fgpartition(I)))


def solve_1f876c06(S, I):
    x1 = rbind(get_nth_f, L1)
    x2 = rbind(get_nth_f, F0)
    x3 = compose(x1, x2)
    x4 = power(x1, TWO)
    x5 = fork(connect, x3, x4)
    x6 = fork(recolor_i, color, x5)
    x7 = fgpartition(I)
    x8 = mapply(x6, x7)
    O = paint(I, x8)
    return O
