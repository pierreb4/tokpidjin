def solve_253bf280_one(S, I):
    return fill(fill(I, THREE, mfilter_f(sfilter_f(prapply(connect, f_ofcolor(I, EIGHT), f_ofcolor(I, EIGHT)), compose(rbind(greater, ONE), size)), fork(either, vline_i, hline_i))), EIGHT, f_ofcolor(I, EIGHT))


def solve_253bf280(S, I):
    x1 = f_ofcolor(I, EIGHT)
    x2 = prapply(connect, x1, x1)
    x3 = rbind(greater, ONE)
    x4 = compose(x3, size)
    x5 = sfilter_f(x2, x4)
    x6 = fork(either, vline_i, hline_i)
    x7 = mfilter_f(x5, x6)
    x8 = fill(I, THREE, x7)
    O = fill(x8, EIGHT, x1)
    return O
