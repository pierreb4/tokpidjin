def solve_253bf280_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(sfilter_f(prapply(connect, f_ofcolor(I, CYAN), f_ofcolor(I, CYAN)), compose(rbind(greater, BLUE), size)), fork(either, vline_i, hline_i))), CYAN, f_ofcolor(I, CYAN))


def solve_253bf280(S, I, x=0):
    x1 = identity(p_g)
    if x == 1:
        return x1
    x2 = rbind(get_nth_t, F0)
    if x == 2:
        return x2
    x3 = c_zo_n(S, x1, x2)
    if x == 3:
        return x3
    x4 = f_ofcolor(I, CYAN)
    if x == 4:
        return x4
    x5 = prapply(connect, x4, x4)
    if x == 5:
        return x5
    x6 = rbind(greater, BLUE)
    if x == 6:
        return x6
    x7 = compose(x6, size)
    if x == 7:
        return x7
    x8 = sfilter_f(x5, x7)
    if x == 8:
        return x8
    x9 = fork(either, vline_i, hline_i)
    if x == 9:
        return x9
    x10 = mfilter_f(x8, x9)
    if x == 10:
        return x10
    x11 = fill(I, x3, x10)
    if x == 11:
        return x11
    O = fill(x11, CYAN, x4)
    return O
