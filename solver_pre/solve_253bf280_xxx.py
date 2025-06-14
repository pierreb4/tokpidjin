def solve_253bf280_one(S, I):
    return fill(fill(I, THREE, mfilter_f(sfilter_f(prapply(connect, f_ofcolor(I, EIGHT), f_ofcolor(I, EIGHT)), compose(rbind(greater, ONE), size)), fork(either, vline_i, hline_i))), EIGHT, f_ofcolor(I, EIGHT))


def solve_253bf280(S, I, x=0):
    x1 = f_ofcolor(I, EIGHT)
    if x == 1:
        return x1
    x2 = prapply(connect, x1, x1)
    if x == 2:
        return x2
    x3 = rbind(greater, ONE)
    if x == 3:
        return x3
    x4 = compose(x3, size)
    if x == 4:
        return x4
    x5 = sfilter_f(x2, x4)
    if x == 5:
        return x5
    x6 = fork(either, vline_i, hline_i)
    if x == 6:
        return x6
    x7 = mfilter_f(x5, x6)
    if x == 7:
        return x7
    x8 = fill(I, THREE, x7)
    if x == 8:
        return x8
    O = fill(x8, EIGHT, x1)
    return O
