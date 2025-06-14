def solve_1f876c06_one(S, I):
    return paint(I, mapply(fork(recolor_i, color, fork(connect, compose(rbind(get_nth_f, L1), rbind(get_nth_f, F0)), power(rbind(get_nth_f, L1), TWO))), fgpartition(I)))


def solve_1f876c06(S, I, x=0):
    x1 = rbind(get_nth_f, L1)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, F0)
    if x == 2:
        return x2
    x3 = compose(x1, x2)
    if x == 3:
        return x3
    x4 = power(x1, TWO)
    if x == 4:
        return x4
    x5 = fork(connect, x3, x4)
    if x == 5:
        return x5
    x6 = fork(recolor_i, color, x5)
    if x == 6:
        return x6
    x7 = fgpartition(I)
    if x == 7:
        return x7
    x8 = mapply(x6, x7)
    if x == 8:
        return x8
    O = paint(I, x8)
    return O
