def solve_ded97339_one(S, I):
    return underfill(I, EIGHT, mfilter_f(apply(fork(connect, rbind(get_nth_f, F0), rbind(get_nth_f, L1)), product(f_ofcolor(I, EIGHT), f_ofcolor(I, EIGHT))), fork(either, vline_i, hline_i)))


def solve_ded97339(S, I, x=0):
    x1 = rbind(get_nth_f, F0)
    if x == 1:
        return x1
    x2 = rbind(get_nth_f, L1)
    if x == 2:
        return x2
    x3 = fork(connect, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, EIGHT)
    if x == 4:
        return x4
    x5 = product(x4, x4)
    if x == 5:
        return x5
    x6 = apply(x3, x5)
    if x == 6:
        return x6
    x7 = fork(either, vline_i, hline_i)
    if x == 7:
        return x7
    x8 = mfilter_f(x6, x7)
    if x == 8:
        return x8
    O = underfill(I, EIGHT, x8)
    return O
