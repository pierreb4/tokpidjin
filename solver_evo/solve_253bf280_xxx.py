def solve_253bf280_one(S, I):
    return fill(fill(I, c_zo_n(S, identity(p_g), rbind(get_nth_t, F0)), mfilter_f(sfilter_f(prapply(connect, f_ofcolor(I, CYAN), f_ofcolor(I, CYAN)), compose(rbind(greater, BLUE), size)), fork(either, vline_i, hline_i))), CYAN, f_ofcolor(I, CYAN))


def solve_253bf280(S, I):
    x1 = identity(p_g)
    x2 = rbind(get_nth_t, F0)
    x3 = c_zo_n(S, x1, x2)
    x4 = f_ofcolor(I, CYAN)
    x5 = prapply(connect, x4, x4)
    x6 = rbind(greater, BLUE)
    x7 = compose(x6, size)
    x8 = sfilter_f(x5, x7)
    x9 = fork(either, vline_i, hline_i)
    x10 = mfilter_f(x8, x9)
    x11 = fill(I, x3, x10)
    O = fill(x11, CYAN, x4)
    return O
